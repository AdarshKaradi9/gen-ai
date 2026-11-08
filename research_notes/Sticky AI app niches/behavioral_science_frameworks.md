# Behavioral-Science Evidence and Expert Frameworks for Consumer-App Retention (gap-fill to retention_mechanics.md)

All sources accessed 2026-11-08. Labels: **[HARD]** = peer-reviewed or company-reported data; **[EXPERT]** = practitioner/VC opinion or framework; **[3P]** = third-party/vendor dataset; **[ANEC]** = anecdote or press narrative. Studies and industry data from before 2023 are marked **(pre-2023)**, and pre-2023 industry data should be treated as **possibly stale**.

This file deliberately leaves out what `retention_mechanics.md` already covers: streaks, Duolingo numbers, Singh 2024 habit timing, Sailer & Homner, Hershfield, the fresh-start effect, and AI-companion regulation.

**Process note for the report writer:** The sandbox network blocked **nature.com, a16z.com, pmc.ncbi.nlm.nih.gov and revenuecat.com**. Figures attributed to those pages come from search-result extracts and secondary coverage, not from reading the full text. The search tool also summarizes results, so each figure below is only as good as that summary. Exact numbers worth quoting should be checked against the primary source. I have not added any numbers from memory.

## 1. Classic behavioral studies: effect sizes, replication status, what worked

### Takeaway
The robust, replicated lessons are:
- Nudges work far less often than experts predict, and their effects are mostly small and short-lived.
- The best gym-megastudy arm rewarded people for **returning after a lapse**.
- Bias-corrected estimates for implementation intentions are much smaller than the classic d≈0.65.
- Temptation bundling's large original effect shrank to about 10–14% in a 6,792-person follow-up.
- The "vaccine is reserved for you" framing beat other reminder texts.

Goal-gradient and endowed-progress effects are well known, but I found no standardized effect size or direct replication for either.

### Cited Findings

