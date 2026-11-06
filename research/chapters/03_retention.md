## What Brings People Back: progression, reward systems, hooks and retention

Getting someone to install a habit app is the easy half. The notes in this corpus agree on one uncomfortable baseline: most apps lose most users fast. AppsFlyer puts average day-30 retention at 3-4%, with over 40% uninstalling within 30 days and half of those on day one [vid:BJEHnGYj_8E]. A Google Play video cites a loss of 77% of new users within three days, a figure that traces to an older (around 2015) Android analysis [vid:Xvjxr0lkcjE].

This chapter collects the patterns the sources use to bend that curve. The strongest evidence comes from Duolingo's retention team, which reports 600+ experiments on the streak alone [vid:_CCwoQZH5hI]. Much of the rest is framework and opinion, flagged as such.

### Pattern 1: Load The Next Trigger

**What it is.** Nir Eyal's Hook Model: Trigger, Action, Variable Reward, Investment, repeated until the user stops needing your external prompts and starts returning on an internal one, such as boredom, loneliness or uncertainty [vid:yM4FBYH2mTM][vid:-jXM4NymIcA]. The external trigger (push, email, app icon) gets paired with a specific feeling ("I'm bored" leads to Facebook) [vid:TDRQfGT6GtE].

**Why it works.** Behaviour needs motivation, ability and a trigger at the same moment (Fogg's B = MAT) [vid:-jXM4NymIcA]. When a trigger fails, Eyal's advice is to make the action easier rather than to push motivation [vid:11dYx_rW_Ks]. The last step, investment, is the one founders skip. A small piece of work after the reward (stating preferences, building something, following someone) stores value and "loads the next trigger", so the product gets better with use [vid:yM4FBYH2mTM][vid:TDRQfGT6GtE].

**Examples.** Eyal's standard walkthrough: Barbra sees a relative's photo on Facebook, clicks through to Pinterest, scrolls a mix of relevant and surprising images for 45 minutes, then pins and follows, which feeds her future feed [vid:yM4FBYH2mTM]. Eyal says "I don't do original research", and no product metrics appear in any of the four Hook-Model notes [vid:TDRQfGT6GtE][vid:yM4FBYH2mTM].

**How to apply.** Answer Eyal's five questions for your app: which internal trigger, which external trigger, what is the simplest action, does the reward satisfy yet leave the user wanting more, and what investment loads the next pass [vid:11dYx_rW_Ks]. 

**Caveat.** The model is a lens, not a proven result, and it is contested: critics in the Tristan Harris and Yu-kai Chou camps see the same mechanics as manipulation, with Chou quoted as saying the Hook model "creates addicts" [vid:11dYx_rW_Ks].

### Pattern 2: Win Days Zero To Seven

**What it is.** Concentrate retention work on the first week.

**Why it works.** Duolingo's retention lead reports that each day from day 1 to day 7 brings a big jump in retention, and "once you hit day seven, it flattens out" because loss aversion has kicked in. The team runs a disproportionate share of experiments in that window (self-reported) [vid:_CCwoQZH5hI]. WSJ reports that over 70% of Duolingo's DAU hold a streak of 7 days or more (company figures) [vid:9KqrnBiyBQ8].

**Examples.** Perfect Streak, a gold streak for seven days without a freeze, is held back until after day 7. Introducing extra concepts earlier "pretty universally" loses [vid:_CCwoQZH5hI]. Albert Cheng gives a benchmark of 30-40% D1 retention as "quite solid" for a consumer app (self-reported heuristic) [vid:2BKmNmnEj9w].

**How to apply.** Keep the first week simple and single-minded. Measure D1, D7 and D14 together, and prefer changes whose D14 effect is larger than their D1 effect, because those compound [vid:_CCwoQZH5hI].

### Pattern 3: The Bend-Not-Break Streak

**What it is.** A daily counter built on loss aversion, softened by forgiveness and sharpened by celebration. Duolingo calls the streak its "biggest growth lever for driving DAUs", with over 9 million users on a streak of a year or longer (self-reported) [vid:_CCwoQZH5hI].

**Why it works.** Losses feel roughly twice as strong as equal gains [vid:2TlIg3VokY8][vid:yBpv5rZoBjA]. A streak turns each day into something you can lose. But a streak that breaks too easily ends the habit, so forgiveness matters as much as the counter.

**Examples, all self-reported by Duolingo unless noted** [vid:_CCwoQZH5hI]:
- Count the natural unit of use. Moving from an XP goal to "one lesson a day" was a large DAU win. Going down to "one exercise" moved DAUs "not one bit" and was shut down.
- Freezes: going from 1 allowed freeze to 2 was a big win. 3 was no better than 2, because people trained to take three days off tend not to come back. Giving new users 2 free freezes at streak start was one of the biggest wins.
- Earn Back: instead of paying gems to repair a lost streak, users do a few lessons within a window to win it back. It was "such a retention winner" because it feels earned.
- Celebration: an odometer animation that ticks the number up, haptics, milestone animations, and a post-lesson streak screen users are deliberately made to pause on.
- Goals: "Commit to my goal" instead of "Continue" was "a massive win". Offering an opt-out to an easier goal almost matched the easier goal itself. Pre-selecting a goal to speed people through lost.

Flamme, a couples app, reports going from 0.8% to about 50% day-30 retention after adding a daily question with a carrot notification and a streak "stick" (self-reported, and the guest's own telling elsewhere starts at 1.2%) [vid:pb4JIH8FubE]. Cal AI sends streak notifications such as "You've logged 70 days straight!" and reports 80%+ retention among users who logged 10,000+ calories (self-reported, from a separate interview) [vid:OsN_MJopMxc].

**How to apply.** Define the streak around your app's real unit and frequency. Peloton uses weekly streaks [vid:_CCwoQZH5hI]. Give 2 freezes early, less flexibility later. Let users earn back a broken streak with real activity rather than money.

**Caveats.** Streaks "work best when they're sitting on top of an app that users care about"; otherwise they distract from fixing the core loop [vid:_CCwoQZH5hI]. Decide on day one whether the streak serves retention or monetization, because gem-bought freezes made Duolingo money it now partly wants to give up [vid:_CCwoQZH5hI]. Tim Gabe calls a single counter "decoration" next to streaks that compound into something, such as the diamond tiers his agency built for Freecash at days 7 and 42 (self-reported agency work) [vid:yBpv5rZoBjA].

### Pattern 4: The Scoreboard Is Not The Game

**What it is.** Points, badges and leaderboards (PBL) are what most apps add first, and they are the weakest layer. Yu-kai Chou: "Good gamification does not start with game elements but really starts with how it motivates our core drives" [vid:v5Qjuegtiyc]. Tim Gabe calls PBL "the three most documented failures in product history" [vid:LXX_qOA5D8E].

**Examples.** LinkedIn retired its Top Voice gold badges in 2024 because they rewarded quantity over quality. Foursquare scrapped mayorships and badges in 2014 because they drove check-ins, not the discovery the business needed [vid:LXX_qOA5D8E]. A peer-reviewed study of Habitica is cited as finding counterproductive effects in 100% of participants, as managing the game buried real work [vid:LXX_qOA5D8E]. In contrast, Apple Watch rings are cited at a 49.5% behaviour change across 160,000 people through completion drive alone [vid:LXX_qOA5D8E]. These figures are third-party studies as quoted by a YouTuber; I could not check the originals.

**Leaderboards done right.** The problem is size, not ranking. "Winnability is the strongest predictor of competitive motivation" (a 2022 study as cited) [vid:LXX_qOA5D8E]. Strava's segments create "thousands of hyper-local micro-competitions" sorted by age and gender, and members who use its social and output features work out 15% more often [vid:LXX_qOA5D8E].

**How to apply.** Count your mechanics. Feature richness follows an S-curve, and if you already have points, badges, challenges and leaderboards, "you're past the peak" [vid:LXX_qOA5D8E]. Track one system users can obsess over: "one visible measure of total progress creates more engagement than 20 scattered badges" [vid:yBpv5rZoBjA]. Signal mastery, not attendance [vid:LXX_qOA5D8E].

**Caveat.** Gamification evidence is mixed. A 2024 meta-analysis as cited found it helps autonomy and relatedness but barely moves perceived competence [vid:LXX_qOA5D8E].

### Pattern 5: Progress That Never Starts At Zero

**What it is.** Levels, XP and progress bars that make momentum visible and keep the next step close.

**Why it works.** The goal-gradient effect: a car-wash loyalty card with two stamps pre-filled was completed at nearly double the rate (academic study cited secondhand) [vid:2TlIg3VokY8]. The Zeigarnik effect: unfinished tasks stay in mind, so partly complete profiles and progress percentages pull users forward [vid:fYs2Mdyasuc].

**Examples.** LinkedIn's profile meter never starts at zero [vid:2TlIg3VokY8]. Peloton's totals never cap ("a user at 500 classes isn't stopping when 600, 700, 1,000 are all theoretically reachable") [vid:yBpv5rZoBjA].

**How to apply.** Pre-fill the first step. Keep thresholds close and make the next level feel reachable [vid:D9SXaj6qQIQ]. Audit for "done" states: "if a user can complete your app, you have a ceiling on retention" [vid:yBpv5rZoBjA].

**Caveat.** Duolingo shipped an in-lesson XP counter that won on engagement, then reverted it to keep the lesson a "learning sanctuary" [vid:_CCwoQZH5hI]. Progress UI can crowd out the actual thing. None of the notes give a tested XP or level curve formula; the corpus is thin here.

### Pattern 6: Surprise As Seasoning

**What it is.** Variable reward: the user knows a reward is coming but not its size or timing.

**Why it works.** Eyal: predictable feedback is "the fridge light"; variability creates a hunting state [vid:-jXM4NymIcA]. He names three kinds: rewards of the tribe (social), the hunt (material or information) and the self (mastery) [vid:yM4FBYH2mTM]. Dopamine rises in anticipation, and further when the reward is unpredictable (Sapolsky, as cited) [vid:4maJty0vQjI].

**Examples.** Finch lets you send your bird to a destination; each location has 15-20 possible discoveries, and some days bring nothing [vid:yBpv5rZoBjA].

**The casino comparison.** The critics describe the same mechanic as a slot machine. Vox: "if it wasn't random... you would not get addicted", and pull-to-refresh is a slot lever [vid:NUMa0QkPzns]. Slot machines are said to addict people 3-4x faster than other gambling [vid:NUMa0QkPzns]. Free-to-play games pair variable reward with virtual currencies and loss-timed purchase prompts, and about half of mobile game revenue comes from under 0.5% of players (Swrve estimate) [vid:fKK9nVLvhGM].

**How to apply.** Keep most of the system predictable and transparent, then add controlled surprise: an unexpected bonus, a milestone that arrives early [vid:yBpv5rZoBjA]. AppsFlyer says to use unexpected rewards "sparingly" [vid:BJEHnGYj_8E]. Tie surprise to the user's real progress, never to payment.

**Counter-evidence.** Variable reward is not required for retention. At Chess.com, switching the post-loss Game Review to show your best moves with encouraging copy gave +25% reviews and +20% subscriptions, a predictable positive reward (self-reported) [vid:2BKmNmnEj9w][vid:TDRQfGT6GtE].

### Pattern 7: White Hat First

**What it is.** Yu-kai Chou's Octalysis framework: eight core drives (Epic Meaning, Accomplishment, Creativity, Ownership, Social Influence, Scarcity, Unpredictability, Loss and Avoidance). Top drives are "white hat": they feel good and are sustainable. Bottom drives are "black hat": powerful, but they "leave a bad taste" and do not last [vid:v5Qjuegtiyc].

**Examples.** White hat: Pain Squad turns a child's pain journal into a detective mission; Opower shows your bill next to "efficient neighbors" and is cited at over $250M saved in a year [vid:v5Qjuegtiyc]. Black hat: countdown timers, lotteries, "a zombie right behind you" [vid:v5Qjuegtiyc].

**How to apply.** Map each mechanic to a drive. Make sure the core reason to return is white hat (meaning, progress, ownership, connection). Use scarcity and loss as short-term nudges, not the engine. Note that the Hook Model's core engine, unpredictability, sits on the black-hat side [vid:yM4FBYH2mTM].

### Pattern 8: A Character Worth Missing

**What it is.** A mascot or relationship that carries emotion, so missing a day feels like letting someone down rather than losing a number.

**Examples.** Finch: 14M+ downloads and 675,000 ratings at 4.9 stars, with a bird whose personality evolves partly outside your control (App Store figures as quoted) [vid:yBpv5rZoBjA]. Duolingo's character animation system shipped in 2022; one video says DAU rose from 14.2M to over 34M in two years afterwards, but that is a correlation the video presents as cause [vid:Du2lkZ_cux8]. Duo's owl personality also runs across push and TikTok, bringing 20-30% of new users on some days (self-reported) [vid:2BKmNmnEj9w]. Flamme's stick was emotional: "Your streak is about to expire - your partner will miss out." "The carrot wasn't just a badge. It was your partner's happiness" [vid:pb4JIH8FubE].

**How to apply.** Give the mascot reactions to success and failure, not just a logo pose [vid:Du2lkZ_cux8]. Find the screenshot moments: Duolingo tracked screenshots and found streak milestones and top-3 leaderboard finishes, then staffed those moments with animators [vid:2BKmNmnEj9w].

**Caveat.** Tim Gabe's agency pitches this, and he also designs progress that can be lost "in a very visually demoralizing way" [vid:AnL49w4yIOw]. Guilt is a tool with a cost; see Pattern 11.

### Pattern 9: 23.5 Hours Later

**What it is.** Time reminders to the user's own rhythm, not to a time they picked.

**Examples.** Duolingo sends two streak notifications a day. A practice reminder 23.5 hours after yesterday's session beat every more complex timing model and beat user-chosen reminder times. A "streak saver" at 10pm goes out only if the streak is not yet extended (self-reported) [vid:_CCwoQZH5hI]. Sensor Tower data shows over 25% of Duolingo usage falls between 9 and 11pm, consistent with streak saving (third-party) [vid:9KqrnBiyBQ8]. A bandit algorithm picks which message each lapsing user gets, and the "passive-aggressive" "It looks like reminders aren't working. We'll stop sending them" lifted retention about 3% (company-reported) [vid:9KqrnBiyBQ8].

**How to apply.** Ask for push permission with a pre-permission screen that says what you will send (Brilliant: "I'll remind you to learn so it becomes a long-term habit") [vid:Qsq-Sj_rojU]. Let users manage notification types: Aftenposten cut uninstalls 9.2% over 60 days this way (Google written guidance, not the video itself) [vid:Xvjxr0lkcjE]. Back off when reminders are ignored. Consider a home-screen widget as a persistent, quiet trigger; Flamme used one, and a Freecash widget redesign is said to have lifted D7 retention by several points (agency claim) [vid:pb4JIH8FubE][vid:sYRhXB_ZcLI].

**Caveat.** A 10pm push is normally spam. It works only because users value what it protects [vid:_CCwoQZH5hI].

### Pattern 10: Read The Shape, Not The Height

**What it is.** Cohort retention is "the best quantitative way to determine if you've made something people want" [vid:VNxBZ7ka5J0].

**How it works.** Group users by first-use week or month. Define "active" as an action that proves value, not an app open. Pick a time window that matches natural frequency: weekly for a daily habit app, much longer for travel [vid:VNxBZ7ka5J0]. Then look for flattening. A lower curve that flattens beats a higher one that keeps sliding. Google Photos' early cohorts dropped sharply but plateaued at 20-40%, which gave the team confidence (self-reported) [vid:VNxBZ7ka5J0].

**Pitfalls.** Wide windows inflate numbers. Notification taps are fake activity (Google+). Paying-but-inactive subscribers are not retained users [vid:VNxBZ7ka5J0]. Build your first curves by hand from logs and check the analytics tool against them [vid:VNxBZ7ka5J0].

**How to apply.** If curves do not flatten, segment by channel, country or user type, find the cohort that retains and acquire more of it [vid:VNxBZ7ka5J0]. Test features by retention: ship to a cohort and check a week later whether those users stayed longer [vid:qDuzzrQKP_M].

### Pattern 11: The Wellbeing Line

**What it is.** The same mechanics that retain users can harm them. A habit app should sit on the right side of that line.

**Evidence.** A 2023 Belgian study of about 2,500 adolescents linked Snapchat streak frequency to FOMO, problematic phone use and lower self-control, and Nevada's Attorney General cited streaks in 2024 litigation (as cited) [vid:LXX_qOA5D8E]. Critics of Duolingo say streak obsession can displace learning [vid:9KqrnBiyBQ8]. Tristan Harris argues apps remove stopping cues and use red badges and random rewards to keep people hooked [vid:NUMa0QkPzns], and TikTok's "recapture" notifications follow the same logic [vid:4maJty0vQjI]. Strava deleted 3.9 million activities after users logged e-bike rides as regular rides to climb leaderboards [vid:yBpv5rZoBjA].

**How to apply.** Use Tim Gabe's test: build mechanics that signal "you got better at the actual thing", not "you opened the app a lot" [vid:LXX_qOA5D8E]. Strava is the model: one hour of real activity for every two minutes in the app [vid:LXX_qOA5D8E]. Keep natural endpoints. Protect the core experience from metrics, as Duolingo did with the "learning sanctuary" [vid:_CCwoQZH5hI]. Eyal's own rule: the tools are a "super power" and should be used for products that improve lives [vid:-jXM4NymIcA].

### Where sources disagree

- **Streaks: engine or liability.** Duolingo calls the streak its top DAU lever [vid:_CCwoQZH5hI]. Tim Gabe says streaks run on fear and draw regulatory scrutiny, and prefers variable reward [vid:LXX_qOA5D8E]. In another video he calls the Duolingo streak mere "decoration" and pushes harder loss mechanics [vid:yBpv5rZoBjA].
- **Variable reward: essential or optional.** Eyal makes it the core of a hook [vid:TDRQfGT6GtE]. Chou classes unpredictability as black hat [vid:v5Qjuegtiyc]. Chess.com's results came from predictable positive feedback [vid:2BKmNmnEj9w].
- **Friction.** Flamme's retention jump came from adding a daily obligation, not removing steps [vid:pb4JIH8FubE], and Duolingo's goal screen lost when friction was removed [vid:_CCwoQZH5hI]. Most onboarding advice says to cut friction.
- **Is retention repeatable?** Nikita Bier says virality is learnable but durable consumer-social retention is a "black swan" that happens maybe once a decade [vid:bhnfZhJWCWY]. The gamification videos promise retention by design.
- **What drove Duolingo.** One video credits character animation [vid:Du2lkZ_cux8]. Duolingo's own team credits hundreds of streak, notification and league experiments [vid:_CCwoQZH5hI].

### Checklist

1. Define the streak around your app's natural unit of use and frequency, daily or weekly [vid:_CCwoQZH5hI].
2. Give new users 2 streak freezes, not 3, and add an earn-back path that requires real activity [vid:_CCwoQZH5hI].
3. Explain the streak in one short sentence and use "Commit to my goal" style copy on the goal screen [vid:_CCwoQZH5hI].
4. Hold new mechanics until after day 7, and focus experiments on days 0-7 [vid:_CCwoQZH5hI].
5. Send the daily reminder about 23.5 hours after the last session, plus one late-evening saver only when the streak is at risk [vid:_CCwoQZH5hI].
6. Stop or slow reminders for users who ignore them [vid:9KqrnBiyBQ8].
7. Replace global leaderboards with small, winnable groups [vid:LXX_qOA5D8E].
8. Track one central progress measure instead of many badges [vid:yBpv5rZoBjA].
9. Make the emotional stake a character or person, not just a number [vid:pb4JIH8FubE][vid:yBpv5rZoBjA].
10. Build weekly cohort curves by hand, with "active" defined as a value action, and watch for flattening [vid:VNxBZ7ka5J0].
11. Map every mechanic to an Octalysis drive and keep the core loop white hat [vid:v5Qjuegtiyc].
12. Check each mechanic against "did the user get better at the real thing?" [vid:LXX_qOA5D8E].
