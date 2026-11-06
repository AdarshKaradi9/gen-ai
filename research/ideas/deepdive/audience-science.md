# Audience and science: who to build for, and what actually works

## Key takeaways for the build

- **Beachhead: US college students aged 18 to 24, sold around their exam calendar.** Pew's 2026 survey says 70% of US adults aged 18 to 29 think they spend too much time on their phone, and 42% say they are on it "almost constantly". About 58% of adults aged 18 to 49 tried to cut back in the past year (Pew, peer-reviewed-grade survey). They choose for themselves, live in friend groups, and have fixed panic dates (finals). Willingness to pay is lower, so keep the annual price under $40.
- **The student lane is already contested.** Opal says 70% of its 10 million users are students (self-reported, and the figure includes high schoolers). A new entrant has to win on the friend-group mechanic and finals content, not on being a "student blocker".
- **Friction works, but modestly, and it fades into autopilot.** The one sec PNAS 2023 field experiment (280 people, 6 weeks) found a 57% reduction in target-app opens versus control, and about 36% of opening attempts were abandoned at the pause (peer-reviewed). The pause should rotate prompts and escalate rather than repeat one static screen.
- **Self-set limits are the best-evidenced lever.** Allcott, Gentzkow and Song (AER 2022) found that letting people set their own future limits cut use of the targeted apps by 22 minutes a day (17%), and their model attributes about 31% of social media use to self-control problems (peer-reviewed; the 31% is from the working paper). Onboarding should have users set their own limits.
- **Social accountability has no direct trial evidence for phone use.** I found no published randomized trial of an accountability partner for screen time. The nearest evidence is a driving study in which commitment plus social competition cut handheld phone use by about 20%. Treat friend notifications as a hypothesis to A/B test, not a proven claim.
- **Honest health claims are available but narrow.** A 2025 PNAS Nexus RCT (Castelo et al., 467 recruited) found that blocking mobile internet for two weeks improved mental health, well-being and sustained attention, but only about a quarter of participants complied fully. Hunt et al. 2018 found that capping social media at about 30 minutes a day for three weeks reduced loneliness and depression in 143 undergraduates. Say "studies link cutting back to better mood and focus", never "cures anxiety" or "raises your GPA".
- **The "years of your life" number is defensible if it is computed conservatively and labeled.** For a 20-year-old using 5.5 hours a day, remaining life expectancy of about 58 years gives about 13 calendar years, or about 20 waking years. Show the formula, count only user-picked apps, and say "at this pace".
- **Guilt-only mechanics are a risk and the evidence on them is thin.** Streak research is mostly qualitative. A small CHI 2016 study found that streaks motivate but create a fragile dependency, and users who break them tend to quit. The character should heal as well as wilt, with streak repair.

## Audience comparison

**US college students (18 to 24).** Size: the National Student Clearinghouse counted about 19.4 million postsecondary students in fall 2025 (verified, NSC via Higher Ed Dive). I could not verify a clean national undergraduate headcount, and the 18 to 24 share is smaller than the total. Screen time: no nationally representative US college figure exists. A device-logged Colombian study found university students averaged 5.37 hours a day (peer-reviewed, small sample). A 2025 UK survey of 2,842 students by Fluid Focus, a blocker company, found 6 hours 12 minutes for university students, and 94% of them said they want to cut back (self-reported, vendor-run, so treat it as an upper bound). Desire to cut back: Pew 2026 found 70% of 18 to 29 year olds say "too much", 62% say their phone hurts their sleep, and 49% say it hurts their productivity (verified). Willingness to pay is the weak spot. Opal offers student discounts, and its own forum has "broke university student" price complaints (anecdotal). They gather on TikTok and Instagram ("lock in", "study with me" content), in dorms, Greek life, clubs, campus subreddits and Discord study servers. Seasonality is sharp. Fall finals run early to mid December, spring finals late April to mid May, quarter-system finals in mid March and early June, and the MCAT, LSAT and bar exam add their own dates. New Year falls between semesters.

**High schoolers via parents.** Size: about 17 million US teens aged 13 to 17 (Census, not re-verified in this pass). Screen time: Gallup's 2023 survey found 4.8 hours a day on social media alone, 5.8 hours for 17-year-olds (verified, Gallup). Desire: only 38% of teens say they spend too much time on their phone, and 63% have not cut back (Pew 2024, verified). Parents care more than the teens do. 76% call managing teen phone time a priority, and about 40% say it is hard to do (Pew 2024). The problem is that this is a different product. The parent pays, the teen resents it, minors' privacy rules apply, and Apple's own Family Controls plus school phone bans already compete. It is not a fit for a playful companion the user chooses for themselves.

