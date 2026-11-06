# Growth deep dive: how screen-time apps acquire users

## Key takeaways for the build

- **Each winner started with one owned distribution asset, then bought scale.** Brainrot had a 200K founder audience: the announcement video got about 1M views and about $10K in a weekend (self-reported). one sec had one viral screen-recording tweet from a 700-follower account. Opal hired a creator who was already a user and grew to 700K followers (self-reported). After that, all three scaled with paid ads and influencers. A solo founder without an audience must build that asset first, ideally a founder-faced or in-house creator account.
- **Run ads on the platforms the app blocks.** one sec's revenue was "doubling every single month" once it ran Instagram ads (self-reported). Opal used paid from the start and judged it by D8 ROAS (self-reported). The proven ad is a UGC before-and-after: "I used to spend 7 hours on my phone", then the screen-time screenshot, then the app (Opal ad, Motion library).
- **The head search terms are taken.** For "screen time", "app blocker" and "phone addiction", the first App Store results are apps with 50K to 91K ratings: Opal, ScreenZen, BePresent, Unrot and Brick (iTunes Search API, verified 6 Nov 2026). Compete on long-tail terms instead: "dopamine detox" is weak (its top result has 25 ratings), and "lock in" and "study blocker" fit the student audience.
- **"Years of your life" is not a differentiator.** Brainrot's onboarding already shows "the years you are on track to lose" and then "get 15 years back" (screensdesign teardown). The differentiators to lead with in content are the friend-accountability alert and the character that heals.
- **The closest analog to copy is Focus Friend, a cute focus character from a creator.** Hank Green's app hit #1 in US Top Free on 19 August 2025, ahead of ChatGPT (Tubefilter, verified chart event). Google Play later named it app of the year (TechCrunch). It is also a direct competitor for students under "study timer".
- **Campus channel: institutions, not just ambassadors.** Fizz grew with paid student ambassadors campus by campus and reached about three-quarters of Stanford undergraduates within 6 months (self-reported). In October 2026, a Calvin University library installed a Brick for finals, and the counseling center gave students a free promo code for LeadMeNot. Libraries and wellness centers will promote a phone-limiting tool for free.
- **Budget about $12K over 8 weeks and expect thousands of installs, not millions.** Creator benchmarks run $125 to $175 a week per creator for 15 posts, or $1 to $2 CPM. US Apple Ads cost a median $1.79 per tap and $2.76 per acquisition (SplitMetrics, Q2 2026). A realistic 8-week target is 10K to 25K installs, provided at least one format hits.

## How the benchmarks actually grew

**Brainrot (launched May 2025).** Yoni Smolyar posted daily build-in-public vlogs for over 400 days and grew to about 200K to 250K followers across Instagram and TikTok (self-reported). Before launch he ran a teaser and waitlist ("I'm building an app, sign up for the waitlist"). His announcement video "got a million views, which turned into maybe $10,000 of revenue in a weekend" (self-reported, Starter Story). Brainrot was #1 Product of the Day and Launch of the Week on Product Hunt on 26 May 2025 (verified on Product Hunt). The Product Hunt newsletter led with "Cure your brainrot", and he claims over 10K downloads that day (self-reported). After launch, "the thing that enabled early growth was influencer content and paid ads. And so we just simply scaled what we knew" (founder, Starter Story). He reports about a couple million downloads and $400K a month (self-reported). Spending about $4K a month on Appstack attribution (Mobile Takeaway recap) signals a serious paid operation. Starter Story's AI-compiled claim of "50-100 automated posts per day" conflicts with the founder's account and is unverified. The App Store rejected the app six times before launch (self-reported).

**one sec (2020).** Frederik Riedel's screen recording of the intercept screen went viral on Twitter from an account with about 700 followers. It brought thousands of downloads in the first days and "fueled growth for months" (self-reported, RevenueCat). He scaled with Instagram ads, reasoning that people scrolling Instagram are exactly the people who want to scroll less. A Max Planck Institute study that found a 57% reduction in use (peer-reviewed, per the founder) became his social proof, and therapists started recommending the app. He reports over 1M downloads and about 23K five-star ratings without investors (W&V, self-reported).

**Opal.** Schlenker found a TikTok creator mentioning Opal and hired her. "Olivia Unplugged" posts calm, research-based content with little branding. Opal reports "zero to 700,000 followers across platforms and millions of views in a few months" (self-reported, Sub Club podcast via Betterlaunch). Opal also licensed an independently made video about smartphones that "reached tens of millions" and ran it as a paid ad (self-reported). Apple featured Opal as App of the Day (verified App Store story, date not found). Its reported scale is $10M ARR with 11 people, 1M+ DAU and 10M+ downloads (self-reported). One Opal ad in the Motion library shows the paid format clearly: "your phone is your toxic situationship", "breaking up with my phone", 7+ hours a day down to about 3, "healed, hydrated, unbothered", a quick block demo, and "Download for free". The ad is 15 seconds long.

