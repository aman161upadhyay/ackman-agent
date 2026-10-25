# Blind strict re-grade

All 94 outputs were regraded, a superset of original MATCH/PARTIAL cases. Candidate identity was anonymized and original grades/provider withheld; source company names remain in documents and the memo, so this is score-blind, not entity-blind. Each final memo/driver/valuation was graded separately, with full pack documents and gold drivers. Stage outputs were excluded. One queryWithLLM judge is not a human adjudication or an independent model-family audit.

Two separate endpoints: semantic recall = same explicit causal claim/polarity; supported recall additionally requires the cited document to support it. Counts can increase: strict regrading is not mechanically constrained below the original. The requested leniency number uses semantic recall, not the additional grounding penalty. Per-driver quotes and judgments are in each run JSON. `raw/` contains an abandoned paired pilot that sometimes enumerated candidate instead of gold drivers; NONE of those pilot results enters these statistics.

Wilson intervals below are descriptive pooled-driver binomial intervals. Drivers within a case, and named/masked pairs, are dependent; these intervals are not confirmatory evidence of population fidelity.

|Set|Condition|Original k/N [95%]|Strict causal k/N [95%]|Strict supported k/N [95%]|
|---|---|---|---|---|
|calibration|named|67/116 [48.7%, 66.4%]|65/116 [47.0%, 64.7%]|47/116 [32.0%, 49.6%]|
|calibration|masked|69/116 [50.4%, 68.0%]|65/116 [47.0%, 64.7%]|49/116 [33.6%, 51.3%]|
|controls|named|19/22 [66.7%, 95.3%]|16/22 [51.8%, 86.8%]|14/22 [43.0%, 80.3%]|
|controls|masked|13/22 [38.7%, 76.7%]|9/22 [23.3%, 61.3%]|9/22 [23.3%, 61.3%]|
|holdout|named|20/41 [34.3%, 63.5%]|19/41 [32.1%, 61.3%]|15/41 [23.6%, 51.9%]|
|holdout|masked|22/41 [38.7%, 67.9%]|14/41 [21.6%, 49.5%]|12/41 [17.6%, 44.5%]|

**Leniency (mean original minus strict causal reproduced share, calibration + hold-out original state MATCH/PARTIAL, n=63 runs; controls excluded): 0.053968 (5.40 percentage points).** Grounding-inclusive gap: 21.19 points. The scores contain no separate categorical driver grade, so original state defines the requested MATCH/PARTIAL subset. All decisions, including controls and original MISS, were regraded for coverage. Negative values mean the second judge credited more causal claims, not evidence that the original was lenient.

After one repair pass, 15 runs still had non-verbatim quote evidence. Deterministic validation rejects those particular claims (candidate-quote failure removes causal credit; doc-quote failure removes support credit). Raw model judgments are preserved, and each file includes audit_validation accepted flags. This is a conservative reproducible endpoint, not human adjudication. See validation.json; a later human audit may recover credit for a genuinely correct paraphrase.

