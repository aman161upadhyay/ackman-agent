# Leakage, freeze and answer-encoding audit

## 1. Every-pack lexical scan
Scanned **47 packs / 364 documents**; **82 date-token hits** beyond meta.as_of_date. Every context is in [date_scan_hits.md](date_scan_hits.md), machine-readable in date_scan.json. These are candidates, not 82 leaks. Guidance, debt maturities, archive URLs and fiscal-year labels account for many obvious false positives. No automatic scan proves a source was publicly available at cutoff. Partial/ambiguous dates are explicitly limited in the script.

## 2. Semantic audit: all 11 hold-outs plus Uber calibration
Dedicated queryWithLLM calls received ONLY cutoff and full docs, not keys, outputs or grader scores. The initial joint regrade incorrectly flagged later gold sources and even misordered calendar months; those incidental semantic_leakage fields are rejected and not used. Authoritative audit records are leakage_semantic/<pack>.json. Ten dedicated checks reported no candidate finding; Meta flagged a scheduled 2026 trial and Uber flagged a later upload path. A separate model adjudication rejected the trial as future guidance/scheduling and retained only archive-provenance uncertainty. **No confirmed realized post-cutoff economic fact was identified in these 12 checks.** This is not independent source-vintage verification and not a clean-bill-of-health claim.

Specific spot checks: Meta D05 says trials were *scheduled*, not that outcomes occurred. Uber D08 expressly says the underlying release is from 2024. CP D09 expressly preserves the two possible forward interpretations instead of supplying the later sell. These are appropriate distinctions. Current-model knowledge leakage can exist with no visibly later assertion.

## 3. Freeze checksum

All **15 listed hashes match current bytes** (14 prompt files plus AGENT.md). Unhashed Markdown files: prompts/README.md, prompts/CHANGELOG.md, prompts/era_e_update_for_forward_runs.md.

Verdict: **current consistency confirmed; historical freeze chronology not independently established.** CHANGELOG explicitly says AGENT.md was synchronized after freezing and its hash was updated in the same manifest. Thus the current AGENT hash cannot certify its original pre-hold-out bytes. The staged runner does not use AGENT.md; this mitigates the sync concern for staged outputs, not one-shot replays. No per-run prompt hash, pack hash or exact internal model snapshot accompanies the benchmark outputs. Preserve immutable timestamped manifests for every run.

## 4. Hold-out identifiers and narrow rules

Boundary-aware case-insensitive grep searched every hold-out meta.company/ticker/alias in AGENT.md and prompts/*.md. **53 pack-file-line matches**, **36 unique lines**; excluding the forward-only addendum and CHANGELOG leaves **23 pack-file-line matches**. Same-company earlier examples (Nike entry, CP activism, Hilton entry, Netflix 2022) are not hold-out trade leakage. Count duplication across aliases/hold-out companies is documented in holdout_mentions.json.

|File|Pack-file-line matches|
|---|---:|
|AGENT.md|23|
|prompts/CHANGELOG.md|3|
|prompts/era_e_update_for_forward_runs.md|27|

The forward-only addendum explicitly contains hold-out trade details and must stay excluded from historical runs. CHANGELOG names sealed pack IDs as operational bookkeeping. AGENT's biography contains 2026 vehicle information and references a February 2026 presentation; these are temporally impure for older replays even without encoding a hold-out action. AGENT's historical Nike/CP/Hilton/Netflix mentions do not establish direct hold-out answer encoding.

Three exception families are especially calibration-shaped: GGP asset-value-over-claims, Hertz concentrated-industry/new-management/liquidity override, and Valeant 2013–2016 platform exception. The exact three case strings occur on **11 lines** across AGENT and gate 1/2 prompts (narrow_exception_mentions.json). CHANGELOG v1.3/v1.4 explicitly attributes those changes to failed runs. This confirms in-sample tuning; it does not establish illegitimate hold-out tuning. Generalize and test each rule on a matched failure case and a different issuer; do not call a fitted case recovery independent fidelity.

## 5. Identity leakage remains unresolved
`tools/run_agent.py:load_pack` replaces company/ticker/aliases only, uses unbounded regex matching, and retains executive names, product names, geography, dates and revealing filenames/URLs. It does not implement the richer masking in research/lookahead_and_evaluation.md. Short ticker replacements can corrupt ordinary words. The runner also labels sorted documents by enumeration starting D01: packs containing D00 then shift relative to filenames; current harness provenance is insufficient to know which mapping was used in existing runs. The strict regrade uses filename Dnn IDs and flags this limitation. Freeze a citation map and do identity-recovery probes. Named–masked differences are identity sensitivity, not a causal leakage estimator.

Stress tests are being produced separately in [stress_tests/](stress_tests/); no results are assumed here.