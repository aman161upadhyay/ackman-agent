STEP 4 — GATE 3: WHAT IS IT WORTH AND WHAT RETURN DO WE EARN? AS_OF_DATE: {{as_of_date}}.

Method (2018 and later): project earnings per share (or FCF per share) 3-5 years out from pack figures; apply a terminal
P/E that reflects risk and growth (≈20-25x simple predictable mid-teens growers; 25-35x dominant 20%+ growers;
12-16x cyclical/levered/lower quality); compute the implied annual return including dividends/buybacks; state the entry
multiple vs the company's own history and the S&P 500; describe the downside case. Prefer theses where returns come from
earnings growth rather than multiple expansion. Thresholds: new position needs ≈20%+ IRR; hold needs ≈15%; below ≈10-12%
is a sell/trim.
Method (before 2018): intrinsic value from sum-of-parts / private-market value / normalised earnings power × peer multiple,
including the value created by the activist plan; need ≈2x upside with limited downside, IRR ≥ 15-20%.

Show your arithmetic in short lines. Use only pack numbers; if a needed input is missing, state the assumption explicitly
and flag it.

Return JSON:
{"method": "era_2018_plus | pre_2018_sum_of_parts",
 "entry_multiple": "e.g. 19x NTM EPS vs 10-yr avg 28x and S&P 21x [Dnn]",
 "eps_or_fcf_path": {"base_year": "...", "base_value": "...", "growth_assumption": "...", "year_3_to_5_value": "...", "assumptions": ["... [Dnn]"]},
 "terminal_multiple": {"value": 0, "why": "risk + growth reasoning"},
 "implied_irr_pct": {"base": 0, "bear": 0, "bull": 0},
 "downside_case": "what we lose if the bear case is right, and why permanent loss is or is not likely",
 "valuation_verdict": "ATTRACTIVE_20_PLUS | ADEQUATE_15_20 | FULL_10_15 | EXPENSIVE_BELOW_10",
 "flagged_assumptions": ["anything not sourced from the pack"]}

GATE 2: {{gate2}}
FACT SHEET: {{fact_sheet}}
