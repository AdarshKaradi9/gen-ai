# Deep dive: Monetization, unit economics and user complaints

## Key takeaways for the build

- **Paid ads do not pay back at a $34.99 annual price.** The base case earns about $0.89 net per install over 12 months (my model, built on RevenueCat medians). Third-party estimates put a US iOS Health & Fitness install at about $3.50 to $8 on TikTok and Meta. Growth has to come from organic short video, referrals through the accountability group, and finals-season timing. Paid ads are only for testing creatives.
- **Use a hard paywall after onboarding with a 7-day trial on the annual plan, not a 3-day trial.** RevenueCat 2026 (verified): trials of 4 days or less convert at a 25.5% median, against 37.4% for 5 to 9 day trials. 55.4% of 3-day trial cancellations happen on Day 0. Hard paywalls convert downloads to paid 5x better than freemium (10.7% vs 2.1%), with nearly identical year-one retention.
- **Lead with the annual plan. Offer monthly and skip weekly.** Health & Fitness is the annual category: 68% of subscriptions and 59% of revenue are annual. Weekly plans keep only 1-2% of subscribers after a year. Weekly pricing is also a named grievance in Brainrot reviews ("$5/week is insane!").
- **Don't run a fake discount on paywall exit.** Brainrot shows a "50% OFF FOREVER" popup after the main paywall. Several 1-star reviews call it "scammy" and ask for the $25 price to be shown up front. The cleanest version of "honest billing" is one honest price, a reminder on day 5 of the trial, and a visible charge date.
- **Trial-to-charge surprise is the most common complaint category**, about 24% of 1-3 star reviews (Unstar, vendor blog, indicative only). The canonical example is Opal's $99.99 yearly charge for someone who "missed canceling by one day" (Opal community forum). A pre-charge reminder costs a little conversion but takes away the most common reason for a 1-star review.
- **Users pay for enforcement that holds and for tracking that is accurate.** They resent paying for something iOS Screen Time does for free, bugs that wipe their progress, and blocks that silently stop. Reliability work on the Screen Time API is a revenue feature, not just QA.
- **Realistic year-one outcomes**, all from my model with assumptions stated below: pessimistic about $600 net MRR at month 12, base about $7K, optimistic about $45K. Cumulative net cash for the year is about $7K, $73K and $450K. The base case needs about 88K installs in year one, mostly organic.
- **Budget for refunds and for year-two churn.** The RevenueCat median refund rate is 4.7% for Productivity and 3.4% in North America. Productivity also has the weakest first annual renewal (23% median), so year-one revenue overstates the long-term value of each payer.

## 1. Paywall teardowns

**Opal.** The Adapty paywall library (third-party estimate, updated Oct 24, 2026) lists these price points:
- Yearly: $99.99, plus older $59.99 and $69.99 variants.
- Monthly: $19.99 and $8.99.
- Weekly: $4.99 and $9.99, plus an "Opal Student Weekly" plan at $9.99.
- An "Opal Pro Subscription" at $49.99.

Adapty's estimate is about 200K monthly downloads. Its revenue figure is inconsistent: $600K/month in the header and $400K in the body text.

Detox.so (third party) reports a free week on the yearly plan and three free days on monthly for web purchases. Opal is the price anchor of the category and draws the most anger about price.

**Brainrot.** The ScreensDesign teardown (third-party observation) describes:
- A 28-step onboarding with an interactive "brain decays as you slide up your screen time" moment, a named "attention profile", and a "years of your life lost" visual that then flips to "get 15 years back".
- A hard paywall at the end, with yearly and weekly plans and "7K+ 5-Star Reviews" as social proof.
- A "50% OFF FOREVER" offer that pops up right after the first paywall.

App Store reviewers report the annual price falling to about $25 after the discount, and the weekly price at about $5 (self-reported by users). The App Store listing states "All features described above require a subscription." The founders say they mostly sell annual plans (Stork.ai, self-reported).

**one sec.** ScreensDesign (third-party estimate): 4 onboarding steps, a soft paywall right after the personalization quiz, a Free vs Pro comparison table, Individual and Family plans, and a 1-week free trial that converts to yearly. Its estimates are 85K installs and $150K a month. The App Store listing (verified) says one app is free forever, and Pro is sold as annual, monthly or lifetime unlock. Unstar puts the price at about $19.99 a year.

