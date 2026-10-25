STEP 2 — GATE 1: IS THIS A PERSHING SQUARE BUSINESS? AS_OF_DATE: {{as_of_date}}.

Using only the fact sheet, score each criterion PASS, FAIL or UNSURE with one sentence of evidence and citations.

Criteria (Pershing Square's published core principles, Jan 2018 slide, plus "durable growth" from the 2019-2026 letters):
1 simple_predictable_fcf — can cash flows be forecast 5-10 years out with confidence, and does the business convert earnings to
  free cash flow with low maintenance capex and pricing power? (recurring, contractual, franchise, network-effect, subscription,
  royalty economics = PASS; hits/fashion, commodity prices, binary science, fast obsolescence, consumer-behaviour turnarounds = FAIL)
2 barriers_to_entry — #1/#2 position; scale, brand, network effects, switching costs, licences
3 limited_extrinsic_exposure — not hostage to commodity prices, rate direction, FX or a single regulator
  (exception: a bounded political/regulatory option can be the thesis — mark UNSURE and say so)
4 strong_financial_profile — investment-grade-like leverage, no refinancing cliff; high leverage + acquisition-dependent growth = FAIL
5 minimal_capital_markets_dependency — the plan does not require issuing equity or rolling debt in a difficult market
6 large_market_cap — large and liquid enough for a 5-20% position for a fund of the era's size (2018+: usually >=$10B; smaller only
  with an asymmetric special reason)
7 attractive_valuation_screen — multiple below the company's own history and/or the S&P 500 for its quality, or a sum-of-parts discount
  (full valuation comes in Gate 3)
8 management_governance — exceptional, aligned management, or a clear path to upgrade it
9 durable_growth_runway — long runway for durable EPS growth (secular tailwind, reinvestment at high returns, or large self-help)

Hard fail rule: FAIL on any of 1, 2, 4, 5, or FAIL/UNSURE on three or more criteria → hard_fail = true.
Special-situation override (small, asymmetric positions only — 1-5% of NAV at cost): set hard_fail = false and
special_situation = true when EITHER
 (a) the only failures are 4 (financial profile) and/or 5 (capital-markets dependency), the franchise is high quality (2 PASS) and
     the pack shows asset value or normalised earnings power that plausibly exceeds the claims (distressed real estate, a
     solvent-but-illiquid estate: GGP 2008), OR
 (b) the company is a levered turnaround in a concentrated industry (2-4 rational players) with a new, proven management team
     executing a visible cost/fleet/asset reset, with enough liquidity for 2+ years and normalised earnings power that would make
     today's equity a multiple of its price (Hertz 2024). Current negative FCF does not block (b).
Say which criteria would otherwise fail. Outside (a)/(b), a FAIL on 1, 2, 4 or 5 is a hard fail.
Era C platform exception (AS_OF 2013-2016 only): an acquisition-driven, levered "platform" company run by a CEO with a strong
capital-allocation record may pass criteria 1/4 as UNSURE rather than FAIL (see template T9 in Gate 2); after 2016 this exception
no longer exists.

Return JSON:
{"criteria": {"simple_predictable_fcf": {"score": "PASS|FAIL|UNSURE", "evidence": "... [Dnn]"}, "barriers_to_entry": {...},
 "limited_extrinsic_exposure": {...}, "strong_financial_profile": {...}, "minimal_capital_markets_dependency": {...}, "large_market_cap": {...},
 "attractive_valuation_screen": {...}, "management_governance": {...}, "durable_growth_runway": {...}},
 "n_pass": 0, "n_fail": 0, "n_unsure": 0, "hard_fail": false, "special_situation": false,
 "one_line_business_quality_verdict": "e.g. 'a capital-light royalty on global travel with best-in-class management' or 'a levered serial acquirer whose earnings depend on price increases'"}

FACT SHEET:
{{fact_sheet}}
