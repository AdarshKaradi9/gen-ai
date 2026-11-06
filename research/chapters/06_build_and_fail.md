## Building Fast and Not Failing: AI-built apps, MVP rules, founder lessons and anti-patterns

Building an app is now cheap. This chapter covers how people build with Claude Code, Cursor and similar tools, where those builds break, how YC-style MVP advice compares with the indie playbook, and why apps die. It ends with a corpus-wide map of where creators contradict each other. Treat every headline revenue number as a claim until the video backs it up (see "Read The Title Last").

### 1. You Are The Product Manager

**What it is.** AI writes the code. Your job is to scope, sequence and check it. Fireship's three rules: pick a popular, simple stack; get good at Git, which he calls non-negotiable because AI "has the power to delete your working code"; and act as the product manager for your AI, breaking work into small, specific steps so the model stays "as deterministic as possible" [vid:Tw18-4U7mts].

**Why it works.** LLMs are best at problems already solved many times on GitHub, so boring stacks get better output [vid:Tw18-4U7mts]. Diego Roshardt makes the same point: older, popular libraries get better AI code [vid:BaWUPamqWlA]. Andrew Codesmith adds a plan-mode step before any code is generated [vid:7u6b52RaQSc].

**The traps, with examples.**
- *Security.* Fireship's cautionary tale is a vibe-coded SaaS with paying customers that was hacked (maxed-out API keys, people bypassing the subscription) and shut down for good [vid:Tw18-4U7mts]. Blake Anderson's early apps reportedly shipped with exposed API keys and bugs [vid:mGMDyPTR7QU]. Jason Lee proxies his OpenAI key through a small Node/Express backend so users cannot drain it, and references an 18-item App Store rejection checklist because vibe-coded apps get rejected for missing reliability and security layers [vid:9atd5lczG2k].
- *The prompt treadmill.* Fireship describes spending 3 days and $500 in Claude credits to build "a crappier version" of a $10 app (satirical, self-reported). His fix is grounding the model with MCP servers (Figma, Stripe, Sentry, GitHub), with a warning that live write access risks "accidentally refunding 10,000 customers with a single prompt" [vid:PLKrSVuT-Dg].
- *Scale.* Yorby's backend was built for about 20 users and fell over at 10,000 (self-reported) [vid:PZylEWhBDqo].
- *Demo is not product.* Jason Lee's animated hydration clone has a mockup paywall that processes no money, and code-only character animation looked stiff until he generated video clips for it [vid:Rk6t9Uq1y9M]. In Dave Ebbelaar's AI course, "the model proposes, code decides": plain code makes the final call, and a golden set of test cases checks every decision [vid:XzjSx7u9mGw].

**How to apply.** Use a mainstream stack (Expo/React Native plus Supabase or Firebase appears in most builds [vid:9atd5lczG2k][vid:7u6b52RaQSc][vid:vw2Yc4Y1PsU]). Commit after every working step. Keep API keys server-side. Write evals or checks for any AI decision.

**Caveats.** The DevForge "Vibe Coding is a Trap" video could not be summarized beyond its title, so it is not evidence either way [vid:ya6520zh4pQ]. Mikey No Code's "Claude Code (FREE)" video actually builds in Base44, a no-code wrapper, and Claude Code itself needs a paid plan [vid:xfptZcCf484].

### 2. Data Model First, Screenshot Wall Second

**What it is.** Two build methods recur among founders who report revenue. Connor Burd writes a text document describing the data model, with sample JSON and notes on each attribute, before prompting, so the AI "doesn't have to make any guesses." He builds core functionality first and onboarding later [vid:CwHD6Fg-Mjs]. For onboarding, he downloads about 20 apps in the niche plus well-designed apps from other categories, screenshots every onboarding screen, lays them all out in one Figma line, and cherry-picks the questions, graphs and screens. Then he pastes Figma screenshots into Claude or Cursor to generate whole screens [vid:CwHD6Fg-Mjs].

**Variants.** Jason Lee gives Claude a competitor's App Store URL to generate a feature list, pulls reference screens from Mobbin, records the real app on a phone, and gives feedback as a narrated screen recording pointing at concrete failures [vid:9atd5lczG2k][vid:Rk6t9Uq1y9M]. Max, who runs 28 apps, keeps a personal library of settings, onboarding and paywall screens ("for some apps I basically copy like 90% of the code"). He asks ChatGPT or Gemini for a detailed implementation plan and has hit 2 hours from idea to App Store submission, with portfolio costs of about $295-310 a month (self-reported) [vid:vw2Yc4Y1PsU].