**Young professionals (roughly 25 to 34).** Pew 2026 found 64% of 30 to 49 year olds say "too much", and a third are on their phone almost constantly (verified). Willingness to pay is higher, since they already pay for Calm, Headspace and productivity tools, and Freedom and Opal's adult pricing ($40 to $100 a year) is aimed at them. The downsides are weak seasonality (New Year only), scattered gathering places and costlier acquisition. This is the natural second market.

**Parents as users themselves.** 46% of teens say a parent is at least sometimes distracted by their phone (Pew 2024, verified). "Model it for your kids" is a good later marketing angle, but parents are time-poor and already targeted by parental-control apps.

**ADHD adults.** CDC (MMWR, October 2024) estimates 6.0% of US adults, about 15.5 million, have a current ADHD diagnosis, and more than half were diagnosed as adults (verified). Studies link ADHD traits, especially inattention, to problematic phone use (Panagiotidi and Overton 2020, 273 adults, peer-reviewed, correlational). The community is reachable and vocal on TikTok, but it also complains about subscription fatigue and paying for apps it forgot about (anecdotal). A product aimed at ADHD invites medical-claim scrutiny. It would be better as an explicit design principle (no shame, low setup) than as the target label.

**Recommendation.** Start with US college students, and launch the first campaign on the fall finals and New Year window. The desire to cut back is strongest here and comes from the students themselves. Friend groups are dense, exam dates create urgency, and short video is their native channel. Price for students: about $29.99 to $34.99 a year with a visible trial-end reminder, and test a group plan in which three friends each get a discount. Plan the move to young professionals once retention is proven.

**Other seasonal moments.** Searches for "digital detox" and account deletion cluster around January (NordVPN data on Australia shows a January rise of up to 24% in account-deletion searches; this is a third-party estimate and not US data). Business Insider called "bricking your phone" "the new Dry January" in 2026. Lent 2027 starts on Ash Wednesday, February 10, and giving up social media for Lent is a common practice, though I found no data on its size. Back-to-school in late August is the other setup moment. I could not find app-download seasonality data for blockers; Appfigures or Sensor Tower would be needed.

## What reduces phone use

