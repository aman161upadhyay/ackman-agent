# Stress tests on the frozen v1.5 Ackman agent (orchestrator-run, 2026-10-25)

All runs use the frozen v1.5 prompt chain on the same current internal model used for the scoreboard; raw outputs (all stages) are in `runs/`. These are behavioural probes, not scoreboard results, and nothing in `prompts/` or `AGENT.md` was changed.

## 1. Name-only recall probe (does the agent decide from memory when the pack is empty?)
Pack replaced by a single document saying no documents were supplied; company name, ticker and date kept (named mode).

| pack | decision | conviction | size | first driver |
|---|---|---|---|---|
| 2025_uber_buy | PASS | low | 0 | The provided data pack contains no information regarding the business, which prevents any  |
| 2022_nflx_buy | PASS | low | 0 | The provided data pack contains no information regarding the business, valuation, or marke |
| 2018_hlt_buy | PASS | low | 0 | not in pack |
| 2016_cmg_buy | PASS | low | 0 | The provided data pack contains no information regarding the business, financial performan |
| 2026_msft_buy | PASS | low | 0 | The provided pack contains no operational or financial data for Microsoft, making it impos |
| ctl_2022_dis_pass | PASS | low | 0 | The data pack is empty, rendering it impossible to evaluate the business against our quali |

**Result: 6/6 PASS with low conviction and size 0.** The grounding rule ("not in pack" beats memory) holds: with no evidence the agent refuses to act, including on names it has strong priors about (Uber, Netflix, Microsoft). This is the positive control for the next probes.

## 2. Counterfactual flips (does a gate-violating fact change the decision?)
A dated document D00 ("supersedes all other documents where they conflict") was prepended to the masked pack, stating facts that violate one of the agent's own gates. The texts are in `packs/flip__*__D00.md`.

| pack (masked) | injected violation | original masked decision | decision after injection | gate1 hard_fail flag | verdict |
|---|---|---|---|---|---|
| 2025_uber_buy | net debt 6.1x EBITDA, negative FCF, covenant waiver (Gate 1 leverage/FCF) | BUY | **PASS** (high, 0%) | true | flipped as it should |
| 2018_hlt_buy | RevPAR -9% for 3rd year, negative unit growth, franchisees not renewing, pricing power lost (Gate 1 durability) | BUY | **BUY** (high, 8%) | false | DID NOT FLIP |
| 2016_cmg_buy | five-year category decline predating food safety, 14 cheaper entrants, structural margin loss, no pricing power (Gate 2: not a temporary problem) | BUY | **BUY** (high, 8%) | true | DID NOT FLIP |
| 2022_nflx_buy | 62x earnings, negative FCF through 2024, buyback suspended, margin compression (Gate 3 valuation) | BUY | **BUY** (high, 8%) | true | DID NOT FLIP |

**Result: 1 of 4 flipped.** Only the balance-sheet violation (Uber) changed the decision. For Hilton, Chipotle and Netflix the fact sheet captured parts of the injected facts (e.g. "RevPAR -9%", "pricing power", "buyback suspended") but the gates and the memo kept the original bullish narrative; in the Chipotle and Netflix runs **gate 1 returned `hard_fail: true` and the decision memo still issued BUY / high / 8%** — the final stage does not enforce upstream gate results. Two defects: (a) one contradicting document is out-voted by eight confirming ones instead of being weighed on its content; (b) `07_decision_memo` can override `hard_fail`. Fix for v1.6: make `hard_fail: true` terminate the chain with PASS (code-level, not prompt-level) and require the fact sheet to carry an explicit "conflicts between documents" field that gates must resolve.

## 3. Masking is not blinding (identity inference)
For every masked run on the scoreboard (47 = 28 calibration + 8 controls + 11 hold-out) the agent's final JSON was searched for the true company name, ticker or alias from `meta.json`.

- Final output names the true company in **31 of 47 masked runs (66%)**.
- In 3 of those the masked pack itself still contained the name (masking residue: General Growth, Howard Hughes, Intercontinental Exchange — aliases missing from `meta.json`).
- In **28** the pack contained no residue: the model inferred the identity from the business description (brands, products, geography) and wrote it into the memo.

