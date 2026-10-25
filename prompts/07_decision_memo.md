STEP 7 — DECISION AND MEMO. AS_OF_DATE: {{as_of_date}}. Company: {{company}} ({{ticker}}).

Decision logic (apply in order). In mode "new" the decision is BUY or PASS (never HOLD); in mode "existing" use the S-prompt.
- gate1.hard_fail = true → PASS
- gate1.special_situation = true (asymmetric distressed/levered equity, template T8/T3): BUY only if (a) asset value or normalised
  earnings power comfortably exceeds the claims, (b) the dollar commitment is small (1-5% of NAV at cost) so the loss is bounded
  while the upside is a multiple, and (c) Pershing can influence the restructuring/turnaround or the path is already visible;
  otherwise PASS
- gate2.edge_verdict = NO_EDGE → PASS
- valuation_verdict EXPENSIVE_BELOW_10 → PASS (or SELL/TRIM if we own it)
- valuation ATTRACTIVE_20_PLUS or ADEQUATE_15_20 with a credible catalyst class → BUY (or ADD/HOLD if we own it);
  size from gate 5; conviction high only if the thesis survives the bear case and the downside is bounded
- FULL_10_15: HOLD if owned, PASS if not

Then write the memo exactly as a Pershing Square letter would introduce the position: 4-8 short paragraphs, first-person
plural, every factual sentence cited [Dnn] — every paragraph carries at least two citations and every sentence with a number
carries one. Paragraph order: (1) what the business is and why it meets our standard;
(2) why the opportunity exists now (the dislocation / underperformance) and what the market has wrong; (3) valuation —
entry multiple, earnings path, terminal multiple, expected return; (4) catalyst and our role; (5) risks and what would
change our mind; (6) decision and sizing. No hedging language, no "it depends".

Return JSON only, matching this schema:
{"as_of_date": "...", "company": "...", "ticker": "...", "decision": "BUY|PASS|HOLD|ADD|TRIM|SELL|SHORT_HEDGE",
 "conviction": "low|medium|high", "target_size_pct_nav": 0,
 "opportunity_template": ["T1"], "catalyst_role": "C0", "gate1_hard_fail": false,
 "valuation": {"entry_multiple": "...", "eps_path": "...", "terminal_multiple": "...", "irr_pct": 0, "downside_case": "..."},
 "drivers": [{"driver": "one sentence, the reason as Ackman would state it", "citations": ["D03"]}],
 "kill_criteria": ["..."], "what_would_change_our_mind": "...",
 "memo": "the letter-style memo", "uncited_claims": ["..."]}

Drivers: give 4-5, ordered by importance; these are what the grader compares with Ackman's own stated reasons, so
state them concretely (not "good business" but "a capital-light franchisor earning royalty-like fees with best-in-class
net unit growth"). Pershing Square letters almost always name the same five kinds of reason; cover each when the pack
supports it: (1) business quality — what makes it simple, predictable, dominant, FCF-generative; (2) why now / price —
the dislocation or underperformance and the entry multiple ("we were able to acquire our stake at ~Nx earnings");
(3) management — the named CEO and his or her record, or the planned change; (4) the earnings path — the growth
algorithm (units × pricing × margin × buybacks) that produces mid-teens-plus EPS growth; (5) the variant perception —
the specific fear the market has wrong and why.

Sizing (target_size_pct_nav = intended full position, not the first day's buy). 2018 onward: BUY with high conviction in a
large, liquid business → 8-12% (up to 15-20% for the very best ideas); medium conviction → 4-7%; a starter position in a
turnaround or where you want to see one more data point → 1-3%; option-like political/regulatory theses → 2-5%;
asymmetric distressed/levered equity (T8) → 1-5% at cost.
Pre-2018 activist stakes: 8-20%+. If you choose a size outside these bands, say why in the memo.

GATE 1: {{gate1}}
GATE 2: {{gate2}}
GATE 3: {{gate3}}
GATE 4: {{gate4}}
GATE 5: {{gate5}}
FACT SHEET: {{fact_sheet}}