**Friction and pauses.** Grüning, Riedel and Lorenz-Spreen (PNAS, February 2023) ran a 6-week field experiment with 280 one sec users. The intervention cut actual target-app opens by 57% versus control, about 36% of attempts were abandoned at the pause, and attempts themselves fell about 37% from week 1 to week 6 (peer-reviewed, per the abstract). Participants had already downloaded one sec, so they were motivated, and competitor marketing often misquotes the figure. Review complaints say people learn to tap through the pause (Unstar, indicative only). So the build should vary the prompt (intention, time left, the character's state) and lengthen the pause after repeated bypasses.

**Self-set limits and commitment devices.** In Allcott, Gentzkow and Song (AER 2022), people who were offered a tool to set future limits on six apps cut use by about 22 minutes a day (17%). Temporary payments to reduce use had persistent effects, which suggests the habit can be broken (peer-reviewed). The same paper models self-control problems as causing about 31% of social media use, which is a defensible, quotable "it's not just you" line.

**Social accountability and gamification.** As above, there is no direct RCT for partner notification. In a randomized driving-safety study, commitment plus weekly gamified social competition cut handheld phone use about 20.5% versus control, and adding money raised the effect to 27.6% (search snippet, not read in full). The honest stance is that social pressure works in neighboring areas (exercise, saving, driving) and is untested here. Measure it with an A/B test from day one: friends on versus off, compared on 30-day retention and minutes reduced.

**Loss framing and guilt, and what backfires.** I found no study testing a "years of life" loss frame on phone use. Evidence that streaks backfire is qualitative. In Renfree et al. (CHI 2016), streaks motivated users but created a dependency, and a broken streak often led people to quit the app and the habit with it. Popular "63% more likely to quit after one missed day" claims have no primary source I could find. Total abstinence also does worse than moderation. A 2024 Pediatrics review found reduction-focused approaches looked better for well-being than full detox, and a 2024 meta-analysis (Narra J, 10 studies, 2,503 people) found a benefit for depressive symptoms but unclear effects elsewhere. The design rule that follows: use moderation targets, not "zero TikTok", with a recoverable character and earn-back days.

## Effects of cutting back (for honest marketing)

- **Mental health and attention.** In Castelo et al. (PNAS Nexus, February 2025), a randomized block of mobile internet (calls and texts still allowed) for two weeks improved mental health, subjective well-being and sustained attention. Gains persisted after access returned, and phone screen time fell from about 314 to 161 minutes a day. Compliance was low, though. Of 467 recruits, about 266 installed the block and about 119 kept it on for at least 10 days. The "reversed 10 years of attention decline" claim comes from press coverage of the paper; do not use it without reading the paper.
- **Loneliness and depression.** Hunt et al. (Journal of Social and Clinical Psychology, 2018) randomized 143 undergraduates to 10 minutes per platform a day across Facebook, Instagram and Snapchat for three weeks. Loneliness and depression fell, most among people who started out more depressed. The sample was small and the study short.
- **Academics.** The links are correlational and small. Sunday et al. 2021 (44 studies, about 148,000 college students) found r = -0.12 between smartphone addiction and academic outcomes, and Paterna et al. 2024 found r = -0.11. One classroom experiment (Glass and Kang 2018, 118 students) found devices in lectures lowered final exam scores by about 5%, roughly half a grade. "Linked to worse grades" is fair; "raise your GPA" is not.
- **Sleep.** 62% of adults under 30 say their phone hurts their sleep (Pew 2026, self-reported perception).

## The "years of your life on your phone" calculation

Formula: years on phone = (daily hours on chosen apps / 24) x remaining life expectancy. A "waking years" version divides by 16 instead of 24.

Inputs: remaining life expectancy at age 20 in the SSA 2022 period life table is 55.63 years for men and 60.87 for women, about 58 on average (verified via search snippet; the SSA page blocked the fetch, so pull the full table into the app at build time). Example: 5.5 hours a day at age 20 gives 13.3 calendar years, or 19.9 waking years (about a third of waking life).

To keep it defensible:
1. Use the user's own Screen Time data or entry, not a population average.
2. Count only the apps the user marks as unwanted, since messaging and maps are not "lost" time.
3. Say "at this pace", because use usually falls with age (Pew's "too much" share drops from 70% at 18 to 29 to 25% at 65 and over), so a straight-line projection overstates.
4. Use calendar years as the headline and offer waking years as a toggle, with the formula one tap away.
5. Never say "lost years of life" or anything that implies harm to lifespan.
6. Calculate "time back" from a measured baseline week minus current use, not from claims.

## What I could not find

US device-logged college screen time; an RCT on accountability partners; willingness to pay by age; seasonal download data; Lent participation; Opal's paying-user mix.

## Sources

- https://www.pewresearch.org/short-reads/2026/09/01/about-half-of-americans-say-they-spend-too-much-time-on-their-smartphone/
- https://www.pewresearch.org/internet/2024/03/11/how-teens-and-parents-approach-screen-time/
- https://news.gallup.com/poll/512576/teens-spend-average-hours-social-media-per-day.aspx
- https://www.highereddive.com/news/fall-2025-enrollment-increased-1-but-the-devil-is-in-the-details/809675/
- https://revvisy.unimetro.edu.co/index.php/visy/article/download/492/347/362
- https://theboar.org/2025/07/most-students-want-to-reduce-screen-time-as-study-finds-they-risk-scrolling-for-25-years-of-their-life
- https://opalapp.com/blog/students-use-opal-app-store-reviews
- https://community.opal.so/t/great-idea-for-an-app-wish-it-wasnt-so-expensive/1018
- https://cdc.gov/mmwr/volumes/73/wr/pdfs/mm7340-H.pdf
- https://link.springer.com/article/10.1007/s12144-020-00785-2
- https://biomed.reviewer.ly/app/publication/acca04da-db72-4607-9e12-26ab2530c8f3
- https://one-sec.app/research/
- https://www.aeaweb.org/doi/10.1257/aer.20210867
- https://www.nber.org/system/files/working_papers/w28936/w28936.pdf
- https://www.socialscienceregistry.org/trials/13182
- https://researchportal.northumbria.ac.uk/en/publications/dont-kick-the-habit-the-role-of-dependency-in-habit-formation-app/
- https://pubmed.ncbi.nlm.nih.gov/39285845/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC11392003
- https://academic.oup.com/pnasnexus/article/4/2/pgaf017/8016017
- https://www.news-medical.net/news/20250219/Blocking-mobile-internet-for-two-weeks-improves-mental-health-and-well-being.aspx
- https://usrtk.org/healthwire/blocking-mobile-phone-internet-may-boost-mood-mental-health-attention/
- https://techcrunch.com/2018/11/09/limiting-social-media-use-reduced-loneliness-and-depression-in-new-experiment
- https://zaguan.unizar.es/record/136426
- https://www.sciencedaily.com/releases/2018/07/180728083617.htm
- https://www.ssa.gov/oact/STATS/table4c6_2022_TR2025.html
- https://www.mediaweek.com.au/35-of-aussies-want-to-remove-themselves-from-the-internet-says-new-research
- https://scour.ing/@hugonoss/p/https://www.businessinsider.com/bricking-your-phone-analog-movement-the-new-dry-january-2026-1
