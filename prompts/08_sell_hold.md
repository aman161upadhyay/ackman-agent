STEP S — EXISTING POSITION REVIEW. AS_OF_DATE: {{as_of_date}}. Company: {{company}} ({{ticker}}). The pack describes a
position Pershing Square already owns, plus what has happened since purchase.

Decide HOLD, ADD, TRIM, SELL or CONTROL and name the reason class exactly as Pershing Square letters do:
CONTROL applies only when the pack shows a long-held position whose discount to intrinsic value has persisted for years despite
engagement, where Pershing can supply primary capital and management itself and can redesign the company's strategy (catalyst
class C4); it is a rare action and must be justified against the alternative of simply adding.
S1 price_reached_value — forward IRR below ≈10-12%; "future returns unlikely to meet our thresholds"
S2 loss_of_predictability_or_thesis_change — the business model or its drivers changed so we can no longer forecast with
   sufficient certainty (sell immediately, even at a loss)
S3 better_use_of_capital — funding a superior opportunity: compare this position's forward IRR with the best alternatives the pack
   shows Pershing has (new dislocations, existing holdings it is adding to, cash from a hedge). If alternatives offer materially
   higher expected returns with similar quality, or the position was a lower-return "proxy" for quality/cash (a conglomerate or
   holding company bought for safety), SELL/TRIM for S3 — Pershing is small enough to be nimble and says so
S4 mistake_permanent_impairment — the original thesis was wrong; admit it, exit, write the post-mortem
S5 risk_management_concentration — trim because the position outgrew limits after appreciation
HOLD/ADD if the thesis is on track and forward IRR ≥ ≈15%; ADD on weakness when the thesis is intact and the drawdown is
sentiment-driven.
For S2/S4 sells, state the mechanism that destroyed predictability (e.g. operating leverage makes intrinsic value very sensitive to
the subscriber/unit growth rate; a model change whose economics cannot yet be forecast), quantify the loss you accept, and apply
the Pershing rule learned from past mistakes: act promptly on information inconsistent with the original thesis rather than wait
for a recovery — the opportunity cost of attention and capital is real.

Return JSON:
{"as_of_date": "...", "company": "...", "ticker": "...", "decision": "HOLD|ADD|TRIM|SELL|CONTROL",
 "reason_class": "S1|S2|S3|S4|S5|THESIS_ON_TRACK", "conviction": "low|medium|high",
 "thesis_at_purchase_vs_now": ["each original driver: intact / strengthened / broken, with evidence [Dnn]"],
 "forward_irr_estimate_pct": 0, "valuation_now": "multiple vs our estimate of intrinsic value [Dnn]",
 "drivers": [{"driver": "one sentence reason for the decision", "citations": ["D02"]}],
 "memo": "3-5 paragraphs in Pershing Square letter voice explaining the decision, every factual sentence cited",
 "uncited_claims": ["..."]}

PACK:
{{pack}}
