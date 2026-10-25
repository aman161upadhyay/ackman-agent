#!/usr/bin/env python3
"""Build audit tables directly from saved evidence/model judgments. No model calls."""
import json,re,collections
from pathlib import Path
from audit import ROOT,OUT,dump
load=lambda p:json.loads((OUT/p).read_text())
rows=load("inventory.json"); hashes=load("hash_audit.json"); dates=load("date_scan.json")
mentions=load("holdout_mentions.json");det=load("deterministic_findings.json")
agg=load("regrade/aggregates.json"); f=load("forward_statistics.json")
manifest={m["pack"]:m for m in load("inputs/manifest.json")}
adjud={r["run"]:r for r in load("divergence/adjudicated.json")["rows"]}
correction=load("divergence/runtime_correction.json")
correction["primary_cause"]=correction["primary_cause"].split()[0]
adjud[correction["run"]]=correction
failure=[r for r in rows if r["original_state"]!="MATCH" or r["original_direction"]!="MATCH"]
causes=collections.Counter(adjud[r["run"]]["primary_cause"] for r in failure)
dump(OUT/"divergence/counts.json",dict(n=len(failure),causes=dict(causes),runs=[r["run"] for r in failure]))
md=["# Divergence analysis\n",
    "Coverage: every original direction or state PARTIAL/MISS, named and masked, including every control false positive. A model judged each pack with the AGENT rules and then adjudicated classification inconsistencies; raw pack-level judgments and adjudicated.json are preserved in divergence/. These are evidence-based hypotheses, not observations of Ackman's private cognition. Primary causes are mutually exclusive; secondary causes can coexist. The staged specification is not identical to AGENT.md.\n",
    "|Primary cause|Count|","|---|---:|"]
names={"i":"Rule missing/ambiguous or not propagated to staged prompts","ii":"Pack missing decisive fact","iii":"Key/grader problem","iv":"Model execution/causal reasoning limitation","v":"Genuine underdetermined process/judgment difference"}
for k in names:md.append(f'|{k}: {names[k]}|{causes[k]}|')
md+=["\n## Three highest-leverage fixes\n",
     "1. **Separate absolute quality from opportunity cost.** Existing-position review must compare a dated alternative, evidence-backed return range and predictability range before HOLD. Define SELL versus TRIM by whether a residual holding remains an admissible fresh purchase; do not make loss recovery an objective. If alternative data are missing, disclose that the S3 result is underdetermined rather than inventing a precise IRR.\n",
     "2. **Propagate hard constraints into the actual staged inputs.** Alibaba's Chinese-VIE exclusion exists in AGENT §5 but is absent from 00_system and 02_gate1. Staged mode never reads AGENT.md. Boeing safety/certification and Disney's changing segment economics require forecastability evidence, not merely a drawdown. Do not hardcode the three company names.\n",
     "3. **Fix evidence and grading before adding exceptions.** Record decision-time ranges and missing facts in keys; isolate controls as synthetic discipline probes; preserve exact citations and full run manifests. HHH CONTROL vocabulary and dated era exceptions must reach all schemas. Run the whole calibration set under one frozen version instead of reusing earlier outputs.\n",
     "## Sell stickiness: concrete evidence\n",
     "- Berkshire: calibration/data_packs/2020_brk_sell/docs/D09_changes_since_purchase.md says: “An investor can find Berkshire undervalued and still prefer a different use of limited capital.” The pack supplies direct alternatives but not a matched numerical IRR comparison. Both HOLDs are a relative-allocation failure, not proof that Berkshire's business quality was misread. A mechanically forced SELL would overstate what the public facts establish.\n",
     "- CP: calibration/data_packs/2025_cp_sell/docs/D09_what_has_changed.md says “Synergies are no longer only a presentation forecast” and “The evidence does not justify replacing either possibility with hindsight.” The March checkpoint precedes disputed April/May exit timing. Tariffs widen outcomes without uniquely determining SELL; the key's later judgment must not be smuggled into the earlier pack.\n",
     "- Nike: both HOLDs retain an estimated return despite a longer repair horizon. D09_what_has_changed.md and D03_latest_results_and_guidance.md contain the prolonged Direct/China repair and margin pressure. S2 exists: the problem is translating a changed forecast distribution into action, not merely failing to mention tariffs.\n",
     "- Chipotle, Starbucks and Hilton: TRIM is not full exit. A partial sale can recognize valuation/opportunity cost while missing the all-or-nothing allocation decision. Report exit recall separately.\n",
     "## Every affected run\n|Run|Original direction/state|Primary cause|Evidence-based rationale|Concrete change|","|---|---|---|---|---|"]
