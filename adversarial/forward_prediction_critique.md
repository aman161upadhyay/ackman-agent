# Forward-prediction critique

## 1. Forecast identity is already inconsistent — confirmed

`forward/next_trade_prediction.json` has **5 new candidates**, summing to **1.05**, but declares expected_new_positions_next_90_days = **1.20**. Markdown presents **8** candidates summing to **1.35** and labels the list “agent output”. Lowe's, Chipotle and Hilton are not in the raw JSON candidates. The separately labeled principal forecast sums to **1.11**. These are not one frozen forecast. The editorial contamination is not just the principal section: three names entered the supposedly raw agent presentation.

Fix: preserve an immutable raw output; generate Markdown mechanically from it; assign separate forecast IDs to the principal and any editorial expansion. Score each against a predeclared candidate universe, including an OTHER bucket. Do not retrospectively choose whichever forecast looks best.

## 2. Historical base rate computed from the index

Ordinary-equity economic initiation episodes, including re-entries; exclude hedges, sponsor/fund structure, inherited SEG, updates and HHH control financing. Visa and Mastercard count as two names, unlike their combined calibration pack. The source explicitly says it is not a complete execution ledger. Some quarters are unknown; do not invent exact purchase quarters from disclosure dates.

|Year|New-name/re-entry episodes|Quarterly annualized mean|
|---|---:|---:|
|2018|4|1.000|
|2019|2|0.500|
|2020|1|0.250|
|2021|3|0.750|
|2022|1|0.250|
|2023|1|0.250|
|2024|3|0.750|
|2025|3|0.750|
|2026|7|2.333 (through Q3)|

2018–2025: **18 / 32 quarters = 0.5625**. Including the seven known 2026 entries through Q3: **25 / 35 = 0.7143**. Treat 2026 Q4 as censored at the October cutoff; the 2026 regime is unusually active, not an entire extra completed year. The raw 1.05 expectation is **1.87×** the pre-2026 quarterly mean; the 1.35 Markdown expectation is **2.40×**. Neither is mathematically impossible, but neither is empirically calibrated by this history. There are too few and too nonstationary observations for spurious probability precision.

Oct 25–Jan 31 is **98 days**, not 90. Expected count is the sum of candidate marginals and need not equal one; it does not determine P(no buy) without dependence assumptions. Independent marginals would imply **0.298** P(no raw-listed buy), only an illustration—not an estimated joint distribution. Shared capital and correlated narratives make independence dubious. Re-entry hypotheses should be distinguished from genuinely unfamiliar names.

## 3. Capital: separate vehicle balances and dates

D06 is more careful than the forecast: PSUS's $5B was >95% deployed, not fresh October capital. $5B minus security cost $4,915,991,173 is **$84,008,827**, but is NOT a cash balance: fees, liabilities, leverage and different observation dates prevent that inference. PSI's $852M cash/investments less $235M debt is **$617M net cash/investments**, while literal cash was $9M; equity stakes are not idle cash. HHH's $2.5–3B is multiyear projected cash, not next-quarter spending capacity. PSH exposure 126% is not a cash figure. Current uncommitted cash is **unknown**, not zero.

Raw marginal probabilities × target weights imply **5.10%** of a common NAV denominator; mechanically applying core AUM $23.0454B gives **$1.175B**, expressly an illustration, not a funding plan. Markdown's expanded list implies **6.55%**. Actual vehicle sizing, correlated selections, exits, financing and additions must be reconciled in a cash bridge. D06 supports no claim that these amounts are available now.

## 4. Screen-to-thesis jump

D04 calls itself “verified prices, not a buy list” and states “Quality is a research gate, not a fact established by price.” Autodesk's risk attribution is expressly unresolved; yet the memo asserts the moat will be reinforced by AI. Copart's drawdown and net cash do not establish temporary salvage-volume pressure. Zoetis has first-two-forecast-year EPS growth −3.05%/3.75%; a cheap multiple alone cannot establish >20% IRR. D04's five-year multiple is five annual observations, not a daily average; off-52-week-high is not proof of a recent 1–6-month dislocation.

The actual screen has no modeled IRR column. The memo's >20% labels lack an EPS/FCF bridge, terminal multiple, horizon and cash-distribution assumptions. Require annualized total return = ((terminal EPS × terminal P/E + accumulated distributions)/entry price)^(1/T)−1, with a cash-flow IRR for dated distributions, and avoid double-counting repurchases already in EPS. Show flat-multiple and compressed-multiple cases. The stored broad LLM forward reviews made unsupported references to scenario columns and treated nonholdings as falsifiers; those assertions are rejected by direct file inspection. No absent scenario numbers are reported here.

## 5. Proposed business falsifiers (not alleged historical observations)

|Candidate|What would falsify the stated investment mechanism|
|---|---|
|Autodesk|Sustained customer retention/pricing or FCF-conversion deterioration attributable to AI workflow substitution, rather than merely a lower multiple.|
|Copart|Persistent salvage-volume/share or auction-liquidity deterioration, or integration economics that destroy returns on incremental capital.|
|Alphabet|Persistent search monetization/share loss to AI channels after accounting for cost to serve; inability of other segments to offset it.|
|Booking|Direct AI-agent distribution captures bookings while take rate or repeat usage deteriorates despite normalized travel demand.|
|Lowe's|Traffic/share and normalized margins fail to recover as housing conditions stabilize; debt-financed repurchases cannot rescue cash returns.|
|Zoetis|Clinic weakness proves company-specific share/product/pricing impairment rather than a reversible end-market slowdown.|
|Chipotle|Repeated traffic deterioration and weaker restaurant-level returns persist despite price/affordability adjustments; unit growth masks damaged same-store economics.|
|Hilton|Owner economics/pipeline conversion and fee growth weaken structurally. Separately, no qualifying price dislocation means the proposed entry trigger never fired.|

Set dated measurement windows and baseline values before observing results. A nonoccurrence does not logically falsify a non-unit probability; use proper scores. A thesis can be wrong even if Ackman buys; an accurate business thesis does not force him to buy.

## 6. Observation and reconciliation

Q3 13F covers September, before forecast origin; a November *disclosure* is not a November *trade*. Q4 13F captures Dec 31, misses Jan 2027 and intraquarter round trips, and does not reveal every derivative/foreign exposure. Separate next-disclosed-action from next-initiated-position endpoints. Obtain source-confirmed initiation dates; label censored outcomes unknown. Freeze Brier-score universe, OTHER/new-name count endpoint and a separate process-driver score. Absence from an incomplete filing is not automatically a zero.

The principal section is clearly labeled, which is good. It is nonetheless an uncalibrated second forecast whose familiarity/re-entry thesis needs its own score, not a correction that can retroactively improve the agent. The raw-versus-Markdown additions are the confirmed contamination; the principal's private influence on the original model is not established.