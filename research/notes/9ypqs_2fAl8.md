# We Studied 2,995 Paywalls. Here's What Actually Converts.
- URL: https://www.youtube.com/watch?v=9ypqs_2fAl8 | Channel: Mobbin | Views: 193521 | Length: 751s (~12.5 min)
- Sources used: https://sozai.app/transcript/studied-paywalls-what-converts/ (full caption transcript + summary); https://www.buzzsprout.com/2522779/episodes/18659063-jonathan-parra-i-made-4-000-app-paywalls-and-learned-this (Superwall Podcast show notes for the expert featured, Jonathan Parra); https://api.superwall.me/blog/the-paywall-tactics-behind-usd100k-month-apps (Superwall blog write-up of the same Parra material)
- Confidence: high (full transcript read; cross-checked against Parra's own podcast/blog material)

## Core claims (3-7 bullets, what the video argues)
- "There is literally no universal best paywall, only better experiments." Ugly, text-heavy, high-friction paywalls sometimes beat beautiful ones; design tests move the needle more than price tests.
- A paywall is a flow, not a screen: users often decide to pay before they see the paywall, so onboarding, feature-unlock moments, settings, and win-back offers are all paywall touchpoints. "Life cycle monetization and the paywalls, that's the only part of the app that makes money."
- Multi-page paywalls "almost always do better than single-page paywalls" because information unfolds gradually and the paywall feels like the natural next step of onboarding rather than a wall.
- Reducing perceived risk (trial timelines, "no commitment, cancel anytime", longer trials) raises conversions; but removing friction does not always help: adding credit-card entry or trial-only-on-annual can filter for serious buyers and raise paying-customer counts.
- Framing beats offer changes: social proof, value framing ("selling different futures"), price anchoring (weekly breakdowns, coffee/therapy comparisons) lifted results without changing the price.
- Keep the base paywall simple (two plans visible, rest behind "view all plans"), default to yearly for highest LTV, and judge success on retention and LTV, not just trial starts.
- Polish and world-building (animations, custom characters) are the new bar now that "anyone can ship an app".

## Specific tactics (concrete, actionable; include numbers, prices, timings, exact UI choices)
- Sell the outcome before asking for money: Opal spends onboarding on "getting 8 years of your life back"; showing users how many years of life they could save moved trial sign-ups from 7% to 17%.
- Multi-page paywall structure: end of onboarding -> "your plan is ready" -> emotional framing ("you'll start feeling like yourself in 4 weeks") -> price. Ask: "is it a natural segue to finish the onboarding?"
- One-time offer: if closed it's gone; pair with animation and haptic feedback to grab attention at the moment of upgrade consideration.
- Blinkist: redesigned the trial screen as a step-by-step timeline (what happens today, when the reminder comes, when you're charged). Result: more trial sign-ups, fewer complaints, push-notification opt-ins went up (the reminder is useful).
- Tipstop: emphasized the free trial, added a discount badge, simplified the offer wording. "The offer didn't change. The way it was presented did." Direct conversions almost tripled.
- Slopes: removed the traditional paywall for a "pay ramp" modeled on Apple's redeem-free-trial pattern: a single action, "redeem your free week." Trial starts +25%.
- Jonathan Parra's go-to tweaks: subtitle "No commitment, cancel anytime" under the CTA ("always seems to do well... bump things up incrementally"); a right chevron on the CTA button (appears on most winning paywalls; not isolated in an A/B test yet); outcome-specific CTA copy instead of "Continue" is "hit or miss".
- Exit-intent sheet: when the user taps cancel on an annual offer, show a sheet offering the monthly plan instead.
- Discounts: avoid aggressive last-minute discounts except Black Friday/Cyber Monday; to stay Apple-compliant, offer a larger trial instead of a deeper discount.
- Outsider: required credit-card details to start the trial; sign-ups dropped by more than half, conversion rate rose 5x, paying customers more than doubled.
- Moonly: free trial offered only on the annual plan.
- Price anchoring: Tide breaks the price into weekly amounts; Ahead compares the subscription to coffee or therapy.
- Headspace tested 7-, 14- and 30-day trials; winner was 14-day trial on the annual plan (longer trial made the pricier plan feel less risky).
- Packaging: default to yearly (highest LTV); show at most two options (yearly + weekly or monthly) to cut cognitive load; hide extra plans behind a "view all plans" button that opens a sheet. Get base stats before optimizing placements.
- Formats Parra likes: table/comparison paywalls that show what you're missing (hard to build in Superwall/RevenueCat, so under-used); video paywalls showing the app in action plus a simple bullet list and social proof.
- Spin-the-wheel paywall: a predetermined Lottie wheel that "lands" on a discount; works for maximizing weekly-price revenue but Parra is skeptical for long-term businesses and notes it's spreading.
- Apple in early 2026 started rejecting paywalls that relied on free-trial toggles judged confusing or misleading.
- Mobbin MCP pitch: lets Claude/ChatGPT/Cursor pull real paywall patterns from Mobbin's library when building with AI.
- From Parra's Superwall blog (same expert, companion material): a stripped-down paywall (big product image, headline, continue button) beat a detailed comparison chart by 111%; cleaning up plan names to "Annual Plan / Monthly Plan / Weekly Plan", CTA "Continue", plus "No commitment, cancel anytime" lifted conversions 10%; drawer strategy reframes $39/year as $0.76/week on X-tap, then a 25-33% one-time offer; native SwiftUI-style paywalls outperformed custom designs "by quite a long shot".

## Named examples (apps/companies cited and what they did)
- Opal (outcome-first onboarding, 7% -> 17% trial sign-ups), Ahead (gradual multi-page unfolding; coffee/therapy price anchor), Blinkist (trial timeline), Tipstop (trial emphasis + discount badge, ~3x direct conversions), Slopes (pay ramp, +25% trial starts), Outsider (credit card required, 5x conversion), Moonly (trial only on annual), Tide (weekly price breakdown), Headspace (14-day trial on annual won), ClassPass (fewer than 5 screens to subscribe, 17 to cancel), Focus Town (Animal Crossing-style polish, cited as the new bar), an unnamed AI girlfriend app (ugliest, most compact squeeze-page paywall outperformed everything Parra designed), Superwall (Jake and Nick: "design tests move the needle the most"), Mobbin MCP.

## Numbers & evidence (any stats, revenue, conversion rates, retention figures; mark self-reported vs third-party)
- "Nearly 3,000 paywalls" (title: 2,995) and hundreds of subscription flows studied on Mobbin; expert has designed "over 4,700 paywalls" (Superwall show notes say 4,500+). Self-reported by Mobbin/Parra.
- Opal trial sign-ups 7% -> 17% (case study as told by Mobbin; company-reported).
- Tipstop direct conversions "almost tripled"; Slopes trial starts +25%; Outsider sign-ups -50%+, conversion rate 5x, paying customers >2x; Headspace 14-day/annual won. All company-reported case studies relayed by Mobbin.
- Average app: Parra's companion blog claims modest lifts from 8% to 15-20% conversion are transformational (self-reported).
- ClassPass: <5 screens to subscribe, 17 to cancel (Mobbin's count).

## Contradictions or caveats (where this disagrees with common advice or other videos)
- Directly contradicts "remove all friction": credit-card-up-front and annual-only trials cut volume but raised paying customers.
- Contradicts "beautiful design converts": the ugliest paywalls sometimes win; "the ugly paywall with a ton of text completely outperformed anything that I would do."
- Warns that urgency/discount tactics (spin the wheel, close-for-a-discount) are being learned by users: "more and more users are getting comfortable closing paywalls because they know they're going to get some kind of offer afterwards."
- Apple compliance is a moving constraint (2026 rejections of trial-toggle paywalls); prefer a bigger trial over a bigger discount.
- Parra's own companion material says tables rarely beat simple bullets and a stripped-down paywall beat a comparison chart by 111%, while in this video he says he's "a huge fan of tables"; treat format preference as app-specific.

## Memorable framings (quotable one-liners or named frameworks, verbatim if available)
- "Sometimes, an ugly paywall could outperform a beautiful one."
- "More friction could increase conversions."
- "A paywall isn't just a screen. It's a flow."
- "When a paywall works, it doesn't feel like you've hit a wall. It feels like the product is asking you to take the natural next step."
- "Even if you have a well-designed paywall, if it appears at the wrong moment, it's still a bad paywall."
- "There is literally no universal best paywall, only better experiments."
- "The metrics that I wish more founders really care the most about is retention and LTV."
- "Maybe the question isn't how do I get people to pay? It's more of how could I create something worth paying for?"
- Named patterns: "pay ramp" (Slopes), "exit intent sheet", "spin the wheel paywall", "one-time offer", "trial timeline paywall", "table-based paywall", "video paywall".
