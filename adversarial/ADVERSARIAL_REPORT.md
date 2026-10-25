# Adversarial review of the Ackman agent, frozen v1.5

## Executive summary

The repository supports a **useful, explicitly caveated historical reasoning prototype**, not demonstrated out-of-sample replication of Ackman's decisions. Its README already acknowledges current-model memory and sell-side weakness. The strongest additional findings are measurement and implementation defects, not evidence of deliberate hold-out manipulation.

- **Direction does not beat the trivial mode policy on calibration or hold-out.** With canonical action mapping and size separated, calibration is **21/28 named and masked**, versus **24/28** for BUY/new, HOLD/existing, SHORT_HEDGE/hedge. Hold-out is **7/11** for both agent conditions and the mode policy. The agent's advantage is in controls: **7/8 named, 5/8 masked** versus 0/8 for that policy, but below always-PASS's 8/8. Across all 47 decisions the agent beats the mode policy **35 versus 31 named; 33 versus 31 masked**. That is real discrimination, but controls—not the headline buy hit rate—supply it.
- **Full exits are the clearest process gap:** only **1/7 distinct sell cases** produces SELL in either condition; **0/4 hold-out exits** does. The other sell outputs are HOLD or TRIM. CP's earlier public checkpoint is genuinely underdetermined; a prompt should not be trained to manufacture its later rationale.
- **Seven original state=MATCH grades violate their own ≥75% driver threshold.** Strict source-only regrading of all **94 runs** yields a conservative, quote-validated causal recall of **65/116 calibration named and masked**, **19/41 hold-out named**, **14/41 masked**. Supported causal recall is lower: **47/116, 49/116, 15/41, 12/41**, respectively. The requested leniency statistic is **5.40 percentage points** mean original minus strict causal share on the **63 calibration/hold-out original MATCH/PARTIAL states**; the grounding-inclusive gap is **21.19 points**. Controls were additionally regraded but excluded from this primary leniency denominator. This is a second automated judgment, not human truth.
- **The staged runtime does not load AGENT.md.** In particular, its categorical Chinese-VIE exclusion is missing from the staged system/gate inputs. Calling masked Alibaba solely a model failure to follow that exclusion is unfair. The pipeline also has conflicting thresholds, action vocabularies and historical exception rules.
- **The forward forecast is not one artifact:** raw JSON has **five candidates, probability sum 1.05**, but declares **1.20 expected new names**; Markdown adds three candidates and sums to **1.35**. The principal's separate sum is **1.11**. This is a confirmed forecast-provenance defect.
- **No confirmed realized future economic fact was found by the dedicated semantic audit of 12 packs.** The complete lexical scan covered **47 packs / 364 documents**, producing **82 future-date token hits**, mostly requiring benign scheduling/fiscal/URL interpretation. All **15 listed hashes match current bytes**, but a mutable AGENT hash updated after freeze does not independently prove historical chronology.

## Contents and evidence map

1. [Baselines and per-decision predictions](baselines.md), [machine-readable](baselines.json)
2. [Strict regrade table, intervals and leniency](regrade/regrade_table.md), [per-run judgments](regrade/)
3. [Leakage, hashes, masking and overfit audit](leakage_audit.md), [all date-hit contexts](date_scan_hits.md)
4. [Every divergence and cause classification](divergence_analysis.md)
5. [Forward forecast critique and falsifiers](forward_prediction_critique.md)
6. [Exact proposed v1.6 replacement blocks and next test set](v1_6_proposals.md)
7. [Reproducible Python scripts](scripts/)
8. [Independent orchestrator stress tests](stress_tests/) — name-only recall and counterfactual flips. These are a separate evidence stream; this report neither waits for them nor assumes their results.

Paths below are relative to ackman-agent/ unless otherwise stated.

## Finding 1 — A buy-enriched benchmark makes direction fidelity look stronger than it is

**Severity: critical to interpretation. Verdict: confirmed.**

Evidence: `adversarial/baselines.json` contains every key, candidate action, baseline prediction and denominator. The mode policy needs no operating facts, no six-gate process and no imitation of Ackman's voice. It matches **24/28 calibration decisions** and **7/11 hold-out decisions**. All seven hold-out buys are matched; none of the four exits is exactly matched.

The supplied scoreboard reports 20/28 named and 19/28 masked calibration direction MATCH. Those scores mix action and conviction/size: `prompts/10_grader.md` says direction can be PARTIAL for “same side but materially different sizing/conviction.” Separating those axes yields 21/28 in each condition. Keys with SHORT, BUY_PROTECTION and SHORT_LONG_DURATION_VIA_OPTIONS are canonically mapped to the benchmark's SHORT_HEDGE output vocabulary; this is disclosed, not treated as economic equivalence between shorting and insurance.