for r in failure:
    a=adjud[r["run"]];esc=lambda s:s.replace("|","/").replace("\n"," ")
    md.append(f'|{r["run"]}|{r["original_direction"]}/{r["original_state"]}|{a["primary_cause"]}|{esc(a["rationale"])}|{esc(a["fix"])}|')
(OUT/"divergence_analysis.md").write_text("\n".join(md))
# Scan detail is deliberately exhaustive and separated from the main report.
md=["# Lexical date hits (not automatically leakage)\n",
    "Generated by scripts/audit.py. The scanner recognizes ISO/slash dates, US numeric month/day/year, named month/day/year and day/month/year, month-year, year-month, quarter-year/year-quarter, and standalone years. Partial dates use the first possible day (conservative for definite post-cutoff classification). It does not infer years from month/day alone, normalize arbitrary prose dates, decode Unix timestamps, or establish source release times. Fiscal years and URL directory years create false positives. No finite regex covers all natural-language dates.\n",
    f'All {dates["pack_count"]} pack directories and {dates["doc_count"]} documents were scanned; {len(dates["hits"])} future-date token hits.\n']
for h in dates["hits"]:
    md.append(f'### {h["file"]}:{h["line"]}\nCutoff {h["cutoff"]}; matched `{h["token"]}` ({h["format"]}).\n\n> {h["context"]}\n')
(OUT/"date_scan_hits.md").write_text("\n".join(md))
counts=collections.Counter(x["file"] for x in mentions)
runtime=[x for x in mentions if x["file"] not in ("prompts/era_e_update_for_forward_runs.md","prompts/CHANGELOG.md")]
narrow=[]
for p in [ROOT/"AGENT.md",ROOT/"prompts/02_gate1_business_quality.md",ROOT/"prompts/03_gate2_why_mispriced.md"]:
    for i,line in enumerate(p.read_text().splitlines(),1):
        if re.search(r"GGP 2008|Hertz 2024|Valeant 2015",line):narrow.append(dict(file=str(p.relative_to(ROOT)),line=i,text=line))
dump(OUT/"narrow_exception_mentions.json",narrow)
md=["# Leakage, freeze and answer-encoding audit\n",
    f"## 1. Every-pack lexical scan\nScanned **{dates['pack_count']} packs / {dates['doc_count']} documents**; **{len(dates['hits'])} date-token hits** beyond meta.as_of_date. Every context is in [date_scan_hits.md](date_scan_hits.md), machine-readable in date_scan.json. These are candidates, not {len(dates['hits'])} leaks. Guidance, debt maturities, archive URLs and fiscal-year labels account for many obvious false positives. No automatic scan proves a source was publicly available at cutoff. Partial/ambiguous dates are explicitly limited in the script.\n",
    "## 2. Semantic audit: all 11 hold-outs plus Uber calibration\nDedicated queryWithLLM calls received ONLY cutoff and full docs, not keys, outputs or grader scores. The initial joint regrade incorrectly flagged later gold sources and even misordered calendar months; those incidental semantic_leakage fields are rejected and not used. Authoritative audit records are leakage_semantic/<pack>.json. Ten dedicated checks reported no candidate finding; Meta flagged a scheduled 2026 trial and Uber flagged a later upload path. A separate model adjudication rejected the trial as future guidance/scheduling and retained only archive-provenance uncertainty. **No confirmed realized post-cutoff economic fact was identified in these 12 checks.** This is not independent source-vintage verification and not a clean-bill-of-health claim.\n",
    "Specific spot checks: Meta D05 says trials were *scheduled*, not that outcomes occurred. Uber D08 expressly says the underlying release is from 2024. CP D09 expressly preserves the two possible forward interpretations instead of supplying the later sell. These are appropriate distinctions. Current-model knowledge leakage can exist with no visibly later assertion.\n",
    "## 3. Freeze checksum\n",
    f"All **{len(hashes['entries'])} listed hashes match current bytes** ({sum(x['file'].startswith('prompts/') for x in hashes['entries'])} prompt files plus AGENT.md). Unhashed Markdown files: "+", ".join(hashes["unhashed"])+".\n",
    "Verdict: **current consistency confirmed; historical freeze chronology not independently established.** CHANGELOG explicitly says AGENT.md was synchronized after freezing and its hash was updated in the same manifest. Thus the current AGENT hash cannot certify its original pre-hold-out bytes. The staged runner does not use AGENT.md; this mitigates the sync concern for staged outputs, not one-shot replays. No per-run prompt hash, pack hash or exact internal model snapshot accompanies the benchmark outputs. Preserve immutable timestamped manifests for every run.\n",
    "## 4. Hold-out identifiers and narrow rules\n",
    f"Boundary-aware case-insensitive grep searched every hold-out meta.company/ticker/alias in AGENT.md and prompts/*.md. **{len(mentions)} pack-file-line matches**, **{len(set((x['file'],x['line']) for x in mentions))} unique lines**; excluding the forward-only addendum and CHANGELOG leaves **{len(runtime)} pack-file-line matches**. Same-company earlier examples (Nike entry, CP activism, Hilton entry, Netflix 2022) are not hold-out trade leakage. Count duplication across aliases/hold-out companies is documented in holdout_mentions.json.\n",
    "|File|Pack-file-line matches|","|---|---:|"]
