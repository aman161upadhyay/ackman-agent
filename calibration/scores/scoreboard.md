# Scoreboard — replay of Pershing Square decisions (prompts v1.5, model: Replit internal current model)

> **Read this first.** These runs use the *current* internal model, which has training data that may include the outcomes of
> every calibration trade and most hold-out trades. They measure **prompt compliance and process plausibility** — whether the
> chain of gates produces Ackman-shaped decisions and reasons from a point-in-time pack — not true out-of-sample fidelity.
> Fidelity evidence requires re-running `tools/run_agent.py` with the pre-dated Llama 3.1 8B (data to Dec 2023) on the
> Mac Mini: for every pack dated 2024-2026 that model cannot know the answer. The **masked** runs (company name and ticker
> replaced by "the Company") are the closer proxy for that condition here; where named and masked disagree, memory is suspected.

Generated 2026-10-25. Scores: `calibration/scores/` (calibration) and `calibration/scores/holdout/` (sealed set, run once
after the prompt freeze; prompts were never edited from hold-out results — see `prompts/CHANGELOG.md` and
`calibration/PROMPT_HASHES_v1.5.txt`). Grader: `prompts/10_grader.md`; grounding share computed in code (sentences with a [Dnn] tag ÷ sentences).

## Summary (95% Wilson intervals)

| Set | n | Direction MATCH | Direction PARTIAL | Direction MISS | State MATCH | State PARTIAL | Driver overlap k/N | Grounding (mean share) | Leakage flags |
|---|---|---|---|---|---|---|---|---|---|
| calibration named | 28 | 20 (71% [53%, 85%]) | 3 | 5 | 16 (57% [39%, 73%]) | 6 | 67/116 (58% [49%, 66%]) | 0.58 | 0 |
| calibration masked | 28 | 19 (68% [49%, 82%]) | 4 | 5 | 12 (43% [27%, 61%]) | 11 | 69/116 (59% [50%, 68%]) | 0.55 | 1 |
| discipline controls named | 8 | 7 (88% [53%, 98%]) | 0 | 1 | 7 (88% [53%, 98%]) | 0 | 19/22 (86% [67%, 95%]) | 0.64 | 0 |
| discipline controls masked | 8 | 5 (63% [31%, 86%]) | 0 | 3 | 5 (63% [31%, 86%]) | 0 | 13/22 (59% [39%, 77%]) | 0.66 | 0 |
| hold-out named | 11 | 7 (64% [35%, 85%]) | 2 | 2 | 4 (36% [15%, 65%]) | 5 | 20/41 (49% [34%, 64%]) | 0.50 | 0 |
| hold-out masked | 11 | 7 (64% [35%, 85%]) | 2 | 2 | 4 (36% [15%, 65%]) | 5 | 22/41 (54% [39%, 68%]) | 0.51 | 0 |

Definitions: *direction* = same action as Ackman (BUY≈ADD; TRIM vs SELL = PARTIAL); *state* MATCH = direction MATCH and ≥75% of
Ackman's stated drivers reproduced; *driver overlap* = Ackman's stated reasons (from letters/X/presentations, in the answer key)
that the agent independently gave, pooled.

## Per-decision results

