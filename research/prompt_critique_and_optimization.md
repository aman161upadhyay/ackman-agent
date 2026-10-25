# Critique and optimisation of the project instructions (for Aman)

You asked me to be the decision-maker, to critique your instructions, and to optimise them. This is that
document. It is blunt where it needs to be. Everything here is reflected in how the repository is built.

## 1. What you asked for, and what I changed

| Your instruction | What is right about it | What I changed and why |
|---|---|---|
| "Train the agent on all of Ackman's trades since 1992" | The archive is the raw material for codifying his process, and the era shifts (Gotham → activist → 3.0 → mega-cap quality) are themselves a finding. | **There is no training.** A frozen Llama 3.1 8B cannot be fine-tuned meaningfully on ~70 decisions without memorising them, and fine-tuning destroys the point-in-time property. "Training" here means (a) writing the process down (AGENT.md + prompts), (b) checking it against calibration trades, (c) revising the prompts, not the weights. Pre-2018 trades are used to test the *era switch*, not to tune 2024-26 behaviour, because the 2007 Ackman and the 2025 Ackman run different policies. |
| "Judge the agent trade by trade, with pre-trade data, in a loop, with an LLM" | Exactly the right loop shape: pack → decision → grade → revise. | Two separations the loop must respect. (1) **Leakage:** every current model (including the one I used tonight) knows what Pershing did. Runs with a current model measure *prompt compliance*, not fidelity. Fidelity evidence comes only from the pre-dated model, masked packs and canaries. (2) **Hold-outs:** anything disclosed after mid-2025 is sealed (`calibration/HOLDOUT_SEALED.md`); prompts were written without those examples and must be frozen (git tag) before the sealed packs are opened. Once opened, they are spent. |
| "Predict his next trade in the next ~2 months" | A forward test is the only test that cannot leak, and it is what Laurion will remember. | It is **outcome-framed**. Base rate: Pershing initiated 1-4 new positions a year in 2018-2025; 2026 is unusual (new PSUS/PS Inc. capital → 6-8 new names). The honest forward deliverable is a **ranked, conditional watchlist with probabilities** and pre-registered scoring: Brier score against the Q3-2026 13F (due 2026-11-16, covers Jul-Sep — a nowcast), the Q4-2026 13F (Feb 2027) and PSH's annual letter. "Name the one trade" is a coin flip dressed up as analysis; "here are 8 names with probabilities and the conditions under which he buys" is a process claim that can be wrong in an informative way. The forward run also uses an addendum with the 2025-26 rotations because, for a forward prediction, recent behaviour is legitimately known. |
| "Use X posts, Reddit, forums" | X is high-value 2023-26: he explains theses there before letters. | Reddit/VIC/forums almost never contain his reasoning; they are useful as **inputs to the packs** (the "what the market was worried about" document that the agent must argue against), not as knowledge for the agent. Treat them that way. |
| "A series of prompts and an AGENT.md" | Correct format for a frozen 8B model: everything it must "know" has to be in the prompt or the pack. | Added: JSON output contracts, a staged chain (fact-sheet → gates → memo) because an 8B model cannot hold a 20-page spec and a 10k-token pack at once, a grader prompt, a leakage prompt, and a runner (`tools/run_agent.py`) that enforces the contracts outside the model. |
| Deck: 4-5 trades (Nike, Brookfield 2024; Uber, Amazon 2025; CP exit; maybe Netflix) | They are the right kind of decisions. | **Too few.** With N=5, 4/5 matches has a 95% Wilson interval of 38%-96%; you cannot distinguish a good agent from a lucky one. Post-Dec-2023 there are ~19 scored decisions once you include exits (Chipotle, CP, Nike, Hilton), adds/trims (Alphabet, Uber), the Hertz turnaround, HHH control, Fannie/Freddie, and the 2026 buys (Meta, Microsoft, Netflix, Visa, Mastercard, S&P Global, ICE, Alcon). Add documented passes and control cases. Report MATCH/PARTIAL/MISS counts with intervals; list divergences first. |
| Rubric: Direction / Reasoning overlap / Discipline / Grounding; Match = same decision + 3 of 4 drivers | Good. The reasoning-overlap criterion is the whole project. | Score **drivers independently of grounding**: a correct driver without a pack citation gets overlap credit but fails "grounded match" (the model remembered it). Require the grader to quote the agent sentence that matched each key driver. Use a strong model as grader plus a human spot-check of every MATCH; record disagreements. |

