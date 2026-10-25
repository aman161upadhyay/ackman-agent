#!/usr/bin/env python3
"""Reproducible, standard-library-only inventory, baselines, hashes and lexical date audit."""
import json, re, hashlib, math, datetime, collections
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "adversarial"
def dump(p, v):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(v, indent=2, ensure_ascii=False))
def wilson(k,n):
    if not n: return [None,None]
    p=k/n; z=1.96; d=1+z*z/n
    c=(p+z*z/(2*n))/d; h=z*math.sqrt(p*(1-p)/n+z*z/(4*n*n))/d
    return [c-h,c+h]
def norm(x):
    if x in ("BUY","ADD"): return "BUY"
    if x in ("SHORT","BUY_PROTECTION","SHORT_LONG_DURATION_VIA_OPTIONS","SHORT_HEDGE"): return "SHORT_HEDGE"
    return x
def main():
    rows=[]; packs={}
    scores=list((ROOT/"calibration/scores").rglob("*__score.json"))
    runs={p.stem:p for p in (ROOT/"calibration/runs").rglob("*.json")}
    for sp in sorted(scores):
        s=json.loads(sp.read_text()); rid=s.get("run",sp.stem.replace("__score",""))
        run=json.loads(runs[rid].read_text()); pid=run["pack"]
        kp=ROOT/"calibration/answer_keys"/("holdout" if "holdout" in sp.parts else "")/(pid+".json")
        key=json.loads(kp.read_text()); pack=ROOT/"calibration/data_packs"/pid
        meta=json.loads((pack/"meta.json").read_text())
        docs={p.name:p.read_text() for p in sorted((pack/"docs").glob("*")) if p.is_file()}
        text="\n".join(docs.values()).lower()
        mode=meta["mode"]
        constant={"new":"BUY","existing":"HOLD","hedge":"SHORT_HEDGE"}[mode]
        # Identity-independent literal quality screen, never fitted to labels.
        quality=bool(re.search(r"capital.light",text) and re.search(r"recurring|subscription|franchis|royalt|network.effect",text))
        negative=bool(re.search(r"negative (?:free.cash.flow|fcf)",text))
        heuristic=("BUY" if quality and not negative else "PASS") if mode=="new" else constant
        group="holdout" if "holdout" in sp.parts else "controls" if pid.startswith("ctl_") else "calibration"
        row=dict(run=rid,pack=pid,group=group,masked=run["masked"],mode=mode,
                 key=key["actual_decision"],agent=run["final"].get("decision"),original_direction=s["direction"],
                 original_state=s["state"],original_k=s["reasoning_overlap"]["k"],n=s["reasoning_overlap"]["n"],
                 mode_baseline=constant,always_pass="PASS",heuristic=heuristic,
                 score_path=str(sp.relative_to(ROOT)),run_path=str(runs[rid].relative_to(ROOT)),
                 key_path=str(kp.relative_to(ROOT)),heuristic_features=dict(quality=quality,negative_fcf=negative))
        rows.append(row)
        if pid not in packs: packs[pid]=dict(meta=meta,docs=docs,key=key,candidates=[])
        packs[pid]["candidates"].append(dict(anonymous_id=rid,final=run["final"]))
    dump(OUT/"inventory.json",rows)
    summary=[]
    for group in ("calibration","controls","holdout"):
        for masked in (False,True):
            rr=[r for r in rows if r["group"]==group and r["masked"]==masked]
            v=dict(group=group,masked=masked,n=len(rr))
            for model in ("agent","mode_baseline","always_pass","heuristic"):
                k=sum(norm(r[model])==norm(r["key"]) for r in rr)
                v[model]=dict(k=k,n=len(rr),rate=k/len(rr),wilson95=wilson(k,len(rr)))
            v["reported_agent_match"]=sum(r["original_direction"]=="MATCH" for r in rr)
            summary.append(v)
    dump(OUT/"baselines.json",dict(definition="Canonical direction: BUY/ADD equivalent; SHORT, BUY_PROTECTION and SHORT_LONG_DURATION_VIA_OPTIONS map to SHORT_HEDGE; TRIM != SELL; sizing ignored. Original judge direction separately reported.",summary=summary,decisions=rows))
    md=["# Baselines on identical decisions\n",
        "The requested 'majority per mode' is the specified policy BUY/new, HOLD/existing, SHORT_HEDGE/hedge, **not a fitted majority** (the selected existing-position keys are mostly exits). Always PASS and this mode policy require no business evidence. Labels come only from keys; no agent outputs are used to fit either policy.\n",
        "The third baseline is a deliberately crude pack-visible literal screen: BUY/new iff the documents contain `capital.light` AND one of recurring/subscription/franchise/royalty/network-effect, and do not contain `negative free cash flow` or `negative FCF`; otherwise PASS. Existing/hedge use HOLD/SHORT_HEDGE. It is not a validated financial model; prose summaries and omissions influence it. Same facts yield identical named/masked baseline actions. No threshold tuning was performed.\n",
        "Canonical action means BUY≈ADD; key SHORT, BUY_PROTECTION and SHORT_LONG_DURATION_VIA_OPTIONS map to SHORT_HEDGE (the benchmark's output vocabulary). This does not mean single-stock shorts and macro insurance are the same process. TRIM≠SELL; conviction/size do not change this direction metric. 'Original' is the supplied grader's direction MATCH, which sometimes penalizes size. Each cell k/n (percent); intervals in JSON.\n",
        "|Set|Condition|Agent exact|Original MATCH|Mode policy|Always PASS|Literal quality|","|---|---|---:|---:|---:|---:|---:|"]
    for v in summary:
        cell=lambda m:f'{v[m]["k"]}/{v["n"]} ({100*v[m]["rate"]:.1f}%)'
        md.append(f'|{v["group"]}|{"masked" if v["masked"] else "named"}|{cell("agent")}|{v["reported_agent_match"]}/{v["n"]}|{cell("mode_baseline")}|{cell("always_pass")}|{cell("heuristic")}|')
    md += ["\n## Where does the agent beat the mode policy?"]
    for v in summary:
        delta=v["agent"]["k"]-v["mode_baseline"]["k"]
        md.append(f'- {v["group"]}, {"masked" if v["masked"] else "named"}: {delta:+d} exact matches ({100*delta/v["n"]:+.1f} percentage points).')
    md += ["\nThe buy-enriched sample makes the mode policy strong. Controls, full exits, and erroneous historic buys—not compliant-sounding buy memos—carry the discrimination. Controls are researcher-imputed nonholdings, not necessarily publicly documented Ackman rejections. Wilson intervals are descriptive; paired named/masked runs and related issuer episodes are not independent.\n",
           "Reproduce: `python3 ackman-agent/adversarial/scripts/audit.py`. Per-decision predictions, features, labels, paths and Wilson intervals are in baselines.json."]
    (OUT/"baselines.md").write_text("\n".join(md))
    # Blind payload: no scores, original state or model/provider identity.
    for i,(pid,p) in enumerate(sorted(packs.items())):
        candidates=[]
        for j,c in enumerate(p["candidates"]):
            candidates.append(dict(anonymous_id=f"C{j+1}",final=c["final"]))
        payload=dict(as_of_date=p["meta"]["as_of_date"],mode=p["meta"]["mode"],docs=p["docs"],
                     answer_key={k:v for k,v in p["key"].items() if k in ("actual_decision","drivers","reason_class","pack_quality_notes")},
                     candidates=candidates)
        dump(OUT/"inputs"/(pid+".json"),payload)
    dump(OUT/"inputs/manifest.json",[
        dict(pack=pid,path=str((OUT/"inputs"/(pid+".json")).relative_to(ROOT.parent)),
             mapping={f"C{i+1}":c["anonymous_id"] for i,c in enumerate(p["candidates"])},
             semantic=pid in [r["pack"] for r in rows if r["group"]=="holdout"] or pid=="2025_uber_buy")
        for pid,p in sorted(packs.items())])
    hashes=[]
    for line in (ROOT/"calibration/PROMPT_HASHES_v1.5.txt").read_text().splitlines():
        h,p=line.split(None,1); p=p.strip()
        actual=hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
        hashes.append(dict(file=p,expected=h,actual=actual,match=h==actual))
    listed={r["file"] for r in hashes}
    unhashed=[str(p.relative_to(ROOT)) for p in (ROOT/"prompts").glob("*.md") if str(p.relative_to(ROOT)) not in listed]
    dump(OUT/"hash_audit.json",dict(entries=hashes,unhashed=unhashed))
    hits=[]; doc_count=0; pack_dates=[]
    months={m.lower():i for i,m in enumerate(["January","February","March","April","May","June","July","August","September","October","November","December"],1)}
    months.update({m[:3]:i for m,i in list(months.items())})
    mpat=r"(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:t(?:ember)?)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)"
    patterns=[
        ("ISO",r"\b((?:19|20)\d{2})[-/](\d{1,2})[-/](\d{1,2})\b",lambda m:(int(m[1]),int(m[2]),int(m[3]))),
        ("US numeric",r"\b(\d{1,2})/(\d{1,2})/((?:19|20)\d{2})\b",lambda m:(int(m[3]),int(m[1]),int(m[2]))),
        ("day-first numeric",r"\b(1[3-9]|2\d|3[01])/(\d{1,2})/((?:19|20)\d{2})\b",lambda m:(int(m[3]),int(m[2]),int(m[1]))),
        ("two-digit-year US",r"\b(\d{1,2})/(\d{1,2})/(\d{2})\b",lambda m:((1900 if int(m[3])>=70 else 2000)+int(m[3]),int(m[1]),int(m[2]))),
        ("month day year",rf"\b({mpat})\.?\s+(\d{{1,2}})(?:st|nd|rd|th)?[,]?\s+((?:19|20)\d{{2}})\b",lambda m:(int(m[3]),months[m[1].lower()[:3]],int(m[2]))),
        ("day month year",rf"\b(\d{{1,2}})\s+({mpat})\.?[,]?\s+((?:19|20)\d{{2}})\b",lambda m:(int(m[3]),months[m[2].lower()[:3]],int(m[1]))),
        ("month year",rf"\b({mpat})\.?\s+((?:19|20)\d{{2}})\b",lambda m:(int(m[2]),months[m[1].lower()[:3]],1)),
        ("year-month",r"\b((?:19|20)\d{2})-(\d{2})\b",lambda m:(int(m[1]),int(m[2]),1)),
        ("quarter-year",r"\bQ([1-4])\s*[- ]?\s*((?:19|20)\d{2})\b",lambda m:(int(m[2]),(int(m[1])-1)*3+1,1)),
        ("year-quarter",r"\b((?:19|20)\d{2})[- ]?Q([1-4])\b",lambda m:(int(m[1]),(int(m[2])-1)*3+1,1)),
        ("year",r"\b((?:19|20)\d{2})\b",lambda m:(int(m[1]),1,1))]
    for pack in sorted((ROOT/"calibration/data_packs").iterdir()):
        if not (pack/"meta.json").exists(): continue
        meta=json.loads((pack/"meta.json").read_text()); cutoff=datetime.date.fromisoformat(meta["as_of_date"])
        pack_dates.append(dict(pack=pack.name,as_of_date=str(cutoff)))
        for p in sorted((pack/"docs").glob("*")):
            if not p.is_file():continue
            doc_count+=1
            for ln,line in enumerate(p.read_text().splitlines(),1):
                spans=[]
                for typ,pat,conv in patterns:
                    for m in re.finditer(pat,line,re.I):
                        if any(a<=m.start() and m.end()<=b for a,b in spans):continue
                        try: date=datetime.date(*conv(m))
                        except (ValueError,KeyError):continue
                        spans.append(m.span())
                        if date>cutoff:
                            hits.append(dict(pack=pack.name,file=str(p.relative_to(ROOT)),line=ln,cutoff=str(cutoff),date=str(date),format=typ,token=m.group(),context=line))
    dump(OUT/"date_scan.json",dict(pack_count=len(pack_dates),doc_count=doc_count,packs=pack_dates,hits=hits))
    mentions=[]
    holdout=[p["meta"] for pid,p in packs.items() if any(r["pack"]==pid and r["group"]=="holdout" for r in rows)]
    for meta in holdout:
        raw=[meta["company"],meta.get("ticker","")]+meta.get("aliases",[])
        terms=set(t for item in raw for t in (item if isinstance(item,list) else [item]))
        for p in [ROOT/"AGENT.md"]+list((ROOT/"prompts").glob("*.md")):
            for ln,line in enumerate(p.read_text().splitlines(),1):
                found=[t for t in terms if t and re.search(r"(?<!\w)"+re.escape(t)+r"(?!\w)",line,re.I)]
                if found:mentions.append(dict(pack=meta["id"],file=str(p.relative_to(ROOT)),line=ln,terms=sorted(found),context=line))
    dump(OUT/"holdout_mentions.json",mentions)
    dump(OUT/"additional_statistics.json",dict(
        pooled={condition:dict(agent=sum(v["agent"]["k"] for v in summary if v["masked"]==mask),
                              mode=sum(v["mode_baseline"]["k"] for v in summary if v["masked"]==mask),n=47)
                for condition,mask in [("named",False),("masked",True)]},
        action_disagreements={group:sum(next(r for r in rows if r["pack"]==p and not r["masked"])["agent"] != next(r for r in rows if r["pack"]==p and r["masked"])["agent"] for p in {r["pack"] for r in rows if r["group"]==group}) for group in ("calibration","controls","holdout")}))
    print(json.dumps(dict(runs=len(rows),packs=len(packs),summary=summary,date_hits=len(hits),hash_mismatch=[h["file"] for h in hashes if not h["match"]]),indent=2))
if __name__=="__main__": main()