The opposite trivial policy, always PASS, gets **8/8 controls**, but zero calibration and hold-out. Neither baseline is a universal investor. The comparison establishes sample composition and marginal discrimination, not that a one-line policy is a better investor.

**Concrete fix:** publish baseline-relative direction, full-exit recall, synthetic-control false-buy rate, causal/supported recall and a balanced fresh test. Keep action, size and conviction separate. Do not select the next test predominantly from actual buys.

## Finding 2 — Grading arithmetic and grounding are not reliable enough for the headline

**Severity: high. Verdict: confirmed arithmetic defect; likely semantic leniency, with judge uncertainty.**

Evidence: `prompts/10_grader.md` requires state MATCH when “k ≥ ceil(0.75·N).” Yet these supplied scores assign MATCH below that threshold:

- `2022_nflx_buy__current__masked`: 3/5
- `2025_amzn_buy__current__named`: 3/5
- `2025_uber_buy__current__named`: 3/5
- `ctl_2022_intc_pass__current__masked`: 2/3
- `ctl_2023_pfe_pass__current__masked`: 2/3
- both `2026_alc_buy` conditions: 3/5

See `adversarial/deterministic_findings.json`; these are rule violations independent of any new model judgment.

The original grader receives a **PACK INDEX**, not full documents (`10_grader.md`). Citation density—sentences with [Dnn] divided by sentences—is not support precision. The scores contain **317 “supported”, nine “cannot_tell”, one “unsupported” spot-check verdicts**; those labels are not verified document entailment.

The strict audit provided each final output, gold drivers and actual docs, concealed original scores/provider and evaluated each run separately. Every semantic credit requires an explicit same-polarity mechanism; every support credit requires source evidence. A pilot that enumerated candidate instead of gold drivers was discarded. After a repair pass, **15 run judgments** still contained non-verbatim evidence quotes; deterministic validation rejects those affected claims while retaining the model's raw judgment. This conservative lower-bound treatment contributes to the decline and must not be hidden.

Examples for source inspection:

- `adversarial/regrade/2026_spgi_buy__current__masked.json`: general network/regulatory barriers do not reproduce the specific profit-pool separation between benchmark businesses and AI-exposed desktops. `calibration/data_packs/2026_spgi_buy/docs/D01_business_overview.md` explicitly distinguishes those activities.
- `calibration/data_packs/2025_uber_buy/docs/D01_business_overview.md` says density observations “support, but do not prove” an advantage and AV distribution value is “an open question.” A citation to that document cannot by itself certify that AV displacement fears are false.
- Hilton's asset-light fee mechanism is genuinely present in both memo and `2018_hlt_buy/docs/D01_business_overview.md`; strictness should not erase economically equivalent paraphrases merely because the company is famous.

**Concrete fix:** compute state/count arithmetic in code; grade claim support against actual documents; preserve accepted evidence spans and key-sufficiency flags; human-double-score disputed cases. Treat regrade numbers as an audit diagnostic, not a superior unchallenged gold standard.

## Finding 3 — The executable specification differs from the advertised one

**Severity: high. Verdict: confirmed.**

Evidence: `tools/run_agent.py:main` loads AGENT only inside `if a.one_shot`; staged mode loads `00_system.md` plus individual step prompts. Therefore AGENT §5's explicit exclusion “Chinese VIEs” is not necessarily supplied to a staged run. It is absent from `00_system.md` and `02_gate1_business_quality.md`.

Other conflicts:

- `00_system.md` permits no CONTROL, while `08_sell_hold.md` permits it and AGENT lists it.
- Gate 3's new-position hurdle is approximately 20%, while `07_decision_memo.md` permits `ADEQUATE_15_20` with a credible catalyst.
- `07_decision_memo.md` says a new position is BUY/PASS; the historical Herbalife key requires a short.
- The saved gate-1 outputs include **six eight-criterion runs** and **68 nine-criterion runs**. The change log documents iterative prompt revisions, but the scoreboard calls the collection “prompts v1.5.” This is consistent with mixed versions **or** model schema noncompliance; absent per-run hashes, exact historical prompt attribution remains unresolved.

**Concrete fix:** generate both runtime modes from one dated rule source; validate action vocabulary and gate arithmetic; record a complete manifest per run; rerun all calibration decisions under the final frozen version before calling it one replay. Missing runtime instructions are not evidence of model disobedience.

## Finding 4 — Sell-side stickiness is genuine, but some exits are not publicly derivable

