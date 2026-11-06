# Parent Check-in

## One-line pitch
A one-tap daily "I'm OK" for parents who live alone, sent from a big button (or a WhatsApp reply), that quietly alerts the family group if the check-in is missed.

## Who exactly
- **Payer:** adult children, especially those living far away. The AARP and National Alliance for Caregiving report counts 63 million US family caregivers in 2025 (verified survey, AARP press release); a secondary summary says about 10% are long-distance (an hour or more away), which I could not confirm in the primary report.
- **Diaspora beachhead:** Indian families with children abroad or in other cities. LASI Wave 1 (2017-18) found 36% of Indians 60+ have at least one migrant child and 35% are empty nesters; living-alone rates are 5.7% overall and 9.0% for women (LASI fact sheet and study abstracts; migration is not split by abroad vs domestic).
- **Where they gather:** NRI Facebook groups, r/AgingParents and r/caregivers (subscriber counts not retrieved; Reddit blocks the fetch script).

## Demand evidence
- **The strongest signal in this batch:** China's "Are You Dead?" (Sileme, known abroad as Demumu) went to number one on Apple's paid chart in China in early January 2026 and reportedly into the US top ten paid apps. Users press one button daily; two missed check-ins email an emergency contact. Three founders built it in about a month and added a roughly 8 yuan (about $1) fee to cover SMS costs (Sixth Tone, CNN syndication, press). Copycats ("Still Alive?") followed within days.
- Note the audience: that wave was young people living alone, not elderly parents, and it spread on the shock of the name.
- Snug Safety has run since 2016 and claims over 1 million check-ins and AARP/Forbes features (self-reported). A syndicated "Savvy Senior" column in March 2026 recommended it to adult children.

## Money proof
- **Snug Safety:** free daily check-in; Dispatch plan about $20/month or $200/year with calls on a miss (press column; not verified on Snug's site). AppGoblin estimates only about 7.8K iOS MAU and 2.2K ratings (third-party estimate). No revenue figure found.
- **Are You Dead? / Demumu:** about $1 paid download at peak; no revenue figure; founders said they aimed to raise $500K (self-reported).
- Medical alert pendants and senior monitoring (Life360, CarePredict, Lifeline) show families pay for safety, but I did not retrieve revenue for those in this pass.
- Overall: real willingness to pay exists for monitoring hardware and services, but no check-in app shows meaningful subscription revenue.

## Competitor weaknesses
- Snug supports only one daily cadence and pushes phone calls into a $20 tier (column, comparison site).
- Demumu alerts by email only and drew backlash for its morbid name; the founders promised elderly-friendly versions, which suggests the original UI was not built for older users (Sixth Tone).
- The core weakness of the category: the parent must install and remember an app. Many elderly parents in India use WhatsApp but not new apps.

## The wedge
Make the parent side app-free: a daily WhatsApp message ("Good morning, tap OK") or a widget with one giant button, in Hindi, Tamil, Telugu and other languages, with the family group as the alert channel. Sell to the child abroad, priced in dollars, with escalation (call a neighbour, then a local contact) as the paid layer. Add a gentle daily mood emoji so the check-in also becomes a small daily conversation.

## The 2-second clip
Split screen: in Pune, a mother taps a big green "I'm OK" at 8:02am; in New Jersey, her son's lock screen shows "Amma checked in, feeling good" with a sun emoji. Honest, but it is a quiet moment rather than a visual transformation.

## Core loop sketch
- **Onboarding aha:** child sets up in two minutes, sends a WhatsApp invite, sees the first check-in arrive.
- **Daily action:** parent taps OK and a mood; family sees a calm green tick.
- **Streak/reward:** a shared "100 good mornings" calendar for the family; parent gets a weekly photo from the grandkids as a reward.
- **Shareable artifact:** monthly family card of moods and check-ins.
- **Paywall:** free single check-in; paid $4.99/month or $39.99/year for escalation calls, multiple check-ins, local contacts. Paywall placed after the first successful check-in, not before.

## Risks
- **Liability and false safety:** a missed alert during a real emergency is a serious reputational and possibly legal risk. Must avoid medical-device claims.
- **Platform:** WhatsApp Business API costs per message and policy limits on automated messaging.
- **Retention:** the payer gets value only when something goes wrong, so perceived value fades; churn risk is high once the novelty of "she's fine" wears off.
- **Saturation:** low revenue competition, but Apple and Google keep adding fall detection and check-in features (Apple's Check In in Messages), which may cap demand.

## Scores
| Criterion | 1-5 | Why |
|---|---|---|
| Two-second aha | 3 | Tap and family sees a tick; clear but not visual (Sixth Tone description of Demumu) |
| Visual short-video hook | 3 | Demumu spread on the name and loneliness discourse, not a demo (press coverage) |
| Money already swims | 2 | Snug ~7.8K MAU, Demumu $1 download; no app with real subscription revenue found (AppGoblin, press) |
| Daily reason to return | 5 | The product is literally a daily check-in |
| Shareable moment | 2 | Private family moment; little to post publicly |
| Unit economics | 2 | Payer is motivated but value is invisible on good days; SMS/WhatsApp costs per user; no proof of LTV |
| **Total** | **17/30** | |

## Verdict
Maybe, leaning skip as a standalone subscription. Demumu proves the concept can explode in attention, but nothing proves people keep paying, and the liability tail is real. Worth a cheap WhatsApp-first experiment aimed at NRI families, where the payer has dollars and genuine anxiety.

## Sources
- https://www.sixthtone.com/news/1018076/China's Viral New App Is a Safety Tool Called 'Are You Dead
- https://keyt.com/news/national-world/cnn-world/2026/01/13/viral-app-in-china-taps-into-national-loneliness-by-asking-are-you-dead/
- https://gazette.com/2026/03/10/savvy-senior-is-your-aging-parent-safe-at-home/
- https://apps.apple.com/us/app/snug-safety/id1122758716
- https://appgoblin.info/apps/1122758716
- https://www.aarp.org/press/releases/2025-07-24-new-report-reveals-crisis-point-for-americas-63-million-family-caregivers.html
- https://zencaregiving.org/caregiving-statistics-us-2025/
- https://www.iipsindia.ac.in/sites/default/files/other_files/LASI_W1_Elderly_India.pdf
- https://ipc2021.popconf.org/abstracts/211497
