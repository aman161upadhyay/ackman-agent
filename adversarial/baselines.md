# Baselines on identical decisions

The requested 'majority per mode' is the specified policy BUY/new, HOLD/existing, SHORT_HEDGE/hedge, **not a fitted majority** (the selected existing-position keys are mostly exits). Always PASS and this mode policy require no business evidence. Labels come only from keys; no agent outputs are used to fit either policy.

The third baseline is a deliberately crude pack-visible literal screen: BUY/new iff the documents contain `capital.light` AND one of recurring/subscription/franchise/royalty/network-effect, and do not contain `negative free cash flow` or `negative FCF`; otherwise PASS. Existing/hedge use HOLD/SHORT_HEDGE. It is not a validated financial model; prose summaries and omissions influence it. Same facts yield identical named/masked baseline actions. No threshold tuning was performed.

Canonical action means BUY≈ADD; key SHORT, BUY_PROTECTION and SHORT_LONG_DURATION_VIA_OPTIONS map to SHORT_HEDGE (the benchmark's output vocabulary). This does not mean single-stock shorts and macro insurance are the same process. TRIM≠SELL; conviction/size do not change this direction metric. 'Original' is the supplied grader's direction MATCH, which sometimes penalizes size. Each cell k/n (percent); intervals in JSON.

|Set|Condition|Agent exact|Original MATCH|Mode policy|Always PASS|Literal quality|
|---|---|---:|---:|---:|---:|---:|
|calibration|named|21/28 (75.0%)|20/28|24/28 (85.7%)|0/28 (0.0%)|7/28 (25.0%)|
|calibration|masked|21/28 (75.0%)|19/28|24/28 (85.7%)|0/28 (0.0%)|7/28 (25.0%)|
|controls|named|7/8 (87.5%)|7/8|0/8 (0.0%)|8/8 (100.0%)|8/8 (100.0%)|
|controls|masked|5/8 (62.5%)|5/8|0/8 (0.0%)|8/8 (100.0%)|8/8 (100.0%)|
|holdout|named|7/11 (63.6%)|7/11|7/11 (63.6%)|0/11 (0.0%)|1/11 (9.1%)|
|holdout|masked|7/11 (63.6%)|7/11|7/11 (63.6%)|0/11 (0.0%)|1/11 (9.1%)|

## Where does the agent beat the mode policy?
- calibration, named: -3 exact matches (-10.7 percentage points).
- calibration, masked: -3 exact matches (-10.7 percentage points).
- controls, named: +7 exact matches (+87.5 percentage points).
- controls, masked: +5 exact matches (+62.5 percentage points).
- holdout, named: +0 exact matches (+0.0 percentage points).
- holdout, masked: +0 exact matches (+0.0 percentage points).

The buy-enriched sample makes the mode policy strong. Controls, full exits, and erroneous historic buys—not compliant-sounding buy memos—carry the discrimination. Controls are researcher-imputed nonholdings, not necessarily publicly documented Ackman rejections. Wilson intervals are descriptive; paired named/masked runs and related issuer episodes are not independent.

Reproduce: `python3 ackman-agent/adversarial/scripts/audit.py`. Per-decision predictions, features, labels, paths and Wilson intervals are in baselines.json.