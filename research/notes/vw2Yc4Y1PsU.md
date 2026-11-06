# I make $10K/month from 28 apps
- URL: https://www.youtube.com/watch?v=vw2Yc4Y1PsU | Channel: Starter Story | Views: 249728 | Length: 841s (~14 min)
- Sources used: https://rosetta.to/u/starterstory/i-make-10k-month-from-28-apps (full caption transcript with chapters); https://www.betterlaunch.co/playbooks/max-28-apps-3 (playbook card quoting the reusable-component tactic)
- Confidence: high (full transcript read)

## Core claims (3-7 bullets, what the video argues)
- A portfolio of tiny single-feature apps, shipped fast and abandoned if they sink, beat years of polishing one pet project: 28 apps in 8 months took Max from $200/month to $10,000/month while keeping his full-time iOS job.
- Ideas come from App Store search demand, not inspiration: find a keyword with enough popularity and low difficulty, confirm competitors actually make money, then build only the single core feature that answers the search.
- Speed comes from a personal component library (settings, onboarding, paywall screens copied wholesale; "for some apps I basically copy like 90% of the code") plus AI planning, not from AI magic.
- Let data decide: ship, watch the post-launch App Store boost fade, keep only apps that stabilize or grow, then return to winners to add polish and ads.
- Revenue follows the 80/20 rule: four apps make ~$1,500/month each; the other 24 make small amounts.

## Specific tactics (concrete, actionable; include numbers, prices, timings, exact UI choices)
- Keyword screen in Astro (ASO tool): popularity at least 20%, difficulty 60-70% or lower; create a temporary app in Astro, add the keyword (e.g., "tree identifier"), pull related keywords ("wood identification" was popular with very low difficulty), select targets.
- Market check: open top competitors' revenue (Sensor Tower or similar / App Store); benchmark is at least $100-200/month for a top competitor, otherwise "there's not that much money in that market."
- Cluster keywords for code reuse: physics AI, chemistry AI, math AI all target students, so one app's code jumps to the neighbors "in just no time."
- Build process: study 2-3 competitors and only the feature tied to the keyword; tell ChatGPT/Gemini the keyword plus UI/UX constraints and ask for a detailed implementation plan; create project, drag-and-drop reusable screens (settings, onboarding, paywall); for metadata, ask ChatGPT for the description tied to the keyword; screenshots and icon from Figma templates copied across projects; ship via Fastlane.
- Timing: record is 2 hours from idea to App Store submission; typical range is a couple of hours to a week.
- Six-step playbook: (1) find strong keywords with good popularity/difficulty and real competitor revenue; (2) study competitors, define the single core feature; (3) plan fast with AI (Cursor or Claude writes out all screens, features and flows so you know which screens to build vs copy); (4) build a lean MVP with only what delivers value; (5) release and move on ("once the app is live, just let it go"), watch the App Store launch boost fade and see if the app sinks or floats; (6) return to winners: polish, bug fixes, add ads to double down.
- Tech stack: Flutter (iOS + Android), Fastlane, Cursor, Firebase (auth, database, hosting), OpenAI and Gemini for image recognition, Mixpanel analytics, Astro (iOS ASO) and Fox Data (iOS + Android ASO).
- Monthly costs: Cursor $20, Fastlane $0, OpenAI ~$200, Gemini $50, Firebase $5-10 (stays in free tier), Mixpanel $0 (free plan), Astro ~$10, Fox Data $0 (free plan); total roughly $295-310/month against ~$10K revenue.
- Advice: "Get it ready bugs free, just one single feature, ship it, and let users tell you what they think about it while you're building another app."

## Named examples (apps/companies cited and what they did)
- Max (iOS engineer, father of two) and his 28-app portfolio; example niches: tree identifier / wood identification, physics/chemistry/math AI study apps.
- Adam Lyttle's YouTube video (February of that year) as the trigger: "you create one app, one feature, ship it, forget about it, and jump onto another app."
- Tools: Astro, Sensor Tower, Flutter, Firebase, Cursor, Claude, ChatGPT, Gemini, Fastlane, Mixpanel, Fox Data, Figma.
- Sponsors/pitches: The Hustle newsletter; Starter Story Build boot camp (code 28APPS for 20% off).

## Numbers & evidence (any stats, revenue, conversion rates, retention figures; mark self-reported vs third-party)
- 28 apps in 8 months; $200/month -> $10,000/month (self-reported).
- 1,000+ subscribers across all apps; 4-5K daily users across the portfolio (self-reported).
- Top 4 apps ~$1,500/month each; remaining apps "very small numbers" (self-reported).
- Keyword thresholds: popularity >= 20, difficulty <= 60-70; competitor revenue >= $100-200/month (Max's rules).
- Build time: 2 hours record; up to a week typical.
- Costs ~$295-310/month (self-reported).

## Contradictions or caveats (where this disagrees with common advice or other videos)
- Contradicts "focus on one product and iterate with users"; Max says years of that produced nothing and the opposite worked.
- Low competitor-revenue bar ($100-200/month) means he deliberately enters tiny markets; this is a volume strategy that relies on App Store launch boosts, which Adam Lyttle's 2026 content says have weakened.
- Monetization specifics (price points, paywall design, subscription vs ads mix) are not discussed beyond "add ads to winners" and "1,000+ subscribers."
- The video is partly a funnel for Starter Story Build, and revenue is unverified.

## Memorable framings (quotable one-liners or named frameworks, verbatim if available)
- "Instead of trying to build the perfect app, he'd ship dozens of apps really fast."
- "Once the app is live, just let it go and move on to the next project."
- "Let data decide which app sinks and which floats."
- "A portfolio of tiny bets" (Pat Walls' framing).
- "The most important advice would be not to be afraid of shipping."
- Named playbook: Max's 6-step build-and-ship process; "the famous 80/20 rule."
