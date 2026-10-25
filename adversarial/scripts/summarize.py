#!/usr/bin/env python3
import json,re,math,collections,datetime
from pathlib import Path
from audit import ROOT,OUT,dump,wilson,norm
def flat(x):
    if isinstance(x,str):return x
    if isinstance(x,list):return "\n".join(flat(v) for v in x)
    if isinstance(x,dict):return "\n".join(flat(v) for v in x.values())
    return str(x)
def clean(s): return re.sub(r"\s+"," ",s).strip().lower().replace("’","'").replace("–","-").replace("—","-")
rows=json.loads((OUT/"inventory.json").read_text())
results=[]; invalid=[]; semantic=[]
for r in rows:
    p=OUT/"regrade"/(r["run"]+".json")
    if not p.exists():continue
    g=json.loads(p.read_text()); key=json.loads((ROOT/r["key_path"]).read_text())
    run=json.loads((ROOT/r["run_path"]).read_text())
    docs={d.name:d.read_text() for d in (ROOT/"calibration/data_packs"/r["pack"]/"docs").glob("*")}
    flags=[]
    if len(g["drivers"])!=r["n"]:flags.append("wrong driver count")
    for d in g["drivers"]:
        ix=d["index"]-1
        if ix<0 or ix>=len(key["drivers"]) or clean(d["gold_driver"])!=clean(key["drivers"][ix]["driver"]):
            flags.append(f'gold identity {ix+1}')
        if d["semantic_present"] and (not d["candidate_quote"] or clean(d["candidate_quote"]) not in clean(flat(run["final"]))):
            flags.append(f'candidate quote {ix+1}')
        if d["evidence_supported"]:
            # Judge sometimes gives Dnn only: resolve only unambiguous prefix.
            found=[v for k,v in docs.items() if k==d["document"] or k.startswith(d["document"]+"_")]
            if len(found)!=1 or not d["document_quote"] or clean(d["document_quote"]) not in clean(found[0]):
                flags.append(f'document quote {ix+1}')
    if flags:invalid.append(dict(run=r["run"],flags=flags))
    accepted=[]
    for d in g["drivers"]:
        i=d["index"]
        causal=d["semantic_present"] and f"gold identity {i}" not in flags and f"candidate quote {i}" not in flags
        supported=causal and d["evidence_supported"] and f"document quote {i}" not in flags
        accepted.append(dict(index=i,causal=causal,supported=supported))
    g["audit_validation"]=dict(flags=flags,accepted=accepted,policy="Exact quote failure receives zero for that endpoint; raw judge judgment retained above.")
    dump(p,g)
    v=dict(r,strict_semantic=sum(d["causal"] for d in accepted),
           strict_supported=sum(d["supported"] for d in accepted),
           validation_flags=flags,primary_cause=g["primary_cause"],cause_evidence=g["cause_evidence"],key_problem=g["key_problem"])
    results.append(v)
    if g["semantic_leakage"]:semantic.append(dict(pack=r["pack"],run=r["run"],hits=g["semantic_leakage"]))
dump(OUT/"regrade/validation.json",invalid)
dump(OUT/"regrade/summary.json",results)
dump(OUT/"semantic_leakage.json",semantic)
table=["# Blind strict re-grade\n",
       "All 94 outputs were regraded, a superset of original MATCH/PARTIAL cases. Candidate identity was anonymized and original grades/provider withheld; source company names remain in documents and the memo, so this is score-blind, not entity-blind. Each final memo/driver/valuation was graded separately, with full pack documents and gold drivers. Stage outputs were excluded. One queryWithLLM judge is not a human adjudication or an independent model-family audit.\n",
       "Two separate endpoints: semantic recall = same explicit causal claim/polarity; supported recall additionally requires the cited document to support it. Counts can increase: strict regrading is not mechanically constrained below the original. The requested leniency number uses semantic recall, not the additional grounding penalty. Per-driver quotes and judgments are in each run JSON. `raw/` contains an abandoned paired pilot that sometimes enumerated candidate instead of gold drivers; NONE of those pilot results enters these statistics.\n",
       "Wilson intervals below are descriptive pooled-driver binomial intervals. Drivers within a case, and named/masked pairs, are dependent; these intervals are not confirmatory evidence of population fidelity.\n",
       "|Set|Condition|Original k/N [95%]|Strict causal k/N [95%]|Strict supported k/N [95%]|","|---|---|---|---|---|"]
summ=[]
for group in ("calibration","controls","holdout"):
    for masked in (False,True):
        rr=[r for r in results if r["group"]==group and r["masked"]==masked]
        n=sum(r["n"] for r in rr);v=dict(group=group,masked=masked,n=n)
        for field in ("original_k","strict_semantic","strict_supported"):
            k=sum(r[field] for r in rr);v[field]=dict(k=k,n=n,rate=k/n,wilson95=wilson(k,n))
        summ.append(v)
        cell=lambda f:f'{v[f]["k"]}/{n} [{100*v[f]["wilson95"][0]:.1f}%, {100*v[f]["wilson95"][1]:.1f}%]'
        table.append(f'|{group}|{"masked" if masked else "named"}|{cell("original_k")}|{cell("strict_semantic")}|{cell("strict_supported")}|')
