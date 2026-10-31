#!/usr/bin/env python3
"""Check that the model under test does not know what happened after its claimed training cutoff (Llama 3.1 8B: Dec 2023).

Two probes, both closed-book (no pack in the prompt):
  A. general post-cutoff facts with a single checkable answer (keyword-scored);
  B. Pershing Square positions first taken in 2024+ (every pack dated 2024+ whose company has no earlier pack), mixed with
     decoy companies Pershing never owned. A model that remembers says "yes" to the real ones more often than to the decoys.
Usage: python tools/cutoff_probe.py --model llama3.1:8b [--repeats 3]
Output: calibration/runs/cutoff_probe__<model>__<timestamp>.json and a verdict on stdout.
"""
import argparse, glob, json, os, re, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from run_agent import chat, parse_json, ROOT

GENERAL = [  # (question, any of these substrings in the answer = knows it)
    ('Who won the 2024 United States presidential election?', ['trump']),
    ('Which national team won UEFA Euro 2024?', ['spain']),
    ('Who were awarded the 2024 Nobel Prize in Physics?', ['hopfield', 'hinton']),
    ('Who became Prime Minister of the United Kingdom in July 2024?', ['starmer']),
    ('Which company announced in January 2024 that it would acquire Juniper Networks?', ['hewlett', 'hpe']),
    ('What was the name of the multimodal model OpenAI released in May 2024?', ['gpt-4o', 'gpt4o', '4o']),
    ('Which cybersecurity company\'s faulty update crashed millions of Windows computers in July 2024?', ['crowdstrike']),
    ('Who won the 2024 Formula One World Drivers\' Championship?', ['verstappen']),
]
DECOYS = ['The Coca-Cola Company', 'Exxon Mobil', 'Pfizer', 'Tesla', 'Walmart', 'Johnson & Johnson']
SYSTEM = 'Answer from memory only. If you do not know, say so. Return JSON only.'

def post_cutoff_positions():
    metas = []
    for p in glob.glob(os.path.join(ROOT, 'calibration', 'data_packs', '*', 'meta.json')):
        with open(p, encoding='utf-8') as f: metas.append(json.load(f))
    earlier = {m['company'] for m in metas if m['as_of_date'] < '2024-01-01'}
    seen, out = set(), []
    for m in sorted(metas, key=lambda m: m['as_of_date']):
        if m['as_of_date'] >= '2024-01-01' and m.get('mode') == 'new' and m['company'] not in earlier and m['company'] not in seen:
            seen.add(m['company']); out.append((m['company'], m['as_of_date'][:4]))
    return out

def ask_position(model, company, year):
    q = (f'Did Pershing Square Capital Management (Bill Ackman\'s fund) buy shares of {company} during {year}? '
         'Return {"answer": "yes|no|unknown", "detail": "one sentence"}.')
    r = parse_json(chat(model, SYSTEM, q, True, 0.0, 4096))
    return str(r.get('answer', '')).strip().lower(), r.get('detail', '')

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--model', required=True); ap.add_argument('--repeats', type=int, default=1)
    a = ap.parse_args()
    out = {'model': a.model, 'run_at': time.strftime('%Y-%m-%dT%H:%M:%S'), 'general': [], 'positions': []}
    for q, keys in GENERAL:
        ans = chat(a.model, 'Answer from memory in one short sentence. If you do not know, say "unknown".', q, False, 0.0, 4096)
        out['general'].append({'q': q, 'answer': ans, 'knows': any(k in ans.lower() for k in keys)})
    real = post_cutoff_positions()
    for company, year in real + [(d, y) for d in DECOYS for y in ('2024', '2025')]:
        for _ in range(a.repeats):
            ans, detail = ask_position(a.model, company, year)
            out['positions'].append({'company': company, 'year': year, 'real': (company, year) in real, 'answer': ans, 'detail': detail})
    g = sum(x['knows'] for x in out['general'])
    yes = lambda rows: sum(r['answer'] == 'yes' for r in rows) / max(len(rows), 1)
    yr, yd = yes([r for r in out['positions'] if r['real']]), yes([r for r in out['positions'] if not r['real']])
    out['summary'] = {'general_known': f'{g}/{len(GENERAL)}', 'yes_rate_real': round(yr, 2), 'yes_rate_decoy': round(yd, 2)}
    os.makedirs(os.path.join(ROOT, 'calibration', 'runs'), exist_ok=True)
    fn = os.path.join(ROOT, 'calibration', 'runs', f"cutoff_probe__{a.model.replace(':','-').replace('/','-')}__{time.strftime('%Y%m%d-%H%M%S')}.json")
    with open(fn, 'w', encoding='utf-8') as f: json.dump(out, f, indent=1, ensure_ascii=False)
    sys.stdout.reconfigure(encoding='utf-8')
    print(fn); print(json.dumps(out['summary']))
    # Two lucky guesses (e.g. "Trump") are plausible from priors; more, or a clear real-vs-decoy gap, means post-cutoff knowledge.
    leak = g > 2 or yr - yd >= 0.25
    print('VERDICT:', 'POSSIBLE POST-CUTOFF KNOWLEDGE - inspect the file before trusting replays' if leak else
          'no evidence the model knows post-cutoff events or 2024+ Pershing positions')

if __name__ == '__main__': main()
