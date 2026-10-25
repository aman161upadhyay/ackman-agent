STEP 1 — FACT SHEET. AS_OF_DATE: {{as_of_date}}. Company: {{company}} ({{ticker}}).

Read the pack documents below and produce a structured fact sheet. Copy numbers exactly; attach the document label
to every item. If an item is absent, write "not in pack". Do not add anything from memory.

Return JSON:
{
 "business_description": "2-3 sentences [Dnn]",
 "segments_and_mix": ["segment: % of revenue/profit [Dnn]"],
 "unit_economics": ["margin, returns, pricing power, capex intensity, FCF conversion [Dnn]"],
 "competitive_position": ["share, rank, moat evidence, peers [Dnn]"],
 "growth_record_and_outlook": ["revenue/EPS growth history and guidance [Dnn]"],
 "balance_sheet": ["net debt, leverage, maturities, rating [Dnn]"],
 "management_and_governance": ["CEO tenure, incentives, capital allocation record, controller/dual-class [Dnn]"],
 "price_and_valuation": ["price, market cap, drawdown from high, P/E (trailing/forward), EV/EBITDA, FCF yield, own-history/peer/S&P comparison [Dnn]"],
 "what_the_market_is_worried_about": ["each worry with its source [Dnn]"],
 "recent_events": ["dated events up to AS_OF_DATE [Dnn]"],
 "pershing_context": ["fund AUM, current holdings, cash, existing stake, any prior engagement [Dnn] or not in pack"],
 "missing_data": ["figures you wanted but the pack lacks"]
}

PACK:
{{pack}}
