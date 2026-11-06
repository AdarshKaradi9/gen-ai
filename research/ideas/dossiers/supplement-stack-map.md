# Supplement Stack Map

## One-line pitch
Scan every bottle in your cabinet and see your whole stack as a body coverage map, with overlaps, totals versus official upper limits, cost per day and a daily "taken" check-off.

## Who exactly
Daily supplement takers with three or more products, especially the biohacker and Huberman-listener crowd and women managing postpartum or perimenopause stacks (both appear in SuppCo reviews). r/Supplements has about 570K-630K members (GummySearch cached snapshot, third-party); r/HubermanLab and r/VitaminD are adjacent. CRN's 2024 survey puts US supplement use at 75% of adults with a median spend of $50/month among users, $100/month for those buying through practitioners.

## Demand evidence
- 75% of US adults use supplements; spending held steady from 2023 to 2024 despite inflation (CRN 2024 survey, industry association data).
- SuppCo has 31K iOS ratings at 4.82 stars, about 123K MAU and 334 new ratings in one week (AppGoblin, third-party estimate). This is strong active demand for stack tracking.
- A wave of 2026 launches (StackDay, VaultStack, Stack Precision, Biostacks Supplement Tracker, Supplement Tracker: Stack, and others on the App Store) shows founders see the opening, and also that the category is filling fast.

## Money proof
- BioStacks: about $64K MRR (TrustMRR, RevenueCat-verified, June 2026, per main agent findings). Note there are several apps using the BioStacks name; the scanner app "Supplement Scanner: BioStacks" scores supplements 0-100.
- Supplements AI: about $69K in 30-day revenue with 256 active subscriptions (TrustMRR, verified, per main agent findings), which implies a high price per subscriber.
- SuppCo: raised a $5.5M seed (Union Square Ventures, True Ventures, Oct 2024, press), 1.2M installs, but AppGoblin estimates under $10K/month IAP (third-party). Its value may sit in brand data and commerce rather than subscriptions.
- Users already spend ~$600/yr on supplements (CRN), so a $40-$60/yr tool that cuts duplicate spend is an easy frame.

## Competitor weaknesses
SuppCo App Store reviews (JustUseApp excerpts): the SuppScore advice is inconsistent ("tells me I need to significantly decrease chromium but then the very next update says..." with nothing changed), product matches can take weeks and some data is wrong, users want to enter contents manually, scoring favours "trusted" brands, and the app lags. A competitor-run review notes SuppCo does not flag when two items in a stack might not play well together (treat with caution, competitor source). JustUseApp's automated analysis rates 64.7% of reviews negative (automated, not audited).

## The wedge
"See your stack, not a score." Incumbents sell an opaque grade and recommendations, which users distrust and which carry medical-advice risk. The wedge is transparent arithmetic: sum each nutrient across all products, show it against published RDA and tolerable upper intake levels from NIH Office of Dietary Supplements with citations, flag duplicates ("you get zinc from 3 products, 2.4x the RDA"), and show cost per day per nutrient. Manual entry and label-photo OCR solve the "waiting weeks for a match" complaint. The body map shows which systems the stack touches. No "take more of X" recommendations.

## The 2-second clip
A hand sweeps eight bottles across a counter; cut to the phone where a body map glows and a red badge pulses on the liver: "Vitamin A: 3 products, above upper limit." Caption: "I scanned my supplement cabinet."

## Core loop sketch
- **Onboarding aha:** scan or photograph 3 bottles, stack totals and body map appear with one surprise (a duplicate or an over-UL nutrient).
- **Daily action:** morning/evening "taken" check-off with reminder, the proven daily unit in this category (SuppCo reviewers cite reminders).
- **Streak/reward:** adherence streak with two freezes; monthly "cost per day" and "stack changes" report.
- **Shareable artifact:** "My Stack" card (products, body coverage, daily cost), the format biohacker communities already post as text lists.
- **Paywall:** hard or soft onboarding wall right after the first stack analysis, $39.99/yr preselected with a 7-day trial, weekly option behind "view all plans". Possible later affiliate revenue for cheaper equivalent products (check FTC disclosure rules).

## Risks
- **Medical advice:** the biggest risk. Drug-supplement interaction warnings and dosing logic are clinical content; Apple says dosage calculators must come from approved sources and reviewers reject uncited health recommendations under guideline 1.4.1 (Apple developer forums, Healthcare Dive). Stay with cited reference values (RDA/UL) and "talk to your doctor or pharmacist" language, and leave drug interactions out of v1. FDA's January 2026 general wellness guidance is more relaxed but does not cover diagnosis or treatment claims.
- **Liability:** a missed over-UL flag (for example vitamin A in pregnancy) could cause harm; label data errors are SuppCo's top complaint.
- **Saturation:** at least six new supplement trackers launched in 2026; a VC-backed incumbent with 123K MAU.
- **Data:** building a reliable label database is costly; OCR plus manual edit is the cheap route.

## Scores
| Criterion | 1-5 | Why |
|---|---|---|
| Two-second aha | 4 | Scan bottles, map plus warning appears (SuppCo shows scan-first onboarding works) |
| Visual short-video hook | 4 | "I scanned my supplement cabinet" is a native reveal format with physical props |
| Money already swims | 4 | Two TrustMRR-verified apps at $64K-$69K/month; users spend ~$50/month on product (CRN) |
| Daily reason to return | 4 | Pills are taken daily; reminders are a cited reason to use SuppCo |
| Shareable moment | 3 | Stack cards suit biohacker communities, less so the mainstream |
| Unit economics | 4 | High-spend users, verified high ARPU at Supplements AI, hard wall plausible |
| **Total** | **23/30** | |

## Verdict
Build, cautiously. This has the best money evidence of the three, with verified solo-scale revenue and a large paying habit, and incumbents have clear trust and data complaints. Win on transparent, cited totals and duplicate/UL flags rather than scores or interaction advice, and launch fast because the category is filling quickly.

## Sources
- https://crnusa.org/newsroom/crn-survey-shows-consistent-supplement-usage-increase-specialty-product-use-over-time
- https://appgoblin.info/apps/6504838951
- https://justuseapp.com/en/app/6504838951/suppco-supplement-scanner/reviews
- https://athletechnews.com/suppco-secures-5-5m-to-make-sense-of-supplements/
- https://suppco-app.pages.dev/blog/suppco-review-2026 (competitor-run, used with caution)
- https://www.appbrain.com/appstore/supplement-scanner-biostacks/ios-6758149582
- https://apps.apple.com/app/id6763328808
- https://apps.apple.com/app/stackday/id6761502044
- https://gummysearch.com/r/Supplements
- https://www.healthcaredive.com/news/apple-raises-entry-bar-for-medical-health-apps/425810/
- https://developer.apple.com/forums/thread/807508
- https://www.foley.com/insights/publications/2026/01/digital-health-policy-fda-relaxes-restrictions-over-wearables-and-ai-decision-ma/
- TrustMRR figures for BioStacks and Supplements AI via main agent findings (FINDINGS_SO_FAR.md)