# Primary requested decision selection: state MATCH/PARTIAL; denominator sensitivity all cases.
selected=[r for r in results if r["original_state"] in ("MATCH","PARTIAL") and r["group"]!="controls"]
leniency=sum((r["original_k"]-r["strict_semantic"])/r["n"] for r in selected)/len(selected)
supported_gap=sum((r["original_k"]-r["strict_supported"])/r["n"] for r in selected)/len(selected)
table += [f'\n**Leniency (mean original minus strict causal reproduced share, calibration + hold-out original state MATCH/PARTIAL, n={len(selected)} runs; controls excluded): {leniency:.6f} ({100*leniency:.2f} percentage points).** Grounding-inclusive gap: {100*supported_gap:.2f} points. The scores contain no separate categorical driver grade, so original state defines the requested MATCH/PARTIAL subset. All decisions, including controls and original MISS, were regraded for coverage. Negative values mean the second judge credited more causal claims, not evidence that the original was lenient.\n',
          f'After one repair pass, {len(invalid)} runs still had non-verbatim quote evidence. Deterministic validation rejects those particular claims (candidate-quote failure removes causal credit; doc-quote failure removes support credit). Raw model judgments are preserved, and each file includes audit_validation accepted flags. This is a conservative reproducible endpoint, not human adjudication. See validation.json; a later human audit may recover credit for a genuinely correct paraphrase.\n',
          "## Every decision\n|Run|Original|Causal|Supported|Causal delta|Supported delta|","|---|---:|---:|---:|---:|---:|"]
for r in results:table.append(f'|{r["run"]}|{r["original_k"]}/{r["n"]}|{r["strict_semantic"]}/{r["n"]}|{r["strict_supported"]}/{r["n"]}|{r["strict_semantic"]-r["original_k"]:+d}|{r["strict_supported"]-r["original_k"]:+d}|')
(OUT/"regrade/regrade_table.md").write_text("\n".join(table))
dump(OUT/"regrade/aggregates.json",dict(summary=summ,selected_n=len(selected),leniency=leniency,supported_gap=supported_gap,validation_n=len(invalid)))
# Deterministic discrepancies in original grading, action and gates.
state_wrong=[];direction_wrong=[];stage_counts=collections.Counter();spot=collections.Counter();sells=[]
for r in rows:
    s=json.loads((ROOT/r["score_path"]).read_text());run=json.loads((ROOT/r["run_path"]).read_text())
    if s["state"]=="MATCH" and (s["direction"]!="MATCH" or r["original_k"]<math.ceil(.75*r["n"])):state_wrong.append(r["run"])
    if s["direction"]=="MATCH" and norm(r["agent"])!=norm(r["key"]):direction_wrong.append(r)
    crit=run.get("stages",{}).get("gate1",{}).get("criteria",{})
    if crit:stage_counts[len(crit)]+=1
    for c in s.get("grounding",{}).get("spot_checks",[]):spot[c.get("verdict","missing")]+=1
    if r["key"]=="SELL":sells.append(r)
dump(OUT/"deterministic_findings.json",dict(state_match_below_threshold=state_wrong,
    direction_match_nonmatching_action=direction_wrong,gate1_criteria_counts=dict(stage_counts),
    grounding_spotchecks=dict(spot),sells=sells))
# Index-derived event count: explicit ordinary-equity new economic positions, reentries included.
index=(ROOT/"compendium/INDEX_2017_2026.md").read_text()
excludes=("update","control","psth","psus","pershing_square_ipo","seg","hedge","swaptions","treasury_short","cds","preferred")
events=[]
for ln,line in enumerate(index.splitlines(),1):
    m=re.match(r"\| \[([^]]+)\]\(trades/((20\d\d)_[^)]+)\.md\) \|",line)
    if not m:continue
    name,file,year=m.groups();year=int(year)
    if not 2018<=year<=2026 or any(t in file for t in excludes):continue
    events.append(dict(name=name,file=file,year=year,index_line=ln,row=line))
yearcounts={year:sum(x["year"]==year for x in events) for year in range(2018,2027)}
pred=json.loads((ROOT/"forward/next_trade_prediction.json").read_text())
prob=sum(c["probability_90d"] for c in pred["candidates"])
weighted_size=sum(c["probability_90d"]*c["size_pct_nav"] for c in pred["candidates"])
dump(OUT/"forward_statistics.json",dict(events=events,by_year=yearcounts,
    full_2018_2025_quarters=32,full_2018_2025_new=sum(yearcounts[y] for y in range(2018,2026)),
    full_2018_2025_rate=sum(yearcounts[y] for y in range(2018,2026))/32,
    through_2026_q3_quarters=35,through_2026_q3_rate=len(events)/35,
    through_cutoff_elapsed_quarters=32+4*(datetime.date(2026,10,25)-datetime.date(2026,1,1)).days/365,
    sum_candidate_probabilities=prob,probability_weighted_nav_pct=weighted_size,
    illustrative_dollars_core_bn=weighted_size/100*23.0454,
    full_candidate_sizes_pct=sum(c["size_pct_nav"] for c in pred["candidates"]),
    horizon_days=(datetime.date(2027,1,31)-datetime.date(2026,10,25)).days,
    principal_sum=sum([.25,.20,.18,.15,.15,.10,.08]),
    psus_gross_minus_security_cost=5000000000-4915991173,
    psi_cash_plus_investments_minus_debt_m=852-235))
print(json.dumps(dict(invalid=invalid,aggregates=summ,leniency=leniency,state_wrong=state_wrong,stage_counts=dict(stage_counts),spots=dict(spot),years=yearcounts,semantic=semantic),indent=2))
