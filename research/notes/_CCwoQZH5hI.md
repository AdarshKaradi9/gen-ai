# Behind the product: Duolingo streaks | Jackson Shuttleworth (Group PM, Retention Team)
- URL: https://www.youtube.com/watch?v=_CCwoQZH5hI | Channel: Lenny's Podcast | Views: 32794 | Length: 5312s (1:28)
- Sources used: https://github.com/ChatPRD/lennys-podcast-transcripts/blob/main/episodes/jackson-shuttleworth/transcript.md (full speaker-attributed transcript, fetched raw); https://www.lennysnewsletter.com/p/behind-the-product-duolingo-streaks (official episode page, takeaways + chapters); https://www.audioscrape.com/podcast/lennys-podcast-product-career-growth/episode/behind-the-product-duolingo-streaks-jackson-shuttleworth-group-pm-retention-team-64060 (transcript preview); https://www.horsy.ai/listenlite/blog/lennys_podcast_behind_the_product_duolingo_streaks__jackson_shuttleworth_group_pm_retention_team (summary); https://blog.duolingo.com/streak-milestone-design-animation/ (Duolingo blog on milestone animation referenced in the episode)
- Confidence: high (full transcript read)

## Core claims (3-7 bullets, what the video argues)
- The streak is Duolingo's most impactful feature after the lessons themselves: "our biggest growth lever for driving DAUs," and the hook that makes notifications work. Over 9 million users have a 1-year-plus streak.
- Streaks are "an engagement hack" built on loss aversion that almost any app can use, but only on top of an app people already want to use. "Streaks work best when they're sitting on top of an app that users care about." Otherwise they distract from fixing the core loop.
- Retention is won or lost in days 0-7. Each day from 1 to 7 is a big jump in retention; "once you hit day seven, it flattens out" because loss aversion has kicked in. The team runs a disproportionate share of experiments on the 0-7 day window.
- Clarity beats cleverness: every element of the streak screen should explain what the feature is and how it works. Simple copy explaining the streak in eight words was a top-3 CURR win.
- Flexibility (streak freezes, Earn Back) is the single biggest mechanic-level DAU driver, but it must be counterweighted by celebrating perfection (Perfect Streak) and by someone guarding "the sanctity of the streak."
- The operating model matters as much as the feature: metric-based teams (CURR / DAU), 600+ experiments in 4 years, ship the simplest V1 and iterate, every change reviewed by the CEO, test rather than debate.
- Users care about the streak because Duolingo visibly cares about it (big animated post-lesson screen, notifications, milestones). Visibility is a design principle, not an accident.

## Specific tactics (concrete, actionable; include numbers, prices, timings, exact UI choices)
- Unit of use: define the streak around the app's natural unit of use. Moving from an XP-goal streak to "do one lesson a day" was a huge DAU win with no loss of meaning. Going further to "one exercise extends the streak" moved DAUs "not one bit" and captured the least-engaged users; shut down.
- Streak goal flow: when a streak starts, show an outcome-framed hook: roughly "you're 7x more likely to finish the course with a 30-day streak" (borrowed from a monetization string: "5.6x more likely to finish the course if you subscribe"). Huge win.
- Tested goal lengths 14/30/50 days: all good, appealing to different users. Then: default to 30 days with an opt-out ("no, I don't think I can hit it") that offers an easier goal. The opt-out button alone was almost as big a win as the easier goal. Then a goal picker where the user chooses the length. Pre-selecting a harder goal to speed users through the screen lost significantly: the act of choosing is where the engagement comes from.
- Copy: CTA changed from "Continue" to "Commit to my goal" on the goal screen: "a massive win." Run copy tests constantly; they are cheap (translate a few strings).
- Streak-start flavor copy explaining the mechanic in ~8 words ("Start a day to extend your streak, but miss a day and it resets" approx.) was worth on the order of 10,000+ DAUs and was a top-3 CURR win at the time.
- Design: lead with the number, not the flame. The flame metaphor did not resonate in India UXR. Redesign used an odometer animation ticking the number up with "7 day streak / 8 day streak." The calendar at the bottom of the streak screen gets more calendar-like each year (days on top, circles, checks) because it makes users realize it is a daily mechanic.
- Streak freezes: going from 1 allowed freeze to 2 was a huge DAU win; 3 was no better than 2 (people trained to take 3 days off tend not to come back). Give new users 2 free streak freezes when they start a streak (previously had to be bought with gems); "holy smokes to that win." Give more flexibility early, less once streaks are long.
- Earn Back: instead of paying gems to repair a lost streak (old "Streak Repair"), let users do a few lessons within a window after losing it to get the streak back. "Such a retention winner" because it feels earned and does not cheapen the streak.
- Perfect Streak: if you go 7 days without using a freeze, the streak turns gold and the calendar bar looks nicer. No reward beyond that; "ultra not complex, and it is really powerful." Perfect Streak is not introduced until after day 7; introducing extra concepts earlier "pretty universally" loses.
- Notifications: two per day tied to the streak. (1) Practice reminder sent 23.5 hours after yesterday's practice (practiced at noon -> reminder 11:30am next day); this beats every more complex timing model and beats letting users pick a reminder time. (2) "Streak saver" at 10pm if the streak is not yet extended ("last chance"); perceived as positive, not spammy, because users value the streak.
- Celebrate with animation, haptics (tested extensively, generally win), milestone "Phoenix Duo"; deliberately make users pause on the post-lesson streak screen rather than speeding them through the funnel.
- Experiment policy: ~50% of experiments win; neutral experiments that add UI are usually shut down to avoid cognitive load unless they are a platform for later wins (and then build that into V1). Shipped-but-reverted example: showing XP ticking up inside the lesson won on engagement but was reverted to keep the lesson a "learning sanctuary."
- Periodically run "reset" experiments: strip the optimized feature back to something simpler that performs as well, to escape local maxima and avoid a "kitchen sink" feature.
- Measure both absolute incremental DAUs and D1 vs D7 vs D14 retention; prefer experiments whose D14 impact exceeds D1 (compounding).
- Team ops: metric-owned teams (retention owns CURR; streak is "soft-owned"); heavy Jira automation and multi-quarter roadmaps so engineering/design never idle between iterations; quarterly review of where the feature is heading; product review by CEO Luis von Ahn, head of product design and a PM leader on every experiment.
- Cadence advice: build the streak around the app's natural frequency (Peloton uses weekly streaks).