for file,n in sorted(counts.items()):md.append(f"|{file}|{n}|")
md+=["\nThe forward-only addendum explicitly contains hold-out trade details and must stay excluded from historical runs. CHANGELOG names sealed pack IDs as operational bookkeeping. AGENT's biography contains 2026 vehicle information and references a February 2026 presentation; these are temporally impure for older replays even without encoding a hold-out action. AGENT's historical Nike/CP/Hilton/Netflix mentions do not establish direct hold-out answer encoding.\n",
     f"Three exception families are especially calibration-shaped: GGP asset-value-over-claims, Hertz concentrated-industry/new-management/liquidity override, and Valeant 2013–2016 platform exception. The exact three case strings occur on **{len(narrow)} lines** across AGENT and gate 1/2 prompts (narrow_exception_mentions.json). CHANGELOG v1.3/v1.4 explicitly attributes those changes to failed runs. This confirms in-sample tuning; it does not establish illegitimate hold-out tuning. Generalize and test each rule on a matched failure case and a different issuer; do not call a fitted case recovery independent fidelity.\n",
     "## 5. Identity leakage remains unresolved\n`tools/run_agent.py:load_pack` replaces company/ticker/aliases only, uses unbounded regex matching, and retains executive names, product names, geography, dates and revealing filenames/URLs. It does not implement the richer masking in research/lookahead_and_evaluation.md. Short ticker replacements can corrupt ordinary words. The runner also labels sorted documents by enumeration starting D01: packs containing D00 then shift relative to filenames; current harness provenance is insufficient to know which mapping was used in existing runs. The strict regrade uses filename Dnn IDs and flags this limitation. Freeze a citation map and do identity-recovery probes. Named–masked differences are identity sensitivity, not a causal leakage estimator.\n",
     "Stress tests are being produced separately in [stress_tests/](stress_tests/); no results are assumed here."]
(OUT/"leakage_audit.md").write_text("\n".join(md))
# Forward computations from raw JSON and Markdown separately.
markdown=(ROOT/"forward/next_trade_prediction.md").read_text();pred=json.loads((ROOT/"forward/next_trade_prediction.json").read_text())
md_candidates=[]
for line in markdown.splitlines():
    if re.match(r"\| \d+ \|",line):
        parts=[s.strip() for s in line.split("|")]
        md_candidates.append(dict(company=parts[2],p=float(parts[4]),size=float(parts[6].rstrip("%"))))
f["markdown_candidates"]=md_candidates;f["markdown_sum"]=sum(x["p"] for x in md_candidates)
f["markdown_weighted_nav_pct"]=sum(x["p"]*x["size"] for x in md_candidates)
f["json_declared_expected"]=pred["expected_new_positions_next_90_days"]
f["annual_base_ratio_raw"]=f["sum_candidate_probabilities"]/f["full_2018_2025_rate"]
f["annual_base_ratio_md"]=f["markdown_sum"]/f["full_2018_2025_rate"]
f["raw_independent_no_new"]=__import__("math").prod(1-c["probability_90d"] for c in pred["candidates"])
dump(OUT/"forward_statistics.json",f)
dump(OUT/"sell_statistics.json",dict(run_count=len(det["sells"]),
    by_action=dict(collections.Counter(r["agent"] for r in det["sells"])),
    distinct_cases=len({r["pack"] for r in det["sells"]}),
    distinct_exact=len({r["pack"] for r in det["sells"] if r["agent"]=="SELL"}),
    holdout_distinct=len({r["pack"] for r in det["sells"] if r["group"]=="holdout"}),
    holdout_exact=len({r["pack"] for r in det["sells"] if r["group"]=="holdout" and r["agent"]=="SELL"})))