| Pack | Set | Agent decision (named / masked) | Named dir / state | Named k/N | Masked dir / state | Masked k/N | Grounding N / M |
|---|---|---|---|---|---|---|---|
| 2005_mcd_buy | calib |  /  | MATCH / PARTIAL | 0/4 | MATCH / PARTIAL | 2/4 | 0.46 / 0.31 |
| 2007_tgt_buy | calib |  /  | MISS / MISS | 1/4 | MATCH / MATCH | 3/4 | 0.43 / 1.00 |
| 2008_ggp_buy | calib |  /  | MATCH / MATCH | 3/4 | MATCH / PARTIAL | 2/4 | 0.33 / 0.23 |
| 2010_jcp_buy | calib |  /  | MISS / MISS | 0/4 | MISS / MISS | 0/4 | 0.55 / 0.50 |
| 2011_cp_buy | calib |  /  | MATCH / MATCH | 3/4 | MATCH / MATCH | 3/4 | 0.36 / 0.50 |
| 2012_hlf_short | calib |  /  | MATCH / MATCH | 3/4 | MATCH / PARTIAL | 2/4 | 1.00 / 0.22 |
| 2013_apd_buy | calib |  /  | MATCH / MATCH | 3/4 | MATCH / MATCH | 3/4 | 0.44 / 0.46 |
| 2013_fnma_buy | calib |  /  | PARTIAL / PARTIAL | 3/4 | PARTIAL / PARTIAL | 2/4 | 0.56 / 0.36 |
| 2015_vrx_buy | calib |  /  | MATCH / MISS | 1/4 | MATCH / PARTIAL | 2/4 | 0.63 / 0.89 |
| 2016_cmg_buy | calib |  /  | MATCH / MATCH | 3/4 | MATCH / PARTIAL | 2/4 | 0.38 / 0.36 |
| 2018_hlt_buy | calib |  /  | MATCH / MATCH | 4/4 | MATCH / MATCH | 4/4 | 0.58 / 1.00 |
| 2018_low_buy | calib |  /  | MATCH / MATCH | 3/4 | MATCH / MATCH | 3/4 | 0.38 / 0.27 |
| 2020_brk_sell | calib |  /  | MISS / MISS | 0/3 | MISS / MISS | 0/3 | 1.00 / 1.00 |
| 2020_cds_hedge | calib |  /  | MATCH / MATCH | 4/4 | MATCH / MATCH | 4/4 | 0.17 / 0.40 |
| 2020_sbux_sell | calib |  /  | PARTIAL / PARTIAL | 2/3 | PARTIAL / PARTIAL | 1/3 | 0.33 / 0.36 |
| 2021_umg_buy | calib |  /  | MATCH / MATCH | 4/5 | MISS / MISS | 3/5 | 0.50 / 0.23 |
| 2022_nflx_buy | calib |  /  | MATCH / PARTIAL | 2/5 | MATCH / MATCH | 3/5 | 0.60 / 0.92 |
| 2022_nflx_sell | calib |  /  | MATCH / MATCH | 3/4 | MATCH / PARTIAL | 2/4 | 1.00 / 1.00 |
| 2023_googl_buy | calib |  /  | MATCH / MATCH | 4/4 | MATCH / MATCH | 3/4 | 0.53 / 0.83 |
| 2023_tsy_short | calib |  /  | PARTIAL / PARTIAL | 3/4 | PARTIAL / PARTIAL | 3/4 | 0.89 / 1.00 |
| 2024_bn_buy | calib |  /  | MATCH / MATCH | 3/4 | MATCH / MATCH | 3/4 | 0.67 / 0.33 |
| 2024_htz_buy | calib |  /  | MISS / MISS | 0/5 | MATCH / MATCH | 4/5 | 0.23 / 0.27 |
| 2024_nke_buy_a | calib |  /  | MATCH / MATCH | 3/4 | MISS / MISS | 3/4 | 0.38 / 1.00 |
| 2024_nke_buy_b | calib |  /  | MATCH / MATCH | 3/4 | MATCH / MATCH | 3/4 | 0.86 / 0.27 |
| 2025_amzn_buy | calib |  /  | MATCH / MATCH | 3/5 | MATCH / MATCH | 4/5 | 0.92 / 0.64 |
| 2025_cmg_sell | HOLD-OUT |  /  | PARTIAL / PARTIAL | 1/3 | PARTIAL / PARTIAL | 1/3 | 0.22 / 0.22 |
| 2025_cp_sell | HOLD-OUT |  /  | MISS / MISS | 0/3 | MISS / MISS | 1/3 | 0.22 / 0.18 |
| 2025_fnma_fmcc_2025 | calib |  /  | MATCH / PARTIAL | 3/5 | MATCH / PARTIAL | 2/5 | 1.00 / 0.20 |
| 2025_hhh_control | calib |  /  | MISS / MISS | 0/4 | MISS / MISS | 0/4 | 0.38 / 0.42 |
| 2025_meta_buy | HOLD-OUT |  /  | MATCH / PARTIAL | 2/4 | MATCH / PARTIAL | 2/4 | 1.00 / 0.58 |
| 2025_nke_sell | HOLD-OUT |  /  | MISS / MISS | 1/3 | MISS / MISS | 1/3 | 0.10 / 0.11 |
| 2025_uber_buy | calib |  /  | MATCH / MATCH | 3/5 | PARTIAL / PARTIAL | 3/5 | 0.69 / 0.36 |
| 2026_alc_buy | HOLD-OUT |  /  | MATCH / MATCH | 3/5 | MATCH / MATCH | 3/5 | 0.57 / 0.42 |
| 2026_hlt_sell | HOLD-OUT |  /  | PARTIAL / PARTIAL | 1/3 | PARTIAL / PARTIAL | 1/3 | 0.80 / 0.90 |
| 2026_ice_buy | HOLD-OUT |  /  | MATCH / MATCH | 3/4 | MATCH / MATCH | 3/4 | 0.46 / 0.62 |
| 2026_msft_buy | HOLD-OUT |  /  | MATCH / PARTIAL | 1/4 | MATCH / PARTIAL | 1/4 | 1.00 / 1.00 |
| 2026_nflx_buy_2 | HOLD-OUT |  /  | MATCH / PARTIAL | 2/4 | MATCH / PARTIAL | 2/4 | 0.53 / 0.75 |
| 2026_spgi_buy | HOLD-OUT |  /  | MATCH / MATCH | 3/4 | MATCH / MATCH | 3/4 | 0.31 / 0.39 |
| 2026_v_ma_buy | HOLD-OUT |  /  | MATCH / MATCH | 3/4 | MATCH / MATCH | 4/4 | 0.31 / 0.42 |
| ctl_2019_ba_pass | control |  /  | MISS / MISS | 0/3 | MISS / MISS | 0/3 | 1.00 / 0.23 |
| ctl_2020_xom_pass | control |  /  | MATCH / MATCH | 3/3 | MATCH / MATCH | 3/3 | 1.00 / 0.80 |
| ctl_2021_baba_pass | control |  /  | MATCH / MATCH | 2/2 | MISS / MISS | 0/2 | 0.69 / 1.00 |
| ctl_2022_cvna_pass | control |  /  | MATCH / MATCH | 3/3 | MATCH / MATCH | 3/3 | 0.46 / 0.50 |
| ctl_2022_dis_pass | control |  /  | MATCH / MATCH | 2/2 | MISS / MISS | 0/2 | 0.92 / 0.55 |
| ctl_2022_intc_pass | control |  /  | MATCH / MATCH | 3/3 | MATCH / MATCH | 2/3 | 0.22 / 0.91 |
| ctl_2023_el_pass | control |  /  | MATCH / MATCH | 3/3 | MATCH / MATCH | 3/3 | 0.33 / 0.92 |
| ctl_2023_pfe_pass | control |  /  | MATCH / MATCH | 3/3 | MATCH / MATCH | 2/3 | 0.50 / 0.33 |

