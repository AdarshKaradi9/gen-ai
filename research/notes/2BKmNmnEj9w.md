# Finding hidden growth opportunities in your product | Albert Cheng (Duolingo, Grammarly, Chess.com)
- URL: https://www.youtube.com/watch?v=2BKmNmnEj9w | Channel: Lenny's Podcast | Views: 27592 | Length: 5125s (~85 min)
- Sources used: https://xiaodouzi-ai-podcast-os.pages.dev/transcripts/2025-10-05__Lennys_Podcast__albert-cheng/index.html (full English transcript with Chinese translation); https://www.lennysnewsletter.com/p/how-to-find-hidden-growth-opportunities-albert-cheng (official episode page: takeaways, timestamps, references); https://rosetta.to/u/lennyspodcast/finding-hidden-growth-opportunities-in-your-product-albert-cheng-duolingo-gramma (summary snippet)
- Confidence: high (full transcript read)

## Core claims (3-7 bullets, what the video argues)
- Growth's job is "to connect users to the value of your product", not metrics hacking with walls and friction.
- Explore/exploit (credited to Brian Balfour via Reforge): explore = find the right mountain; exploit = climb it. Apply it at the insight level: when one experiment reveals a human-psychology insight, swarm adjacent surfaces with it ("expand it out 10X") until results go non-significant, then go divergent again.
- Retention is "gold" for consumer subscription; without it you are forced to monetize on day one with paid UA. For mature daily-use products, existing-user retention is the bigger lever than new-user retention; Grammarly is the exception (activation/install "aha" matters most because you don't open it daily).
- Freemium should make the core value permanently free, then "sample" premium features inside the free experience; showing paid suggestions to free users nearly doubled Grammarly upgrades.
- Experiment volume and the experimentation system (growth model, instrumentation, tooling) matter more than any single test; Chess.com went from ~0 (pre-2023) to 50 to ~250/yr with a stated 1,000/yr target.
- Brand/marketing and growth experimentation are complements, not rivals: Duolingo's owl/TikTok brought 20-30% of new users on some days (per in-product "how did you hear about us").
- Hire for high agency and "clock speed" over domain experience; experience can be a crutch when AI is shifting the ground.

## Specific tactics (concrete, actionable; include numbers, prices, timings, exact UI choices)
- Chess.com Game Review: data showed 80% of reviews happened after wins. On a loss, the product now surfaces brilliant/best moves and the coach says encouraging copy ("Losing, just part of learning, keep it up") instead of blunders: +25% game reviews, +20% subscriptions, large retention lift. Then audit every "cold pattern" (puzzles success rating, copy, button colors) for positivity.
- Grammarly "reverse free trial in real time": intersperse a capped sample of paid suggestions (tone, clarity, rewrites) among free spelling/grammar underlines; cap refreshes roughly daily. Prerequisite step: instrument suggestion types and paywall views first.
- Retention heuristic: D1 retention around 30-40% is "quite solid" for a consumer app; much lower questions user intent/ability to grow DAU.
- Mature-product mix: ~80% of Chess.com DAU/WAU are existing users; new and resurrected users are similar in size, so design an explicit resurrected-user experience (Duolingo: social push "your friend just started", re-placement test for lapsed learners).
- Duolingo virality: temporarily add screenshot tracking to find hotspots (streak milestones, funny challenges, top-3 leaderboard), then staff those moments with illustrators/animators; "you can 5X or 10X" sharing by improving moments users already screenshot.
- Gamification three pillars (from Jorge Mazal): core loop (lesson -> reward -> streak -> next-day push), metagame (path, leaderboards, achievements), profile (visible investment).
- Chess.com beginners: 75%+ self-identify as new/beginner; <1/3 win their first game; losing cuts retention ~10% vs winning. Experiments: route self-declared beginners to a learn-to-play flow instead of live games; hide ratings for the first five games; offer coach/bot/friend games.
- Experiment ops: expect 30-50% win rate; use experiment-explorer tools to pattern-match hypotheses; AI text-to-SQL Slack bot for ad-hoc data questions; AI prototypes (v0, Lovable, Figma Make) of onboarding/home/board as shared starting points; no-code configurability for home and pricing screens; experiment with push/email copy and App Store screenshots too.
- Don't build in-house experimentation from day one (used Statsig at Grammarly); start with a third-party A/B tool and "crawl, walk, run".
- Verify instrumentation: one company had retention configured backwards for three months, so positives read as negatives.

## Named examples (apps/companies cited and what they did)
- Chess.com: Game Review positivity flip; 250 -> 1,000 experiments/yr goal; beginner onboarding tests; co-founders Erik Allebest and Danny Rensch preach PLG.
- Grammarly: >90% free users; paid-suggestion sampling nearly doubled upgrades (PM Kyla); growth team handed current-user retention back to core product because suggestion quality/frequency drives it; B2C2B/product-led sales.
- Duolingo: product changes "multiple times per day" per user; Green Machine handbook; streaks; virality team; Duo owl personality across push and TikTok; 20-30% of new users on some days from brand channels.
- Reforge/Brian Balfour: explore vs exploit. Jorge Mazal: growth model and gamification pillars. Atlassian report: ~40% of product teams run no experiments. Chariot (failed "Chariot Direct" dynamic routing: solution seeking a problem, ignored drivers/ops, PR before validation).

## Numbers & evidence (any stats, revenue, conversion rates, retention figures; mark self-reported vs third-party)
- Self-reported by Cheng: +25% reviews / +20% subs from Game Review change; upgrades "nearly doubled" at Grammarly; D1 30-40% benchmark; 80% existing users at Chess.com; 75% beginners, <33% first-game wins, 10% retention gap; 50 -> 250 -> 1,000 experiments; 30-50% win rate; 20-30% of Duolingo new users from brand on some days.
- Third-party: Lenny cites Duolingo at ~$12B market cap; Atlassian State of Product 2026 (40% no experimentation); 800M chess players worldwide (Cheng).

## Contradictions or caveats (where this disagrees with common advice or other videos)
- Counter to "show mistakes to help users learn": users review wins, not losses; positivity drove engagement.
- Counter to "giving away premium kills conversion": sampling paid features doubled upgrades.
- Counter to the indie-app focus on day-0 conversion (Cal AI, Superwall videos): Cheng prefers organic/word-of-mouth growth plus retention, and says consumer reverse trials "are a little bit harder" than in B2B, favoring normal free trials for consumer.
- Counter to "always focus on existing-user retention": not for install-and-forget products like Grammarly.
- Counter to hiring on experience: prefers agency and speed.

## Memorable framings (quotable one-liners or named frameworks, verbatim if available)
- "Growth as the job is to connect users to the value of your product."
- "User retention is gold for consumer subscription companies."
- Explore and exploit: "finding the right mountain to climb" vs "climbing that mountain effectively."
- "It's basically a reverse free trial but in real time while you're writing."
- "Sometimes experience could be a crutch."
- "The system matters just as much as any given experiment, probably even more."
- Core loop / metagame / profile (gamification pillars).