md=["# Forward-prediction critique\n",
    "## 1. Forecast identity is already inconsistent — confirmed\n",
    f"`forward/next_trade_prediction.json` has **{len(pred['candidates'])} new candidates**, summing to **{f['sum_candidate_probabilities']:.2f}**, but declares expected_new_positions_next_90_days = **{f['json_declared_expected']:.2f}**. Markdown presents **{len(md_candidates)}** candidates summing to **{f['markdown_sum']:.2f}** and labels the list “agent output”. Lowe's, Chipotle and Hilton are not in the raw JSON candidates. The separately labeled principal forecast sums to **{f['principal_sum']:.2f}**. These are not one frozen forecast. The editorial contamination is not just the principal section: three names entered the supposedly raw agent presentation.\n",
    "Fix: preserve an immutable raw output; generate Markdown mechanically from it; assign separate forecast IDs to the principal and any editorial expansion. Score each against a predeclared candidate universe, including an OTHER bucket. Do not retrospectively choose whichever forecast looks best.\n",
    "## 2. Historical base rate computed from the index\n",
    "Ordinary-equity economic initiation episodes, including re-entries; exclude hedges, sponsor/fund structure, inherited SEG, updates and HHH control financing. Visa and Mastercard count as two names, unlike their combined calibration pack. The source explicitly says it is not a complete execution ledger. Some quarters are unknown; do not invent exact purchase quarters from disclosure dates.\n",
    "|Year|New-name/re-entry episodes|Quarterly annualized mean|","|---|---:|---:|"]