**Severity: high. Verdict: confirmed action gap; mixed likely causes.**

Evidence: `adversarial/deterministic_findings.json` identifies **14 sell runs**: two SELL, six HOLD, six TRIM. The two SELLs are the same Netflix-2022 case in named/masked conditions. For hold-out sells, both conditions produce two HOLDs and two TRIMs.

Berkshire's `D09_changes_since_purchase.md` explicitly says:

> “An investor can find Berkshire undervalued and still prefer a different use of limited capital.”

The agent still HOLDS. Nike's runs acknowledge a more demanding recovery yet retain HOLD. These are failures to translate relative allocation or changed predictability into a full exit, not merely missing sell keywords.

CP deserves a fairer verdict. Its March-2025 `D09_what_has_changed.md` says:

> “It is possible for the operational thesis to be progressing while prospective risk-adjusted attractiveness changes.”
>
> “The evidence does not justify replacing either possibility with hindsight.”

The key records disputed April-versus-May exit timing and later explanations. The earlier pack does not uniquely compel SELL. Forcing an answer-specific tariff rule would manufacture apparent fidelity.

**Concrete fix:** make S2/S3 evaluation precede HOLD, require comparable alternatives and forecast ranges, distinguish residual ownership from full exit, and mark public-evidence underdetermination prospectively. Add the 2026 Alphabet/UMG/Hertz exits to a newly sealed test, not to exemplars.

## Finding 5 — Controls expose weak discrimination, but are not eight observed Ackman passes

**Severity: high. Verdict: confirmed.**

Evidence: `ctl_2021_baba_pass/meta.json` calls itself:

> “Constructed discipline control, not documented historical rejection.”

That distinction applies to interpreting the control benchmark. Masked Boeing, Alibaba and Disney produce BUY; Boeing also does so named. The issue is therefore not exclusively loss of identity memory.

Boeing safety/certification uncertainty and Disney's changing streaming/legacy economics require underwriting, not a “temporary fear” label. Alibaba additionally exposes the missing runtime prohibition described above.

**Concrete fix:** retain these useful negative probes but label them constructed discipline tests. Use explicit public declines for claims about actual Ackman rejection behavior. Enforce economic risk classifications rather than company-name blacklists; test equivalent masked positive and negative cases.

## Finding 6 — Masking and freeze checks establish less than their strongest reading

**Severity: medium-high. Verdict: confirmed limitations; no confirmed hold-out tuning.**

Evidence: `run_agent.py:load_pack` substitutes only company, ticker and aliases with case-insensitive unbounded regex. Executives, brands, URLs, filenames, distinctive economics and exact dates can identify a case. Short ticker substitutions can damage ordinary words. The script also relabels sorted documents starting at D01 even where filenames start D00; citation mapping must be explicit.

There are **four calibration action disagreements**, **two control disagreements**, and **zero hold-out action disagreements** between conditions. These are identity sensitivity, not a numerical leakage estimate. Unmasked company knowledge can be helpful, harmful or outcome-contaminated.

All **15 manifest hashes** match current bytes. However, CHANGELOG says AGENT's hash was updated after synchronization; matching current bytes does not independently establish what existed before scoring. The forward-only addendum contains hold-out specifics and is deliberately outside the historical chain. Older same-company exemplars are not direct evidence of forbidden hold-out examples.

The identifier audit finds **53 pack-file-line hits on 36 unique lines**; details and exclusions are in leakage_audit.md. Three exception families—GGP, Hertz, Valeant—were explicitly added following calibration failures, with **11 exact-case mention lines** across AGENT and gates 1/2. That is confirmed in-sample tuning, not proof of hold-out contamination.

**Concrete fix:** immutable pre-run manifests, comprehensive economically preserving masking, identity-recovery tests, new-issuer tests of each exception, and independently dated checkpoint provenance. The December-2023 pretraining cutoff does not certify all later instruction tuning or clean older replays.

## Finding 7 — The forward forecast has inconsistent probabilities, provenance and an unclosed funding plan

**Severity: high for forward use. Verdict: confirmed.**

Evidence: the raw JSON and Markdown disagree on candidate membership and expected count: **1.05 actual raw sum, 1.20 declared, 1.35 Markdown**. The latter adds Lowe's, Chipotle and Hilton to the purported agent list. Separately labeled principal reconciliation is good practice, but cannot explain away additions made outside that section.