**Why it works.** A clear schema and visual references remove the ambiguity where agents drift, which matches Fireship's "product manager" rule [vid:Tw18-4U7mts].

**Caveats.** Copying another app's character art and screens is fine for practice, but a commercial app needs original or licensed assets [vid:Rk6t9Uq1y9M]. Codesmith says AI-generated designs "suck" and design was his real bottleneck [vid:7u6b52RaQSc].

### 3. Ship Something Bad Within A Month

**What it is.** Michael Seibel's whole talk compresses to "launch something bad quickly." Time-box the spec to about three weeks, write it down, cut it when you overrun ("if there's no non-important things, start cutting important things"), and don't fall in love with it. Hold the problem and customer tightly and the solution loosely [vid:1hHMwLxN6EM]. Airbnb launched with no payments and no map, Twitch began as one low-res channel, and Stripe's founders integrated it for you by hand [vid:1hHMwLxN6EM]. In his longer lecture he suggests about two weeks, to avoid "MVP drift" [vid:C27RVio2rOs].

**Indie evidence (self-reported).** Cal AI v1 took three weeks of coding plus a week of App Store review: two screens and a camera button. Zach Yadegari's rule is never to spend more than a month on an MVP [vid:qDuzzrQKP_M]. Connor Burd built Payout in under two weeks [vid:CwHD6Fg-Mjs], and Diego Roshardt built his MVP in two weeks [vid:BaWUPamqWlA]. Kevin Hale's framing is that the values that win the first user are the ones that get you to scale [vid:sz_LgBAGYyo].

**Caveats.** "Lean" does not mean pre-hyped. Zach describes a friend whose Figma-mockup TikToks drew millions of views, but the outsourced app shipped months later, after the hype had died and competitors had appeared. If you pre-validate, be ready to ship immediately [vid:qDuzzrQKP_M]. Michael Skok's bar is stricter: spend twice as long on the problem as on the solution, and require roughly a 10x gain-to-pain ratio before people will switch [vid:q8d9uuO1Cf4]. Chris Raroque launches only when beta analytics show users sticking for several days [vid:MnF-zJhyUtE].

### 4. Make Them Pay Before You Build Much

**What it is.** Validation means money or behaviour, not compliments. Ash Maurya's order is demo, then sell, then build. Swap "Would you use this?" for "Will you pre-order this?" and pivot only on feedback from paying customers [vid:Pydut1BMlBw]. His companion posts report about $35,000 from 209 customers in about 40 days using this method (self-reported) [vid:Pydut1BMlBw]. Seibel says starting with a price is "almost always better than starting free," and suggests making the product slightly harder to use to see whether people use it anyway [vid:C27RVio2rOs].

**Examples.** OpusClip emailed hand-polished clips to prospects before any UI existed. About 60% replied positively (self-reported). Next they ran a Discord bot, and the product-market-fit signal was users complaining about queue length and daily quota [vid:HQ3eVt2jgAY]. One YC founder sold a $250/month contract with no code and shipped a rough version in seven days [vid:NZp5j5hvn9I]. Jen Abel's advice is to find 30 people by hand before buying tools [vid:969dwgu98qc].

**Caveats.** Consumer subscription founders often skip this. Connor Burd tells you to skip the waitlist and just build [vid:CwHD6Fg-Mjs], while Raroque says to set up the waitlist before writing code [vid:MnF-zJhyUtE]. Altman's bar is softer and harder at once: build something so good that people "spontaneously tell their friends" [vid:0lJKucu6HJc].

### 5. Proven Demand Beats Novelty

**What it is.** Pick ideas where money is already changing hands.
- Steven Cravotta works through evergreen categories (health, wealth, relationships, status, convenience, freedom), checks Google Trends for rising interest and Sensor Tower for competitor revenue, and treats competitors as a green flag [vid:z_fARFqjLoY].
- Blake Anderson looks for niches "heavily monetized with physical products" (looksmaxxing: skincare, gua sha) where no software exists. He validates by opening a fresh social account and consuming only that niche's content until he is "essentially becoming the target market" [vid:5u9u8yzPEpA].
- Max requires keyword popularity of at least 20, difficulty of 60-70 or lower, and a top competitor earning at least $100-200 a month [vid:vw2Yc4Y1PsU].
- Zach scrolls the top 200 in each category for anything that has been stagnant for years [vid:qDuzzrQKP_M].
- Burd: "If you're creating a modified version of an existing app, then congrats, your app is already validated" [vid:CwHD6Fg-Mjs].

**Review mining.** Read competitors' bad reviews for repeated unmet needs [vid:SI8T1yvmoRs][vid:VfNRd5Rk0cM]. Rootd's founder found "how do I get through one right now" in panic-app reviews, and its SOS button has not changed since the MVP (self-reported) [vid:VfNRd5Rk0cM].