**Brick.** Brick spread through UGC around the act of "bricking" ("addicted to bricking", "un-Bricked my phone", per Dazed and Movieguide). The physical object makes it a visible status item. I found no figures for its ad spend or creator deals. Its campus use is real: Calvin's library mounted a Brick for study nights and finals (Calvin Chimes, Nov 2026).

**ScreenZen.** Free and tip-supported, with 53K ratings at 4.86 (verified). I found no founder interview or growth story.

**Newer entrants.** Unrot (June 2025) already has 57K ratings and an estimated 2.2M installs (AppGoblin, third-party estimate). "Lock In - Reset Your Life" (June 2025) has 27.7K ratings (verified). A 2025 entrant can still accumulate ratings fast.

## Content formats that work in this niche

I could not verify view counts for specific TikTok trend videos. TikTok tag pages do not expose them, and Reddit and YouTube were out of scope. The formats with evidence behind them:

1. **Screen-time before-and-after.** The screenshot is the proof. Examples are Opal's UGC ad and the repeated LOCKR template, "the app that lowered my screen time by 75%". This is the safest format for paid ads.
2. **Character reaction.** Brainrot's "FaceTime from your brain" interrupt (Mobile Takeaway recap) and Focus Friend's knitting bean are both easy to film. A wilting-then-healing companion fits this format, and the friend alert ("Sam unlocked TikTok at 1:14am") can be a skit.
3. **The founder's own story.** Brainrot's daily vlogs and one sec's raw screen recording both came from a real person with a real problem.
4. **Educational with a soft brand.** Olivia Unplugged-style "your attention is being stolen" clips. This format builds a following slowly but compounds.
5. **"Lock in" study content.** TikTok's "lock in studying" discover page shows the trend (stare at a wall for 10 minutes, then focus for 2 hours). This is the natural student format, with a study-hours counter on screen.

## ASO

From the iTunes Search API (US, 6 Nov 2026; this approximates but does not equal live store ranking):

- **"screen time"**: Opal (91K ratings), ScreenZen (53K), BePresent (72K), Unrot (57K), ClearSpace, one sec. Not winnable at launch.
- **"app blocker" / "screen time blocker"**: Opal, ScreenZen, Refocus, AppBlock, Brick (60K), BePresent. Also not winnable. A small new app ("67: Strict Screen Time Blocker", 81 ratings) still appears third for "screen time blocker", so exact-phrase titles can get some placement.
- **"focus" / "study timer"**: Forest, Flora, Focus Friend and Study Bunny dominate.
- **"lock in"**: Lock In (27.7K), then small apps, then Opal. Medium difficulty and on-trend for students.
- **"dopamine detox"**: The top result has 25 ratings and one sec appears fourth. This is the weakest field found.
- **"brainrot"**: Brainrot owns it, surrounded by Italian-brainrot games. Avoid.

AppGoblin gives "screen time" about 1,448 competing apps and a difficulty of 42.8 on its own scale (third-party model). The recommended name pattern, per the playbook, puts the primary keyword first and never repeats words between name and subtitle. For example, "[Name]: Lock In & Study Blocker" with the subtitle "Dopamine detox, friend check-ins", and "screen time" and "app blocker" in the 100-character keyword field. Expect ASO to contribute little in the first 8 weeks, since HabitKit took about 6 months to reach a top 10 (self-reported).

## Campus distribution

- **Fizz:** Fizz ran controlled launches one campus at a time with paid student ambassadors (donuts, hats, flyers). It hired about 20 ambassadors at Ithaca, and moderators were paid $500 a month at Washington and Lee (student press). Its Stanford penetration claims (5,100 users and 80% weekly active in Jan 2022, later "95%") are self-reported.
- **Gas:** Gas launched state by state in order of school start dates, so each wave arrived when students were together (press reports).
- **Calvin University (Oct 2026):** The library and Student Senate promoted a mounted Brick for midterms and finals. The counseling center, campus ministries and residence life promoted LeadMeNot with a free promo code. This is the cheapest channel found: wellness offices actively look for tools like this.
- I found no published finals-week campaign with download numbers for any student app. Treat the finals plan below as untested.

## 8-week launch plan (solo founder, starting the week of 9 Nov 2026)

Assumptions: the Family Controls distribution entitlement is requested now, since approval is a known delay; the app is in TestFlight by week 2; and the app is live by week 3. Fall finals at most US schools fall in weeks 5 and 6 (7 to 20 Dec). The planning targets below are my estimates built on the self-reported benchmarks above, not forecasts.

