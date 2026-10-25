# ackman-agent — a process-faithful Bill Ackman / Pershing Square decision agent

Built overnight 2026-10-25 for Aman Upadhyay (HBS Seminar in Investing, Fall 2026; sponsor Laurion Capital).
Goal: an LLM agent that reproduces **how** Ackman decides — the gates, evidence, thresholds and language — graded against
his real decisions trade by trade, with a hold-out firewall, a forward prediction, and tooling to run it offline on a
Mac Mini with Llama 3.1 8B (training data to Dec 2023).

## Repository map

| Path | What it is |
|---|---|
| `AGENT.md` | The agent specification (v1.5): era switch 1992-2026, six-gate pipeline, Pershing's eight published principles, templates T1-T9, sell rules S1-S5 + CONTROL, pass rules, post-mortem rules, output contract, exemplars (calibration trades only). |
| `prompts/` | The staged prompt chain `00_system` → `01_fact_sheet` → `02`-`06` gates → `07_decision_memo` (new ideas), `08_sell_hold` (existing positions), `09_hedge` (macro), `10_grader`, `11_leakage_check`, `12_forward_next_trade`; `one_shot_full.md` for bigger models; `schema_decision.json`; `CHANGELOG.md` (every prompt change and the calibration case that motivated it); `era_e_update_for_forward_runs.md` (forward runs only). |
| `tools/` | `run_agent.py` (Ollama / any OpenAI-compatible endpoint; `--mask`, `--one-shot`), `grade.py`, `scoreboard.py` (Wilson CIs), `canary.py` (checks the model does not know post-cutoff facts). |
| `calibration/` | 44 point-in-time data packs (`data_packs/<id>/docs/D01..`, `meta.json`), answer keys (`answer_keys/`, sealed set in `answer_keys/holdout/`), runs, scores, `scores/scoreboard.md`, `HOLDOUT_SEALED.md`, `PROMPT_HASHES_v1.5.txt`. |
| `compendium/` | Trade-by-trade dossiers 1992-2026 (`trades/`, 111 files; indexes by era; `SCHEMA.md`). Each: dates, size, thesis at the time, how/why decided, Ackman's own words, public discussion, outcome, lessons, sources. |
| `archive/` | Ackman profile, the eight official principles (Jan 2018 slide), 20 reasoning patterns, letters/interviews guides, `x_posts/` (88 authenticated posts, JSON + markdown), `forums/` (Reddit, VIC/COBF/Seeking Alpha/press). |
| `investor_profiles/` | 12 investor profiles + `what_makes_a_great_investor.md` + `ackman_vs_peers.md`. |
| `research/` | Best practices for investor-persona agents, look-ahead/evaluation design, and the critique/optimisation of the original brief (`prompt_critique_and_optimization.md`). |
| `forward/` | Frozen evidence pack (D01-D08, as of 2026-10-25) and `next_trade_prediction.md` / `.json`. |
| `run_log.md`, `RESEARCH_GUIDE.md` | What was done, by whom, with what evidence; how to extend the research. |

## Results in one paragraph
On 28 calibration decisions (1992-2025) the frozen chain, run on Replit's current internal model, matched Ackman's **direction
in 71% (named) / 68% (masked)** and reproduced **58-59% of his stated reasons**; on the 11 sealed hold-out decisions
(H2 2025-2026, never used for tuning) it matched **direction in 64%** and **49-54% of stated reasons**, with zero leakage flags.
On 8 discipline controls (names Ackman never bought at value-looking moments) it said PASS 7/8 named but only 5/8 masked —
Boeing 2019, Alibaba 2021 and Disney 2022 slipped through as "temporary fears", the clearest defect to fix next (v1.6).
It is strongest on his signature trade — a dominant, simple, FCF-generative franchise bought on a fear he judges temporary —
and weakest on sells, where it holds when he sells for comparative reasons ("better use of capital", "the distribution of
outcomes widened"). Full numbers, intervals and the divergence table: `calibration/scores/scoreboard.md`. These runs
measure prompt compliance on a model that may remember the outcomes; the fidelity test is the Llama 3.1 8B replay below.

## Run it on the Mac Mini (offline)
```bash
# 1. Install Ollama (https://ollama.com) and pull the model
ollama pull llama3.1:8b
# 2. Prove the model is pre-dated (should answer "unknown" to post-2023 canaries)
python tools/canary.py --model llama3.1:8b
# 3. Replay one decision, masked, with the staged chain; then grade it
python tools/run_agent.py --model llama3.1:8b --pack calibration/data_packs/2025_uber_buy --mask
python tools/grade.py calibration/runs/<run>.json calibration/answer_keys/2025_uber_buy.json
# 4. Replay everything dated after the model's cutoff and build the scoreboard
for p in calibration/data_packs/202[4-6]_*; do python tools/run_agent.py --model llama3.1:8b --pack $p --mask; done
python tools/scoreboard.py calibration/scores > calibration/scores/scoreboard_llama.md
```
`run_agent.py` also takes `--base-url` / `--api-key` for any OpenAI-compatible server and `--one-shot` for larger models.
Keep prompts frozen while scoring hold-outs; log any change in `prompts/CHANGELOG.md` with the calibration case that motivated it.

## The firewall
Calibration = decisions disclosed up to mid-2025. Sealed hold-out = Meta 2025, the 2025 exits (Nike, Chipotle, CP) and all
2026 decisions (Hilton exit; Microsoft, Netflix #2, Visa/Mastercard, S&P Global, ICE, Alcon buys). `AGENT.md` and the prompts
cite no hold-out specifics; the era-E addendum is appended only for forward runs. Prompts were frozen (hashes recorded) before
the hold-out packs were opened and were not edited afterwards.

## Forward prediction (scored 2 Nov 2026 reviews, 16 Nov 13F, 16 Feb 2027 13F)
`forward/next_trade_prediction.md` — the agent's ranked candidates with 90-day probabilities, likely changes to existing
positions, the single most likely next disclosed action, a separately-labelled principal's reconciliation, and the scoring plan.

## Licence / provenance
All source material is public (SEC filings, Pershing Square letters and presentations, X posts, press). Every compendium
entry and pack document carries its sources and dates; gaps are marked rather than filled. Prepared with Replit Agent.
