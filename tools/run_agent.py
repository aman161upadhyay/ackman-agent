#!/usr/bin/env python3
"""Run the Ackman agent prompt chain on a point-in-time data pack with a local Ollama model.

Usage:
  python tools/run_agent.py --pack calibration/data_packs/2025_uber_buy --model llama3.1:8b
  python tools/run_agent.py --pack ... --model llama3.1:8b --one-shot          # single call from AGENT.md (strong models)
  python tools/run_agent.py --pack ... --model llama3.1:8b --mask              # replace company name/ticker with 'the Company'
  python tools/run_agent.py --pack ... --mask --check-mask                     # print the masked pack + residue report, no model call
  python tools/run_agent.py --pack ... --no-enforce                            # v1.5 behaviour: trust the model's gate verdicts
Env: OLLAMA_URL (default http://localhost:11434). Set OPENAI_BASE_URL/OPENAI_API_KEY (or --base-url/--api-key) to use an
OpenAI-compatible endpoint instead.
Outputs: calibration/runs/<pack_id>__<model>__<timestamp>.json (all stage outputs + final decision + provenance).
"""
import argparse, hashlib, json, os, re, sys, time, glob, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROMPTS = os.path.join(ROOT, 'prompts')
FROZEN_HASHES = os.path.join(ROOT, 'calibration', 'PROMPT_HASHES_v1.5.txt')
RUNNER_VERSION = '1.5.1'
MASK = 'the Company'

def read(p):
    with open(p, encoding='utf-8') as f: return f.read()

def sha256(p):
    with open(p, 'rb') as f: return hashlib.sha256(f.read()).hexdigest()

# ---------- masking ----------
# v1.5 used an unbounded case-insensitive re.sub, which rewrote tickers inside ordinary words ("flow" -> "fthe Company" for
# LOW, "disciplined" -> "the Companyciplined" for DIS) and crashed when meta.ticker was a list (2026_v_ma_buy).

def _tickers(meta):
    t = meta.get('ticker') or []
    return [x for x in (t if isinstance(t, list) else [t]) if x]

def _names(meta):
    company = meta.get('company') or ''
    names = [company] + list(meta.get('aliases') or [])
    names += [p for p in re.split(r'\s+(?:and|&)\s+', company) if p != company]   # "Visa and Mastercard" -> Visa, Mastercard
    return [n.strip() for n in names if n and n.strip()]

def mask_text(text, meta):
    """Replace names and tickers on word boundaries, longest first. Single-word names match case-sensitively so an alias
    like "Target" does not eat "target price"; one-letter tickers are only masked in ticker contexts ($V, NYSE: V, (V))."""
    for n in sorted(set(_names(meta)), key=len, reverse=True):
        if re.search(r'\s', n): text = re.sub(r'(?<!\w)' + re.escape(n) + r'(?!\w)', MASK, text, flags=re.I)
        else: text = re.sub(r'(?<!\w)(?:' + re.escape(n) + '|' + re.escape(n.upper()) + r')(?!\w)', MASK, text)   # Nike, NIKE
    for t in sorted(set(_tickers(meta)), key=len, reverse=True):
        if len(t) >= 2:
            text = re.sub(r'(?<![\w.])' + re.escape(t) + r'(?![\w])', 'XXX', text)
        else:
            text = re.sub(r'(\$|\b(?:NYSE|NASDAQ|Nasdaq|TSX|NYSE American)\s*:\s*|\()' + re.escape(t) + r'(?![\w])', r'\1XXX', text)
    return text

STOP = {'inc', 'inc.', 'corp', 'corp.', 'corporation', 'company', 'companies', 'holdings', 'group', 'the', 'and', 'card',
        'networks', 'properties', 'international', 'general', 'global', 'canadian', 'pacific', 'brands'}

def mask_residue(text, meta):
    """Distinctive name fragments still visible after masking (e.g. 'McDonald' when only "McDonald's" was an alias)."""
    frags = set()
    for n in _names(meta):
        for w in re.findall(r"[A-Z][\w'.-]{3,}", n):
            w = re.sub(r"('s|\.)$", '', w)
            if w.lower() not in STOP: frags.add(w)
    out = {}
    for w in sorted(frags):
        c = len(re.findall(r'(?<!\w)' + re.escape(w) + r'(?!\w)', text))
        if c: out[w] = c
    glued = re.findall(r'\w' + re.escape(MASK) + r'|' + re.escape(MASK) + r'[a-z]', text)
    if glued: out['_glued_mask'] = len(glued)
    return out

