# Divergence analysis

Coverage: every original direction or state PARTIAL/MISS, named and masked, including every control false positive. A model judged each pack with the AGENT rules and then adjudicated classification inconsistencies; raw pack-level judgments and adjudicated.json are preserved in divergence/. These are evidence-based hypotheses, not observations of Ackman's private cognition. Primary causes are mutually exclusive; secondary causes can coexist. The staged specification is not identical to AGENT.md.

|Primary cause|Count|
|---|---:|
|i: Rule missing/ambiguous or not propagated to staged prompts|1|
|ii: Pack missing decisive fact|0|
|iii: Key/grader problem|0|
|iv: Model execution/causal reasoning limitation|43|
|v: Genuine underdetermined process/judgment difference|2|

## Three highest-leverage fixes

1. **Separate absolute quality from opportunity cost.** Existing-position review must compare a dated alternative, evidence-backed return range and predictability range before HOLD. Define SELL versus TRIM by whether a residual holding remains an admissible fresh purchase; do not make loss recovery an objective. If alternative data are missing, disclose that the S3 result is underdetermined rather than inventing a precise IRR.

2. **Propagate hard constraints into the actual staged inputs.** Alibaba's Chinese-VIE exclusion exists in AGENT §5 but is absent from 00_system and 02_gate1. Staged mode never reads AGENT.md. Boeing safety/certification and Disney's changing segment economics require forecastability evidence, not merely a drawdown. Do not hardcode the three company names.

3. **Fix evidence and grading before adding exceptions.** Record decision-time ranges and missing facts in keys; isolate controls as synthetic discipline probes; preserve exact citations and full run manifests. HHH CONTROL vocabulary and dated era exceptions must reach all schemas. Run the whole calibration set under one frozen version instead of reusing earlier outputs.

## Sell stickiness: concrete evidence

- Berkshire: calibration/data_packs/2020_brk_sell/docs/D09_changes_since_purchase.md says: “An investor can find Berkshire undervalued and still prefer a different use of limited capital.” The pack supplies direct alternatives but not a matched numerical IRR comparison. Both HOLDs are a relative-allocation failure, not proof that Berkshire's business quality was misread. A mechanically forced SELL would overstate what the public facts establish.

- CP: calibration/data_packs/2025_cp_sell/docs/D09_what_has_changed.md says “Synergies are no longer only a presentation forecast” and “The evidence does not justify replacing either possibility with hindsight.” The March checkpoint precedes disputed April/May exit timing. Tariffs widen outcomes without uniquely determining SELL; the key's later judgment must not be smuggled into the earlier pack.

- Nike: both HOLDs retain an estimated return despite a longer repair horizon. D09_what_has_changed.md and D03_latest_results_and_guidance.md contain the prolonged Direct/China repair and margin pressure. S2 exists: the problem is translating a changed forecast distribution into action, not merely failing to mention tariffs.

- Chipotle, Starbucks and Hilton: TRIM is not full exit. A partial sale can recognize valuation/opportunity cost while missing the all-or-nothing allocation decision. Report exit recall separately.