**ClearSpace.** ScreensDesign (third-party estimate): 7 onboarding steps, then the paywall after the quiz and the permission grants. It offers a single annual plan with a 7-day trial, framed by a benefits timeline and a before/after graphic. Estimates are 25K installs and $60K a month. The App Store in-app purchase list (verified):
- Annual: $44.99, $49.99 and $59.99 variants.
- Monthly: $6.99.
- Family: $79.99.

ClearSpace already has a "Teammates" feature that notifies a friend when you exceed your limits. That matters for our wedge: the accountability group is not new. Its execution and its audience have to be the difference.

**Jomo.** Per App Store snippets and a Habit Doom check on Oct 10, 2026 (secondary): $5.99 monthly, $29.99 annual with a 3-day trial on annual only, and $99.99 lifetime. A Family tier is reported at $59.99 a year. I could not load Jomo's Adapty page.

**Pattern.** The serious players run annual-first plans priced at $20 to $100 a year. Their trials run 3 to 7 days and mostly sit on the annual plan. Lifetime options appear only with the indie or ethics-branded apps (one sec, Jomo). The paywall sits right after an emotional, personalized onboarding.

## 2. Category benchmarks

These come from RevenueCat State of Subscription Apps 2026 (verified from the report page; the data covers 2025, 115K apps and $16B in revenue). Note that the report sorts apps by category, and a screen-time app could be filed under Productivity or Health & Fitness.

| Metric | Health & Fitness | Productivity / other |
|---|---|---|
| Download-to-trial, D30 | 6.9% median (top performers above 23%) | North America overall: 7.1% median, 15.0% top quartile |
| Trial-to-paid | 37.7% median, 51.4% top quartile | North America overall: 34.2% median |
| Download-to-paid, D35 | 2.9% median, 6.2% top quartile | Hard paywall 10.7% vs freemium 2.1% (all apps) |
| Plan mix | 68% annual by volume, 59% of revenue | Report text is internally inconsistent (says 77% monthly in one place, 77% yearly in another) |
| Year-one retention, annual | Annual renewal rate 86.4% among active users | Productivity year-one annual retention about 23%; first annual renewal 23% (lowest category) |
| Refund rate | Most categories 3-4% | Productivity 4.7% (highest); North America 3.4% |
| Revenue per install | $0.48 at D14, $0.66 at D60 | |

**Trial length** (all apps): 25.5% median conversion for trials of 4 days or less, 37.4% for 5 to 9 days, 42.5% for 17 to 32 days.

**Retention by plan, year one** (all apps): weekly 1-2%, monthly 6-14%, annual 20-40% (overall annual median 28%, down from 31%).

**Price effect on annual plans:** low-priced annual plans keep 36% of subscribers through year one, against 23% for high-priced ones. Higher-priced annual plans also lose more at the first renewal (37% vs 24%).

**Adapty State of In-App Subscriptions 2026** (vendor data; $3B in revenue, 16K apps):
- Health & Fitness has the highest one-year install LTV, $1.21 globally, with North America about 2x the global average across categories.
- In Health & Fitness, trials raise LTV for annual subscribers. In Productivity, direct buyers are worth more ($56.95 vs $49.13).
- High-priced apps earn about 3x the LTV of low-priced ones.

These two sources pull in opposite directions on price. RevenueCat says cheap annual plans retain better; Adapty says expensive plans earn more. A $34.99 to $39.99 price sits near the Health & Fitness median annual price ($39.99 to $44.99) and is defensible against both.

## 3. CPI and LTV per install