**Goal-gradient (Kivetz, Urminsky & Zheng 2006, JMR 43:39–58; pre-2023)**
- [HARD] Customers given a 12-stamp coffee card with 2 pre-filled "bonus" stamps completed the 10 required purchases **faster** than customers with a plain 10-stamp card. The authors ruled out habituation, expiration concerns, time trends and heterogeneity as explanations. In their model, effort is a function of the *proportion* of distance remaining to the goal. — [Columbia Business School abstract](https://business.columbia.edu/faculty/research/goal-gradient-hypothesis-resurrected-purchase-acceleration-illusionary-goal)
- No Cohen's d and no direct replication turned up in search. Wiki-style claims of a "non-linear" acceleration near the goal are unsourced. — [search summary of skill-wiki page](https://skill-wiki.github.io/atom/frontend-design/fact-goal-gradient-effect)

**Endowed progress (Nunes & Drèze 2006, JCR; pre-2023)**
- [HARD, via secondary summary] In a car-wash field experiment, 300 loyalty cards were handed out. Half needed 10 stamps; the other half needed 10 but came with 2 already stamped, so both groups needed 8 more washes. Redemption was **34% for endowed cards vs 19% for plain cards**. These figures come from a Wikipedia summary; check the JCR original before quoting. — [Wikipedia, Goal pursuit](https://en.wikipedia.org/wiki/Goal_pursuit)
- No replication or meta-analysis found in this pass (see Gaps).

**Gym megastudy (Milkman et al., Nature, Dec 2021; DOI 10.1038/s41586-021-04128-4; pre-2023)**
- [HARD, via press] Design: **54** four-week digital programs, built by 30 scientists from 15 universities, tested on **more than 60,000** 24 Hour Fitness members. Gym check-ins were the outcome, and members were followed for 10 weeks afterward. — [CNN via KTVZ](https://ktvz.com/health/cnn-health/2021/12/08/these-are-the-best-ways-to-up-your-workout-habits-according-to-study-of-over-60000-people/); [CBS](https://www.cbsnews.com/sacramento/news/workout-habits-exercise-gym)
- [HARD, via press] **About 45%** of interventions significantly raised weekly visits during the 4 weeks, by roughly **9%–27%** over control.
  - Best arm: a micro-incentive of about **$0.09** (in points) for **returning after a missed workout**, **+27%**.
  - Telling people that exercise is a growing trend (a dynamic social norm): **+24%**.
  - **More than 300 experts' predictions did not match** which interventions worked best.
  — [CNN via KTVZ](https://ktvz.com/health/cnn-health/2021/12/08/these-are-the-best-ways-to-up-your-workout-habits-according-to-study-of-over-60000-people/); [Polar blog](https://www.polar.com/blog/a-new-megastudy-reveals-why-we-return-to-the-gym/)
- Conflict: one secondary outlet said only "8%" of interventions were significant. This looks like a misreading of the 45% figure. — [Psychology Today](https://psychologytoday.com/ie/blog/trust-games/202112/most-experiments-don-t-work-and-s-ok)
- Persistence after the program ended could not be verified because nature.com was blocked (see Gaps).

**Flu-vaccine megastudy (Milkman et al., PNAS 119(6) e2115126119, Feb 2022; pre-2023)**
- [HARD] **689,693** Walmart pharmacy patients were randomized to one of **22** text reminders or a no-message control. The average reminder raised vaccination by **about 2.0 percentage points (6.8%)** over 3 months. The best message was a **two-text sequence, sent 3 days apart, saying a vaccine was "waiting for" / reserved for the patient**, an ownership or endowment framing. — [Wharton BCFG](https://bcfg.wharton.upenn.edu/research/a-680000-person-megastudy-of-nudges-to-encourage-vaccination-in-pharmacies/); [EconPapers](https://econpapers.repec.org/RePEc:nas:journl:v:119:y:2022:p:e2115126119)
- Note: the paper was published in 2022, not 2021 as the task brief states. The exact "reserved" wording and the arm's specific lift were not confirmed in the snippets.

**Temptation bundling (Milkman, Minson & Volpp 2014, Management Science; pre-2023) and its large follow-up**
- [HARD] Original study: gym-goers who could only listen to tempting audiobooks at the gym visited **51%** (full treatment) and **29%** (intermediate) more often than controls at first. The effects **declined over time**, especially after Thanksgiving. — [PubMed 25843979](https://pubmed.ncbi.nlm.nih.gov/25843979/); [Wharton PDF](https://faculty.wharton.upenn.edu/wp-content/uploads/2017/07/TemptationBundling.pdf)
- [HARD] Kirgios et al. 2020, *OBHD* 161:20–35 (N = **6,792**): giving people audiobooks plus encouragement to bundle raised the chance of a weekly workout by **10–14%** and average weekly workouts by **10–12%**, during the program and **up to 17 weeks after**. **Encouragement alone did not robustly** increase visits. The authors suspect that receiving a free audiobook "leaks" the bundling idea on its own. — [EconPapers](https://econpapers.repec.org/RePEc:eee:jobhdp:v:161:y:2020:i:s:p:20-35)
- Replication status: the effect replicated in direction at much smaller magnitude, roughly a 4–5x shrinkage from the original 51% headline. The brief mentions a "2021 megastudy replication" of temptation bundling; I could not confirm whether temptation bundling was one of the 54 megastudy arms (see Gaps).

**Implementation intentions (Gollwitzer & Sheeran 2006, pre-2023; updated 2024)**
- [HARD] The 2006 meta-analysis of 94 independent tests found **d = 0.65** on goal attainment, a medium-to-large effect. — [Univ. Konstanz](https://www.socmot.uni-konstanz.de/publications/implementation-intentions-and-goal-achievement-meta-analysis-effects-and-processes)
- [HARD, via secondary] Sheeran, Listrom & Gollwitzer (2024) covered **642 tests**. After correcting for publication bias, the estimate falls: trim-and-fill gives **d = 0.35**, and robust Bayesian meta-analysis gives **d = 0.15 (95% CI 0.08–0.22)**. This is a material downgrade and should be verified against the paper. — [The Behavioral Scientist glossary](https://www.thebehavioralscientist.com/glossary/implementation-intentions)
- [HARD] Wang, Wang & Gai 2021 (*Frontiers in Psychology*) meta-analysed **MCII** (mental contrasting plus implementation intentions). Effects were moderated by intervention style, and the authors say the small number of studies limits conclusions. — [Frontiers](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2021.565202/pdf)

**Commitment contracts and loss aversion (Giné, Karlan & Zinman 2010, AEJ: Applied 2:213–235; pre-2023)**
- [HARD] In the CARES study, about 2,000 smokers in the Philippines were randomly offered a voluntary commitment savings account. Signers deposited their own money, forfeited it if they failed a urine test at 6 months, and were also given **surprise tests at 12 months**. Intent-to-treat effects were about **+3.4 to +5.7 percentage points** in cessation, against control rates of **8.9%–14.7%**, and the effect **persisted at 12 months**. — [IPA PDF](https://es.poverty-action.org/sites/default/files/publications/put_your_money_where_your_butt_is.pdf); [FTC conference PDF](https://www.ftc.gov/sites/default/files/documents/public_events/first-annual-microeconomics-conference/dkarlan.pdf)
- Conflict of interest, disclosed in the paper: Karlan is President of stickK.com and Zinman sits on its research advisory board. — [IPA PDF](https://es.poverty-action.org/sites/default/files/publications/put_your_money_where_your_butt_is.pdf)
- Uptake is the hidden limit: the effect is an intent-to-treat effect on everyone *offered* the contract, and only a minority signed up. I did not retrieve the exact take-up rate. No published stickK success rate for referees or contracts was found.

**Social norms / social proof (Opower; Allcott & Rogers, AER 2014; pre-2023)**
- [HARD] Opower mailed home energy reports with **neighbor comparisons** to more than 6 million households. Usage dropped right after each of the first few reports, and those effects **decayed within months**. With repeated reports, households formed more persistent habits. In a randomized arm where reports stopped after about 2 years, effects persisted, so earlier cost-effectiveness estimates had been "dramatically understated". — [Allcott & Rogers PDF (Harvard)](https://toddrogers.scholars.harvard.edu/resource/allcottrogersaer2014pdf); [J-PAL](https://povertyactionlab.org/media/file-research-paper/short-run-and-long-run-effects-behavioral-interventions-experimental)
- The commonly quoted "~2% reduction" figure was **not confirmed** in the retrieved snippets.
- The megastudy's "+24% from framing exercise as a growing trend" result (above) is the most app-relevant social-norm finding with a number attached.

**Variable reward / variable-ratio schedules in apps**
- [ANEC/EXPERT] Claims that phones and feeds work like slot machines rest mostly on operant-conditioning research in **animals**. No controlled app experiment or meta-analysis on variable-ratio schedules turned up. — [Psychology Today, "The Vegas effect of our screens"](https://www.psychologytoday.com/gb/blog/tech-happy-life/201901/the-vegas-effect-of-our-screens)
- [HARD-adjacent] A Karger paper on mobile gambling apps (DOI 10.1159/000495663) hypothesizes that higher engagement predicts persistence during extinction. The excerpt showed only the hypothesis, not the results. — [Durham repository](https://durham-repository.worktribe.com/OutputFile/1308510)
- [EXPERT critique] Critics of the Hooked model point out that big habit products such as **Google (low reward variability) and Uber (no variable reward)** contradict the model's variable-reward step. — [Big Think review](https://bigthink.com/?p=54491)
- [EXPERT critique] One commentary argues that AI chat runs on **continuous**, not intermittent, reinforcement, so slot-machine analogies may misdescribe AI-app stickiness. — [You On AI field guide](https://www.youonai.ai/fieldguide/high/gambling_analogy_failure.html)

### Inferences
- The best megastudy arm (a small reward for coming back after a miss) and the "reserved for you" text both support **lapse-recovery** and **ownership** framing as levers for AI apps. Examples: "your plan for today is ready", or a bonus for returning after a missed day. This lines up with the streak-repair evidence in retention_mechanics.md.
- Expert predictions were poorly calibrated in the megastudies. Mechanics should be A/B-tested, not chosen by intuition.
- Implementation-intention prompts ("when and where will you do X?") are cheap and directionally positive. Their realistic effect is small (d of about 0.15–0.35), not 0.65.
- Commitment contracts with money at stake can work, but only for the minority who opt in. They suit a power-user tier better than default onboarding.

### Gaps
- Milkman 2021 megastudy: persistence after the 4-week program, and whether a temptation-bundling arm was included, could not be confirmed (nature.com blocked).
- Endowed-progress and goal-gradient: no standardized effect sizes, replications or meta-analyses found. The Nunes & Drèze 34% vs 19% figures come from a Wikipedia summary.
- No stickK aggregate success data was found, and no CARES take-up rate was retrieved.
- No peer-reviewed RCT of variable-ratio rewards in consumer apps was found.

## 2. Expert frameworks and benchmarks (Eyal, Chen, Winters, Verna, Reforge, Lenny, a16z, Sequoia, 2025–26 AI-retention commentary)

### Takeaway
Hard 2025–26 data shows that AI subscription apps retain **worse** than non-AI apps. RevenueCat reports 21.1% vs 30.7% annual-plan retention, with AI apps churning about 30% faster, though AI apps earn about 41% more per payer. a16z reframes early AI churn as "tourist" churn and recommends judging cohorts by M12/M3, pointing to ChatGPT's "smile" curve. Sequoia's 2023 figures (14% median DAU/MAU, 42% month-1 retention) are stale baselines. Practitioner benchmarks from Lenny and Casey Winters conflict across secondary write-ups and could not be verified.

### Cited Findings

**Nir Eyal: Hooked (2014) and ethics**
- [EXPERT] The Hook model is a loop of trigger, action, variable reward and investment. Eyal himself concedes that the model can be a "recipe for manipulation". Reviewers say the book's ethics discussion is underdeveloped. — [Big Think](https://bigthink.com/?p=54491); [SuperSummary](https://www.supersummary.com/hooked/chapters-6-8-summary/); [Behavioral Scientist](https://www.thebehavioralscientist.com/?p=2407)
- Eyal's "Manipulation Matrix" and his *Indistractable* (2019) stance were **not retrieved** in search (see Gaps).

**Retention-curve doctrine (Andrew Chen et al.)**
- [EXPERT, secondary] The cohort retention curve should **flatten** above zero, and the plateau, not the starting number, is the product-market-fit signal. These are secondary summaries of the widely cited Chen-style doctrine; the original andrewchen.com posts were not retrieved. — [echai.ventures](https://echai.ventures/startingup/growth-metrics/what-is-a-good-retention-curve-and-how-do-i-know-if-mine-is-flattening); [Mastering Retention (Substack)](https://jacksoslow.substack.com/p/mastering-retention)
- [EXPERT caveat] A "smile" (an upturn) does not always mean users are becoming more engaged. It can come from a product launch or from reactivation campaigns. — [Userpilot](https://userpilot.com/blog/retention-curve/)

**Lenny Rachitsky & Casey Winters benchmarks (survey of about 20 growth practitioners; original not reachable)**
- [EXPERT, secondary, conflicting] One summary gives 6-month retention of **consumer subscription ~40% good / ~70% great**, **consumer social ~25% / ~45%**, and enterprise SaaS ~70% / ~90%. — [Marketplace Guide](https://themarketplaceguide.pages.dev/articles/retention-benchmarks-decoded-what-good-actually-looks-like-for-marketplace-founders-and-why-your-bar-is-different/)
- retention_mechanics.md cites a different figure from the same family of summaries: 30% / 50% for *consumer transactional*. The two are probably different rows of the same table. Verify against Lenny's Newsletter before quoting.
- Other secondary sources say consumer subscription 12-month retention is **10–25%**. — [Parsa VC](https://medium.com/parsa-vc/consumer-subscription-kpi-benchmarks-retention-engagement-and-conversion-rates-9ac13b57c3d3)

**a16z, 2025 (blocked; via search extracts)**
- [EXPERT] "Retention Is All You Need" by Santiago Rodriguez & Alex Immerman (Sep 10, 2025) argues that leading AI companies have a **measurement problem, not a retention problem**. Early "AI tourist" churn inflates M1 losses. The post proposes **M12/M3** (one-year retention among users who survived to month 3) as the leading indicator, and cites ChatGPT's cohort curve as a "smile" that would look stronger if app usage were included. — [a16z](https://a16z.com/ai-retention-benchmarks/) (blocked; via search summary); [OfficeChai coverage](https://officechai.com/ai/ai-products-retention-curves)
- [3P via EXPERT] a16z's December 2025 consumer-AI piece, as quoted secondhand, cites Yipit data: **month-12 desktop retention ~50% for ChatGPT vs ~25% for Gemini**, desktop only. It also says D30 is **above 30%** for top consumer apps. Secondary only. — [a16z, State of Consumer AI 2025](https://a16z.com/state-of-consumer-ai-2025-product-hits-misses-and-whats-next/) (blocked); [VC Cafe](https://www.vccafe.com/consumer-ai-is-back-retention-will-decide-who-wins/)
- [EXPERT] a16z's "Cinderella glass slipper effect" post argues that early cohorts who find an exact fit retain unusually well in the AI era. Content was not retrieved beyond the title. — [a16z](https://a16z.com/the-cinderella-glass-slipper-effect-retention-rules-in-the-ai-era/)

**Sequoia, "Generative AI's Act Two" (Sep 2023; STALE)**
- [3P, 2023] Generative-AI apps had a **median DAU/MAU of 14%**, against 51% for incumbent consumer apps; **AI companionship (Character.ai) was the exception**. Median **one-month retention was 42%**, against 63% for consumer entertainment, social, games and education apps. **ChatGPT led at 56%**. — [Voicebot.ai](https://voicebot.ai/2023/10/03/generative-ai-apps-struggle-with-retention-and-engagement-charts/); [getcoai summary](https://getcoai.com/research-reports/sequoia-capital-insight-generative-ais-billion-dollar-infancy/)
- These figures are more than three years old and predate GPT-4o, voice and agents. Use them only as a historical baseline.

**RevenueCat State of Subscription Apps, Mar 2026 (hard 2026 AI-app data; revenuecat.com blocked)**
- [3P/HARD] AI apps vs non-AI apps:

  | Metric | AI apps | Non-AI apps |
  |---|---|---|
  | Annual-plan 12-month retention | **21.1%** | **30.7%** |
  | Monthly-plan 12-month retention | **6.1%** | **9.5%** |

  AI apps churn **about 30% faster** at the median and earn **41% more first-year revenue per payer**. High-retention AI apps on monthly plans kept 10.9% at 12 months, and top AI apps on annual plans matched the non-AI 30.7%. Sample: more than 115,000 apps and more than $16B in revenue. The data covers RevenueCat customers only and counts subscriptions, not people. Weekly-plan figures conflict across secondary sources (1.2% vs 1.7%, or 2.5%). — [TechCrunch, Mar 10 2026](https://techcrunch.com/2026/03/10/ai-powered-apps-struggle-with-long-term-retention-new-report-shows); [PPC Land](https://ppc.land/ai-apps-earn-41-more-per-user-but-churn-30-faster-revenuecat-finds/); [Veed summary](https://www.veed.io/learn/revenuecat-2026-why-ai-apps-churn-fast); [RevenueCat (blocked)](https://www.revenuecat.com/blog/growth/ai-app-retention-study)
- [3P, vendor blog, weak] AI companion apps typically report DAU/MAU in the **10–25%** range (2026). This is not authoritative. — [getkapex.ai](https://getkapex.ai/blog/ai-companion-retention-benchmarks)

**Elena Verna, Reforge, Casey Winters (beyond the benchmark table)**
- Their original material (Verna on retention over acquisition and product-led growth; Reforge retention or engagement frameworks) was **not retrieved** in this pass.

### Inferences
- For an AI app, expect worse headline retention than non-AI peers and plan monetization around it: annual plans, and high revenue per payer to offset churn.
- Judge product-market fit on the curve **after** the tourist phase (an M12/M3-style measure, or the plateau after month 2–3) rather than on M1.
- Sequoia 2023 and RevenueCat 2026 agree on direction: AI apps underperform on retention, and companionship or daily-utility uses are the exceptions. That consistency over time strengthens the case for building habits into AI apps.
- The Hooked model is widely used but empirically thin and ethically contested. Treat it as vocabulary, not evidence.

### Gaps
- No primary text was read from andrewchen.com, Lenny's Newsletter, Reforge, Elena Verna, a16z or Sequoia (hosts blocked or not surfaced). Every expert benchmark above is secondhand.
- Eyal's Manipulation Matrix and *Indistractable* ethics position were not found in search.
- a16z's specific M12/M3 benchmark values were not retrieved.

## 3. Mechanics previously lacking evidence: daily puzzles, time-limited events, year-in-review, personalized AI feedback/tutoring, push notifications

### Takeaway
- **AI tutoring:** now has two credible 2025 RCTs with sizeable *learning* effects: Nigeria, about 0.3 SD in 6 weeks, and Harvard physics, about 2x the gains of active learning. Neither measures consumer-app retention.
- **Daily puzzles:** NYT Games shows scale (11.2B plays in 2025, 4.2B of them Wordle) and supports a growing bundle (about 13.8M subscribers in Q3 2026). There is no public causal retention metric.
- **Annual recaps:** Spotify Wrapped 2025 reached 200M engaged users and 500M shares in 24 hours.
- **Live events:** Pokémon GO events have only revenue-level data (more than $1B in 2025).
- **Push notifications:** evidence points to an inverted U, with small positive lifts and diminishing or negative returns at high frequency.

### Cited Findings

**Daily drops and daily puzzles (NYT Games)**
- [HARD, company via AP, Jan 2026] NYT puzzles were played **more than 11.2 billion times in 2025**, including **Wordle 4.2 billion times**. Crossplay, launched Jan 2026, is the 11th game and the first two-player one. About **half of subscribers take the ~$30/month all-access bundle**. — [Fox/AP syndication](https://www.fox32chicago.com/news/new-york-times-crossplay-multiplayer-game); [Newser](https://img1-cdn.newser.com/story/382375/forget-wordle-nyt-rolls-out-its-first-multiplayer-game.html)
- [HARD, company results via secondary, Nov 4 2026] Q3 2026 results:
  - **+420,000 net digital-only subscribers**, to about **13.76–13.8M**.
  - Revenue **$768.5M (+9.7%)**.
  - Digital-only subscription revenue **+14.6%**.
  - The company is on pace for **15M subscribers by end-2027**.
  — [Quartr summary](https://quartr.com/events/the-new-york-times-company-nyt-q3-2026_3PJgPSrf); [Editor & Publisher](https://www.editorandpublisher.com/stories/the-new-york-times-adds-420000-digital-subscribers,264340); [PPC Land](https://ppc.land/new-york-times-digital-ad-sales-gain-12-below-its-own-forecast/)
- [HARD, Q3 2025] Bundle and multiproduct subscribers were **6.27M (51%)** at Q3 2025. — [Nasdaq/Zacks](https://www.nasdaq.com/articles/how-new-york-times-digital-bundle-strategy-winning-subscribers)
- [3P, 2023, possibly stale] YipitData found subscribers spent **more time in Games than in news** in 2023. — [Fox/AP syndication](https://www.fox32chicago.com/news/new-york-times-crossplay-multiplayer-game)
- Warning: many 2026 "Wordle drives NYT subscribers" pages in search results are auto-generated spam on unrelated domains with conflicting numbers. They were excluded.

**Annual recaps (Spotify Wrapped 2025)**
- [HARD, company-reported via press, Dec 2025] **More than 200M engaged users in the first ~24 hours** (+19% YoY). An "engaged user" is someone who viewed at least one Wrapped story. In 2024, reaching 200M took about 62 hours. There were **more than 500M shares on day one** (+41% YoY), counting native shares, screenshots and downloads. New features: "listening age", Wrapped groups, and a live multiplayer "Wrapped Party". — [TechCrunch](https://techcrunch.com/2025/12/04/spotify-says-wrapped-2025-is-its-biggest-yet-with-200m-users-in-its-first-day); [Music Business Worldwide](https://www.musicbusinessworldwide.com/spotify-wrapped-campaign-hit-200m-engaged-users-in-24-hours-a-19-yoy-increase); [Music Week](https://www.musicweek.com/digital/read/spotify-wrapped-2025-was-biggest-ever-with-200-million-engaged-users/093178)
- These figures show reach and virality. There is no causal data on whether Wrapped reduces churn.
- Strava Year in Sport and Duolingo Year in Review: no figures found.

**Time-limited live events (Pokémon GO)**
- [HARD-ish, company PR] Under Scopely, which now publishes the game, Pokémon GO generated **more than $1B in revenue in 2025** with "millions" of daily players. GO Fest 2026 had "record attendance", with no numbers given. — [Scopely press release](https://www.scopely.com/en/news/pokemon-go-celebrates-its-10-year-anniversary-by-transforming-times-square-into-an-immersive-real-world-adventure)
- [ANEC] Community Days run monthly, 3-hour local-time windows (for example Dec 6–7, 2025, 2–5pm). Players have pushed back on higher paid-ticket prices. — [Pocket Gamer](https://www.pocketgamer.com/pokemon-go/december-2025-community-day); [Sportskeeda](https://www.sportskeeda.com/pokemon/better-double-prizes-players-react-increased-price-pokemon-go-sprigatito-community-day-ticket)
- No public data separates the Community Day effect on DAU or revenue. No data was found on Fortnite seasons or on countdown timers.

**Personalized AI feedback and tutoring RCTs**
- [HARD, World Bank working paper WPS 11125, May 2025] De Simone, Tiberti, Barron, Manolio, Mosuro & Dikoru, "From Chalkboards to Chatbots".
  - Design: an RCT in Edo State, Nigeria. First-year senior-secondary students used **Microsoft Copilot (GPT-4)** for English in after-school sessions, **twice a week, 90 minutes each, for 6 weeks**, working in pairs. One secondary source puts the sample at about 759 students in 9 schools.
  - Effects: **about 0.31 SD** on a combined test, and **0.23 SD in English** (abstract; some coverage says 0.24). The blog frames this as close to "two years of typical learning" in 6 weeks.
  - The 1.2–2.2 SD full-year figure is an **extrapolation**, not a measured result.
  — [World Bank blog](https://blogs.worldbank.org/en/education/From-chalkboards-to-chatbots-Transforming-learning-in-Nigeria); [EconPapers WPS 11125](https://econpapers.repec.org/RePEc:wbk:wbrwps:11125)
- [HARD, peer-reviewed] Kestin, Miller et al., "AI tutoring outperforms in-class active learning", *Scientific Reports* 15:17458 (Jun 3, 2025; DOI 10.1038/s41598-025-97652-6).
  - Design: a crossover RCT in Harvard's Physical Sciences 2 (fall 2023), **N = 194**, using a custom tutor called "PS2 Pal" built on research-based pedagogy.
  - Results (from secondary coverage): **about 2x learning gains** compared with active-learning class, and less time on task (about 49 vs 60 minutes, median). Students also reported higher engagement and motivation. The exact figures were not verified because PMC was blocked.
  - Caveats: two topics only, short-term tests, elite sample.
  — [PMC record (blocked)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12179260/); [ETC Journal review](https://etcjournal.com/2025/11/10/review-of-kestin-et-al-s-june-2025-harvard-study-on-ai-tutoring/); [Gigazine](https://gigazine.net/gsc_news/en/20250730-ai-tutor-physics-course-engagement/)
- Both trials measure **learning under supervised or structured use**. Neither measures voluntary return rates in a consumer app.

**Push notifications**
- [HARD, peer-reviewed, 2024–25] "Campaigns That Click", *Information Systems Research* (DOI 10.1287/isre.2024.0917). Using more than 200 push campaigns plus controlled experiments, the authors find pushes lift same-day click-throughs, but **repeated exposure produces diminishing responsiveness and may reduce engagement at high frequency**. — [INFORMS](https://pubsonline.informs.org/doi/10.1287/isre.2024.0917)
- [HARD, micro-randomized trial, 2018 (pre-2023)] In an mHealth app, a tailored push raised 24-hour engagement by **3.9% (risk ratio 1.039)**, with a larger effect on weekends. — [JMIR mHealth / PMC6293241](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6293241/)
- [ANEC, industry A/B] A test on about 1M users found 25% fewer pushes came with 10% fewer unsubscribes, but other arms that cut pushes lost retention. — [FunCorp on Medium](https://medium.com/@FunCorp/experimenting-with-push-notifications-for-user-retention-tested-on-a-million-strong-audience-d08d15ce57b9)
- [ANEC, vendor] Claims such as "+23% from using the first name" are unsourced. — [Statsig](https://www.statsig.com/perspectives/push-experiments-engagement)

### Inferences
- A daily drop, like a puzzle or a "today's brief", plus a bundle is the best-documented consumer subscription retention pattern of 2024–26 (NYT). Its causal effect on churn is not public, so present it as a strong case study, not proof.
- An annual or periodic AI-generated "Wrapped" works as an acquisition and virality event (500M shares). AI apps have rich personal data for these recaps, but there is no evidence they reduce churn.
- The AI-tutoring RCTs support "personalized AI feedback" as delivering real *value*. Retention still needs separate mechanics (scheduling, social structure) because both trials ran in structured settings, such as pairs in school sessions.
- Notifications: default to a few high-relevance pushes, in the style of Duolingo's streak-saver message, and watch opt-out rates. More pushes have diminishing and possibly negative returns.

### Gaps
- NYT does not disclose a Games-only subscriber count or games retention curve for 2026. No retention data for Wordle players was found.
- No data on Strava Year in Sport, Duolingo Year in Review, Fortnite seasons, countdown timers, or Community Day DAU uplift.
- Exact Kestin et al. effect sizes were not read from the paper (PMC blocked).
- No RCT links LLM feedback to *voluntary consumer-app retention*. This is an open evidence gap.