## Every affected run
|Run|Original direction/state|Primary cause|Evidence-based rationale|Concrete change|
|---|---|---|---|---|
|2005_mcd_buy__current__masked|MATCH/PARTIAL|iv|Model invented a 13D filing and future campaign strategy not supported by the pack.|Limit catalyst role to publicly available information at the cutoff.|
|2005_mcd_buy__current__named|MATCH/PARTIAL|iv|Model framed a spin-off as a near-term catalyst despite management's explicit rejection of it.|Reflect management's explicit rejection of restructuring as of September 30, 2005.|
|2007_tgt_buy__current__named|MISS/MISS|iv|Model failed to execute an activist catalyst despite acknowledging the relevant data in its notes.|Apply the T3 Hidden value template for Target's real estate and credit-card segment.|
|2008_ggp_buy__current__masked|MATCH/PARTIAL|iv|Model failed to reconcile debt portions and incorrectly classified the investment as a simple restructuring.|Distinguish between consolidated and unconsolidated debt and acknowledge specific Chapter 11 constraints.|
|2010_jcp_buy__current__masked|MISS/MISS|iv|Model performed unnecessary gate failures for a correct PASS decision instead of following the Pershing Square voice.|Remove redundant gate structuring and adhere to the Era B turnaround prohibition.|
|2010_jcp_buy__current__named|MISS/MISS|iv|Model included redundant boilerplate headers for a correct PASS decision.|Remove unnecessary structural fields and focus on the JCP lesson regarding retail turnarounds.|
|2012_hlf_short__current__masked|MATCH/PARTIAL|iv|Model assumed an 'illegal pyramid scheme' as fact despite the pack stating it was an allegation.|Maintain neutrality regarding the legality of the compensation structure.|
|2013_fnma_buy__current__masked|PARTIAL/PARTIAL|iv|Model incorrectly used headline profits that included accounting releases.|Reconcile the distinction between enterprise profit and distributable common equity profit.|
|2013_fnma_buy__current__named|PARTIAL/PARTIAL|iv|Model used unsupported terminal multiples and incorrectly assumed a 5% position.|Remove speculative multiples and acknowledge the lack of public disclosure.|
|2015_vrx_buy__current__masked|MATCH/PARTIAL|iv|Model ignored warnings against acquisition-dependent growth and applied retired rules.|Apply post-2017 rules; business fails Gate 1 criteria for simple/predictable growth.|
|2015_vrx_buy__current__named|MATCH/MISS|iv|Model used retired 'Platform Value' logic and ignored leverage concerns.|Re-evaluate under modern Gate 1 principles regarding high leverage and M&A dependence.|
|2016_cmg_buy__current__masked|MATCH/PARTIAL|iv|The model executed the thesis accurately but did not prioritize specific 13D disclosure.|No change required.|
|2020_brk_sell__current__masked|MISS/MISS|v|Model identified the position as a HOLD, ignoring the rule regarding opportunity cost.|Apply the better use of capital rule (S3) leading to a SELL decision.|
|2020_brk_sell__current__named|MISS/MISS|v|Model prioritized a 'thesis intact' narrative over the opportunity cost of holding cash.|Prioritize opportunity cost analysis to fund higher-conviction, direct-equity alternatives.|
|2020_sbux_sell__current__masked|PARTIAL/PARTIAL|iv|Model labeled a TRIM when a SELL was required for returns below the hurdle.|Correct the decision to SELL to align with the S1 strategy rule.|
|2020_sbux_sell__current__named|PARTIAL/PARTIAL|iv|Model failed to execute a SELL for a position that reached intrinsic value.|Update the decision to SELL consistent with S1 criteria.|
|2021_umg_buy__current__masked|MISS/MISS|iv|Model treated temporary cash-flow noise as a structural hard-fail.|Re-evaluate predictability using streaming growth data rather than Q1 cash timing.|
|2022_nflx_buy__current__named|MATCH/PARTIAL|iv|Model ignored the Netflix rule regarding unpredictability after subscriber loss.|Assess as a failure of the 'simple and predictable' gate and conclude with SELL or PASS.|
|2022_nflx_sell__current__masked|MATCH/PARTIAL|iv|Model retained thesis structure instead of performing an immediate exit-on-change.|Demonstrate strict compliance with the Netflix rule for immediate exit when predictability falls.|
|2023_tsy_short__current__masked|PARTIAL/PARTIAL|iv|Model inferred specific numerical details not supported by the pack.|Remove speculative numerical claims and characterize protection qualitatively.|
|2023_tsy_short__current__named|PARTIAL/PARTIAL|iv|Model inferred precise terms not in the pack.|Eliminate unsupported numerical payoff and premium metrics.|
|2024_htz_buy__current__named|MISS/MISS|iv|Model ignored the special-situation override rule for levered turnarounds.|Apply special-situation override (Template T8) for levered equity opportunities.|
|2024_nke_buy_a__current__masked|MISS/MISS|iv|Model chose HOLD instead of BUY for a market dislocation.|Re-evaluate based on the T1 Temporary crisis template and Era E rules.|
|2025_fnma_fmcc_2025__current__masked|MATCH/PARTIAL|iv|Model assumed investor scenarios were authenticated government commitments.|Recalibrate conviction to account for Treasury consent timing uncertainty.|
|2025_fnma_fmcc_2025__current__named|MATCH/PARTIAL|iv|Model failed to distinguish between retained earnings and available common equity.|Refine driver analysis to distinguish earnings from equity and acknowledge amendment hurdles.|
|2025_hhh_control__current__masked|MISS/MISS|iv|Model failed to incorporate specific strategic plan parameters for an active control platform.|Prioritize the holding company/insurance strategic plan as the core thesis.|
|2025_hhh_control__current__named|MISS/MISS|iv|Model defaulted to a passive HOLD rather than the intended active platform strategy.|Reflect the strategic intent of a holding company with insurance-backed capital.|
|2025_uber_buy__current__masked|PARTIAL/PARTIAL|iv|Model modeled growth based on authorization rather than execution.|Re-align growth with reported FCF trends and adjust multiples with correct denominators.|
|ctl_2019_ba_pass__current__masked|MISS/MISS|iv|Model treated high-risk safety issues as a temporary play.|Identify unquantifiable regulatory risk as a Gate 1 FAIL per Section 5 guidelines.|
|ctl_2019_ba_pass__current__named|MISS/MISS|iv|Model failed to execute requirements against extrinsic, uncontrollable risks.|Recognize that lack of a common return-to-service schedule makes the business unsuitable.|
|ctl_2021_baba_pass__current__masked|MISS/MISS|i|The staged system and gate1 prompts failed to propagate the Chinese-VIE prohibition defined in AGENT.md to the actual runtime [L1-L2].|Include the Chinese-VIE prohibition from AGENT.md in the staged system and gate1 prompts.|
|ctl_2022_dis_pass__current__masked|MISS/MISS|iv|Model labeled a BUY despite the pack specifying streaming losses prevent a core investment.|Identify that current losses and content requirements fall outside core investment criteria.|
|2025_cmg_sell__current__masked|PARTIAL/PARTIAL|iv|Model proposed a TRIM instead of a SELL despite a fundamental thesis change.|Reclassify as SELL according to the S2 rule.|
|2025_cmg_sell__current__named|PARTIAL/PARTIAL|iv|Model proposed a TRIM instead of a SELL for a thesis change and reduced predictability.|Reclassify as SELL to align with the S2 rule.|
|2025_cp_sell__current__masked|MISS/MISS|iv|Model maintained HOLD despite tariff uncertainty and better alternatives.|Apply the sell rule for tariff-driven loss of forecast confidence and compare IRRs.|
|2025_cp_sell__current__named|MISS/MISS|iv|Model ignored sell precedence where tariff uncertainty reduces forecastability.|Re-evaluate conviction in face of tariff uncertainty and compare IRR against alternatives.|
|2025_meta_buy__current__masked|MATCH/PARTIAL|iv|Model relied on speculative terminal multiple assumptions not derived from data.|Focus on reported financials and management guidance without speculative terminal multiples.|
|2025_meta_buy__current__named|MATCH/PARTIAL|iv|Model overstepped current-date constraints by framing future position building.|Adhere to the point-in-time nature of the snapshot.|
|2025_nke_sell__current__masked|MISS/MISS|iv|Model maintained a HOLD despite the key's SELL decision and loss of profitability underwriting.|Acknowledge loss of predictability and apply rule S2 for a SELL decision.|
|2025_nke_sell__current__named|MISS/MISS|iv|Model acknowledged broken fundamentals but failed to shift to SELL.|Reflect that structural headwinds necessitate a SELL decision per S2 rules.|
|2026_hlt_sell__current__masked|PARTIAL/PARTIAL|iv|Model imputed specific IRR percentages not mandated by the pack.|Align IRR thresholds with qualitative descriptions; account for the dated observation context.|
|2026_hlt_sell__current__named|PARTIAL/PARTIAL|iv|Model used unsupported claims regarding fiduciary duty to rotate capital.|Remove unattributed claims; re-evaluate based on valuation multiple and operating growth.|
|2026_msft_buy__current__masked|MATCH/PARTIAL|iv|Model projected growth using speculative, unverified multiples.|Focus on verified financials and avoid over-extrapolating unverified forward multiples.|
|2026_msft_buy__current__named|MATCH/PARTIAL|iv|Model used predictive modeling not supported by the pack's warnings.|Remove speculative terminal multiple projections not supported by data.|
|2026_nflx_buy_2__current__masked|MATCH/PARTIAL|iv|Model missed the context regarding nonrecurring termination payments.|Re-underwrite using current-period adjustments to distinguish recurring income from one-time receipts.|
|2026_nflx_buy_2__current__named|MATCH/PARTIAL|iv|Model failed to account for the distortive effect of nonrecurring payments.|Update EPS/FCF projections to strip out nonrecurring payments.|