## What the loop found (calibration → prompt changes, all logged in prompts/CHANGELOG.md)

1. **Buys of quality on dislocation are the easy part.** Every Era D/E "quality compounder on a scare" pack (Alphabet 2023,
   Hilton 2018, Lowe's 2018, Chipotle 2016, UMG 2021, Amazon/Uber/Nike/Brookfield 2024-25, and on the sealed set Visa/Mastercard,
   S&P Global, ICE, Alcon 2026) came back BUY with 3-4 of Ackman's 4-5 stated reasons, named or masked.
2. **The agent is stickier than Ackman.** On sells it under-reacts: CP 2025 (HOLD vs SELL for tariff/opportunity-cost reasons),
   Nike 2025 (HOLD vs SELL after re-underwriting the repair cost), Berkshire 2020 (HOLD vs SELL "we can be more nimble"), and it
   says TRIM where he sold outright (Starbucks 2020, Hilton 2026, Chipotle 2025). Ackman's sell reasons are often comparative
   judgments (a better use of capital; a distribution of outcomes that became too wide) that a pack states weakly.
   Prompt v1.4 added the comparative S3 test; it did not fix Berkshire. This is the main open fidelity gap.
3. **Era rules matter and are now explicit.** Masked GGP 2008 and Hertz 2024 came back PASS until the spec operationalised the
   asymmetric distressed/levered-equity template (T8, v1.3-v1.4); masked Valeant 2015 came back PASS under modern rules until
   the era-C "platform" template (T9, retired 2017) was added — the spec now reproduces both the 2015 decision and the rule change.