## Every decision
|Run|Original|Causal|Supported|Causal delta|Supported delta|
|---|---:|---:|---:|---:|---:|
|2005_mcd_buy__current__masked|2/4|0/4|0/4|-2|-2|
|2005_mcd_buy__current__named|0/4|0/4|0/4|+0|+0|
|2007_tgt_buy__current__masked|3/4|3/4|1/4|+0|-2|
|2007_tgt_buy__current__named|1/4|0/4|0/4|-1|-1|
|2008_ggp_buy__current__masked|2/4|3/4|2/4|+1|+0|
|2008_ggp_buy__current__named|3/4|3/4|2/4|+0|-1|
|2010_jcp_buy__current__masked|0/4|0/4|0/4|+0|+0|
|2010_jcp_buy__current__named|0/4|0/4|0/4|+0|+0|
|2011_cp_buy__current__masked|3/4|2/4|0/4|-1|-3|
|2011_cp_buy__current__named|3/4|3/4|1/4|+0|-2|
|2012_hlf_short__current__masked|2/4|3/4|0/4|+1|-2|
|2012_hlf_short__current__named|3/4|2/4|0/4|-1|-3|
|2013_apd_buy__current__masked|3/4|3/4|3/4|+0|+0|
|2013_apd_buy__current__named|3/4|3/4|3/4|+0|+0|
|2013_fnma_buy__current__masked|2/4|2/4|2/4|+0|+0|
|2013_fnma_buy__current__named|3/4|2/4|1/4|-1|-2|
|2015_vrx_buy__current__masked|2/4|1/4|1/4|-1|-1|
|2015_vrx_buy__current__named|1/4|1/4|1/4|+0|+0|
|2016_cmg_buy__current__masked|2/4|0/4|0/4|-2|-2|
|2016_cmg_buy__current__named|3/4|4/4|2/4|+1|-1|
|2018_hlt_buy__current__masked|4/4|4/4|4/4|+0|+0|
|2018_hlt_buy__current__named|4/4|4/4|3/4|+0|-1|
|2018_low_buy__current__masked|3/4|3/4|3/4|+0|+0|
|2018_low_buy__current__named|3/4|3/4|3/4|+0|+0|
|2020_brk_sell__current__masked|0/3|1/3|1/3|+1|+1|
|2020_brk_sell__current__named|0/3|0/3|0/3|+0|+0|
|2020_cds_hedge__current__masked|4/4|4/4|1/4|+0|-3|
|2020_cds_hedge__current__named|4/4|3/4|2/4|-1|-2|
|2020_sbux_sell__current__masked|1/3|3/3|1/3|+2|+0|
|2020_sbux_sell__current__named|2/3|3/3|3/3|+1|+1|
|2021_umg_buy__current__masked|3/5|4/5|3/5|+1|+0|
|2021_umg_buy__current__named|4/5|5/5|5/5|+1|+1|
|2022_nflx_buy__current__masked|3/5|0/5|0/5|-3|-3|
|2022_nflx_buy__current__named|2/5|3/5|2/5|+1|+0|
|2022_nflx_sell__current__masked|2/4|2/4|2/4|+0|+0|
|2022_nflx_sell__current__named|3/4|2/4|1/4|-1|-2|
|2023_googl_buy__current__masked|3/4|4/4|4/4|+1|+1|
|2023_googl_buy__current__named|4/4|4/4|2/4|+0|-2|
|2023_tsy_short__current__masked|3/4|3/4|2/4|+0|-1|
|2023_tsy_short__current__named|3/4|2/4|2/4|-1|-1|
|2024_bn_buy__current__masked|3/4|4/4|3/4|+1|+0|
|2024_bn_buy__current__named|3/4|2/4|2/4|-1|-1|
|2024_htz_buy__current__masked|4/5|2/5|2/5|-2|-2|
|2024_htz_buy__current__named|0/5|2/5|2/5|+2|+2|
|2024_nke_buy_a__current__masked|3/4|3/4|3/4|+0|+0|
|2024_nke_buy_a__current__named|3/4|2/4|2/4|-1|-1|
|2024_nke_buy_b__current__masked|3/4|3/4|3/4|+0|+0|
|2024_nke_buy_b__current__named|3/4|3/4|3/4|+0|+0|
|2025_amzn_buy__current__masked|4/5|4/5|4/5|+0|+0|
|2025_amzn_buy__current__named|3/5|3/5|1/5|+0|-2|
|2025_fnma_fmcc_2025__current__masked|2/5|1/5|1/5|-1|-1|
|2025_fnma_fmcc_2025__current__named|3/5|2/5|0/5|-1|-3|
|2025_hhh_control__current__masked|0/4|0/4|0/4|+0|+0|
|2025_hhh_control__current__named|0/4|0/4|0/4|+0|+0|
|2025_uber_buy__current__masked|3/5|3/5|3/5|+0|+0|
|2025_uber_buy__current__named|3/5|4/5|4/5|+1|+1|
|ctl_2019_ba_pass__current__masked|0/3|0/3|0/3|+0|+0|
|ctl_2019_ba_pass__current__named|0/3|0/3|0/3|+0|+0|
|ctl_2020_xom_pass__current__masked|3/3|2/3|2/3|-1|-1|
|ctl_2020_xom_pass__current__named|3/3|2/3|2/3|-1|-1|
|ctl_2021_baba_pass__current__masked|0/2|0/2|0/2|+0|+0|
|ctl_2021_baba_pass__current__named|2/2|2/2|2/2|+0|+0|
|ctl_2022_cvna_pass__current__masked|3/3|3/3|3/3|+0|+0|
|ctl_2022_cvna_pass__current__named|3/3|3/3|3/3|+0|+0|
|ctl_2022_dis_pass__current__masked|0/2|0/2|0/2|+0|+0|
|ctl_2022_dis_pass__current__named|2/2|1/2|1/2|-1|-1|
|ctl_2022_intc_pass__current__masked|2/3|1/3|1/3|-1|-1|
|ctl_2022_intc_pass__current__named|3/3|3/3|3/3|+0|+0|
|ctl_2023_el_pass__current__masked|3/3|2/3|2/3|-1|-1|
|ctl_2023_el_pass__current__named|3/3|2/3|2/3|-1|-1|
|ctl_2023_pfe_pass__current__masked|2/3|1/3|1/3|-1|-1|
|ctl_2023_pfe_pass__current__named|3/3|3/3|1/3|+0|-2|
|2025_cmg_sell__current__masked|1/3|1/3|1/3|+0|+0|
|2025_cmg_sell__current__named|1/3|0/3|0/3|-1|-1|
|2025_cp_sell__current__masked|1/3|0/3|0/3|-1|-1|
|2025_cp_sell__current__named|0/3|1/3|1/3|+1|+1|
|2025_meta_buy__current__masked|2/4|1/4|1/4|-1|-1|
|2025_meta_buy__current__named|2/4|3/4|3/4|+1|+1|
|2025_nke_sell__current__masked|1/3|0/3|0/3|-1|-1|
|2025_nke_sell__current__named|1/3|0/3|0/3|-1|-1|
|2026_alc_buy__current__masked|3/5|4/5|4/5|+1|+1|
|2026_alc_buy__current__named|3/5|4/5|3/5|+1|+0|
|2026_hlt_sell__current__masked|1/3|3/3|1/3|+2|+0|
|2026_hlt_sell__current__named|1/3|3/3|1/3|+2|+0|
|2026_ice_buy__current__masked|3/4|1/4|1/4|-2|-2|
|2026_ice_buy__current__named|3/4|3/4|3/4|+0|+0|
|2026_msft_buy__current__masked|1/4|0/4|0/4|-1|-1|
|2026_msft_buy__current__named|1/4|1/4|1/4|+0|+0|
|2026_nflx_buy_2__current__masked|2/4|1/4|1/4|-1|-1|
|2026_nflx_buy_2__current__named|2/4|0/4|0/4|-2|-2|
|2026_spgi_buy__current__masked|3/4|0/4|0/4|-3|-3|
|2026_spgi_buy__current__named|3/4|1/4|0/4|-2|-3|
|2026_v_ma_buy__current__masked|4/4|3/4|3/4|-1|-1|
|2026_v_ma_buy__current__named|3/4|3/4|3/4|+0|+0|