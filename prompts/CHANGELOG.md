# Prompt change log (every change names the calibration case that motivated it)

## v1.1 — 2026-10-25 (after first current-model run on 2025_uber_buy)
- 07_decision_memo: drivers must cover the five reason-types Pershing letters use (quality, why-now/price, management,
  earnings path, variant perception). Motivation: Uber run omitted the management driver (Dara) and the price/dislocation
  driver, both of which Ackman stated explicitly (X post 2025-02-07).
- 06/07: explicit sizing bands by conviction for 2018+ (high 8-12%, medium 4-7%, starter 1-3%, options 2-5%). Motivation:
  Uber run sized 4% with "high" conviction; the actual position was ~8-12% at cost.
- 10_grader: grounding share is now computed in code (tools/grade.py and the JS harness); the grader only spot-checks
  citations and flags leakage. Motivation: the LLM grader returned claims=0 instead of counting.

## v1.0 — 2026-10-25
- Initial AGENT.md and prompt chain written from the archive (letters to mid-2025) before any pack was run.

## v1.2 — 2026-10-25 (after runs on 2025_amzn_buy, 2022_nflx_sell, 2011_cp_buy)
- AGENT.md Gate 1 and 02_gate1 now use Pershing's published eight core principles (Jan 2018 slide, Feb 2026 presentation)
  verbatim as criterion names, plus "durable growth runway". Motivation: fidelity to the firm's own checklist; the archive
  worker recovered the slide.
- 05_gate4: for T2/C3 theses, name the specific operator if the pack contains one. Motivation: CP run said "new leadership"
  without naming Hunter Harrison although the pack documented his record.
- 08_sell_hold: S2/S4 sells must state the predictability mechanism and the "act promptly" rule. Motivation: Netflix 2022 run
  missed two of Ackman's four stated reasons (operating leverage sensitivity; act promptly on thesis-inconsistent information).
- AGENT.md references archive/02_reasoning_patterns.md (20 patterns) as the pattern vocabulary for memos.

## v1.3 — 2026-10-25 (after runs on 2024_nke_buy_b, 2024_bn_buy, 2022_nflx_buy, 2008_ggp_buy)
- 03_gate2: new template T8 asymmetric distressed/levered equity (GGP 2008, Hertz 2024) requiring an asset-value/earnings-power
  vs claims line. 02_gate1: special-situation override when only the financial-profile criteria fail. 07: decision logic and
  sizing (1-5% at cost) for T8. Motivation: masked GGP run → PASS (hard fail on leverage) while named run → BUY; the named run
  may have used memory, the masked run exposed that the spec did not operationalise the asymmetric distressed template.
- 07: memo citation density rule (≥2 citations per paragraph; every numeric sentence cited). Motivation: grounding share ranged
  0.27-0.92 across runs with identical instructions.

## v1.4 — 2026-10-25 (after runs on 2015_vrx_buy, 2024_htz_buy, 2023_googl_buy, 2020_brk_sell, 2024_nke_buy_a)
- 03_gate2: template T9 "platform value", allowed only for AS_OF 2013-2016 and documented as retired in 2017. 02_gate1: matching
  era-C exception. Motivation: Valeant 2015 masked run → PASS by modern rules (correct for today's process) but the era switch
  did not represent the 2013-16 platform thesis that Ackman actually used; the spec now reproduces both and documents the
  retirement (the divergence is the finding).
- 02_gate1: special-situation override (b) for levered turnarounds in concentrated industries with proven new management
  (Hertz 2024), capped at 1-5% of NAV. Motivation: both Hertz runs → PASS; Pershing bought a ~1-2% asymmetric position.
- 08_sell_hold: S3 comparative test (position IRR vs alternatives in the pack; "proxy" holdings). Motivation: Berkshire 2020 runs
  → HOLD; Ackman sold to redeploy into higher-return direct holdings ("we can be more nimble").
- 07: in mode "new" the decision is BUY or PASS. Motivation: Nike-a masked run returned HOLD for a new position.

## v1.5 — 2026-10-25 (FROZEN before any hold-out run)
- 08_sell_hold: CONTROL action (C4) for long-held discounted positions where Pershing supplies capital and management.
  Motivation: HHH 2025 runs → HOLD; the vocabulary had no control action.
- 09_hedge: explicit drivers array for grading consistency. Motivation: 2020 CDS runs graded from memo only.
- Prompts frozen at this version for the sealed hold-out runs (2025_meta_buy, 2026_msft_buy, 2026_hlt_sell, 2025_cp_sell,
  2026_nflx_buy_2, 2025_cmg_sell, 2025_nke_sell and any later 2026 packs). No prompt edits after this point tonight.

## v1.5 note — AGENT.md synchronised after the freeze (documentation only)
- AGENT.md header, Gate 1 override text, T8/T9 templates, CONTROL action and output contract were brought in line with
  prompts v1.3-v1.5. The staged chain used by every run reads prompts/*.md, whose hashes in calibration/PROMPT_HASHES_v1.5.txt
  are unchanged; AGENT.md's hash was updated in the same file. No logic was changed in response to hold-out results.

## Runner 1.5.1 — 2026-10-31 (tools only; no prompt or AGENT.md text changed, hashes unchanged)
- run_agent.py masking: word-boundary, longest-first replacement; single-word names case-sensitive (plus ALL-CAPS), tickers
  case-sensitive, one-letter tickers only in ticker contexts; list tickers supported (2026_v_ma_buy crashed); "X and Y"
  companies also mask X and Y; residue report of name fragments still visible (`--check-mask`). Motivation: v1.5 masking
  mangled ordinary words in 29 of 47 packs ("cash flow" -> "cash fthe Company" for LOW). Masked v1.5 runs are not comparable.
- run_agent.py document labels now follow the filename's Dnn (9 packs start at D00 and were shifted by one under v1.5).
- run_agent.py applies 02_gate1's hard-fail rule and 07's deterministic decision rules in code; the model's own call is kept
  in final.model_decision. Motivation: in 41 of 74 v1.5 calibration runs gate1 returned hard_fail=true and most memos
  still bought (CMG/NFLX flip tests). Enforcement changes historical results; grade both calls before comparing to v1.5.
- Provenance per run: runner version, Ollama model digest, prompt SHA-256s vs PROMPT_HASHES_v1.5.txt, pack hash.
- grade.py requires --model (was defaulting to the 8B model under test) and takes --decision enforced|model.
- cutoff_probe.py added; canary.py documented as a grounding check. All tools read and write UTF-8.
