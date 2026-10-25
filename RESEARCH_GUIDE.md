# Research guide for all workers on the Ackman-agent project

## What this project is
Aman Upadhyay (HBS, Seminar in Investing, Fall 2026; sponsor Laurion Capital) must build an AI agent that
reasons like **Bill Ackman** (Pershing Square). The agent is graded on *fidelity of decision AND reasoning*
to Ackman's real decisions, replayed point-in-time, not on returns. Rubric per trade: Direction, Reasoning
overlap (did it cite the drivers Ackman cited?), Discipline (does it pass on what he passed on?), Grounding
(claims traceable to the data pack, not model memory). The final model is a small, pre-dated open model
(Llama 3.1 8B, data to Dec 2023), so everything the agent must "know" has to be written down explicitly.

Today's date: 25 October 2026. Anything up to today is fair game for the archive. Be especially careful
to capture 2024-2026 events accurately (Nike, Brookfield, Uber, Amazon, Hertz, Howard Hughes control,
Fannie/Freddie, Hilton exit, Microsoft, Netflix 2026, Visa/Mastercard/S&P Global, Pershing Square's 2026
IPO/Holdco, CP exit) because they are the calibration and hold-out trades.

## Tools that work here (use them from CodeExecution)
- `webSearch({ query, searchQueries: [..], count: 10, isTextExtended: true })` — best first move. Returns snippets + URLs.
- `webFetch({ url })` — fetch a page/PDF as markdown (50k-char chunks; use `startIndex` to continue).
- `externalApi__exa({ path:'/search', method:'POST', headers:{'Content-Type':'application/json'}, body:{ query, numResults: 10, contents:{ text:{ maxCharacters: 3000 } }, startPublishedDate?, endPublishedDate?, includeDomains? } })` — semantic search with page text; also `/contents` with `urls:[...]` to pull full text.
- `externalApi__firecrawl({ path:'/scrape', method:'POST', headers:{'Content-Type':'application/json'}, body:{ url, formats:['markdown'] } })` — works on x.com profile and status URLs (returns post text + thread), on SEC EDGAR pages, PDFs, most news sites. `/search` with `body:{ query:'site:x.com/BillAckman uber', limit:10 }` finds X posts by topic.
- `queryWithLLM({ content, query })` — ask a question of a long document instead of reading it all. Use it to extract quotes/figures from long letters/PDFs.
- NOT available: the X API (`externalApi__x` returns 402), nitter/xcancel mirrors (down). Reddit pages: `webFetch` is blocked, but try Firecrawl on `https://old.reddit.com/...` and search snippets via `webSearch`/Exa.
- Keep ≤5 Exa/Firecrawl requests in flight at once. webSearch/webFetch can be parallelised more freely.

## High-value primary sources
- Pershing Square Holdings materials (letters, annual/interim reports, investor presentations, 2014-2026):
  https://pershingsquareholdings.com/materials/ and PDFs under https://assets.pershingsquareholdings.com/
  e.g. 2025 Annual Report: https://assets.pershingsquareholdings.com/wp-content/uploads/2026/02/18175039/Pershing-Square-Holdings-Ltd.-2025-Annual-Report.pdf
  2026 Annual Investor Presentation: https://assets.pershingsquareholdings.com/wp-content/uploads/2026/02/11144917/2026-Annual-Investor-Presentation.pdf
- Seeking Alpha / MarketScreener re-posts of PSH letters (H1/H2 each year, 2015-2026).
- Pre-2014 annual letters: search "Pershing Square annual letter 2008 pdf", Scribd, ValueWalk, Wayback, Insider Monkey, "Pershing Square investor letter" + year; 13D filings and exhibits on EDGAR (Pershing Square Capital Management CIK 1336528; Pershing Square Holdco CIK 2026053); Ira Sohn / Value Investing Congress presentations (Target, GGP, Herbalife "Who wants to be a millionaire?", MBIA "Is MBIA Triple A?", Farmer Mac "Buying the Farm", JCP, Fannie/Freddie "It's time to get off our Fannie", Burger King, Air Products, Valeant/Allergan, Howard Hughes, Chipotle, Netflix).
- Books: *Confidence Game* (Christine Richard, 2010) on MBIA; *The Big Short*-era coverage; *Dear Chairman* (Jeff Gramm) chapter on Ackman; *Pershing Square* case studies (HBS cases: "Pershing Square's Bet on Target", "Bill Ackman and Herbalife", "General Growth Properties", "Canadian Pacific").
- Interviews: Lex Fridman #413 (Feb 2024), David Rubenstein / Bloomberg Wealth, CNBC Squawk Box / Delivering Alpha, Invest Like the Best, Dealbook, Graham & Doddsville, Oxford Union, Bloomberg "The David Rubenstein Show", Masters in Business (Barry Ritholtz), Ackman's own X account (long posts explaining Uber, Nike, Hertz, Fannie/Freddie, Alphabet, Howard Hughes).
- 13F trackers: 13f.finance/fund/pershing-square, valuesider, whalewisdom, dataroma, secform4.com (13D/13G history), insidermonkey, stockcircle.
- Transcripts: Pershing Square Holdings annual investor calls/presentations (Feb each year), H1 calls (Aug/Sep), on stockanalysis.com / Seeking Alpha / Motley Fool.

## Writing rules
1. Every factual claim gets a source (URL + date) inline or in a numbered list. Prefer primary sources.
2. **No hindsight contamination** in "point-in-time" sections: write only what was knowable on that date and date-stamp numbers.
3. Quote Ackman verbatim wherever possible; his *stated reasons at the time* are the grading key. Mark hindsight quotes as hindsight.
4. Be honest about losses and reversals; divergences are as valuable as matches.
5. Where sources conflict or you are unsure, say so explicitly (`unverified`, `conflicting`). Never invent dates, numbers or quotes.
6. Write dense, factual prose and tables; no filler, no marketing tone.
7. Files are Markdown; keep each under ~60 KB; split if needed. Write with the `writeFile` callback or the WriteFile tool.
8. When you finish, append a short entry to `ackman-agent/run_log.md` (what you produced, open gaps).
