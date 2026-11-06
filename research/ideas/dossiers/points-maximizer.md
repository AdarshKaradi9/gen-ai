# Points Maximizer: which card to use, and what your points are worth

## One-line pitch
Tell it which cards you hold and it shows, at the checkout, which card earns the most, then turns your points balances into concrete trips ("your 87K Chase points = a business-class seat to Tokyo").

## Who exactly
US credit card rewards hobbyists and the much larger group of "points-curious" cardholders. r/churning has roughly 664K-676K members (third-party trackers; growth peaked around 2021 and has slowed). r/awardtravel size not found this round. The Points Guy is big enough that its founder invests in adjacent startups (Timeshifter round, press). Beachhead: 25-40 year old US professionals with 2-5 rewards cards who never redeem well.

## Demand evidence
- point.me reported 220K active subscribers in 2023 (Skift, company-sourced) and 1.5M registered users in its first year with ARR up 1,860% (self-reported).
- CardPointers claims 1M+ users (App Store description, self-reported); AppGoblin estimates about 97K iOS MAU (third-party).
- MaxRewards: about 156K iOS MAU estimated, Android about 98K installs (AppGoblin, third-party).
- Points content is a large creator niche (TPG, travel hacking TikTok), though I did not get hashtag counts this round.

## Money proof
- point.me raised $2M seed (2022), $10M Series A (2023) and $15M Series B (2024) with American Express and Bilt partnerships (press releases). Less than 20% of revenue from concierge (Skift, 2023).
- Roame (YC, about $500K pre-seed, third-party aggregators) runs a free search plus paid tiers for longer search windows and more programs, plus affiliate revenue.
- CardPointers: RevenueCat SDK detected, AppGoblin bracket "<$10K/month" on iOS (third-party estimate, likely understated because it sells heavily on the web with lifetime deals; unverified).
- MaxRewards: revenue not available. AwardWallet: no numbers found this round.
- Money in this niche is real but concentrated in award search and affiliate card referrals, which pay high bounties (not quantified here).

## Competitor weaknesses
- CardPointers and MaxRewards are built for enthusiasts: dense card lists, 5,000-card databases and offer auto-adding. Beginners bounce.
- Bank-linking (MaxRewards) breaks when banks change logins; offer auto-add relies on scraping that banks can block. I did not collect review quotes this round, so this is an inference from feature design, not verified complaints.
- Award search tools (point.me, Roame) answer "where can I go" only after you know what you want; none starts from "here is what you already have, visualised".

## The wedge
Start from the balance, not the search. Snap or type your balances and see them converted into three dream redemptions with a cash value ("you are sitting on $4,200 of flights"). Then a simple "which card here?" widget for daily spend. Beginner-friendly, visual, US-only at first, with revenue from a subscription plus card referral affiliate links.

## The 2-second clip
A screen shows "Chase UR: 87,000 points"; it morphs into a lie-flat seat photo with "Tokyo, business class, worth $4,200" stamped on it.

## Core loop sketch
- Onboarding aha: pick your cards from logos (no bank login), enter rough balances, instant "your points are worth $X" reveal.
- Daily action: "which card?" lookups at checkout via widget or location prompt; weekly "new sweet spot for your points" alert.
- Streak/reward: running "extra rewards earned this year" counter; monthly report.
- Shareable artifact: "I booked a $6K suite for $90 in taxes" redemption card; points-value leaderboard among friends.
- Paywall: after the value reveal; $9.99/month or $59.99/year, annual preselected; affiliate card bounties as second revenue line.

## Risks
- Saturation: CardPointers, MaxRewards, AwardWallet, point.me, Roame, Seats.aero and bank-built tools; well-funded players with issuer partnerships.
- Platform: award availability data needs airline scraping or paid feeds; banks and airlines block scrapers. Affiliate card programs require approval and compliance (US CARD Act style disclosures, FTC endorsement rules).
- Market: US-centric; churning community growth has slowed (Hive Index trend).
- Retention: daily use depends on remembering at checkout; many users drop the "which card" habit.

## Scores
| Criterion | 1-5 | Why |
|---|---|---|
| Two-second aha | 3 | "Points become a business-class seat" is visual; card choice itself is not |
| Visual short-video hook | 3 | Redemption-win content is popular in travel hacking; format proven by creators, not apps |
| Money already swims | 4 | point.me 220K subs (2023) and $27M raised; paid tiers at Roame, CardPointers |
| Daily reason to return | 3 | Every purchase is a touchpoint, but the habit is fragile |
| Shareable moment | 3 | Redemption bragging cards; finance balances are less shareable |
| Unit economics | 4 | Affluent users, $60/year pricing plus affiliate bounties; CPI in finance is high |
| **Total** | **20/30** | |

## Verdict
Maybe. Money clearly flows here and the users are affluent, but the field is crowded with funded tools and data access is the hard part. The beginner "your points are worth $X" angle is the only opening that suits a solo founder; build it if you can secure an award-data source and affiliate approvals early.

## Sources
- https://skift.com/2023/09/05/travel-rewards-booking-startup-point-me-raises-10-million
- https://prnewswire.com/news-releases/pointme-raises-15m-in-series-b-funding-establishing-it-as-a-tech-leader-at-the-intersection-of-personal-finance-and-travel-rewards-302251145.html
- https://techcrunch.com/2023/09/05/real-time-flight-rewards-search-engine-point-me-raises-10m/
- https://appgoblin.info/apps/1472875808
- https://appgoblin.info/apps/com.maxrewards
- https://appgoblin.info/apps/1435710443
- https://www.vcbacked.co/company/roame-holdings
- https://roame.travel/subscription
- https://app.dealroom.co/companies/roame
- https://thehiveindex.com/communities/r-churning/
- https://gummysearch.com/r/churning/
- https://athletechnews.com/timeshifter-takes-circadian-app-from-jet-lag-to-night-shift-5-3m-raised-to-date/
