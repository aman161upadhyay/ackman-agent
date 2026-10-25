FORWARD — WHAT DOES PERSHING SQUARE DO IN THE NEXT 60-90 DAYS? AS_OF_DATE: {{as_of_date}}.

Inputs: (a) Pershing Square's current portfolio, cash, recent sales and public statements (pack); (b) the "library":
a list of large, simple, predictable, FCF-generative, dominant businesses Pershing has followed or named, with current
price, drawdown from 52-week high, forward P/E vs own 5-year history, consensus EPS growth, and the reason for any recent
drawdown (pack); (c) macro/market context (pack).

Method:
1 Rank library names by the Pershing Square trigger: quality PASS on all 8 criteria AND a 15-30%+ drawdown in the last
  1-6 months caused by a fear you can argue is temporary or wrong (T1/T4) or a fixable underperformance (T2), AND
  implied IRR ≥ 20% at the current price, AND size/liquidity adequate for a 5-10% position (≥$25B market cap unless
  special). Exclude names Pershing already owns at full size, names in excluded industries, and controlled companies
  with misaligned controllers.
2 For existing holdings: flag likely TRIM/SELL (forward IRR < 10-12%, or needed to fund a better idea) and likely ADD
  (thesis intact, stock down).
3 Consider the pattern of recent purchases (mega-cap technology franchises, payments/data networks, capital-light
  compounders) and recent public comments naming companies.
4 Output a ranked list with a probability that Pershing initiates/changes the position within 90 days, the expected
  action and size, and the one-paragraph thesis in letter voice. Probabilities should sum to a realistic expected
  count (Pershing typically initiates 1-4 new positions a year; 2026 was unusually active due to new capital).

Return JSON:
{"as_of_date": "...", "expected_new_positions_next_90_days": 0.0,
 "candidates": [{"rank": 1, "company": "...", "ticker": "...", "action": "NEW_BUY|ADD|TRIM|SELL", "probability_90d": 0.0,
   "template": "T1|T2|T3|T4|T5|T6", "trigger": "what dislocation/underperformance and when [Dnn]", "valuation": "multiple, IRR [Dnn]",
   "size_pct_nav": 0, "thesis_paragraph": "letter voice, cited", "what_would_confirm": "what filing/statement would reveal it"}],
 "existing_position_changes": [{"company": "...", "action": "...", "probability_90d": 0.0, "reason_class": "S1..S5", "why": "..."}],
 "uncited_claims": ["..."]}

PACK:
{{pack}}
