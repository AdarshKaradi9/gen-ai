# I vibe coded a $20K/month mobile app in 14 days
- URL: https://www.youtube.com/watch?v=CwHD6Fg-Mjs | Channel: Starter Story | Views: 747846 | Length: 806s (~13.5 min)
- Sources used:
  - https://rosetta.to/u/starterstory/i-vibe-coded-a-20k-month-mobile-app-in-14-days (full caption transcript with chapters)
  - https://bulletpointpodcast.pages.dev/starterstory/i-vibe-coded-a-20k-month-mobile-app-in-14-days (structured bullet summary of the same episode; cross-check)
- Confidence: high (full transcript read)

## Core claims (3-7 bullets, what the video argues)
- Connor Burd, 23, no CS background, has ~6 apps doing "over a million dollars in sales a year" (self-reported); his newest, Payout, was built in under two weeks "100% with AI" and hit $20k/month in ~50 days.
- Onboarding is the product: "90% of users will probably only ever see your onboarding if you have a paywalled section," so spend as long designing onboarding as the core feature.
- A simple app with 1-3 good features can make real money if the onboarding converts; "your onboarding will pull most of the weight."
- Build apps that tap core human desires - be healthier, make more money, look attractive - so paying feels obvious (Payout: "make more money").
- Validation is cheap now: modified versions of existing apps are pre-validated; for new ideas check TikTok/Instagram comments for people asking how to solve the problem, then skip the waitlist and just build.
- Growth path: influencer campaign in the niche -> repeat formats that work with more creators -> use the UGC library as paid ads -> Facebook ads as the "most consistent way to drive revenue growth."

## Specific tactics (concrete, actionable; include numbers, prices, timings, exact UI choices)
- Research: download ~20 apps in the niche plus beautiful apps from other categories; screenshot every onboarding screen; lay them all out in one Figma line; cherry-pick questions, graphs and screens; re-skin to your theme.
- Onboarding must (1) invoke emotion ("most purchases are made emotionally"), (2) show the strongest incentives / how life improves, (3) feel personalised, (4) include charts/graphs so it "feels more scientific" and proven.
- Payout onboarding as demoed: activity notifications permission -> social proof screen -> paywall with weekly and yearly options, designed to push users to yearly for higher LTV.
- Vibe-coding prep: write a text doc describing the data model with sample JSON and notes per attribute before prompting so the AI "doesn't have to make any guesses"; build core functionality first, onboarding later; paste Figma screenshots into Claude/Cursor to generate whole screens; iterate but don't be picky - ship a version fast.
- Tooling: Claude Code for coding (only AI tool used), Figma (UI, App Store screenshots, icon), Mixpanel (analytics), Next.js + TypeScript (site/backend), Vercel (hosting), GitHub, Expo (cross-platform builds), RevenueCat (subscription analytics and price testing).
- Marketing: partner with a creator already in the niche; aim for "relatable, viral content ... that comes off as natural and unprocessed"; once a video performs, commission the same format from other creators; ads should balance entertainment (cheaper delivery on Meta) with explicit product push (conversion).
- Launch inside RevenueCat's Shipaton hackathon for visibility: Payout won the "Build and Grow" award ($65,000 prize) among 55,000+ entrants (self-reported).

## Named examples (apps/companies cited and what they did)
- Payout: class-action-lawsuit discovery app; lists settlements with eligibility, prepares a mailable PDF claim form, has a wallet tab (claims in progress) and forms tab; example settlement shown: NBA Top Shot Meta-pixel privacy case.
- Hotspot Events: Connor's first app, a social app that took 6-8 months and failed - "apps that are social are super hard to scale," so he moved to utilities.
- Starter Story Build (host Pat Walls' AI-coding cohort) is the sponsor.
- RevenueCat Shipaton.

## Numbers & evidence (any stats, revenue, conversion rates, retention figures; mark self-reported vs third-party)
- Self-reported: $20k/month revenue within ~50 days of an early-August launch; 12,000+ downloads; 300+ subscriptions; $1M+ lifetime subscription revenue across ~6 apps; "over a million dollars in sales a year"; built in <2 weeks; $65k hackathon prize from 55,000+ entrants.
- No retention, trial-conversion or CAC figures given. Weekly vs yearly price points are not stated.

## Contradictions or caveats (where this disagrees with common advice or other videos)
- "14 days" is the build time; $20k/month took ~50 days and an influencer push - the title compresses the two.
- Advocates long, emotional, quiz-and-chart onboarding for every app, which Tim Gabe (Aa89MC8jX2c) says is only justified when it buys personalisation or filters buyers.
- Fireship (Tw18-4U7mts) warns that vibe-coded apps with real customers get hacked; Connor's process addresses only build speed, not security.
- Agrees with Zach Yadegari that social apps are hard and utilities are easier, and that influencers come before paid ads; disagrees with An Nayal/PlayKit's organic-first sequence by treating paid Facebook ads as the destination.
- Monetisation leans on a paywall before value ("90% only see onboarding"), i.e. optimised for conversion, not retention.

## Memorable framings (quotable one-liners or named frameworks, verbatim if available)
- "The apps that I build are designed to make money from day one."
- "Realistically, 90% of users will probably only ever see your onboarding if you have a paywalled section in your app."
- "Most purchases are made emotionally and are not logical when it comes to consumers."
- "If you're creating a modified version of an existing app, then congrats, your app is already validated by other people."
- "I really believe that any app can make thousands of dollars these days ... if you can even capture a tiny grain of sand."
- "Build something simple with a great onboarding ... You only really need one to three good features and your onboarding will pull most of the weight for you."