| Week | Focus | Actions | Spend |
|---|---|---|---|
| 1 | Warm-up and waitlist | Create 2 TikTok accounts plus Instagram. Warm them for 2 to 3 days by searching "screen time" and "lock in". Then post 3 a day per account, 2+ hours apart, using founder-story and screen-time-reveal formats. Build a waitlist page. Email wellness centers and libraries at 3 pilot campuses. | $0 |
| 2 | Build in public | Keep 6 posts a day. Show the character wilting on real usage. Recruit 5 student ambassadors per pilot campus (15 total) at $100 a month plus $1 per verified install. | $500 |
| 3 | Launch | Announcement video to the waitlist. Launch on Product Hunt the same day. Ask for a review after the first healthy day, never in onboarding. Test one ideal-fit student creator for $100 to $150. | $1,500 |
| 4 | Find winners | Hand the 2 best formats to 8 to 10 student micro-creators at $150 a week each for 15 posts, plus bonuses ($100 at 100K views, $500 at 500K). Start Apple Ads on brand, "lock in", "study blocker" and "dopamine detox" terms at $30 a day. | $2,000 |
| 5 | Finals push 1 | Run "Lock-In Week": a shareable study-hours card and group challenges of 3 friends. Ambassadors table at libraries during study nights. Offer counseling centers a free-access promo code. | $2,500 |
| 6 | Finals push 2 | Post the "I locked in for 42 hours" cards. If about 20 organic posts have cleared benchmark, put Meta and TikTok Spark ads behind the top 3 at $75 a day, optimized for trial start. | $3,000 |
| 7 | Holiday lull | Turn off campus spend. Run "screen time over the break" and New Year content (Business Insider framed bricking as "the new Dry January"). Cut creators below 0.3% view-to-install. | $1,500 |
| 8 | Read and decide | Calculate realized LTV per install in RevenueCat. Keep paid only where CPI is below it. Line up the January spring-semester relaunch at 5 more campuses. | $1,000 |

**Total:** about $12K, with creators about $5K, paid about $4.5K, and ambassadors and campus about $2.5K.

**Benchmarks to watch:**
- **Watch-past-3-seconds:** 75 to 80% or higher.
- **View-to-install:** 0.5 to 1% for demo formats and 0.05 to 0.2% for memes (Flamme, self-reported).
- **Views:** low thousands per post in weeks 1 and 2, with a first 10K+ post around week 3 (Playkit, self-reported).
- **Apple Ads:** CPA under about $3, against the $2.76 US median.
- **Paid CPI:** below realized LTV per install, with no exceptions.

**Planning target:** 300+ posts and 3M to 5M cumulative views, which at 0.3 to 0.5% conversion gives 10K to 25K installs. Kill criterion: if no post clears 50K views by week 5, change the hook format, not the posting volume.

## Sources

- https://www.wearefounders.uk/he-built-an-app-to-fix-his-phone-addiction-it-made-26k-in-30-days/
- https://www.starterstory.com/stories/how-i-built-it-400k-month-ios-app
- https://www.starterstory.com/businesses/brainrot-screen-time-control/growth-channels
- https://www.stork.ai/blog/the-400k-app-that-started-with-phone-addiction
- https://themobiletakeaway.com/i/2026-11-02-the-mobile-takeaway
- https://www.producthunt.com/products/brainrot-2/launches
- https://screensdesign.com/showcase/brainrot-screen-time-control
- https://www.revenuecat.com/blog/growth/frederik-riedel-expected-12-his-app-cut-screen-time-by-57/
- https://www.wuv.de/themen/ki-tech/apple-deutscher-entwickler-ist-neuer-shooting-star
- https://www.betterlaunch.co/playbooks/kenneth-schlenker-opal-billion-user-9
- https://www.buzzsprout.com/2432582/episodes/18334466-how-opal-reached-10m-arr-with-11-employees
- https://motionapp.com/library/opal-1-screen-time-app
- https://apps.apple.com/us/story/id1638394648
- https://www.indianweekender.co.nz/news/meet-the-influencers-urging-you-to-stop-scrolling
- https://www.dazeddigital.com/life-culture/article/69100/1/could-bricking-my-phone-help-me-feel-more-present
- https://www.tiktok.com/@icy4k/video/7645474981370924302
- https://www.tiktok.com/discover/lock-in-studying-trend
- https://www.tubefilter.com/2025/08/20/hank-green-tops-app-store-charts-focus-friend/amp/
- https://techcrunch.com/2025/11/18/hank-greens-focus-friend-is-google-plays-app-of-the-year
- https://appgoblin.info/apps/6746537171
- https://appgoblin.info/apps/6751114843/keywords
- https://itunes.apple.com/search?term=screen%20time&country=us&entity=software
- https://stanforddaily.com/2022/01/23/from-buzz-to-fizz-anonymous-social-platform-takes-off-at-stanford/
- https://theithacan.org/?p=49642
- https://ringtumphi.net/7268/arts-life/new-app-fizz-launches-on-campus/
- https://thehustle.co/10-18-22-gas-app
- https://calvinchimes.org/2026/11/02/three-apps-students-are-using-to-help-limit-screen-time/
- https://splitmetrics.com/blog/apple-search-ads-cost
- https://www.mobileaction.co/report/apple-ads-2026-benchmark-report/metrics-analysis-of-search-results-ads/
- https://www.apptweak.com/en/aso-blog/apple-ads-benchmarks