There are no rigorous public CPI tables. RocketShip HQ states plainly that Meta publishes none. All figures below are third-party estimates from agency blogs:
- TikTok, Health & Fitness, Tier-1 iOS: $3.50 to $8.00 (theviralapp.com). Health apps aimed at 18 to 34 year-olds sit at the low end.
- Health & Fitness, US iOS: $2.00 to $5.50 (semnexus); $3.50 to $7.00 (admiral.media).
- Meta health median: $7.80, with a $5 to $12 interquartile range (cited via RocketShip HQ's summary).

I found no student-specific CPI data. My working assumption is $3 to $6 on TikTok for a strong UGC creative aimed at 18 to 24 year-olds in the US, and $5 to $10 on Meta. Students also tend to convert worse on price than the average Health & Fitness buyer, which is an assumption and not a sourced figure.

LTV per install over 12 months in my model, net of Apple's 15% small-business commission and refunds:

| Scenario | LTV per install |
|---|---|
| Pessimistic | $0.34 |
| Base | $0.89 |
| Optimistic | $1.83 |

These sit sensibly next to RevenueCat's $0.66 D60 revenue per install and Adapty's $1.21 global figure. Even the optimistic case is below the cheapest credible CPI.

Payback on paid ads would need roughly 2x to 4x better unit economics. Possible levers are a higher price ($59.99 or more, in Opal's range), a download-to-paid rate above 8%, or year-two renewals. A first annual renewal of 23-36% adds only about $7 to $11 per annual payer. Paid ads are therefore an amplifier for organic winners (Spark Ads on posts that already perform), not the engine.

## 4. What users pay for vs resent

**Opal**
- "I missed canceling my subscription by one day and am now out over $100. This feels like a dark pattern... either make the trial at least 14 days or funnel it into a monthly subscription instead of forcing yearly." (community.opal.so, user J_P)
- "It's very unclear to me why Opal... would cost $90 a year when the iPhone allows you in the settings to set restrictions" (App Store review via justuseapp).
- A user praised the app: "this app is single handedly saving my college degree" (App Store listing review). Students do pay when it works.

**Brainrot**
- "when exiting out there was a 50% off the annual plan... that feels scammy. Just offer the $25/year subscription straight away... $5/week is insane!" (App Store).
- "Why do I have to pay before even using the app?... give us like a 3 day free trial at least" (App Store).
- "It isn't until AFTER you're prompted to share your data and allow them access to my screen time app info, that they hit you with the pay wall. Not cool" (justuseapp).
- "Brainrot will reset my screen time after a day of perfect use... It has also deleted my usage over the past week. I was proud of my progress and now it is gone... I will be pursuing a refund" (justuseapp).

**one sec**
- "one sec was magic for ten days then I started tapping through on autopilot." Also "$20/year to add a breathing screen feels steep once the novelty wears off." Both quotes are from Unstar, a vendor blog; I did not verify them.
- Unscroll's summary of 874 Reddit users (a vendor-run aggregation): people leave one sec because "it only interrupts the moment you open an app, not the endless scrolling once inside, and users become immune to the breathing exercise after a few days."

**Brick**
- Reddit quote (via Unscroll): "The brick is pricey and it doesn't take a genius to bypass some things, even in Strict Mode, but, man, it's so effective for me."
- Promolatte cites a Reddit user who bypassed it "through settings or a phone restart". I could not verify the original thread.
- Cybernews lists app crashes during setup, only five emergency unbricks, and browser workarounds. Other reviewers mention NFC taps that need several attempts.
- The friction of physically walking to the puck is what users praise most.

**Summary.** Users will pay for:
- blocks that actually hold (strict modes, physical friction);
- accurate stats and progress that survives bugs;
- encouragement and goals beyond what native Screen Time offers;
- a fair, playful character.

They resent:
- surprise annual charges and short trials;
- fake or exit-intent discounts;
- weekly pricing;
- paying for features iOS offers free;
- silent block failures;
- the paywall appearing after permissions have been granted;
- interventions that wear off.

I found no direct Reddit threads; the Reddit material is only available through search snippets and vendor summaries.

## 5. Year-one scenarios (months 1-12)

**Assumptions shared by all three scenarios:**
- iOS only.
- Annual plan at $34.99 with a 7-day trial, and monthly at $6.99. No weekly or lifetime plan.
- Apple Small Business Program commission of 15%, so net is 85%.
- Annual subscribers do not renew inside year one.
- Monthly subscriptions follow RevenueCat-style renewal curves.
- Trial conversions happen in the month of install.
- No seasonality is modelled. In practice, launch into finals (late April or early December) to get a spike.
- Install volumes are my assumptions, not benchmarks. For reference, third-party estimates are ClearSpace 25K a month, one sec 85K and Opal 200K. Brainrot's self-reported launch day was 5K installs.

| Assumption | Pessimistic | Base | Optimistic | Basis |
|---|---|---|---|---|
| Installs, month 1 | 2,000 | 5,000 | 10,000 | Assumption |
| Monthly installs after launch | 1,500, +3%/mo | 4,000, +12%/mo | 8,000, +20%/mo | Assumption |
| Download-to-trial | 6% | 10% | 15% | RC: H&F median 6.9%, North America top quartile 15% |
| Trial-to-paid | 25% | 35% | 45% | RC: ≤4 day trials 25.5%, North America median 34.2%, H&F top quartile 51.4% |
| Download-to-paid (result) | 1.5% | 3.5% | 6.75% | RC: H&F D35 median 2.9%, top quartile 6.2% |
| Annual share of payers | 60% | 70% | 75% | RC: H&F 68% annual |
| Monthly plan: first renewal / later renewals | 50% / 70% | 57% / 75% | 62% / 80% | RC: first renewal 53-61%, later renewals 65-82% |
| Refunds | 5% | 4% | 3% | RC: Productivity 4.7%, North America 3.4% |

**Outputs** (my model; MRR normalizes annual plans to /12; net is after Apple's commission):

| Month | Pessimistic: installs / gross MRR | Base: installs / gross MRR | Optimistic: installs / gross MRR |
|---|---|---|---|
| 1 | 2,000 / $130 | 5,000 / $695 | 10,000 / $2,576 |
| 3 | 1,545 / $245 | 4,480 / $1,551 | 9,600 / $6,185 |
| 6 | 1,688 / $405 | 6,294 / $3,139 | 16,589 / $14,506 |
| 9 | 1,845 / $563 | 8,843 / $5,269 | 28,665 / $28,546 |
| 12 | 2,016 / $729 | 12,423 / $8,220 | 49,534 / $52,636 |

| Year-one totals | Pessimistic | Base | Optimistic |
|---|---|---|---|
| Installs | 21K | 88K | 267K |
| Active annual subscribers at month 12 | 181 | 2,061 | 13,121 |
| Active monthly subscribers at month 12 | 29 | 316 | 2,057 |
| Net MRR at month 12 | $619 | $6,987 | $44,740 |
| Cumulative net cash | $7.0K | $73.4K | $452K |

The year-two risk is the first annual renewal. At RevenueCat's 23% Productivity median, roughly three quarters of month-1 annual payers leave at month 13. At the 36% low-price median, about two thirds leave.

The optimistic case roughly matches ClearSpace's estimated scale by mid-year. Reaching it requires top-quartile conversion and about 50K organic installs a month by month 12.

## Gaps

- I did not find student-specific CPI, conversion or price elasticity data.
- I did not find direct Reddit threads; Reddit blocks the fetch script.
- Jomo's Adapty page did not load.
- Brainrot's ScreensDesign install and revenue fields read 0.
- Opal's Adapty revenue figure is internally inconsistent ($400K vs $600K).
- The RevenueCat plan-mix text contradicts itself for Productivity.

## Sources

- https://adapty.io/paywall-library/opal-screen-time-for-focus/
- https://screensdesign.com/showcase/brainrot-screen-time-control
- https://screensdesign.com/showcase/one-sec-screen-time-focus
- https://screensdesign.com/showcase/clearspace-reduce-screen-time
- https://apps.apple.com/us/app/id1572515807
- https://apps.apple.com/us/app/id1532875441
- https://apps.apple.com/us/app/id6744338972
- https://apps.apple.com/us/app/id1497465230
- https://apps.apple.com/app/id1609960918
- https://habitdoom.com/blog/opal-vs-screenzen-jomo-one-sec
- https://detox.so/blog/is-opal-free
- https://www.revenuecat.com/state-of-subscription-apps-2026-productivity
- https://adapty.io/blog/health-fitness-app-subscription-benchmarks/
- https://adapty.io/state-of-in-app-subscriptions-2026
- https://www.rocketshiphq.com/meta-cost-benchmarks-mobile-app-installs/
- https://theviralapp.com/blog/tiktok-cpi-benchmarks-app-category-2026/
- https://semnexus.com/cpi-benchmarks-app-category-platform-2026
- https://admiral.media/how-much-does-app-marketing-cost/
- https://community.opal.so/t/7-days-into-a-full-year-seems-extreme/955
- https://justuseapp.com/en/app/1497465230/opal-save-time-daily/reviews
- https://justuseapp.com/en/app/6744338972/brainrot-screen-time-control/reviews
- https://unstar.app/blog/opal-forest-freedom-one-sec-jomo-screen-time-apps-ranked-2026
- https://www.unscroll.io/alternatives-to/one-sec-screen-time-app
- https://habitdoom.com/blog/screen-time-reward-apps-reddit
- https://cybernews.com/reviews/brick-phone-blocker-review/
- https://promolatte.com/lifestyle/tech/product-reviews-tech/brick-reviews/
- https://www.stork.ai/blog/the-400k-app-that-started-with-phone-addiction
