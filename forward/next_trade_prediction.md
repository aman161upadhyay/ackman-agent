# Forward prediction — Pershing Square's next trade (as of 2026-10-25, horizon to 2027-01-31)

**What this is.** The agent (AGENT.md + prompts v1.5, run on the current internal model with the era-E addendum and the frozen
evidence pack in `forward/pack/`) was asked what Pershing Square does in the next 60-90 days. It is a *process* prediction —
the names the Pershing Square gates would select from today's dislocations — scored on decision-and-reasoning fidelity when
the disclosures arrive, never on stock returns. Raw agent output: `forward/next_trade_prediction.json`.

**Base rate.** Pershing Square historically initiates 1-4 new positions annually; while 2026 was unusually active due to new vehicle capital raises, the current environment emphasizes deployment into library compounders on dislocation rather than aggressive expansion [L415, L416]. Expected number of new names initiated by 31 Jan 2027: **≈1.35** (sum of the
probabilities below). PSH NAV was -6.9% YTD at 20 Oct 2026 [D06], and 2026 already saw the most active rotation in a decade
(Meta, Microsoft, Netflix #2, Visa, Mastercard, S&P Global, ICE, Alcon in; Hilton, Alphabet, UMG, Hertz, Nike, Chipotle, CP out) [D07].

## 1. Ranked candidates for a NEW position (names not owned at 30 Jun 2026 + ICE/Alcon)

| # | Company | Action | P(90d) | Template | Size | Trigger (pack) | Valuation (pack) |
|---|---|---|---|---|---|---|---|
| 1 | Autodesk (ADSK) | NEW_BUY | 0.35 | T1 | 5% | A 21.2% drawdown driven by market concerns over AI disruption of design workflows [L505, L506]. | 19.40x forward P/E, IRR > 20% [L508]. |
| 2 | Copart (CPRT) | NEW_BUY | 0.25 | T1 | 4% | 35.9% drawdown attributed to salvage-unit growth concerns and integration costs [L522, L523]. | 17.85x forward P/E, IRR > 20% [L525]. |
| 3 | Alphabet (GOOG) | NEW_BUY | 0.20 | T1 | 6% | 21.6% drawdown due to AI search and capex concerns [L665, L666]. | 23.39x forward P/E, IRR > 20% [L668]. |
| 4 | Booking Holdings (BKNG) | NEW_BUY | 0.15 | T4 | 5% | 29.4% drawdown caused by AI agent disintermediation fears [L488, L489]. | 14.01x forward P/E, IRR > 20% [L491]. |
| 5 | Lowe's (LOW) | RE_ENTRY_BUY | 0.15 | T1 | 5% | 32.2% drawdown [L559]; ~15.9x forward P/E [L561] | 32.2% drawdown [L559]; ~15.9x forward P/E [L561] |
| 6 | Zoetis (ZTS) | NEW_BUY | 0.10 | T1 | 4% | 45.2% drawdown from weak clinic demand [L594, L595]. | 13.12x forward P/E, IRR > 20% [L597]. |
| 7 | Chipotle (CMG) | RE_ENTRY_BUY | 0.10 | T2 | 5% | 34.8% drawdown [L577]; ~21.8x forward P/E [L579] | 34.8% drawdown [L577]; ~21.8x forward P/E [L579] |
| 8 | Hilton (HLT) | RE_ENTRY_BUY | 0.05 | T1 | 4% | Not in pack | Not in pack |

### Theses in letter voice (agent output, citations to forward/pack)
**1. Autodesk (ADSK) — NEW_BUY, P=0.35, 5% of NAV.**

Autodesk is a dominant software franchise with high switching costs and a capital-light business model that fits perfectly within our library of quality compounders [L514]. The market's fear regarding AI-driven disintermediation is misplaced; the company's established design workflows create deep defensive moats that our analysis suggests will be reinforced, not replaced, by AI integration [L514]. At current levels, the valuation dislocation offers an attractive opportunity to initiate a position in a simple, predictable business with high free-cash-flow conversion [L104, L514].

*What would change our mind:* see kill criteria in AGENT.md Gate 5
*What would confirm it:* Form 13F for 31-Dec holdings (filed 16 Feb 2027) or a Q4 portfolio update [L423].

**2. Copart (CPRT) — NEW_BUY, P=0.25, 4% of NAV.**

Copart represents a classic network-effect business with dominant share in the salvage auction market [L531]. While recent integration costs and fluctuations in salvage volumes have spooked investors, the structural economics of the business remain intact and highly FCF-generative [L104, L531]. We view this drawdown as temporary and unwarranted, allowing us to build a meaningful stake at an entry multiple that is compelling relative to its historical performance [L120, L531].

*What would change our mind:* see kill criteria in AGENT.md Gate 5
*What would confirm it:* Form 13F for 31-Dec holdings (filed 16 Feb 2027) [L423].

**3. Alphabet (GOOG) — NEW_BUY, P=0.20, 6% of NAV.**

Having previously owned Alphabet, we understand the business deeply and its durable advantages in the digital advertising and search ecosystem [L674]. Recent market volatility stemming from AI-related search and capex anxiety has created an opportunity to re-enter this dominant, capital-light compounder [L104, L674]. We believe the long-term earnings trajectory is robust, and the current multiple fails to reflect the intrinsic value of its core franchises [L121, L674].

*What would change our mind:* see kill criteria in AGENT.md Gate 5
*What would confirm it:* Form 13F for 31-Dec holdings (filed 16 Feb 2027) [L423].

**4. Booking Holdings (BKNG) — NEW_BUY, P=0.15, 5% of NAV.**

Booking Holdings operates a highly capital-light demand aggregation model that remains a leader in the travel industry [L497]. We disagree with the market's current narrative that AI agents will successfully disintermediate its travel moat [L497]. The distribution economics in the travel sector are robust, and we believe the current pricing gap provides a substantial margin of safety for a business that continues to execute well [L184, L497].

*What would change our mind:* see kill criteria in AGENT.md Gate 5
*What would confirm it:* Form 13F for 31-Dec holdings (filed 16 Feb 2027) [L423].

**5. Lowe's (LOW) — RE_ENTRY_BUY, P=0.15, 5% of NAV.**

Lowe's remains a high-quality home-improvement franchise that fits our library criteria [L567]. The business is currently facing temporary cyclical headwinds related to housing and interest-rate sensitivity [L558], providing an attractive entry point for a proven compounder [L567]. At ~15.9x forward earnings, we believe the market is over-discounting the durability of its unit economics [L561].

*What would change our mind:* see kill criteria in AGENT.md Gate 5
*What would confirm it:* 13F filing or public disclosure of position initiation

**6. Zoetis (ZTS) — NEW_BUY, P=0.10, 4% of NAV.**

Zoetis remains a high-quality leader in animal health and is a known quantity within our library [L603]. The recent valuation dislocation is a response to clinic demand headwinds which we judge to be temporary rather than structural [L603]. We are comfortable re-underwriting the firm's normalized earnings power and believe the current price offers an asymmetric risk-reward profile for a long-term compounder [L184, L603].

*What would change our mind:* see kill criteria in AGENT.md Gate 5
*What would confirm it:* Form 13F for 31-Dec holdings (filed 16 Feb 2027) [L423].

**7. Chipotle (CMG) — RE_ENTRY_BUY, P=0.10, 5% of NAV.**

Chipotle is a dominant franchise with unique unit economics that we have successfully navigated in the past [L585]. While the current drawdown is driven by consumer affordability and traffic concerns [L576], the fundamental strength of the brand remains intact [L585]. We continue to watch this for potential re-entry as the market processes near-term volume volatility [L147].

*What would change our mind:* see kill criteria in AGENT.md Gate 5
*What would confirm it:* 13F filing or public disclosure of position initiation

**8. Hilton (HLT) — RE_ENTRY_BUY, P=0.05, 4% of NAV.**

While Hilton is an admirable, capital-light compounder we know well, we exited in February 2026 at full value to fund superior capital allocation opportunities [L381]. Without a significant dislocation to our estimates of intrinsic value, we prefer to maintain our current mega-cap technology and data network focus [L414].

*What would change our mind:* see kill criteria in AGENT.md Gate 5
*What would confirm it:* Significant 15-30% price dislocation on temporary sentiment


## 2. Existing positions — likely changes

| Holding | Action | P(90d) | Reason class | Why |
|---|---|---|---|---|
| S&P Global (SPGI) | ADD | 0.40 | THESIS_ON_TRACK_ADD | The 18.5% drawdown driven by macro volatility and AI fears allows us to add to a high-quality data and ratings business we know intimately [L541, L549]. |
| Meta Platforms (META) | ADD | 0.35 | THESIS_ON_TRACK_ADD | We continue to view the market's AI capital expenditure anxiety as a temporary mispricing of a dominant, capital-light advertising franchise [L630, L639]. |

## 3. Single most likely next disclosed action
**S&P Global (SPGI) — ADD, P≈0.4.**
Given Pershing Square's deep intimacy with S&P Global and our confidence in its ratings and index franchises, the current 18.5% drawdown provides an ideal opportunity for an add-on trade [L539, L549]. We view the recent price pressure as reflecting broader AI/macro sentiment rather than an impairment of intrinsic value, making this the most efficient path for deploying capital during periods of index-wide volatility [L540, L549].

## 4. Principal's reconciliation (Replit, not the agent — kept separate so the agent is scored on its own output)
The agent's list is driven by the D04 screen's drawdown and multiple columns. Two adjustments I would make from the
pattern evidence in the compendium, offered as a second, clearly-labelled forecast:
1. **Re-entries rank higher than new software names.** In 2026 Pershing re-entered Netflix four years after selling it [D07];
   it knows Lowe's (2018-23), Zoetis (2014-16), Chipotle (2016-25) and Alphabet (2023-26) intimately, and the D04 figures put all
   four 20-45% below their highs at multiples below their own history. Familiar names clear the research bottleneck faster than
   Autodesk or Copart, which Pershing has never owned and which are outside its historical circle (design software; auto salvage,
   with Copart also at the bottom of the size range at ~$27B).
2. **Booking fits the 2025-26 trigger exactly.** A dominant, capital-light network with enormous buybacks, 29% off its high on a
   narrative ("AI agents disintermediate OTAs") of the same shape Pershing rejected for Uber/AVs and Alphabet/search in 2025
   [D04][D08] — the T4 "misunderstood secular narrative" template — at ~14x forward earnings.
Reconciled ranking: **Booking 0.25, Alphabet re-entry 0.20, Lowe's re-entry 0.18, Zoetis re-entry 0.15, Autodesk 0.15,
Copart 0.10, Chipotle re-entry 0.08** (E[new] ≈ 1.1). Most likely disclosed action overall: an **add to S&P Global or Meta on
weakness**, as the agent says, because Pershing adds to intact theses before it opens new ones (Uber, UMG 2025; Amazon 2026).

## 5. How to score this (January-February 2027)
Aman should score this in early 2027 by evaluating whether the logic of 'dislocation-driven quality purchases' was maintained. Decision fidelity should be measured by comparing observed additions to the 'library' criteria (e.g., did they buy a non-Pershing company with <15% drawdown, or one that was levered/acquisition-heavy?). Unobserved positions as of the final pack date are not 'wrong,' but the reasoning for why a trade was NOT taken (e.g., waiting for deeper price drops in a specific sector) should be held against the eventual disclosures.

Scoring events: PSH/PSUS Q3 portfolio reviews **2 Nov 2026**; PS Inc. Q&A **3 Nov 2026**; Q3 13F **16 Nov 2026** (holdings at
30 Sep — a September purchase is not a November purchase); Q4 13F **16 Feb 2027** (outside the horizon: unobserved ≠ wrong).
Grade (a) each predicted action against executed actions (SEC/issuer evidence only); (b) the stated reasons in the first letter
or call that discusses the position against the thesis paragraph above, using `prompts/10_grader.md`; (c) the Brier score of
the probability table over the candidate set; (d) record the result under `calibration/scores/holdout/forward_2026Q3.json`.

Uncited claims flagged by the agent: The 2026/2027 market outlook remains influenced by political stability and resolution of conflicts..