**Why it works.** Painful, already-paid-for problems convert, and they are easier to market [vid:z_fARFqjLoY].

**Counter-evidence.** The OpusClip CEO warns against two idea types: features an incumbent can bundle (a note-taker against Zoom) and prompt wrappers the next model release makes redundant. He recommends owning a vertical workflow and running three filters: a niche you "cannot further segment," a boring industry, and work people already pay agencies or freelancers to do [vid:HQ3eVt2jgAY]. Adam Lyttle worried that iOS 18's ChatGPT integration would make his scanner apps obsolete [vid:3sLP2bcD5Xg]. For first-time founders, social apps are a trap. Burd's first app, a social app, took 6-8 months and failed [vid:CwHD6Fg-Mjs], and Zach notes that a utility needs only one person to get value [vid:qDuzzrQKP_M].

### 6. Support Is The Roadmap

**What it is.** Kevin Hale's Support Driven Development: everyone, engineers included, does customer support [vid:sz_LgBAGYyo][vid:12D8zEdOPYo].

**Numbers (Wufoo, self-reported, 2014-era web SaaS).**
- Ten people supported about 500,000 users, with replies in 7-12 minutes during business hours.
- Engineers spent 4-8 hours a week on support.
- An "emotional state" dropdown on the support form was filled in 75.8% of the time.
- An A/B-tested documentation redesign cut support load by 30% overnight [vid:12D8zEdOPYo].

Hale's argument is that stonewalling (ignoring tickets) drives churn, and that adding features widens the "knowledge gap" between what users know and what the app can do [vid:sz_LgBAGYyo].