def load_pack(pack_dir, mask=False):
    with open(os.path.join(pack_dir, 'meta.json'), encoding='utf-8') as f: meta = json.load(f)
    docs = sorted(glob.glob(os.path.join(pack_dir, 'docs', '*.md')))
    parts = []
    for i, d in enumerate(docs, 1):
        m = re.match(r'(D\d+)', os.path.basename(d))   # keep the filename's Dnn so citations map back (packs with D00 used to shift)
        label = m.group(1) if m else f"D{i:02d}"
        body = read(d)
        parts.append(f"===== [{label}] {os.path.basename(d)} =====\n{body}\n")
    pack = "\n".join(parts)
    residue = None
    if mask:
        pack = mask_text(pack, meta)
        residue = mask_residue(pack, meta)
        meta = dict(meta, company=MASK, ticker='XXX')
    elif isinstance(meta.get('ticker'), list):
        meta = dict(meta, ticker='/'.join(meta['ticker']))
    return meta, pack, residue

def fill(template, **kw):
    out = template
    for k, v in kw.items():
        out = out.replace('{{' + k + '}}', v if isinstance(v, str) else json.dumps(v, ensure_ascii=False, indent=1))
    return out

def chat(model, system, user, json_mode=True, temperature=0.1, num_ctx=16384):
    base = os.environ.get('OPENAI_BASE_URL')
    if base:  # OpenAI-compatible
        req = urllib.request.Request(base.rstrip('/') + '/chat/completions', method='POST',
            headers={'Content-Type': 'application/json', 'Authorization': 'Bearer ' + os.environ.get('OPENAI_API_KEY', 'x')},
            data=json.dumps({'model': model, 'temperature': temperature,
                             'messages': [{'role': 'system', 'content': system}, {'role': 'user', 'content': user}],
                             **({'response_format': {'type': 'json_object'}} if json_mode else {})}).encode())
        resp = json.load(urllib.request.urlopen(req, timeout=600))
        return resp['choices'][0]['message']['content']
    url = os.environ.get('OLLAMA_URL', 'http://localhost:11434').rstrip('/') + '/api/chat'
    payload = {'model': model, 'stream': False, 'options': {'temperature': temperature, 'num_ctx': num_ctx},
               'messages': [{'role': 'system', 'content': system}, {'role': 'user', 'content': user}]}
    if json_mode: payload['format'] = 'json'
    req = urllib.request.Request(url, method='POST', headers={'Content-Type': 'application/json'}, data=json.dumps(payload).encode())
    resp = json.load(urllib.request.urlopen(req, timeout=1800))
    return resp['message']['content']

def parse_json(s):
    try: return json.loads(s)
    except Exception:
        m = re.search(r'\{.*\}', s, flags=re.S)
        if m:
            try: return json.loads(m.group(0))
            except Exception: pass
    return {'_raw': s}

# ---------- provenance ----------

def model_digest(model):
    """Ollama's content digest for the exact weights used (None for OpenAI-compatible endpoints or if unreachable)."""
    if os.environ.get('OPENAI_BASE_URL'): return None
    try:
        url = os.environ.get('OLLAMA_URL', 'http://localhost:11434').rstrip('/') + '/api/tags'
        for m in json.load(urllib.request.urlopen(url, timeout=10)).get('models', []):
            if m.get('name') == model or m.get('model') == model: return m.get('digest')
    except Exception: pass
    return None

def provenance(files, model, pack_dir):
    frozen = {}
    if os.path.exists(FROZEN_HASHES):
        for line in read(FROZEN_HASHES).splitlines():
            if line.strip(): h, p = line.split(None, 1); frozen[p.strip()] = h
    hashes = {os.path.relpath(f, ROOT).replace(os.sep, '/'): sha256(f) for f in files}
    pack_files = sorted(glob.glob(os.path.join(pack_dir, 'meta.json')) + glob.glob(os.path.join(pack_dir, 'docs', '*.md')))
    pack_hash = hashlib.sha256(b''.join(sha256(f).encode() for f in pack_files)).hexdigest()
    return {'runner_version': RUNNER_VERSION, 'model_digest': model_digest(model), 'prompt_sha256': hashes,
            'prompts_match_frozen_v1_5': all(frozen.get(p) == h for p, h in hashes.items()) if frozen else None,
            'pack_sha256': pack_hash, 'endpoint': os.environ.get('OPENAI_BASE_URL') or os.environ.get('OLLAMA_URL', 'http://localhost:11434')}