for y,n in f["by_year"].items():md.append(f'|{y}|{n}|{n/(3 if y=="2026" else 4):.3f}'+(" (through Q3)" if y=="2026" else "")+"|")
md += [f"\n2018–2025: **{f['full_2018_2025_new']} / 32 quarters = {f['full_2018_2025_rate']:.4f}**. Including the seven known 2026 entries through Q3: **25 / 35 = {f['through_2026_q3_rate']:.4f}**. Treat 2026 Q4 as censored at the October cutoff; the 2026 regime is unusually active, not an entire extra completed year. The raw 1.05 expectation is **{f['annual_base_ratio_raw']:.2f}×** the pre-2026 quarterly mean; the 1.35 Markdown expectation is **{f['annual_base_ratio_md']:.2f}×**. Neither is mathematically impossible, but neither is empirically calibrated by this history. There are too few and too nonstationary observations for spurious probability precision.\n",
     f"Oct 25–Jan 31 is **{f['horizon_days']} days**, not 90. Expected count is the sum of candidate marginals and need not equal one; it does not determine P(no buy) without dependence assumptions. Independent marginals would imply **{f['raw_independent_no_new']:.3f}** P(no raw-listed buy), only an illustration—not an estimated joint distribution. Shared capital and correlated narratives make independence dubious. Re-entry hypotheses should be distinguished from genuinely unfamiliar names.\n",
     "## 3. Capital: separate vehicle balances and dates\n",
     f"D06 is more careful than the forecast: PSUS's $5B was >95% deployed, not fresh October capital. $5B minus security cost $4,915,991,173 is **${f['psus_gross_minus_security_cost']:,.0f}**, but is NOT a cash balance: fees, liabilities, leverage and different observation dates prevent that inference. PSI's $852M cash/investments less $235M debt is **$617M net cash/investments**, while literal cash was $9M; equity stakes are not idle cash. HHH's $2.5–3B is multiyear projected cash, not next-quarter spending capacity. PSH exposure 126% is not a cash figure. Current uncommitted cash is **unknown**, not zero.\n",
     f"Raw marginal probabilities × target weights imply **{f['probability_weighted_nav_pct']:.2f}%** of a common NAV denominator; mechanically applying core AUM $23.0454B gives **${f['illustrative_dollars_core_bn']:.3f}B**, expressly an illustration, not a funding plan. Markdown's expanded list implies **{f['markdown_weighted_nav_pct']:.2f}%**. Actual vehicle sizing, correlated selections, exits, financing and additions must be reconciled in a cash bridge. D06 supports no claim that these amounts are available now.\n",
     "## 4. Screen-to-thesis jump\n",
     "D04 calls itself “verified prices, not a buy list” and states “Quality is a research gate, not a fact established by price.” Autodesk's risk attribution is expressly unresolved; yet the memo asserts the moat will be reinforced by AI. Copart's drawdown and net cash do not establish temporary salvage-volume pressure. Zoetis has first-two-forecast-year EPS growth −3.05%/3.75%; a cheap multiple alone cannot establish >20% IRR. D04's five-year multiple is five annual observations, not a daily average; off-52-week-high is not proof of a recent 1–6-month dislocation.\n",
     "The actual screen has no modeled IRR column. The memo's >20% labels lack an EPS/FCF bridge, terminal multiple, horizon and cash-distribution assumptions. Require annualized total return = ((terminal EPS × terminal P/E + accumulated distributions)/entry price)^(1/T)−1, with a cash-flow IRR for dated distributions, and avoid double-counting repurchases already in EPS. Show flat-multiple and compressed-multiple cases. The stored broad LLM forward reviews made unsupported references to scenario columns and treated nonholdings as falsifiers; those assertions are rejected by direct file inspection. No absent scenario numbers are reported here.\n",
     "## 5. Proposed business falsifiers (not alleged historical observations)\n",
     "|Candidate|What would falsify the stated investment mechanism|","|---|---|",
     "|Autodesk|Sustained customer retention/pricing or FCF-conversion deterioration attributable to AI workflow substitution, rather than merely a lower multiple.|",
     "|Copart|Persistent salvage-volume/share or auction-liquidity deterioration, or integration economics that destroy returns on incremental capital.|",
     "|Alphabet|Persistent search monetization/share loss to AI channels after accounting for cost to serve; inability of other segments to offset it.|",
     "|Booking|Direct AI-agent distribution captures bookings while take rate or repeat usage deteriorates despite normalized travel demand.|",
     "|Lowe's|Traffic/share and normalized margins fail to recover as housing conditions stabilize; debt-financed repurchases cannot rescue cash returns.|",
     "|Zoetis|Clinic weakness proves company-specific share/product/pricing impairment rather than a reversible end-market slowdown.|",
     "|Chipotle|Repeated traffic deterioration and weaker restaurant-level returns persist despite price/affordability adjustments; unit growth masks damaged same-store economics.|",
     "|Hilton|Owner economics/pipeline conversion and fee growth weaken structurally. Separately, no qualifying price dislocation means the proposed entry trigger never fired.|",
     "\nSet dated measurement windows and baseline values before observing results. A nonoccurrence does not logically falsify a non-unit probability; use proper scores. A thesis can be wrong even if Ackman buys; an accurate business thesis does not force him to buy.\n",
     "## 6. Observation and reconciliation\n",
     "Q3 13F covers September, before forecast origin; a November *disclosure* is not a November *trade*. Q4 13F captures Dec 31, misses Jan 2027 and intraquarter round trips, and does not reveal every derivative/foreign exposure. Separate next-disclosed-action from next-initiated-position endpoints. Obtain source-confirmed initiation dates; label censored outcomes unknown. Freeze Brier-score universe, OTHER/new-name count endpoint and a separate process-driver score. Absence from an incomplete filing is not automatically a zero.\n",
     "The principal section is clearly labeled, which is good. It is nonetheless an uncalibrated second forecast whose familiarity/re-entry thesis needs its own score, not a correction that can retroactively improve the agent. The raw-versus-Markdown additions are the confirmed contamination; the principal's private influence on the original model is not established."]
(OUT/"forward_prediction_critique.md").write_text("\n".join(md))
print(json.dumps(dict(causes=dict(causes),date_hits=len(dates["hits"]),packs=dates["pack_count"],docs=dates["doc_count"],mentions=len(mentions),unique_mention_lines=len(set((x["file"],x["line"])for x in mentions)),narrow=len(narrow),forward=f["markdown_sum"]),indent=2))