From `compendium/INDEX_2017_2026.md`, ordinary equity initiation/re-entry counts for 2018–2025 are **4, 2, 1, 3, 1, 1, 3, 3**: **18/32 = 0.5625 per quarter**. Seven 2026 entries bring the through-Q3 count to **25/35 = 0.7143**. The index is not a complete execution ledger. The raw forecast is **1.87×**, and Markdown **2.40×**, the pre-2026 quarterly mean. This is an uncalibrated regime assumption, not a mathematical contradiction. The stated Oct-25–Jan-31 horizon is **98 days**, not 90.

D06 explicitly warns “Do not add AUM to cash.” PSUS's IPO was mostly deployed, PSI net investments are not liquid cash, HHH projected cash is multiyear, and current deployable cash is unknown. Raw probability-weighted candidate weights imply **5.10%** of a common NAV denominator, or an illustrative **$1.175B** using core AUM—not a reconciled vehicle-level funding plan.

D04 expressly labels itself “verified prices, not a buy list.” It contains no modeled IRR column. Claims of >20% IRR need a growth/margin/share-count/terminal-multiple bridge, not a drawdown plus forward P/E. A 13F cannot fully score a 98-day initiation window crossing January.

**Concrete fix:** one immutable raw forecast rendered mechanically; separate principal forecast ID; coherent probability sum and horizon; vehicle-level capital bridge; business falsifiers; distinct disclosure/action endpoints and censoring rules. See forward_prediction_critique.md for candidate-by-candidate falsifiers.

## Audit boundaries and reproducibility

All changes are confined to adversarial/. No frozen prompt, AGENT.md, key or pack was modified. Scripts use Python 3 standard library; model judgments use queryWithLLM with at most four requests in flight. Original scores were concealed from strict judges. Full source docs were supplied; quote validation is deterministic. Regrade and cause classification remain single-model judgments; repeated prompts and repair passes are not independent raters.

The divergence audit covers **46 affected runs**. Its model-assigned primary categories, after the explicit runtime correction, are **one missing/ambiguous runtime rule, zero missing-fact primaries, zero key/grader primaries, 43 model-execution primaries and two genuine judgment/process differences**. These counts are **not causal identification**: the judge's tendency to blame execution is itself a limitation, and secondary pack/key issues are documented. In particular CP timing and historical lesson application deserve independent human review.

Reproduce deterministic outputs, in order:

```bash
python3 ackman-agent/adversarial/scripts/audit.py
python3 ackman-agent/adversarial/scripts/summarize.py
python3 ackman-agent/adversarial/scripts/reports.py
```

The saved inputs, strict rubric, per-run model outputs, abandoned pilot, repair records, validation failures, dedicated semantic checks and cause adjudications preserve the audit trail. Scripts do not silently rerun models or overwrite frozen v1.5 assets. Wilson intervals are descriptive; drivers and named/masked runs are not independent investment decisions.

**Bottom line:** v1.6 should prioritize executable-rule consistency, honest evidence/grade validation, comparative sell discipline and a balanced genuinely fresh test. More Ackman-like vocabulary or additional famous-case exceptions would improve resemblance without establishing fidelity.


---

## Addendum (orchestrator, 2026-10-25, after the report above was written) — stress-test results

Independent behavioural probes on the frozen v1.5 chain, documented in [stress_tests/RESULTS.md](stress_tests/RESULTS.md)
with raw outputs in stress_tests/runs/ and injected documents in stress_tests/packs/:

1. Name-only recall probe (empty pack, real name): 6/6 PASS, low conviction, size 0 — the grounding rule holds.
2. Counterfactual flips (a superseding D00 document violating one gate): 1 of 4 buys flipped (Uber, leverage). Hilton, Chipotle
   and Netflix stayed BUY/high/8%; in the Chipotle and Netflix runs gate 1 returned hard_fail=true and step 7 still issued BUY.
   This is direct evidence for Finding 5's "executable-rule consistency": the memo stage overrides upstream gates.
3. Masking is not blinding: the final output names the true company in 31 of 47 name-masked runs (3 masking residues, 28 inferred).
4. Misattribution: relabelling masked packs with a wrong famous name flipped 2 of 3 BUYs to PASS with the evidence unchanged.
5. Repeatability: two borderline controls were BUY in 2 of 3 fresh runs each (coin-flips); the CP 2025 sell was HOLD in 4 of 4
   (stable divergence).

These results are consistent with Findings 1-5 and sharpen the v1.6 priorities: (a) enforce hard_fail in code; (b) a
"document conflicts" field in the fact sheet that gates must resolve; (c) triplicate runs on controls and sells with majority
reporting; (d) relabel "masked" as "name-masked" everywhere; (e) the pre-dated Llama 3.1 8B replay remains the only clean
fidelity test for post-2023 packs.