# ---------- code-level enforcement of the gate rules in 02_gate1 and 07_decision_memo ----------
# v1.5 left these to the model; the stress tests found memos that bought after Gate 1 returned hard_fail=true (CMG, NFLX).

HARD_CRITERIA = ['simple_predictable_fcf', 'barriers_to_entry', 'strong_financial_profile', 'minimal_capital_markets_dependency']

def _true(v): return v is True or str(v).strip().lower() == 'true'

def _score(v): return str(v.get('score', '') if isinstance(v, dict) else v).strip().upper()

def gate1_hard_fail(g1):
    """Apply 02_gate1's rule to the criteria the model scored: FAIL on 1/2/4/5, or FAIL/UNSURE on 3+, is a hard fail unless
    the model invoked the special-situation override (whose (a)/(b) tests need judgement, so they stay with the model)."""
    crit = g1.get('criteria') or {}
    fails = [k for k in HARD_CRITERIA if _score(crit.get(k, '')) == 'FAIL']
    weak = [k for k, v in crit.items() if _score(v) in ('FAIL', 'UNSURE')]
    by_rule = bool(fails) or len(weak) >= 3
    special = _true(g1.get('special_situation'))   # the override sets hard_fail=false by definition, even if the model left it true
    return {'model_hard_fail': _true(g1.get('hard_fail')), 'rule_hard_fail': by_rule, 'special_situation': special,
            'hard_criteria_failed': fails, 'fail_or_unsure': weak,
            'hard_fail': (_true(g1.get('hard_fail')) or by_rule) and not special}