## Named examples (apps/companies cited and what they did)
- Duolingo: streak, streak freeze, Streak Repair -> Earn Back, Perfect Streak, streak goals, leaderboards (30-person weekly XP leagues), gems economy, Phoenix Duo milestone animation; acquired animation studio Hobbes (Detroit) which now owns motion and haptics.
- Peloton: weekly streaks fit a COVID-era usage pattern.
- Royal Match, Pokemon TCG app, mobile games generally: source of mechanics ideas; mobile games frame streaks differently because "played a game 3,000 days in a row" lands differently than "learned Spanish 3,000 days."
- FarmVille (Lenny): cautionary example of harvest-every-hour mechanics.
- Jorge Mazal's Lenny newsletter post on Duolingo's growth model (CURR as the most leveraged metric).
- Bing Gordon (board member): "the reason why users care about your streak so much is because you care about your streak so much."

## Numbers & evidence (any stats, revenue, conversion rates, retention figures; mark self-reported vs third-party)
- Duolingo ~$14B market cap at recording (Dec 2024), doubled in six months; ~600M users (Lenny/official page, third-party market data).
- 9M+ users with 1-year-plus streaks (self-reported by Shuttleworth).
- 600+ experiments on the streak in 4 years, roughly one every other day; ~50% win rate (self-reported).
- Eight-word explanatory copy ~10,000+ incremental DAUs, top-3 CURR win (self-reported, ~4 years prior).
- "7x more likely to finish the course with a 30-day streak" and "5.6x more likely if you subscribe" are in-app claims Duolingo tested as copy (self-reported).
- Retention curve: big jumps each day from day 1 to 7, flattens after 7 (self-reported data).
- Streak freezes: 2 > 1 (huge), 3 = 2; 2 free freezes at streak start was one of the biggest wins (self-reported). Extra freezes hurt CURR but raised weekly-active return rate enough to net positive.
- Practice reminder at 23.5h after last practice beats all more complex models (self-reported).
- Shuttleworth's own streak: ~400 days (self-reported).

## Contradictions or caveats (where this disagrees with common advice or other videos)
- Easier is not always better: making the streak trivially easy (one exercise) did nothing; too much flexibility (3 freezes) trains users to skip days. There is a line where the streak gets "cheapened" and it may be a one-way door.
- Removing friction can lose: pre-selecting the goal lost; the opt-out button won. Intentional choice beats a frictionless funnel on this screen.
- Stated preference loses to revealed behavior: user-set reminder times lost to "23.5 hours after you last practiced."
- Monetization vs retention tension: streak freezes bought with gems generate revenue; the team is running an experiment that takes "a small hit to revenue" for a retention win and wishes several monetization hooks were gone. Decide on day one whether the streak is a monetization or retention feature.
- Against pure metric-chasing: a winning experiment (in-lesson XP counter) was reverted for product coherence; the CEO asks "what else are you going to do with this?"
- A 10pm push notification is normally considered spammy; here it is welcomed because of the feature it protects.

## Memorable framings (quotable one-liners or named frameworks, verbatim if available)
- "Streaks are a great engagement hack... but at the core, you have to have an app that people want to use."
- "Once you get to seven days, loss aversion kicks in, and you retain."
- "We'd much rather test it than debate it for days and days."
- "Commit to my goal" (replacing "Continue").
- Streak Serenity Prayer (cross-stitched by co-lead Antonia): "Luis, grant me the serenity to accept the flexibility I need, the courage to reach perfection when I can, and the wisdom to celebrate regardless." Flexibility vs perfection vs celebration is the streak strategy; "bend not break."
- "Form should follow a function here... lead with the number, not necessarily the flame."
- "The sanctity of the streak" and "an extinction level event" (if 9M long-streak users stopped caring).
- "Jackson, you child, we're not even 30% of the way optimized."
- "The reason why users care about your streak so much is because you care about your streak so much." (Bing Gordon)
- "Unit of use" as the thing a streak should count.
- Metric: CURR (current user retention rate) as Duolingo's most leveraged DAU driver.