## 2. The three failure modes your plan is most exposed to

1. **Right answer, wrong reasoning (or memory).** A current model says BUY Uber in Jan 2025 because it knows Pershing did.
   Fixes built in: pre-dated model as the primary subject; masked twins (`--mask` replaces company/ticker with "the
   Company"); canary sentences planted in packs (`tools/canary.py`) to prove the pack was read; leakage checker prompt.
2. **Prompt overfitting.** Every time you edit AGENT.md after seeing a miss on Uber, the Uber score becomes meaningless.
   Fixes: calibration vs sealed split; prompt versions tagged in git; a change log that states which calibration case
   motivated each change; sealed runs only after a tag.
3. **Model capacity masquerading as process error.** An 8B model may fail Gate 3 arithmetic no matter how good the
   prompt. Fixes: deterministic arithmetic where possible (the runner can compute IRR from the model's stated inputs),
   staged prompts, temperature 0, `num_ctx` 16k, and a paired comparison with a stronger model on the same packs
   (if the 70B passes and the 8B fails with the same prompt, it is capacity, not process).

## 3. What is actually novel in your project (lean into it)

- The **era switch** as an explicit parameter: the same agent must produce a 13D-style activist plan for CP in 2011 and a
  quiet 8% position in Uber in 2025. Most "investor persona" agents are a static checklist (see
  `research/agent_building_best_practices.md` on the ai-hedge-fund Ackman agent: five ratios and a hard-coded score).
- **Discipline as a first-class output.** Ackman's edge is mostly in what he does not buy. A pass-set with his stated reasons
  (and control names that fail his gates — biotech, commodity, levered acquirers, controlled companies) is a stronger test
  than buys.
- **Divergence reporting.** The two places where his modern rules contradict his past (Valeant 2015, Herbalife 2012) are
  the best demonstration that the agent encodes a *process*, not a biography.

## 4. The optimised one-page brief (use this with any model or person)

> Build an agent that reproduces Pershing Square's decision process on a given date using only a dated evidence pack.
> Inputs: AGENT.md (process spec), prompts/ (staged chain), a pack (D01-Dnn). Output: one decision with 3-5 cited drivers,
> a valuation with IRR, a catalyst class, kill criteria, and a memo in letter voice. Evaluation: calibration set (≤ mid-2025)
> for tuning; sealed set (H2-2025 onward) opened once after a git tag; metrics = direction, driver overlap (k of N),
> discipline, grounding, leakage flags; report with Wilson intervals and a divergence table. Subjects: Llama 3.1 8B
> (primary, pre-dated), one current model (compliance baseline), both named and masked. Forward: a ranked watchlist with
> 90-day probabilities, scored by Brier against the next two 13Fs. Deliver to Laurion: the archive, the spec, the prompts,
> the packs, the scoreboard, and the retrospective with the misses first.

## 5. Things I deliberately did not do

- No fine-tuning, no RAG index, no knowledge graph (the team doc rules them out, and they would hide where the
  knowledge came from).
- No single-point "next trade" claim without probabilities.
- No use of 2026 decisions as examples in the agent spec (they are the test).
- No claim that tonight's current-model runs are fidelity evidence; they are prompt debugging and are labelled as such in
  `calibration/scores/`.

## 6. Timeline fit (your deck: v1 by 28 Oct, blind test to 11 Nov, basket to 25 Nov, final 2 Dec)

- 26-28 Oct: install Ollama on the Mac Mini, run `tools/run_agent.py` on the calibration packs with `llama3.1:8b`, grade,
  fix prompt failures that are *process* errors (not capacity errors). Tag `v1.0`.
- 29 Oct-11 Nov: run the sealed packs once (named and masked), grade blind, write the divergence table. Do not touch
  prompts for the sealed set; if you must, tag `v1.1` and report both.
- 16 Nov: Q3-2026 13F — score the nowcast portion of the forward list. 12-25 Nov: Laurion basket — the agent should PASS on
  most names; the quality of the pass reasons is the result.
- 2 Dec: retrospective. Lead with the misses.
