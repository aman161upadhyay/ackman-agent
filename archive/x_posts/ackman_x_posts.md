# Bill Ackman: investment-relevant X archive

**Cutoff/retrieval: 2026-10-25.** Companion machine-readable archive: [ackman_x_posts.json](ackman_x_posts.json).

**Coverage:** 88 unique status URLs with full main-post text as exposed by Firecrawl; 27 classified as containing an explicit buy/sell/hedge or proposed-transaction reason. **The requested 150+ target was not reached.** This is a partial, source-grounded archive, not an exhaustive timeline.

## Method, provenance and use

1. Used Firecrawl `POST /search`, body `{query: "site:x.com/BillAckman <topic>", limit: 10}`, for **every requested topic**. Successful results were followed by Firecrawl `POST /scrape` with `formats: ["markdown"]`. Repeated **429** errors required retries and left discovery gaps. No X API or mirrors were used.
2. Scraped [the profile](https://x.com/BillAckman) successfully. Its returned “Latest Posts” ranged from October 21–22, 2026. Only investment-relevant posts were admitted; the October 22 Fannie/Freddie post matched its individual status scrape. A profile scrape is not a guarantee of the complete latest timeline.
3. Returned threads supplied additional Ackman-authored status URLs, timestamps and individual texts. Those records carry `source_container_url` in JSON. Other users' comments and quoted third-party posts were **not attributed to Ackman**; selected critiques are in [the professional/public-commentary archive](../forums/vic_cobf_sa_press.md).
4. `full_text` in JSON is the **main post**, not the entire surrounding page. Thread posts are separate records where admitted. Linked letters, images, Spaces, video and missing quote-posts were not silently transcribed. Markdown/HTML entities and shortened links may be scraper artifacts; whitespace is normalized for readability. Text was not independently authenticated through the unavailable X API.
5. Below, **R = explicit transaction reason**, **N = no explicit transaction reason in the post**. “N” does not mean irrelevant: announcements, defenses of a holding, product observations and endorsements can matter without stating why a security was bought/sold. Reasons supplied only by a linked letter are **not** counted as stated in the post.
6. Quotes below are verbatim passages from returned text; long posts use **selected passages**, not an implied complete transcription. JSON holds the full returned main-post text for every admitted record. Source URLs and timestamps are in JSON; Markdown dates are UTC calendar dates.
7. All business facts, valuation figures, political forecasts and allegations inside quotations remain **Ackman's dated statements**, not independent findings. Post dates are the information-availability dates. Retrospective material must not be inserted into earlier point-in-time packs.

## Uber — product research, purchase thesis and AV debate

### 2024-05-23 — driver-tip allegation [N]

[Post](https://x.com/BillAckman/status/1793488978965856436)

> I took an @Uber today and for the first time was offered a NYC yellow cab. I thought good for Uber supporting the cabbies. I asked the driver about his experience with Uber and he surprised me by saying it was bad.

> He explained that even when the passenger agreed to pay a tip to the driver on the Uber app, the driver did not receive a tip and Uber kept the tip for itself.

**Correction follows next day.** The allegation is not accepted as established misconduct.

### 2024-05-24 — corrects premise, retains product criticism [N]

[Post](https://x.com/BillAckman/status/1793838467530580336)

> I was glad to learn from @Uber that the drivers are receiving their tips. That said, the taxi drivers themselves believe that they are not receiving them because their dashboards show no tips from Uber riders.
>
> This software failure results in angry drivers and Uber customers being perceived as stiffing the drivers.
>
> While it is great to learn from Uber that the drivers ultimately receive their tips, this is a serious flaw in the software and system that should be fixed.
>
> I spoke with Dara today and he confirmed that a fix is immediately underway. As I said in my initial post on the subject, I am an Uber and Dara fan and am confident that this will be rectified shortly.

### 2025-02-07 — two purchase disclosures, conflicting share counts [R]

**16:23:33 UTC:** [first status](https://x.com/BillAckman/status/1887900012937617903):

> Beginning in early January, we began acquiring a position in @Uber. Today, we own 33.3 million shares.

**16:27:08 UTC:** [later status](https://x.com/BillAckman/status/1887900916734738888):

> Beginning in early January, we began acquiring a position in @Uber. Today, we own 30.3 million shares.

Both texts were individually scraped and preserved; do not silently replace one number inside the other source. The later text continues:

> I have been a long-term customer and admirer of Uber beginning when Edward Norton showed me the app in its early days. I was also fortunate to be a day-one investor in the company through a small investment in a venture fund.
>
> While a great business, Uber suffered from erratic management. Since he joined the company in 2017, Dara Khosrowshahi CEO has done a superb job in transforming the company into a highly profitable and cash-generative growth machine.
>
> We believe that Uber is one of the best managed and highest quality businesses in the world. Remarkably, it can still be purchased at a massive discount to its intrinsic value. This favorable combination of attributes is extremely rare, particularly for a large cap company.
>
> We will have more to share about our thinking on the company shortly.

**Reasoning labels:** management transformation; profitable cash-generative growth; business quality; discount to intrinsic value. AV economics are **not stated in this purchase post**, even if later discussion emphasizes them.

### 2025-02-07 — shareholder product suggestions [N]

[Post, 21:00:14 UTC](https://x.com/BillAckman/status/1887969644234879172)

> You are most welcome. We are also super excited to be along for the Uber ride.
>
> Some more ideas:
>
> If I want to order Ubers for mom, the kids and me as we leave an event, I haven’t found functionality to do so. I have to use three separate accounts on different phones. A customer should be able to order an unlimited number of simultaneous Ubers and track each trip to make sure each guest makes it home. This will of course drive more volume.
>
> Tipping doesn’t work well. The tip is decided the next time one books a trip and by then, you don’t remember the ride. Instead, why not give the customer the opportunity to have a standard tip for every trip which can be modified after the fact for the rare case where you want to tip more or less?

The returned thread contains Dara Khosrowshahi's response about multi-ride abuse prevention and work on tipping; that response is **not Ackman's own language**.

### Later recommendations / endorsements [all N]

| Date | Source | Full short main-post text |
|---|---|---|
| 2025-03-22 | [Post](https://x.com/BillAckman/status/1903241963274408436) | “All of these arguments are supportive of @Uber. You should buy some.” |
| 2025-12-15 | [Post](https://x.com/BillAckman/status/2000545621288366177) | “We agree on @Uber. A well articulated bull thesis on the key issues.” |
| 2025-12-24 | [Post](https://x.com/BillAckman/status/2003652070466011501) | “An excellent piece on @Uber” |
| 2026-02-14 | [Post](https://x.com/BillAckman/status/2022636030076023127) | “Good piece on $UBER” |
| 2026-08-11 | [Post](https://x.com/BillAckman/status/2087288418392752393) | “Good analysis.” |

A recommendation referring to “these arguments” is not a recovery of those arguments. Scraped replies to the August 2026 endorsement debate private-owner AV capacity, Tesla's direct customer relationship and ride prices; see the companion commentary file, not the Ackman quote field.

## Nike — turnaround conviction and instrument substitution

### 2025-04-06 — risk size, options, permanent capital [R: prospective buying discipline]

[Post](https://x.com/BillAckman/status/1909023242536570991). Selected passages:

> 3. We have only one investment, Nike 3-year call options, that is directly affected by the tariffs, a position that represents 1.5% of our portfolio.

> 4. Unlike other asset managers, our capital base is more than 90% permanent so we are not exposed to redemptions from investors.

> All of the above said, we don’t short stocks and we have no hedges in place that would protect us from a self-inflicted market crash as we are long only.
>
> We will suffer mark-to-market losses if the market crashes, but we will not be sellers in a declining market.
>
> We will be buyers of great businesses at highly discounted prices which will benefit us and our investors over the long term.

This is not a claim of no embedded leverage in securities/companies: his separate no-margin assertion concerns financing and liquidity. The stated 1.5% must not be interpreted as notional exposure without further evidence.

### 2025-04-29 — Elliott Hill confidence [N]

[Post](https://x.com/BillAckman/status/1917058177297719406)

> I spoke to Elliott Hill, CEO of @Nike who apologized for the gaffe. Nike is in the midst of a turnaround which makes mistakes more likely to occur with talent turning over etc.
>
> Elliott is the right choice to fix the company, and he clearly has a lot of work to do. I am confident he will get it done.

This is management/turnaround conviction, not a new purchase disclosure.

### 2025-05-16 — 13F common-stock exit did not mean no economic exposure [N]

[Post](https://x.com/BillAckman/status/1923202256746278942)

> Our 13F reflects our sale of @Nike common stock, but does not reflect our purchase of over-the-counter call options in a similar notional amount. In our letter, we previously explained the reasons for the switch.

**Important classification:** transaction and instrument are explicit; the reasons are **referred to a letter, not stated in this post**. Do not substitute a third-party reply about capital efficiency/leverage for Ackman's words. This directly qualifies later “sold entire Nike position” headlines.

## Brookfield / Amazon / Meta — multi-company disclosure and hindsight

### 2026-05-15 — earlier buys described retrospectively [R]

[Microsoft thesis post](https://x.com/BillAckman/status/2055206659849437592), selected passage:

> For example, we acquired Alphabet $GOOG when the stock declined substantially on the release of ChatGPT in late 2022, Amazon $AMZN in the weeks following Liberation Day, and $META more recently on the market's response to the company's unexpectedly large cap ex guidance and expenditures.

The passage is dated **2026**, not contemporaneous entry documentation for those earlier investments. Its Alphabet wording is not an exact first-purchase date.

### 2026-06-15 — PSUS deployed portfolio [R]

[Post](https://x.com/BillAckman/status/2066552745025527940), selected passage:

> Since its IPO on April 29th, PSUS has deployed nearly 85% of its capital in 12 companies including Amazon, Microsoft, UBER, Meta, Brookfield, Restaurant Brands, Fannie Mae and Freddie Mac at prices we believe to be extremely attractive.

The post's “double discount” argument is quoted under PSUS below. This is a portfolio-wide statement, **not a standalone Brookfield company thesis**. No long Brookfield-specific Ackman post was recovered.

## Hertz — long explanatory purchase thesis

### 2025-04-17 — operational repair, fleet values, leverage and AV optionality [R]

[Post](https://x.com/BillAckman/status/1912955549542744462). Selected passages from the full text retained in JSON:

> We began accumulating shares in @Hertz late last year, and as of today, we have a 19.8% stake in the company comprised of outright share ownership and total return swaps.
>
> Hertz can be thought of as an operating company combined with a highly leveraged portfolio of automobiles. A misstep years ago with respect to the company’s purchase of Teslas created operating issues, some customer demand issues, and exposed the company to an unanticipated reduction in residual values when @Tesla dramatically reduced the price of its cars, leading to large operating losses.
>
> We believe that a combination of: (1) an improving industry structure and more rational competitive behavior, (2) the near resolution of the company’s over exposure to Teslas, (3) a successful operational turnaround plan under a new management team with a track record of success in an adjacent industry, and (4) the company’s leveraged capital structure will enable Hertz shareholders to generate a highly attractive return on investment.

> Hertz is uniquely well-positioned in the current tariff environment, where auto tariffs are likely to cause used car prices to rise. Hertz owns a fleet of over 500,000 vehicles valued at approximately $12 billion. A 10% increase in used car prices would equate to a $1.2 billion gain on its auto assets – equivalent to approximately half of the company’s current market capitalization.

> Valuation
> Using management’s nearer term targets of $1,500 revenue per unit (RPU), low $30s/day vehicle operating expenses, and ~$300 depreciation per unit (DPU), and assuming modest increases by 2029, including an increase in fleet utilization from 80% to 85%, we estimate that Hertz could generate approximately $2 billion of Adjusted EBITDA (a metric which is net of auto depreciation and interest expense for the company’s fleet and asset-backed financing).
>
> At 7.5 times EBITDA, a valuation that we believe to be conservative in light of improvements in the competitive posture of the industry, we estimate that Hertz will be worth ~$30 per share by 2029.

> Now for a fun thought experiment:
>
> What if UBER partnered with Hertz on an AV fleet roll out over time?

> Investing is risky. There are no guarantees of a successful outcome. Caveat emptor.

**Point-in-time discipline:** The 2029 target is conditional, not an outcome. Auto-price appreciation is a sensitivity, not a realized fleet gain. The Uber AV idea is explicitly a **thought experiment**, not an announced agreement. JSON also retains his liquidity/maturity argument and the operational levers; independent leverage/travel-demand criticism is in the press archive.

## Alphabet / Google / Microsoft / AI

### 2026-05-15 — Microsoft detailed underwriting [R]

[Post](https://x.com/BillAckman/status/2055206659849437592). Selected passages:

> As two of the largest forces in equity markets -- growing index ownership and increasing amounts of capital controlled by extremely short-term-oriented, leveraged, volatility-intolerant investors -- converge, we have found occasional opportunities to acquire some of the most dominant long-term compounding franchises at attractive valuations.

> Microsoft operates two of the most valuable franchises in enterprise technology, which account for approximately 70% of the company's overall profits: M365 and Azure.

> We began building our position in MSFT in February following a meaningful share price decline after the company reported its fiscal Q2 2026 results. We were able to establish our position at a valuation of 21 times forward earnings, broadly in line with the market multiple and well below Microsoft's trading average over the last few years.

> We believe Microsoft's recent share price decline has been principally driven by investor concerns around two key issues: i) the competitive positioning of M365 against increasingly capable AI lab offerings (notably Anthropic's Claude Cowork), and ii) the durability of Azure's growth, especially in light of Microsoft's evolving relationship with OpenAI.

> In our view, investors underestimate the resilience of the M365 franchise given its deeply embedded role across enterprises and highly attractive price-value proposition. Unlike point software solutions, which may be vulnerable to disintermediation by better-performing AI alternatives, M365 is tightly integrated into the daily workflow of nearly every large enterprise and is supported by Microsoft's identity, security, compliance, and data governance infrastructure, which would be nearly impossible to replicate.

> We view Microsoft's recent decision to restructure its OpenAI partnership not as a concession but as part of a deliberate pivot toward a more open, multi-model architecture that better serves enterprise customers, who increasingly seek optionality across model providers.

> To support Azure's rapid growth amid persistent supply constraints, Microsoft has raised its calendar year 2026 capex budget to approximately $190 billion. Consistent with what we have observed at hyperscaler peers Amazon and Google, we view this spend as growth capex that should drive future revenue generation. This is particularly true for Microsoft, given that roughly two-thirds of its capex budget is allocated to server and networking equipment that correlates directly with near-term revenue.

**Full-text material in JSON additionally covers:** M365 users/bundle economics; enterprise security/identity/compliance; Azure cloud and inference demand; OpenAI economic interest; LinkedIn, gaming and Bing; Copilot product effort; seat-plus-consumption pricing; model-agnostic Foundry usage; reported M365/Azure growth. All are his **dated asserted figures and judgments**, not independently validated here.

### 2026-05-15 — Google/Microsoft rotation announcement [N]

[Post](https://x.com/BillAckman/status/2055310176480006552), recovered inside the next day's returned thread:

> We sold Google and bought Microsoft. Interesting. I have enormous respect for Chris.

### 2026-05-16 — finite capital and relative opportunity cost [R]

[Post](https://x.com/BillAckman/status/2055544065580544457)

> To be clear, our sale of $GOOG was not a bet against the company. We are very bullish long term on Alphabet. But at current valuations and in light of our finite capital base, we used $GOOG as a source of funds for $MSFT.

This directly rebuts a simplistic interpretation that the Google sale itself proves an adverse absolute business thesis. The scraped thread contains independent critiques about relative growth, valuation and taxes; those are not his reasons.

## Howard Hughes / HHH — proposed control and capital allocation

### 2020-03-28 — supplies primary capital [R]

[Post](https://x.com/BillAckman/status/1244012077947240448), retrieved in the COVID thread:

> Just this Friday, we invested $500m to provide the Howard Hughes Corp., one of the largest real estate development companies in the US, with the capital it needs to continue its various development projects which will create 1,000s of construction and other jobs.

[Next post](https://x.com/BillAckman/status/1244012079197061122):

> These jobs and development projects will help the economy recover. HHC’s equity offering on Friday is the first, hopefully of many, equity offerings that will provide fuel for an economic recovery. Without this capital, HHC would have had to mothball many of its projects.

### 2025-01-13 — proposal letter release [N]

[Post](https://x.com/BillAckman/status/1878767294136078657), selected passage:

> The lawyers have been a bit slow so my apologies to Howard Hughes Holdings $HHH shareholders and employees for the delay. But thanks to @X, I don’t need the lawyers to distribute our proposal letter.

The post links [the primary proposal letter](https://assets.pershingsquareholdings.com/2025/01/13060332/HHH-Proposal-Letter.pdf).

### 2025-01-14 — proposal economics, fees and holding-company thesis [R]

[Post](https://x.com/BillAckman/status/1879226799944503341). Selected passages:

> - ManagementCo acquires $1.0 billion of HHH common stock at $85 per share from existing shareholders of HHH other than the Pershing Square Funds, which today own 37.6% of HHH.

> - HHH becomes a diversified holding company that pursues the acquisition of controlling interests in public and private companies with a goal of growing HHH’s intrinsic value per share over the long term at a high compound annual return; in other words, a modern-day Berkshire Hathaway.

> - Holdco receives a management and advisory fee of 1.5% of HHH’s market capitalization paid quarterly.  We reduce Pershing Square Holdings, Ltd. and the Pershing Square private funds management fees by an amount equal to the fees we earn on the HHH stock owned by the Pershing Square funds to avoid charging our clients double fees.  This will have the effect of reducing the Pershing Square funds' management fees by about 10-12% for so long as they hold HHH stock.

> - HHH is capitalized with balance sheet cash and excess free cash flow from HHC, which we anticipate will grow substantially.  HHH should also have access to public equity and debt capital.

> - The transaction is subject to board approval as well as approval by the majority of the minority shareholders of HHH.  There is no certainty the transaction will close and subject also to the negotiation of a definitive agreement and other documents.

JSON preserves the full plain-English summary, including the tender, debt funding, team, non-tendering fund holdings, approval and ownership assumptions. **Do not combine this January proposal with the later May definitive terms.**

### 2025-02-18 — revised primary-share proposal [R]

[Post](https://x.com/BillAckman/status/1891957378603491339). Selected passages:

> Pershing Square has submitted a proposal to Howard Hughes Holdings (NYSE: HHH) https://www.howardhughes.com/ to acquire 10 million newly issued shares of the company at $90 per share.  When combined with the 18.9 million shares that are currently held by the Pershing Square Funds, we will own 48% of the company.

> The new HHH will acquire controlling interests in private and public companies that meet Pershing Square's criteria for business quality.

> Owning small and growing MPCs that will eventually become large cities in the best pro-business markets in the country is a great long-term business.  It's a lot better than a dying textile company.

**Proposal only**, not an executed 48% acquisition.

### 2025-02-18 — 13D/presentation [N]

[Post](https://x.com/BillAckman/status/1891976316490047650):

> We will be filing a Schedule 13D shortly, which attaches a copy of tomorrow's Howard Hughes presentation.

### 2025-05-05 — transformation announcement [N]

[Post](https://x.com/BillAckman/status/1919353524229743071):

> I will be on @CNBC at 8:30am EST to discuss the transformation of @HowardHughesHQ into a diversified holding company.

The full post links the release describing a **$900 million / nine-million newly issued share investment**, rather than the February ten-million-share proposal.

### 2025-12-18 — Vantage [N]

[Post](https://x.com/BillAckman/status/2001664773155381474):

> Howard Hughes Holdings to Acquire Vantage Group Holdings $HHH

Full post announces a Space and links the company release. A future-tense transaction announcement does not alone establish completion.

### 2026-04-20 — Marc Grandisson board appointment [N]

[Post](https://x.com/BillAckman/status/2046179099962466756):

> Howard Hughes Holdings ($HHH) Appoints Former Arch Capital CEO Marc Grandisson to its Board

JSON retains the full linked release URL.

### 2026-09-25 — reduce real-estate capital intensity, invest in insurance [N]

[Post](https://x.com/BillAckman/status/2103483711157150001), selected passage:

> At the meeting, among other topics, we will discuss how we intend to accelerate the transformation of HHH to an insurance holding company by dramatically reducing the capital intensity of our Howard Hughes Communities real estate subsidiary, freeing up capital to be invested in Vantage, our insurance subsidiary.

The full returned post ends “To register, visit:” with no URL. No missing link was fabricated.

**Seaport gap:** Topic search attempted; returned material did not establish a substantive Seaport investment thesis. No Seaport post admitted by mere keyword association.

## Fannie Mae / Freddie Mac / FNMA / FMCC

### 2024-12-30 — detailed common-equity recommendation [R]

[Post](https://x.com/BillAckman/status/1873818034428694837). Selected passages:

> We have owned Fannie Mae and Freddie Mac common stock for more than a decade. Today, they trade at or around our average cost. As such, they have not been great investments to date.
>
> What makes them particularly interesting today versus any other time in history is that there is a credible path for their removal from conservatorship in the relative short term, that is, in the next two years.

> The scenario we envision is that:
>
> (1) the GSEs are credited with the dividends and other distributions paid on the government senior preferred, which would have the effect of fully retiring the senior preferreds at their stated 10% coupon rate with an extra $25 billion profit (in excess of the preferreds’ stated yield) to the government. This extra profit could be justified as payment to the government for its standby commitment to the GSEs during conservatorship.
>
> (2) the GSEs’ capital ratio is set at 2.5% of guarantees outstanding, a level which would have enabled the GSEs to cover nearly seven times the their actual realized losses incurred during the Great Financial Crisis — a true fortress-level balance sheet.

> Assuming a Q4 2026 IPO, the two companies collectively would need only raise about $30 billion to meet the 2.5% capital standard, a highly achievable outcome. Freddie needs more than Fannie (which will need little if any capital) because it has grown its guarantee book more quickly than Fannie in recent years.
>
> We estimate the value of each company at the time of their IPOs in 2026 at ~$34 per share. We assume their IPOs are priced at $31 per share reflecting a ~10% discount to their intrinsic values.

> We believe the junior preferreds are also a good investment, but they do not offer nearly the same return because their upside is capped.

> There remains a high degree of uncertainty about the ultimate outcome so you should limit your exposure to what you can afford to lose if you choose to invest.

**These are assumptions and forecasts, not completed outcomes.** JSON includes the retained-capital, taxpayer-profit, mortgage-insurer comparison and earnings-power arguments. No independent validation of the proposed 2.5% capital standard or retirement of senior preferreds is implied.

### 2025-05-31 — Tim Howard endorsement [N]

[Post](https://x.com/BillAckman/status/1928830707679244340):

> An important piece on Fannie Mae and Freddie Mac by Tim Howard former Vice Chair and CFO of Fannie Mae.

### 2025-08-10 — merger commentary link [N]

[Post](https://x.com/BillAckman/status/1954556514502320482):

> Risk Matters: It’s Time to Merge Fannie Mae and Freddie Mac | Robert H. Smith School of Business

Full post links the university article; it does not contain his own merger underwriting.

### 2025-09-15 — senior-preferred conversion, warrants and disclosure [N]

[Post](https://x.com/BillAckman/status/1967591777676001406), selected passages:

> Those that have suggested that the government is going to unilaterally convert the senior preferred stock (SPS) into common stock and massively dilute shareholders have lost the plot.
>
> The only way for a successful IPO to occur is to respect the original contract where the SPS receives a 10% return and the government receives 79.9% of both companies through the exercise of warrants.

> F2 institutional ownership is increasing every day. It is not as visible as usual because F2 shares are not considered 13F securities and there is no requirement for institutions to disclose their ownership stakes.

His conclusion about acceptable dilution is a political/market argument, **not a legal determination** that the government cannot choose another capital structure.

### 2025-11-13 — proposal Space and retained ownership [N]

[Post](https://x.com/BillAckman/status/1989004405392240688), selected passages:

> On the Space, we will share a proposed transaction which will enable the @realDonaldTrump Administration to achieve all of its objectives of maximizing value for taxpayers, eliminating the risk of mortgage spreads widening, and enabling the U.S. Treasury to demonstrate a mark-to-market value for its shareholdings in the two companies.

> And to dispel market rumors to the contrary, we have not sold our stake in the two companies and remain the largest common shareholder of both companies with more than 210 million shares.

The proposed year-end timing in the full post is his forecast on that date, not proof the transaction subsequently occurred.

### 2025-12-30 through 2026-10-22 — continuing endorsements [all N]

| Date | Source | Full returned main-post text |
|---|---|---|
| 2025-12-30 | [Post](https://x.com/BillAckman/status/2006134656203178145) | “This was a good one. It remains our best idea for 2026.” |
| 2026-07-26 | [Post](https://x.com/BillAckman/status/2081510804948463985) | “On Fannie Freddie, an important read.” / “Bullish.” |
| 2026-10-22 | [Post](https://x.com/BillAckman/status/2113316038846951517) | “Some thoughts on Fannie $FNMA and Freddie Mac $FMCC” |

The last item was also visible on the profile scrape. Its short returned caption does **not** justify inventing the content of an unseen attachment or audio discussion.

## Netflix / Visa / Mastercard / S&P Global

### 2022-01-26 — Netflix purchase [R]

[Post](https://x.com/BillAckman/status/1486460691519361024):

> We recently purchased more than 3.1m shares of @Netflix which makes us a top-20 holder. I have long admired Reed Hastings and the remarkable company he and his team have built. We are delighted that the market has presented us with this opportunity.

The post links the [2022-01-26 investor letter](https://assets.pershingsquareholdings.com/2022/01/26170421/Pershing-Square-Capital-Management-L.P.-Releases-Letter-to-Investors-01-26-2022.pdf). This short post expresses management/business admiration; the detailed business thesis is in the letter and is not silently imported into the quote.

**2022 exit gap:** No full Ackman X exit post was recovered in this run. The actual exit-letter/press discussion is linked in [reddit.md](../forums/reddit.md) and [vic_cobf_sa_press.md](../forums/vic_cobf_sa_press.md).

### 2022-07-30 — payments advocacy was not a disclosed investment [N]

[Post](https://x.com/BillAckman/status/1553518818051428358):

> For the record, neither I nor my firm have any economic interest, long or short, in @Visa, @Mastercard, @PayPal, Amex or any other any payments company, processing company, bank or other financial institution.

This is a date-specific no-position statement. It does not contradict later 2026 additions; it prevents classifying all 2020–2022 payments-company advocacy as investment disclosure.

### 2026-08-13 — six new-position updates [N]

[Post](https://x.com/BillAckman/status/2087707181919424838):

> Pershing Square $PS announced earnings this evening in advance of our call tomorrow at 9am ET and our Spaces on @X which will follow the call.
>
> Please read our letter in advance of the call which explains the quarter and provides updates on the portfolio and six new positions in $NFLX, $V, $MA, $ICE, $ALC, and $SPGI

**No detailed reason for any of the six is stated in the post itself.** A primary pointer, not a substitute for the dated letter. No missing full Visa/Mastercard/S&P Global thesis has been invented.

## Universal Music / UMG

### 2024-11-08 — listing-access and valuation catalyst [N]

[Post](https://x.com/BillAckman/status/1854890043548352932), selected passages:

> Pershing Square has a contractual right to cause UMG to be listed in the US. We will exercise this right and achieve a US listing for UMG no later than some time next year.
>
> UMG trades at a large discount to its intrinsic value with limited liquidity in significant part due to it not having its primary listing on the @NYSE or @NasdaqExchange and not being eligible for S&amp;P 500 and other index inclusion.
>
> We are going to fix this. Now is a good and appropriate time to do so.

The full text combines PSH's own Amsterdam-listing issue with a distinct UMG listing/domicile discussion. A plan and a contractual right are not evidence the move was completed.

### 2025-01-15 — registration-rights sale and US-listing economics [R]

[Post](https://x.com/BillAckman/status/1879654093129388474), selected passages:

> To clarify today's $UMG press release posted below, Pershing Square exercised its registration rights in UMG in order to catalyze a U.S. listing of the company.  Our reg rights agreement requires that Pershing Square sell $500 million of UMG shares (of its current $3.3 billion investment in the company) in connection with the U.S. listing, a sale we will complete in order for the listing to occur.
>
> We exercised our right to cause UMG to list in the U.S. because we believe it will substantially increase demand for (and the valuation of) UMG shares from investors who by mandate are limited to investing in securities listed on U.S. exchanges, and likely attract additional analyst coverage for the company.  We also believe the U.S. listing will greatly improve trading liquidity for the shares.

Distinguish this prospective contractual sale from the March portfolio-concentration trim.

### 2025-03-13 — reduce concentration after outperformance [R]

[Post](https://x.com/BillAckman/status/1900272994720899537):

> We decided to sell a portion of our UMG position today.  UMG has substantially outperformed the rest of our portfolio (other than the GSEs) year to date in light of its extremely strong recent results.
>
> UMG was our largest position going into the day at more than ~27% of our capital.  After the sale, it will still be our largest position at about ~17% of the portfolio.
>
> SLG and the UMG team have done a superb job growing the company.  We believe UMG is one of the best businesses we have ever owned.
>
> Late last year, we exercised our registration rights in order that UMG obtains a listing on a major U.S. exchange later this year, which we believe will be extremely beneficial to the company.
>
> In a world of uncertainty, owning a royalty on music with the best management team in the industry is a blissfully comfortable and profitable place to be.

This is a sizing/relative-allocation action while retaining strong business conviction, not a blanket repudiation of the thesis.

### 2026-04-07 — presentation [N]

[Post](https://x.com/BillAckman/status/2041484273459294631):

> This is the slide deck for our 10am EDT/4pm CET @UMG presentation.

Full post links [New UMG.pdf](https://x-shared.s3.us-east-1.amazonaws.com/New+UMG.pdf). The presentation itself is not silently included in post text.

### 2026-04-08 — AI uploads versus listening/revenue share [N]

[Post](https://x.com/BillAckman/status/2041843742911406580), selected passages:

> Thank you for sharing. The purpose of this page in our presentation is to show that despite the rapid proliferation of AI-generated music content on streaming platforms, this content has not gained share. This is best demonstrated by looking at the most recent year, the period in which AI music uploads have been the highest. As the page shows, there has been little to no correlation between share of content uploaded to streaming platforms and its listening share.

> UMG is taking several steps to maintain and grow its market share: 1) expanding its footprint in emerging markets as they become more relevant, 2) signing deals that incorporate artist-centric principles to demonetize "noise", tracks that do not surpass a threshold level of streams (e.g., 1,000 streams), or pay a multiplier for must-have content, 3) negotiating wholesale price increases for their content, and 4) expanding in label &amp; artist services with the formation of Virgin Music and acquisitions like Downtown Music.
>
> We believe that while streaming services have been and will continue to be overwhelmed by low-quality content, users will continue to want to listen to music that drives culture and fandom, and that UMG, due to its role in the ecosystem, will continue to attract, nurture, and break the artists that create it.

The full post explicitly distinguishes **stream counts from royalties** and lower-monetization emerging-market streams. This is a holding-thesis defense and an explanation of his chart, not independent confirmation that AI presents no risk.

## Canadian Pacific / CPKC — retrospective management-change lesson

### 2023-12-22 [R, retrospective on 2011]

[Post](https://x.com/BillAckman/status/1738048537403826379), selected passages:

> In 2011, CP was the worst run railroad in North America. Its board was comprised of the most illustrious Canadian CEOs and leaders. They were very proud.
>
> We bought 12% of the railroad. We recommended they hire Hunter Harrison, the best railroader in history. They gave us the Heisman.

> We installed Hunter as CEO and recruited Keith Creel, his protege. Keith runs CP today. He is even better than Hunter, may he rest in peace.

> CP showed the difference changing one leader can make.

The complete post is in JSON. It uses the CP episode to discuss Harvard; only the actual historical-investment reasoning is relevant to this archive. His narrative of the vote/board must be checked against 2011–2012 primary records before being used as an exact contemporaneous timeline. No 2026 CP exit post was recovered.

## Hilton / Restaurant Brands / Lowe's / Chipotle

### 2020-03-28 — names bought during COVID [N]

[Post](https://x.com/BillAckman/status/1244012086889414657):

> On CNBC I also disclosed that we were buying stocks like Hilton, Restaurant Brands and Starbucks.  By disclosing what we were buying in real time, I was sending a very bullish message to the markets, likely increasing the prices we would have to pay to buy more of these stocks.

The “N” label reflects that this post supplies actions/communication, while the recovery/valuation reason is in surrounding thread posts below.

### 2025-03-01 — Berkshire capital redeployed to larger discounts [R, retrospective]

[Post](https://x.com/BillAckman/status/1895820623533748645), selected passages:

> I explained on the podcast that we sold Berkshire during Covid because we found better things to do with our capital.  Again, this was not meant as a criticism.  While Berkshire stock declined significantly during the Covid crash, other businesses we knew as well, traded to even larger discounts to intrinsic value, so we redeployed capital from Berkshire to those companies which included Hilton, Loews, Restaurant Brands and others.

Within the same post, his reported podcast quote says:

> We could redeploy the capital in Hilton at $55 a share and Lowe's at $70, and other businesses, and that turned into a very good decision. So the benefit of owning liquid securities is you can sell a 70 cent dollar to buy a 40 cent dollar. And that's what we did, and maybe some at 30 cents.

**Text caution:** “Loews” in the explanatory paragraph and “Lowe's” in the quote are both preserved. He subsequently warns about transcript errors. The specific prices and relative-value characterization are 2025 hindsight, not a reconstructed 2020 buy ticket.

### 2026-01-06 — Hilton franchisor economics and management [N]

[Post](https://x.com/BillAckman/status/2008508677766979938), selected passages:

> .@HiltonHotels is one of the largest hotel brands and franchisors. Hilton hotels are owned by thousands of entrepreneurs and investors around the world. The hotel in question is managed and operated by a franchisee, not by Hilton corporate. Hilton helps market the hotel, coordinate reservations, and makes sure the hotel consistently meets the high standards it sets for its customers.

> Hilton is one of the best managed companies in the world. Its CEO, Chris Nassetta, is one of the most outstanding CEOs in the world.  I know that he is highly respected by @realDonaldTrump and the current administration.

The returned text calls him a customer/shareholder on that date. It is not an exit disclosure or a purchase valuation model.

**Chipotle gap:** Search returned product/political and general-profile hits; no sufficiently useful long investment post admitted. **Lowe's:** only the retrospective above recovered. **QSR:** dated COVID thread and later PSUS holdings statement, not a dedicated original thesis.

## Interest rates / 30-year Treasury hedge

### 2023-08-03 — structural inflation, supply/demand, asymmetric hedge [R]

[Post](https://x.com/BillAckman/status/1686906272937869312), selected passages:

> I have been surprised how low US long-term rates have remained in light of structural changes that are likely to lead to higher levels of long-term inflation including de-globalization, higher defense costs, the energy transition, growing entitlements, and the greater bargaining power of workers. As a result, I would be very surprised if we don’t find ourselves in a world with persistent ~3% inflation.

> So if long-term inflation is 3% instead of 2% and history holds, then we could see the 30-year T yield = 3% + 0.5% (the real rate) + 2% (term premium) or 5.5%, and it can happen soon. There are many times in history where the bond market reprices the long end of the curve in a matter of weeks, and this seems like one of those times.
>
> That’s why we are short in size the 30-year T — first as a hedge on the impact of higher LT rates on stocks, and second because we believe it is a high probability standalone bet. There are few macro investments that still offer reasonably probable asymmetric payoffs and this is one of them.
>
> The best hedges are the ones you would invest in anyway even if you didn’t need the hedge.  This fits that bill, and also I think we need the hedge.

Full text additionally covers deficits/new issuance, QT, Treasury maturity management, China/Japan demand and fiscal/governance concerns. Forecast yield arithmetic is his model, not an observed yield.

### 2023-08-03 — finite-downside option implementation [R]

[Thread post, 02:08:36 UTC](https://x.com/BillAckman/status/1686921981076086784), returned with the preceding post:

> We implement these hedges by purchasing options rather than shorting bonds outright. This makes it easier to sleep at night as it makes your downside finite. Our sleep-at-night test’ is a critical risk management tool.

The unusual punctuation is preserved from returned text.

### 2023-08-03 — Buffett's bills are not 30-year bonds [N]

[Post](https://x.com/BillAckman/status/1687109824511959040):

> We actually agree. Buffett would never buy 30-year Treasurys at anywhere near current yields. His purchases are just cash management using short-term T-bills. We also invest our cash in short term Treasurys.

His claim about Buffett is his interpretation. Maturity/cash-management distinctions matter more than a superficial “both trading Treasuries” comparison.

### 2023-09-22 — swaptions and continuing thesis [R]

[Post](https://x.com/BillAckman/status/1705056634072863102), selected passages:

> I believe that long-term rates, e.g, 30-year rates, will rise further from here. As such, we remain short bonds through the ownership of swaptions.

> The long-term inflation rate plus the real rate of interest plus term premium suggests that 5.5% is an appropriate yield for 30-year Treasurys. And query whether 0.5% is a sufficient real long term rate in an increasingly risky world.

> But I could be wrong. AI might save us.

JSON preserves the long structural-inflation, energy, issuance, foreign-demand, QT and technical argument. **Exit gap:** a full October 2023 bond-short-covering post was not recovered in this run; no exit quotation or date invented.

## Tariffs 2025 — preserve changing views, not a frozen narrative

These are policy/market-risk statements, generally **N**, not evidence he executed a short or hedge. The April 6 portfolio post explicitly says otherwise.

| Date | Source | Verbatim selected passage | Context |
|---|---|---|---|
| 2025-04-04 | [Post](https://x.com/BillAckman/status/1908084169885753848) | “An extremely insightful piece on tariffs and @realDonaldTrump’s strategy.” | Endorsement, not his own model. |
| 2025-04-06 | [Post](https://x.com/BillAckman/status/1908992002366292286) | “The president has an opportunity to call a 90-day time out, negotiate and resolve unfair asymmetric tariff deals, and induce trillions of dollars of new investment in our country.” | Long warning about business confidence, spending and investment. |
| 2025-04-06 | [Post](https://x.com/BillAckman/status/1909023242536570991) | “We will suffer mark-to-market losses if the market crashes, but we will not be sellers in a declining market.” | Portfolio statement; Nike calls, cash, no margin, permanent capital, no crash hedge. **R for prospective buying discipline**. |
| 2025-04-07 | [Post](https://x.com/BillAckman/status/1909206619897946361) | “It was unfair of me to lash out at @howardlutnick. I don’t think he is pursuing his self interest.” | Withdraws personal-incentive criticism while maintaining policy objection. |
| 2025-04-07 | [Post](https://x.com/BillAckman/status/1909215779305992338) | “The global economy is being taken down because of bad math.” | Criticism of tariff calculation; his assertion, not independently checked here. |
| 2025-04-08 | [Post](https://x.com/BillAckman/status/1909586890887438817) | “I am advocating for a 30, 60, or 90- day pause before the tariffs are implemented tomorrow to enable negotiations to be completed without a major global economic disruption that will harm the most vulnerable companies and citizens of our country.” | Supports using tariffs to negotiate, opposes immediate disruption. |
| 2025-04-09 | [Post](https://x.com/BillAckman/status/1910097472040653191) | “Looking at the facts objectively, the only word that comes to my mind is ‘brilliant.’” | Post-pause praise; full text retains disagreement over initial sequencing. |
| 2025-04-13 | [Post](https://x.com/BillAckman/status/1911381955641213023) | “The problem is that there remain millions of small and medium-size American businesses that suffer from an inability to adapt to the tariffs on China overnight.” | Requests temporary China reduction/pause despite praise for initial leverage. |
| 2025-05-01 | [Post](https://x.com/BillAckman/status/1918064533366608264) | “If the tariffs are paused, the pressure on the U.S. economy is largely removed  and time becomes our friend and China’s enemy in the negotiation.” | Distinguishes time pressure on US businesses from China negotiation leverage. |

**Full returned main texts for all nine are in JSON.** The changes are decision-process evidence; do not flatten the sequence into either uninterrupted endorsement or uninterrupted opposition.

## Pershing Square IPO / PSUS / Pershing Square Inc.

### 2024-02-07 — initial filing [N]

[Post](https://x.com/BillAckman/status/1755317238574252153):

> Today, Pershing Square USA, Ltd., filed a registration statement with the SEC for an initial public offering of its common shares.

The “12 to 24 core holdings / free-cash-flow-generative” phrase returned in search was in a **third-party comment**, not the main post. It has not been misattributed to Ackman's post text.

### 2024-07-31 — withdrawal / aftermarket problem [R, offering decision]

[Post](https://x.com/BillAckman/status/1818724659673620530), selected passage from posted release:

> Would investors be better served waiting to invest in the aftermarket than in the IPO?
>
> This question has inspired us to reevaluate PSUS’s structure to make the IPO investment decision a straightforward one. We will report back once we are ready to launch a revised transaction.

Full release text is retained in JSON. This 2024 withdrawal is distinct from the 2026 launch.

### 2026-03-10 — combined manager/fund offering [N]

[Post](https://x.com/BillAckman/status/2031349206363914308), selected passages:

> Today, Pershing Square Inc. (PSI), an alternative asset management company, filed to go public along with Pershing Square USA, Ltd. (PSUS) a new closed ended investment company managed by Pershing Square.
>
> In the combined offering, investors in the IPO of PSUS will receive shares in PSI for no additional consideration. For example, if an investor buys 100 shares of PSUS in the IPO, they will receive 20 shares of PSI at no additional cost.

The main post also says registration statements are **not yet effective**. Filing/terms are not completed issuance on this date. Full linked-letter/prospectus pointers and disclaimer retained.

### 2026-06-15 — deployment and double discount [R]

[Post](https://x.com/BillAckman/status/2066552745025527940), selected passages:

> Furthermore, as of this moment, PSUS is trading at a ~20% discount to the net asset value (NAV) of its underlying holdings so a buyer of the stock at today’s price is acquiring the current portfolio at a double discount. We believe the PSUS discount to NAV has emerged due to short-term technical factors related to the IPO that should moderate over time.
>
> Pershing Square management and affiliates are all-in, having acquired more than ten million shares or $500+ million of PSUS in the IPO and in the market thereafter.
>
> In summary, we believe PSUS and its portfolio holdings represent an extremely attractive bargain at today’s share price and we have put our money where our mouth is.

The cause and expected duration of the discount are his interpretation. Manager ownership/alignment does not itself resolve the closed-end-discount objection.

### 2026-08-13 — earnings / new names [N]

[Post](https://x.com/BillAckman/status/2087707181919424838), quoted under Netflix/payments above, directs readers to the quarterly letter. Separate the listed manager `$PS` and the investment fund `$PSUS`.

## Buffett / Berkshire / capital-allocation discipline

### 2024-12-06 — investment education [N]

[Post](https://x.com/BillAckman/status/1864876389163323716):

> This is a book worth buying. I am preordering now. I attended many Berkshire meetings over the years. Buffett and Munger are not just great investors. They are superb educators about business, life and more.

### 2025-03-01 — sale was relative valuation, governance is capital allocation [R, hindsight]

[Long post](https://x.com/BillAckman/status/1895820623533748645), selected passage:

> Our job is to oversee how's management doing, make sure they have the right incentives, make sure they make the right capital allocation decisions, but we view our job as more chief capital allocator. Maybe we focus on designing compensation incentives and then making the hard decision sometimes to replace a leader, but we don't run the business.

The post explains the COVID Berkshire sale as recycling a smaller discount into larger discounts, and discusses his interpretation of Buffett versus Abel governance. Full text is in JSON; it is **2025 hindsight**.

[Follow-up, 13:10:33 UTC](https://x.com/BillAckman/status/1895823975957332209) [N]:

> Some of my quotes above are garbled as the transcript is not entirely accurate.

This warning travels with the earlier post; it must not be lost when training on a purported exact podcast quotation.

## Herbalife / Valeant lessons

### 2024-02-15 — psychological, not economic, short [N]

[Post](https://x.com/BillAckman/status/1758165289458405602), selected passages:

> It is a very good day for my psychological short on @Herbalife. And it is an even better day for the world to see one of the biggest pyramid schemes fail.

> The FTC’s failure to act made Carl Icahn a billion dollars and cost Pershing Square investors a billion dollars, but that’s a side show.

**Full text in JSON contains interested-party allegations about regulators and others, not findings accepted by this archive.** Its chronology concerning Harris is questionable and requires checking; do not silently repair the quote or adopt it as historical fact. The useful reasoning lesson is his stated frustration with a regulatory catalyst and the distinction between perceived analytical vindication and realized investment outcome.

**Valeant X gap:** Combined Valeant/Herbalife-lessons search produced no useful recovered X thesis. Do not invent a “lesson tweet”; see dated independent criticism and Ackman-letter coverage in [vic_cobf_sa_press.md](../forums/vic_cobf_sa_press.md).

## COVID CDS hedge — complete recovered 2020-03-28 thread sequence

The [scraped container](https://x.com/BillAckman/status/1244012074931490817) returned **25 individually identified Ackman posts**, including the later 21:28:43 UTC addition. Text and per-post timestamps are retained in JSON. These are his defense after monetization, not a February initiation-day memorandum.

The two Howard Hughes posts are quoted above; they remain part of this sequence, not extra duplicate records.

To keep Markdown files below 60 KB, the full verbatim sequence and individual links are in [ackman_x_posts_covid_thread.md](ackman_x_posts_covid_thread.md), with the same 25 records in JSON. Its central reinvestment rationale is:

> We received $2.6 billion from liquidating our insurance policies. Because of our belief that the economy and markets would eventually recover from this crisis, and stocks were trading at bargain prices, we reinvested this capital in companies we know well.

[Source](https://x.com/BillAckman/status/1244012076428902401) [R]. Other thread posts explain protection of consumer-sensitive holdings, cheap CDS, offsetting portfolio losses, monetization chronology, pre-CNBC purchases and the subsequent unhedged position.

## Search coverage / explicit open gaps

All requested terms were attempted, including generic phrases that can be polluted by unrelated comments. Successful but empty combined searches included Restaurant Brands/QSR, Canadian Pacific/CPKC, and Valeant/Herbalife lessons; narrower or thread searches later recovered some relevant material. Search failures were predominantly **429**, not proof of no posts.

| Topic | Admitted evidence / limitation |
|---|---|
| Uber | Two purchase posts, earlier product issue/correction, shareholder suggestions and later endorsements. |
| Nike | Three-year-call risk sizing, CEO conviction, common-to-OTC-call clarification. Full original turnaround letter not transcribed as an X post. |
| Brookfield | PSUS multi-company update only; no long standalone thesis recovered. |
| Amazon | 2026 retrospective entry description and PSUS update; not a full 2025 purchase post. |
| Hertz | Long original disclosure with conditional model/AV thought experiment. |
| Alphabet/Google; Microsoft | Full Microsoft thesis, rotation and finite-capital clarification; earlier Alphabet timing is retrospective. |
| Howard Hughes/HHH | COVID equity support, January/February proposals, May announcement, Vantage and 2026 capital-intensity strategy. |
| Fannie/Freddie/FNMA | Long 2024 recommendation, 2025 capital-structure/ownership defense and 2026 endorsements/latest caption. |
| Netflix | 2022 purchase and 2026 new-position pointer; 2022 X exit post missing. |
| Visa; Mastercard; S&P Global | 2022 no-position qualification and 2026 portfolio-letter pointer; detailed individual theses missing. |
| Hilton | 2020 purchases, 2025 retrospective capital redeployment and 2026 franchise/management statement; exit post missing. |
| Chipotle | No substantive admitted standalone investment post. |
| Restaurant Brands/QSR | 2020 names bought, 2025 retrospective and 2026 PSUS holdings; dedicated thesis missing. |
| UMG | Listing catalyst, required sale, concentration trim and AI/music defense. 2021 original X transaction thread missing. |
| Canadian Pacific/CPKC | 2023 retrospective management-change lesson; 2026 exit post missing. |
| Lowe's | 2025 retrospective only. |
| Interest rates/30-year Treasury/hedge | August/September 2023 long theses and options implementation; covering post missing. |
| Tariffs 2025 | Nine admitted posts documenting warning, portfolio exposure, pause request and changed assessment. |
| IPO/PSUS/Pershing Square Inc | 2024 filing/withdrawal; 2026 combined offering, deployment/NAV discount and quarterly pointer. |
| Intrinsic value; free cash flow; we bought/we sold; position; 13F | Covered through actual business/transaction posts, not generic phrase occurrence alone. |
| Buffett/Berkshire | Maturity comparison, education, relative-value sale/governance retrospective and transcript warning. |
| Valeant/Herbalife lessons | Herbalife hindsight post; substantive Valeant X lesson missing. |
| Seaport | No substantive admitted investment post. |
| AI | Microsoft platform/capex thesis, UMG consumption defense and Treasury productivity caveat; unrelated education/political posts excluded. |

**Completion status:** usable partial archive with explicit gaps. Do not call it 150 posts, exhaustive X coverage, complete threads, or a verified full record of his 2024–2026 executions. The JSON's `posts` array is the countable corpus; repeated Markdown cross-references are not additional posts.
