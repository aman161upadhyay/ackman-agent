# Prompt chain for the Ackman agent

The chain exists because the target model is small (Llama 3.1 8B). One decision = 7 short calls, each with a
JSON output that is passed to the next call. A strong model can run the whole thing from AGENT.md in one call
(use prompts/one_shot_full.md), but the staged chain scores better on grounding with small models.

| # | file | input | output |
|---|---|---|---|
| 0 | 00_system.md | — | system prompt for every call (identity, rules, era switch) |
| 1 | 01_fact_sheet.md | pack docs | structured, cited fact sheet (normalises the pack) |
| 2 | 02_gate1_business_quality.md | fact sheet | 8 criteria PASS/FAIL/UNSURE + hard_fail |
| 3 | 03_gate2_why_mispriced.md | fact sheet + gate1 | opportunity template T1-T7 + evidence, or PASS |
| 4 | 04_gate3_valuation.md | fact sheet + gate2 | EPS path, terminal multiple, IRR, downside |
| 5 | 05_gate4_catalyst_role.md | all prior | catalyst class C0-C4 + plan |
| 6 | 06_gate5_risk_sizing.md | all prior | kill criteria, size, liquidity, hedge overlay |
| 7 | 07_decision_memo.md | all prior | final JSON (schema_decision.json) + memo in letter voice |
| alt | 08_sell_hold.md | pack for an existing position | SELL/HOLD/ADD/TRIM with reason class S1-S5 |
| alt | 09_hedge.md | macro pack | SHORT_HEDGE / NO_HEDGE with asymmetry maths |
| eval | 10_grader.md | agent JSON + answer key | rubric scores (direction, reasoning overlap, discipline, grounding) |
| eval | 11_leakage_check.md | agent output + as_of | flags any post-date fact |
| fwd | 12_forward_next_trade.md | current library + market pack | ranked next-trade candidates with probabilities |

Conventions: pack documents are labelled D01, D02, ... in the order given; every factual sentence ends with [Dnn].
Temperature 0-0.2. Use JSON mode where the runtime supports it. Keep each call's context < 12k tokens for 8B models.