Consequence: the "masked" column of the scoreboard is **not** an estimate of what a model ignorant of the company would do; it is at best a mild handicap. For a current model the named/masked gap (71% vs 68% direction) understates memory contamination. The only clean fidelity test remains the pre-dated Llama 3.1 8B replay on packs dated after December 2023, as the README already states — the stress test makes that caveat quantitative.

Per-run list: 2005_mcd_buy [inferred by model]; 2007_tgt_buy [inferred by model]; 2008_ggp_buy [residue in masked pack: General Growth/General Growth Properties]; 2010_jcp_buy [inferred by model]; 2012_hlf_short [inferred by model]; 2013_fnma_buy [inferred by model]; 2015_vrx_buy [inferred by model]; 2016_cmg_buy [inferred by model]; 2018_hlt_buy [inferred by model]; 2018_low_buy [inferred by model]; 2020_brk_sell [inferred by model]; 2021_umg_buy [inferred by model]; 2022_nflx_buy [inferred by model]; 2022_nflx_sell [inferred by model]; 2023_googl_buy [inferred by model]; 2024_nke_buy_b [inferred by model]; 2025_amzn_buy [inferred by model]; 2025_cmg_sell [inferred by model]; 2025_cp_sell [inferred by model]; 2025_fnma_fmcc_2025 [inferred by model]; 2025_hhh_control [residue in masked pack: Howard Hughes]; 2025_meta_buy [inferred by model]; 2025_nke_sell [inferred by model]; 2025_uber_buy [inferred by model]; 2026_ice_buy [residue in masked pack: Intercontinental Exchange]; 2026_msft_buy [inferred by model]; ctl_2019_ba_pass [inferred by model]; ctl_2022_cvna_pass [inferred by model]; ctl_2022_dis_pass [inferred by model]; ctl_2022_intc_pass [inferred by model]; ctl_2023_pfe_pass [inferred by model]

## 4. Misattribution probe (does the name override the evidence?)
Masked packs were relabelled with a wrong, famous name (name substituted for "the Company" throughout).

| true pack | relabelled as | original masked decision | decision under wrong name | reading |
|---|---|---|---|---|
| 2025_uber_buy | BABA | BUY | **PASS** (low) | Uber's facts under Alibaba's name became a PASS: the label changed the answer |
| 2018_hlt_buy | BA | BUY | **PASS** (high) | Hilton's facts under Boeing's name became a PASS: the label changed the answer |
| 2016_cmg_buy | INTC | BUY | **BUY** (high) | Chipotle's facts kept their BUY under Intel's name (content won; memo still talks about food safety) |
| ctl_2022_dis_pass | HLT | BUY (false positive) | **BUY** (medium) | Disney control stayed a false BUY under Hilton's name |
| ctl_2021_baba_pass | UBER | BUY (false positive) | **PASS** (low) | Alibaba control became PASS under Uber's name — see the repeat test: this case is noisy |

**Result: in 2 of 3 relabelled buy cases the wrong name flipped a BUY into a PASS** while the evidence was unchanged. The agent is partly name-driven in named mode — consistent with probe 3. The Llama replay, canary checks and a required "identity-independent" justification field are the mitigations.

## 5. Repeatability (how much of MATCH/MISS is sampling noise?)
Three fresh masked runs of two borderline controls and one sell.

| pack | original | run 1 | run 2 | run 3 |
|---|---|---|---|---|
| ctl_2021_baba_pass | BUY | BUY | PASS | BUY |
| ctl_2022_dis_pass | BUY | BUY | BUY | PASS |
| 2025_cp_sell | HOLD | HOLD | HOLD | HOLD |

**Result: the two control false positives are coin-flips (BUY in 2 of 3 repeats each), while the CP sell is a stable divergence (HOLD in 4 of 4).** Single-run scoring therefore overstates precision on borderline cases. v1.6 protocol: run every control and every sell three times and report the majority decision plus the disagreement rate; treat a case as a defect only if it fails in >=2 of 3.

## What this changes in the headline numbers
- Direction match on buy-only packs is close to the trivial baseline (see `../baselines.md`); the informative decisions are the 8 controls, the 6 sells and the 2 error cases, and those are exactly where probes 2, 4 and 5 show name sensitivity, gate overrides and noise.
- The masked column should be relabelled "name-masked" in every table; "blind" is reserved for the Llama 3.1 8B replay on post-2023 packs.
- The three defects that matter for v1.6, in order: hard-fail enforcement in code; conflict handling in the fact sheet; triplicate runs on controls and sells.
