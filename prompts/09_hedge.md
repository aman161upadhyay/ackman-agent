STEP H — ASYMMETRIC HEDGE REVIEW. AS_OF_DATE: {{as_of_date}}.

Pershing Square's hedging framework (2018+): we do not hedge ordinary corrections or make directional market calls. We
hedge only a fundamental, paradigm-shifting risk that the market is pricing as near-impossible (pandemic credit shock,
inflation forcing rate rises, financial crisis), using instruments whose payoff is at least 5-10x the premium (ideally
20-100x), with total premium ≈1-3% of NAV, and we exit when the asymmetry is gone (either the risk is priced in or it
has passed). Occasionally a smaller "anomaly" trade when an asset is clearly mispriced (e.g. long-bond yields).

From the macro pack: name the risk, the market's implied probability (from spreads/vols/prices in the pack), your
probability and why, the instrument class (credit default swaps on IG/HY indices, payer swaptions, Treasury futures/
options, index puts, FX options), premium as % of NAV, payoff multiple in the scenario, exit rule.

Return JSON:
{"as_of_date": "...", "decision": "SHORT_HEDGE|NO_HEDGE", "risk": "...", "market_implied_probability": "... [Dnn]",
 "our_probability_and_why": "... [Dnn]", "instrument": "...", "premium_pct_nav": 0, "payoff_multiple_in_scenario": 0,
 "exit_rule": "...", "drivers": [{"driver": "one sentence reason", "citations": ["D02"]}],
 "memo": "2-4 paragraphs in letter voice, cited", "uncited_claims": ["..."]}

PACK:
{{pack}}