**Modern versions.** Kaching says about 95% of its Shopify reviews come from customer support interactions, and it pays agents bonuses per review (self-reported) [vid:vLLBzUZr6-s]. Raroque runs a Canny feedback board (his planner's list feature exists only because of user votes), PostHog analytics (30 minutes to set up), and a 5-email, 2-week onboarding sequence he calls a "huge unlock" for 14-day retention (self-reported, no figures) [vid:MnF-zJhyUtE].

**How to apply.** Answer support yourself. Mine tickets for the underlying problem rather than the literal feature request [vid:sz_LgBAGYyo]. Fire abusive customers: Justin Kan refunded one four times and then banned them [vid:C27RVio2rOs].

**Caveat.** This conflicts with the Cal AI and TikTok-farm habit of outsourcing support and outreach to VAs [vid:sz_LgBAGYyo].

### 7. The 95% Claim, Audited

**The claim.** Cravotta says marketing is about 95% of an app's success: a mediocre app with great marketing can win, a great app nobody can market will not [vid:z_fARFqjLoY]. Elsewhere he says 90% [vid:PX30Fb8TlcE][vid:RGT7PX4TQ8w]. Codesmith: "Distribution is the issue now," so spend 20-30% of your time on content [vid:7u6b52RaQSc]. Zach ranks marketing the highest lever "if all else is equal" [vid:qDuzzrQKP_M].

**What the evidence shows.** None of these percentages is measured. Cravotta's own notes label it opinion [vid:PX30Fb8TlcE]. The best third-party data point is about cost, not causation. CNBC-reviewed documents show Cal AI spending about $770k a month on marketing against about $1.4M gross profit and about $274k net operating income [vid:OsN_MJopMxc]. Marketing is the biggest line item. That does not make product irrelevant: Cal AI's reviews flag accuracy problems, so the "aha" feature is also its main complaint driver [vid:OsN_MJopMxc].

**Counter-voices.** Hale calls marketing "the tax you pay for not making a remarkable product" [vid:12D8zEdOPYo]. Altman puts 80% of the work in building something people recommend unprompted [vid:0lJKucu6HJc]. A UGC agency founder says "marketing can't fix a bad product" [vid:gUL6q-FndRE]. Nikita Bier argues virality is learnable but retention is luck [vid:bhnfZhJWCWY].

**Practical reading.** Budget real time for distribution from day one. Do not read "95%" as permission to ship a weak core.

### 8. Why Apps Die

The notes give these recurring causes. Most are founder opinion, not studies.
- **Never launching.** "You'd be surprised at how many founders' journeys end before a single user has actually interacted with a product" [vid:1hHMwLxN6EM].
- **Unvalidated or low-pain idea.** Cravotta [vid:z_fARFqjLoY] and Skok, who calls this the #1 cause [vid:q8d9uuO1Cf4], both rank it first. Both are assertions.
- **Skipping research and optimization.** Cravotta says research separated Puff Count from "failed apps dying at 100 downloads," and that paywall testing reportedly took it from $3K to $30K MRR (third-party claim) [vid:RGT7PX4TQ8w].
- **Social-app cold start** [vid:CwHD6Fg-Mjs][vid:qDuzzrQKP_M]. Hunter Isaacson calls games "double hard" for small founders [vid:DTree0unT_0].
- **Security and infrastructure debt** [vid:Tw18-4U7mts][vid:PZylEWhBDqo].
- **Closing platform windows.** Lyttle's 2026 content says the launch-day organic boost is gone, his paywall style started getting rejected by Apple, and keyword-chasing got developer accounts terminated [vid:3sLP2bcD5Xg].
- **Quitting or pivoting too early.** Seibel says to iterate on the solution, not the problem, and to judge progress over about 2 years, not 2 months [vid:C27RVio2rOs].
- **Co-founder breakups.** Blake left RizzGPT after a power struggle [vid:5u9u8yzPEpA]. Ash Maurya's advice is to "date before committing" [vid:Pydut1BMlBw].

### 9. Read The Title Last

This genre's titles routinely overstate. Examples from the notes:
- **No revenue at all.** "$10K/Month Mobile App Using AI in 15 Minutes": the app built on camera has zero users and zero revenue [vid:SI8T1yvmoRs].
- **Someone else's revenue.** "$80K/Mo mobile app with Claude Code": the figure belongs to an unnamed reference app, not the creator's clone [vid:UMjeSU6C4qU]. Waterllama's ~$100K/month is repeated without verification [vid:Rk6t9Uq1y9M], and ReciMe is $800k/month in one video but ~$500k in another [vid:9atd5lczG2k][vid:q4pSLc13OTs].
- **Compressed timelines.** "$20K/month in 14 days": 14 days was the build. Revenue took about 50 days and an influencer push [vid:CwHD6Fg-Mjs].
- **Gross dressed as recurring.** "$25K/month" is gross collections against about $14K MRR [vid:KgS3hbpxTzE]. A "$34K/month" title sits over a dashboard showing $24k MRR [vid:pvjalHFNM9Q].
- **Profit that isn't profit.** Cal AI's "$1.4M/month" is gross profit, not net [vid:OsN_MJopMxc]. Its revenue is pre-renewal, since 95% of subscriptions were yearly and none had renewed yet [vid:qDuzzrQKP_M].
- **Shifting user counts.** OpusClip's user numbers range from 12M to 50M depending on who is speaking [vid:HQ3eVt2jgAY]. Blake's "$100 of marketing to $80K/month" story is disputed [vid:mGMDyPTR7QU].
- **The honest counterexample.** The only third-party-verified figure among these indie claims is "$10k": lifetime revenue, currently about $105 a month [vid:xLwgYzdOD4A].

Many of these videos are also funnels: Starter Story Build [vid:vw2Yc4Y1PsU], Cravotta's Posted [vid:RGT7PX4TQ8w], Manus affiliate links [vid:SI8T1yvmoRs], Base44 affiliate links [vid:RQPVR6_WYoM]. Ask whose revenue it is, gross or net, monthly or lifetime, and before or after renewals.

### Where creators contradict each other (whole corpus)

| Topic | One camp | Other camp |
|---|---|---|
| Onboarding length | Long quiz-style flows sell. Cal AI runs 28-29 screens [vid:wMk_t8F1rOc][vid:MZDvGzxr3gY][vid:CwHD6Fg-Mjs] | Minimal input, register later [vid:Xvjxr0lkcjE]. Long only if it buys personalization [vid:Aa89MC8jX2c]. "Do you need that many? Probably not" [vid:QMo2T5apdYw]. Perceived length matters more than screen count [vid:Qsq-Sj_rojU] |
| Paywall timing | Paywall before any feature use [vid:dKif3Eo3frk][vid:PX30Fb8TlcE] | Give value first [vid:2TlIg3VokY8]. Immediate post-signup paywalls are "catfishing" [vid:vAN7kmpTdy4]. Duolingo keeps 91% of users free [vid:9KqrnBiyBQ8] |
| Price level | Higher prices convert [vid:sYRhXB_ZcLI][vid:RGT7PX4TQ8w] | Low prices on purpose [vid:5u9u8yzPEpA][vid:DTree0unT_0]. Cal AI's $70/year made less per download than $30 [vid:qDuzzrQKP_M] |
| Free vs charge early | Charge from day one [vid:C27RVio2rOs][vid:Pydut1BMlBw] | Launch free, monetize after reviews [vid:vLLBzUZr6-s]. Lyttle later reversed his own users-first stance [vid:_Fiwx6lm5YU] |
| Paid ads | Don't sleep on paid; scale winners [vid:e_t1gYkvZkI][vid:CwHD6Fg-Mjs] | Paid is the worst-margin channel at 0-30% [vid:5u9u8yzPEpA]. 2026 growth is organic [vid:HjnXnssrj4M]. No paid for social apps [vid:RVnnqTrSKZY] |
| Influencer pay | Flat upfront fees, judged by RPM vs CPM [vid:qDuzzrQKP_M] | Performance-only CPM [vid:RVnnqTrSKZY] |
| Accounts and authenticity | 20-40 throwaway accounts; AI faces are fine [vid:pb4JIH8FubE][vid:PZylEWhBDqo] | Audiences must not detect an ad [vid:9r4kS9zZj9s] |
| ASO | ASO built a $50K/month app [vid:I2GG0lyb_RI][vid:VfNRd5Rk0cM] | ASO is largely dead for new apps [vid:HjnXnssrj4M] |
| Portfolio vs focus | 28 tiny apps, let data decide [vid:vw2Yc4Y1PsU] | Give one problem about 2 years [vid:C27RVio2rOs]. Lyttle now favors feature-worthy apps [vid:3sLP2bcD5Xg] |
| Research depth | Some conversations, then build [vid:1hHMwLxN6EM]. Six interviews [vid:j2w4y7pDi8w]. "Audience comes last" [vid:6V4y0AX69h4] | 2-3 weeks of ICP work and 20-30 interviews per decision [vid:HQ3eVt2jgAY] |
| Streaks and gamification | Streaks are a core retention engine [vid:_CCwoQZH5hI][vid:pb4JIH8FubE] | Default streaks and PBL are a liability [vid:LXX_qOA5D8E]. Black-hat drives are unsustainable [vid:v5Qjuegtiyc] |
| Reward design | Variable reward is essential [vid:TDRQfGT6GtE] | Predictable encouragement lifted retention [vid:2BKmNmnEj9w]. Most of the system should be transparent [vid:yBpv5rZoBjA] |
| Polish | Animation drove Duolingo's DAU [vid:Du2lkZ_cux8] | Ugly, text-heavy paywalls win [vid:9ypqs_2fAl8]. Prettier screenshots lost an A/B test [vid:I2GG0lyb_RI] |
| Copying | Copy proven formats and flows [vid:q4pSLc13OTs][vid:CwHD6Fg-Mjs] | Copying fails for context reasons [vid:24QMRDXck70][vid:QaDsk4iH1aw] |
| Trial disclosure | Hide trial length on the plan card [vid:24QMRDXck70] | Put charge timing front and center [vid:sYRhXB_ZcLI] |
| Features | Add gamification layers [vid:pb4JIH8FubE] | Every feature widens the knowledge gap [vid:sz_LgBAGYyo] |

Most of these splits come down to context. Subscription utilities on paid acquisition favor long onboarding, hard paywalls and influencers. Word-of-mouth, social and marketplace products favor value first, launching free and organic growth. Pick the camp that matches your acquisition model, not the one with the bigger title.

### Checklist

1. Write the data model as sample JSON before your first prompt [vid:CwHD6Fg-Mjs].
2. Use a popular stack and commit after every working step [vid:Tw18-4U7mts].
3. Keep AI API keys behind your own backend and check App Store rejection risks before submitting [vid:9atd5lczG2k].
4. Build a Figma wall of about 20 competitor onboarding screens before you design your own [vid:CwHD6Fg-Mjs].
5. Time-box the MVP to 3-4 weeks, write the spec down, and cut it when you slip [vid:1hHMwLxN6EM][vid:qDuzzrQKP_M].
6. Ask for a pre-order or payment, not "would you use this?" [vid:Pydut1BMlBw].
7. Check that competitors earn money and that search interest is rising before you commit [vid:z_fARFqjLoY][vid:vw2Yc4Y1PsU].
8. Avoid ideas an incumbent can bundle or the next model release can absorb [vid:HQ3eVt2jgAY].
9. Set up analytics and a feedback board before launch, and launch only when beta users stick for several days [vid:MnF-zJhyUtE].
10. Answer support yourself, and turn tickets into fixes for root causes [vid:sz_LgBAGYyo].
11. Plan distribution from day one, but don't treat "marketing is 95%" as data [vid:z_fARFqjLoY][vid:OsN_MJopMxc].
12. Before trusting a revenue title, ask: whose revenue, gross or net, monthly or lifetime [vid:SI8T1yvmoRs][vid:KgS3hbpxTzE].