4. **Named vs masked divergence flags memory.** GGP 2008 (named BUY / masked PASS before v1.3), Target 2007 (named PASS /
   masked BUY), UMG 2021 (named BUY / masked PASS), Valeant 2015 (named BUY / masked PASS before v1.4). Treat named-run matches
   on famous trades with suspicion; masked results are the ones to compare with the Llama replays.
5. **Judgment-heavy specifics are missed even when direction is right**: recruiting Hunter Harrison by name (CP 2011),
   "act promptly on thesis-inconsistent information" (Netflix 2022), the McOpCo IPO mechanics (McDonald's 2005), the
   Treasury-warrant alignment (Fannie 2013). Prompts v1.2 nudged two of these; the rest are left as measured gaps.
6. **Grounding varies 0.1-1.0 with identical instructions** — a model property, not a prompt property. A citation-density rule
   (v1.3) raised the floor only slightly. On an 8B model expect lower; `tools/grade.py` reports it per run.
7. **Discipline controls (8 names Ackman never bought at value-looking moments: Intel 2022, Boeing 2019, Disney 2022, Alibaba 2021,
   Carvana 2022, Exxon 2020, Estée Lauder 2023, Pfizer 2023).** Named: 7/8 PASS (Boeing → BUY). Masked: 5/8 PASS — Boeing, Alibaba
   and Disney came back BUY as "temporary fears". With the name hidden the agent loses the pass rules it should have applied
   (a safety/certification binary is not a temporary scare; a China VIE is uninvestable for Pershing; streaming losses plus
   linear decline widen the forecast range). This is the clearest prompt defect found tonight and the first item for v1.6
   (make Gate 1 criterion 3 ask explicitly: "is the fear a regulatory/safety/legal binary or a jurisdiction Pershing cannot
   influence?"). It was NOT fixed tonight because the prompts were frozen for the hold-out runs.
8. **Zero leakage flags** on hold-outs (one false positive on calibration): the point-in-time packs built by the research
   workers held, and the agent did not visibly use post-cutoff facts even when it probably knew them.

## Divergence table (where the modern process and Ackman's actual decision differ — reported, not "fixed")

| Decision | Agent under 2024-26 rules | Ackman then | Why they differ |
|---|---|---|---|
| Valeant 2015 | PASS (leverage + acquisition-dependent growth) | BUY, ~20% | Era-C platform thesis; retired after the loss (lesson table, AGENT.md §6) |
| J.C. Penney 2010 | PASS (retail turnaround needing a new customer) | BUY, activist, ~18% | Post-mortem rule "no retail turnarounds that need customers to change behaviour" |
| Herbalife 2012 | SHORT only under Era B/C rules; PASS after 2018 | SHORT, $1B | 2018 rule: no public shorts |
| Berkshire 2020 sell | HOLD | SELL (S3) | Comparative-nimbleness judgment weakly represented in packs |

## How to turn this into fidelity evidence (the Mac Mini run)
```
python tools/run_agent.py --model llama3.1:8b --pack calibration/data_packs/2025_uber_buy --mask   # masked, staged chain
python tools/grade.py  calibration/runs/<run>.json calibration/answer_keys/2025_uber_buy.json
python tools/scoreboard.py calibration/scores > calibration/scores/scoreboard_llama.md
```
Run every pack dated after 2023-12 (the model's cutoff) first; those are the genuinely out-of-sample replays. Keep the hold-out
scores in `calibration/scores/holdout/` and never edit prompts from them.
