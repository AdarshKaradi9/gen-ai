# Resale Scanner ("Flip or Skip")

## One-line pitch
Point your camera at an item in a thrift store or garage sale and in two seconds see what it really sells for on eBay, Depop and Poshmark, your profit after fees, and a big FLIP or SKIP verdict.

## Who exactly (the beachhead audience and where they gather online, with sizes)
Part-time resellers and "side hustle" thrifters, mostly US, who decide in the aisle with a phone in hand. Where they gather:
- r/Flipping: about 513K-514K members, up about 69K-71K in the past year, roughly +15% (Hive Index and GummySearch, third-party counts).
- r/reselling about 107K members, r/Resell about 35K (GummySearch).
- Discord "Flipping Biz Hub" about 16K members (Hive Index).
- TikTok thrift-flip content: I could not find a reliable hashtag view count in my searches, so this is unverified.

## Demand evidence (searches, communities, trend signals, with sources)
- r/Flipping is growing about 15% a year (GummySearch, third-party).
- Supply-side signal: a single App Store search returns at least 14 near-identical scanners launched in 2025-2026 (ThriftHaul, ResalePal, Thrift AI Profit Finder, Underpriced, ResaleScan, FlipStart, SnapFlip, Thrift Pal, ThriftGenius, ThriftFlip, ThriftCheck, Price Snap, ThriftAI, The Thrifter). Many builders see demand; that is also a saturation warning.
- eBay itself pushes photo-first selling: its "Magical Listing" tool generates title, category, specifics and a price from a photo, and has been expanded to private sellers in the US, UK and Germany (Value Added Resource, eBay Innovation). It is a listing tool, not an in-aisle buy decision tool.

## Money proof (competitors with revenue/downloads, pricing, labelled by evidence type)
- SnapFlip: about 195 MAU, under $10K/month, 44% IAP / 56% ads; 24 ratings; $7.99/week with 7-day trial or $39.99/year (AppGoblin, third-party estimate; pricing from listing).
- Underpriced: PeerPush shows about $500 MRR and claims "over 10,000 resellers" (self-reported, unverified).
- No scanner in this niche showed verified revenue above small amounts in my searches. Adjacent proof that resellers pay for tools exists historically (ScoutIQ for book scouting), but I did not find current ScoutIQ pricing or revenue in my searches.
- Verdict on money: people clearly make money reselling, but I found no proof that an AI thrift scanner app makes meaningful money yet.

## Competitor weaknesses (what 1-2 star reviews and complaints say)
- Accuracy on the long tail: an aggregator of Thrift AI Profit Identifier reviews lists "inaccurate search results and broken links" as the top complaint (Marlvel, 68 reviews, small sample, third-party).
- A competitor's own blog admits niche, vintage and rare items get "inaccurate or generic" results and that pricing lags trends (Underpriced AI blog, vendor source).
- Active listings vs sold prices: many apps show asking prices, not sold comps. One developer says eBay's Marketplace Insights (sold data) API is locked to enterprise, so apps use scrapers (Product Hunt developer post, anecdotal).
- Google Lens is free and already "good enough" for identification; the paid layer must be the price truth and verdict.

## The wedge (the specific angle that beats incumbents)
Pick one category where sold comps are dense and mistakes are expensive, for example vintage clothing labels (Depop/Poshmark) or sports cards, and be visibly right there, showing real sold comps with dates, a confidence band, and fee-adjusted profit. Pair with a weekly "what to hunt" drop so the app is useful between trips. General "scan anything" is already a commodity.

## The 2-second clip
A hand holds up a $4 thrift store jacket under fluorescent light; the phone snaps it and a green card slams in: "Sold for $78 (12 sales, 30 days). Profit $51. FLIP." Cut to the shopper sprinting to the register.

## Core loop sketch
- Onboarding aha: 3 questions (where you sell, what you hunt, typical budget), then a free first scan of anything in the room.
- Daily/weekly action: scans during weekend thrift runs, plus a daily "find of the day" push with what it sold for.
- Streak/reward: weekly hunt streak and a running "profit found" counter in My Flips.
- Shareable artifact: a "Paid $4, sold $78" receipt card with the before photo, watermarked.
- Paywall: after the plan reveal and first scan; $7.99/week or $39.99-49.99/year with trial, scan caps to control API cost.

## Risks (regulatory, platform, saturation, retention)
- Data dependence on eBay; sold-data scraping can break or violate terms.
- Saturation: 14+ lookalikes, mostly built in 2026.
- Liability from bad calls; users churn after one wrong verdict.
- Usage is bursty (weekends), so weekly plans churn.

## Scores
| Criterion | 1-5 | Why |
|---|---|---|
| Two-second aha | 5 | Photo to price and verdict in one frame (competitor listings show this exact flow) |
| Visual short-video hook | 4 | Thrift-flip "paid $4, sold $80" format is natural; I could not verify TikTok view counts |
| Money already swims | 2 | Resellers earn, but scanner apps show <$10K/mo (AppGoblin) and $500 MRR (PeerPush, self-reported) |
| Daily reason to return | 2 | Thrift trips are weekly at best; daily needs an invented content hook |
| Shareable moment | 4 | Profit receipt card is screenshot bait |
| Unit economics | 3 | Profit motive supports $40/yr, but heavy competition raises CPI and bursty usage churns |
| **Total** | **20/30** | |

## Verdict
Skip as a general scanner; maybe only as a single-category specialist with real sold comps. The demo is perfect, but the field filled up with near-identical apps in 2026 and none shows meaningful revenue, which suggests the hook converts to installs better than to subscriptions.

## Sources
- https://thehiveindex.com/communities/r-flipping/
- https://gummysearch.com/r/Flipping
- https://gummysearch.com/r/reselling/
- https://appgoblin.info/apps/6761262922
- https://peerpush.com/p/underpriced-flip-smarter-skip-faster
- https://apps.apple.com/us/app/id6758965824
- https://apps.apple.com/us/app/-/id6762850899
- https://www.producthunt.com/products/lensflip-scan-know-flip
- https://www.valueaddedresource.net/ebay-ai-magical-listing-revisited/
- https://innovation.ebayinc.com/stories/magical-listing-tool-harnesses-the-power-of-ai-to-make-selling-on-ebay-faster-easier-and-more-accurate/
- https://marlvel.ai/api/llm/apps/shopping/com-thrift-profit-identifier-free
- https://underpricedai.com/blog/ai-pricing-tools-for-resellers
