# Sealed hold-out decisions (DO NOT use in prompt design, exemplars, or tuning)

Rule: the agent prompt (AGENT.md, prompts/*) may cite Pershing Square decisions disclosed up to mid-2025.
Everything below is held out. Packs for these are built by a worker who writes only the point-in-time
documents; the answer keys live in `calibration/answer_keys/holdout/` and are opened only at scoring time
(after v1 prompts are frozen). Results on these are the project's evidence; results on calibration trades are
prompt debugging.

| id (pack / key) | decision | pack as_of (cutoff) | first disclosed |
|---|---|---|---|
| 2025_meta_buy | BUY Meta Platforms after the Q3-25 capex scare | 2025-11 | PSH 2025 annual report, Feb 2026 |
| 2025_nke_sell | SELL Nike (exit Nov 2025) | 2025-11 | Q4-25 13F / PSH 2025 annual report |
| 2025_cp_sell | SELL Canadian Pacific Kansas City (2025; April-vs-May timing conflict preserved in key) | 2025 | PSH 2025 annual report |
| 2025_cmg_sell | SELL Chipotle (exit Nov 2025) | 2025-11 | Q4-25 13F / PSH 2025 annual report |
| 2026_hlt_sell | SELL Hilton (2 Feb 2026) | 2026-01 | PSH 2025 annual report / Q1-26 13F |
| 2026_msft_buy | BUY Microsoft (Feb 2026, after the 30 Jan earnings drop) | 2026-01-30 | Q1-26 13F (May 2026) |
| 2026_nflx_buy_2 | BUY Netflix #2 (Q2 2026) | 2026-04-20 | PS Inc H1-26 letter, Aug 2026 |
| 2026_v_ma_buy | BUY Visa and Mastercard (Q2 2026) | 2026-03-31 | Q2-26 13F |
| 2026_spgi_buy | BUY S&P Global (Q2 2026) | 2026-Q2 | Q2-26 13F |
| 2026_ice_buy | BUY Intercontinental Exchange (after 30 Jun 2026, i.e. Q3 — corrected from "Q2") | 2026-06-30 | PS Inc H1-26 letter / Q3-26 13F |
| 2026_alc_buy | BUY Alcon (after 30 Jun 2026, i.e. Q3 — corrected from "Q2") | 2026-06-30 | PS Inc H1-26 call / Q3-26 13F |
| (not built) 2026_googl_exit, 2026_umg_exit, 2026_htz_exit | Alphabet and UMG fully exited H1 2026; Hertz exited July 2026 | 2026 | PS Inc H1-26 letter / 13Fs — candidates for the next hold-out batch |
| forward_2026Q3 | whatever the Q3-2026 13F (due 2026-11-16) and the 2 Nov reviews show | 2026-Q3 | not yet public — see forward/next_trade_prediction.md |
| forward_2026Q4 | Q4-2026 13F (16 Feb 2027) | 2026-Q4 | not yet public |

Status (2026-10-25): all 11 built packs were run ONCE under frozen prompts v1.5 (hashes in PROMPT_HASHES_v1.5.txt); results
in scores/holdout/ and scores/scoreboard.md. No prompt was edited afterwards.

Discipline (pass) hold-outs: to be chosen from names Ackman publicly declined or never touched despite
screens suggesting them (see `calibration/pass_cases.md`).