def enforce_decision(final, g1, g2, g3, verdict):
    """Deterministic parts of 07_decision_memo's decision logic, applied after the memo. Returns the list of overrides;
    the model's own call stays in final['model_decision'] so both can be graded (grade.py --decision model)."""
    notes, dec = [], str(final.get('decision', '')).upper()
    if dec in ('HOLD', 'ADD', 'TRIM', 'SELL'):
        notes.append(f'mode new allows BUY or PASS only; model said {dec}'); dec = 'BUY' if dec == 'ADD' else 'PASS'
    if dec == 'BUY' and verdict['hard_fail']:
        notes.append(f"gate1 hard fail ({'model' if verdict['model_hard_fail'] else 'rule'}: "
                     f"{', '.join(verdict['hard_criteria_failed'] or verdict['fail_or_unsure'])}) -> PASS"); dec = 'PASS'
    if dec == 'BUY':
        edge = str(g2.get('edge_verdict', '')).upper().replace(' ', '')
        val = str(g3.get('valuation_verdict', '')).upper()
        if edge == 'NO_EDGE': notes.append('gate2 NO_EDGE -> PASS'); dec = 'PASS'
        elif val.startswith('EXPENSIVE_BELOW_10') or val.startswith('FULL_10_15'): notes.append(f'gate3 {val} -> PASS'); dec = 'PASS'
    if dec == 'BUY' and verdict['special_situation']:
        try:
            if float(final.get('target_size_pct_nav') or 0) > 5:
                notes.append(f"special situation capped at 5% NAV (model said {final.get('target_size_pct_nav')})"); final['target_size_pct_nav'] = 5
        except (TypeError, ValueError): pass
    if notes:
        final['model_decision'] = final.get('decision'); final['decision'] = dec; final['enforced_by_code'] = True
        if dec == 'PASS': final['target_size_pct_nav'] = 0
    return notes

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--pack', required=True); ap.add_argument('--model', default='llama3.1:8b')
    ap.add_argument('--one-shot', action='store_true'); ap.add_argument('--mask', action='store_true')
    ap.add_argument('--temperature', type=float, default=0.1); ap.add_argument('--num-ctx', type=int, default=16384)
    ap.add_argument('--base-url', help='OpenAI-compatible endpoint (sets OPENAI_BASE_URL)'); ap.add_argument('--api-key')
    ap.add_argument('--no-enforce', action='store_true', help='v1.5 behaviour: do not apply the gate rules in code')
    ap.add_argument('--check-mask', action='store_true', help='print the masked pack and residue report, then exit')
    a = ap.parse_args()
    if a.base_url: os.environ['OPENAI_BASE_URL'] = a.base_url
    if a.api_key: os.environ['OPENAI_API_KEY'] = a.api_key
    meta, pack, residue = load_pack(a.pack, a.mask)
    if a.check_mask:
        sys.stdout.reconfigure(encoding='utf-8'); print(pack); print('RESIDUE:', json.dumps(residue), file=sys.stderr); return
    if residue: print('WARNING mask residue (identifying fragments left in the pack):', json.dumps(residue), file=sys.stderr)
    system = read(os.path.join(PROMPTS, '00_system.md'))
    common = dict(as_of_date=meta['as_of_date'], company=meta['company'], ticker=meta['ticker'])
    out = {'pack': os.path.basename(a.pack.rstrip('/\\')), 'model': a.model, 'mode': meta.get('mode', 'new'), 'masked': a.mask,
           'as_of_date': meta['as_of_date'], 'started': time.strftime('%Y-%m-%dT%H:%M:%S'), 'enforced': not a.no_enforce,
           'mask_residue': residue, 'stages': {}}
    used = [os.path.join(PROMPTS, '00_system.md')]
    def prompt(name): used.append(os.path.join(PROMPTS, name)); return read(os.path.join(PROMPTS, name))
    def step(name, **kw): return parse_json(chat(a.model, system, fill(prompt(name), **kw, **common), True, a.temperature, a.num_ctx))
    t0 = time.time()
    mode = meta.get('mode', 'new')
    if a.one_shot:
        used.append(os.path.join(ROOT, 'AGENT.md'))
        p = fill(prompt('one_shot_full.md'), agent_md=read(os.path.join(ROOT, 'AGENT.md')), pack=pack, mode=mode, **common)
        out['final'] = parse_json(chat(a.model, system, p, True, a.temperature, max(a.num_ctx, 32768)))
    elif mode == 'existing':
        out['final'] = step('08_sell_hold.md', pack=pack)
    elif mode == 'hedge':
        out['final'] = step('09_hedge.md', pack=pack)
    else:
        fs = step('01_fact_sheet.md', pack=pack); out['stages']['fact_sheet'] = fs
        g1 = step('02_gate1_business_quality.md', fact_sheet=fs); out['stages']['gate1'] = g1
        verdict = gate1_hard_fail(g1); out['gate1_check'] = verdict
        # the chain always runs to the memo (v1.5 memos bought after a Gate-1 hard fail in 41 of 74 calibration runs),
        # so the model's call and the rule-enforced call come from the same run
        g2 = step('03_gate2_why_mispriced.md', fact_sheet=fs, gate1=g1); out['stages']['gate2'] = g2
        g3 = step('04_gate3_valuation.md', fact_sheet=fs, gate2=g2); out['stages']['gate3'] = g3
        g4 = step('05_gate4_catalyst_role.md', fact_sheet=fs, gate1=g1, gate2=g2, gate3=g3); out['stages']['gate4'] = g4
        g5 = step('06_gate5_risk_sizing.md', fact_sheet=fs, gate1=g1, gate2=g2, gate3=g3, gate4=g4); out['stages']['gate5'] = g5
        fin = step('07_decision_memo.md', fact_sheet=fs, gate1=g1, gate2=g2, gate3=g3, gate4=g4, gate5=g5); out['final'] = fin
        if not a.no_enforce: out['overrides'] = enforce_decision(fin, g1, g2, g3, verdict)
    out['elapsed_s'] = round(time.time() - t0, 1)
    out['provenance'] = provenance(sorted(set(used)), a.model, a.pack)
    os.makedirs(os.path.join(ROOT, 'calibration', 'runs'), exist_ok=True)
    fn = os.path.join(ROOT, 'calibration', 'runs', f"{out['pack']}__{a.model.replace(':','-').replace('/','-')}__{time.strftime('%Y%m%d-%H%M%S')}{'__masked' if a.mask else ''}.json")
    with open(fn, 'w', encoding='utf-8') as f: json.dump(out, f, indent=1, ensure_ascii=False)
    sys.stdout.reconfigure(encoding='utf-8')
    print(fn); print(json.dumps({k: out['final'].get(k) for k in ['decision', 'conviction', 'target_size_pct_nav', 'reason_class']}, ensure_ascii=False))
    for n in out.get('overrides') or []: print(' override:', n)
    for d in out['final'].get('drivers', []): print(' -', d.get('driver') if isinstance(d, dict) else d)

if __name__ == '__main__': main()
