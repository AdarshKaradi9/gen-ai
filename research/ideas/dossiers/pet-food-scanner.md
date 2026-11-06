# Pet Food Scanner ("Is this safe for my dog?")

## One-line pitch
Point your phone at a dog or cat food bag, a treat, or the human food your pet just grabbed, and get an instant safety and quality verdict personalised to your pet, plus a light daily care loop (meals, treats, weight, meds).

## Who exactly
Beachhead: US dog owners aged 25 to 40 who buy premium or "fresh" food, worry about ingredients (BHA/BHT, unnamed meat meals, grain-free debates) and already film their dogs. Secondary: new puppy and kitten owners in their first 90 days, who ask "can my dog eat X?" constantly.
Where they gather: r/dogs, r/cats, r/puppy101, dog TikTok and Instagram, breed Facebook groups. I could not fetch Reddit subscriber counts in this pass (Reddit blocked the about.json fetch), so community sizes are unverified here and should be checked before committing.

## Demand evidence
- Market size (verified, industry body): APPA reports US pet industry spend of $158B in 2025, with food and treats about $68.3B, and projects about $165B in 2026. APPA also found 22% of owners spent less on pets in 2025, which favours "value for money" framing.
- Supply-side signal: at least ten AI pet food scanners launched on iOS in 2025-2026 (PetScan Food AI, Kibble, Hapu, PetWise, Dog Food Scanner & Advisor, PawBite, Paws AI, Max, PetScans, PetsyDNA, Pawdi on Product Hunt). Many founders are betting on the same idea.
- Anecdotal user pull: a Reddit thread in r/Animals asks for an app to check pet food ingredient lists in store.
- Yuka (human food and cosmetics) proves the "scan and get a score" format at scale: 4.8 stars from 88.5K App Store reviews and 4.7 from 177K Google Play reviews; third-party trackers estimate roughly 2.4M installs a month (third-party estimate). Yuka has no pet mode in the results I found.

## Money proof
- Pet care trackers: 11pets Android about 754K installs, about 194K MAU, $10K+/month (AppGoblin, third-party estimate); 11pets iOS under $10K/month. Pet Care Tracker apps are mostly under $1K-$10K/month (AppGoblin, Adapty paywall library).
- Pet food scanners: Hapu (launched Aug 2025) has 19 ratings and about 206 MAU, under $10K/month (AppGoblin estimate). PetsyDNA claims 500K+ US owners (self-reported, no ratings shown on App Store). No scanner showed verified revenue on TrustMRR or meaningful AppGoblin estimates.
- Summary: owners spend heavily on pets, but no pet scanner app has shown that this converts to app subscriptions yet. Money swims in pet food, not (yet) in pet food apps.

## Competitor weaknesses
The scanner cohort is too young for review themes: most have under 20 ratings. Visible weaknesses from listings: (1) barcode-only apps (Max, Safe Pet Treats) fail on treats, bulk and imported products; Safe Pet Treats has not been updated since January 2021. (2) Most score the bag once and offer no reason to return. (3) Scoring rules are opaque, with no vet sourcing shown. (4) None leads with the emergency moment ("my dog just ate grapes"). Pet care trackers (11pets) are form-heavy logs with no aha.

## The wedge
Lead with the panic moment, not the kibble audit: "Snap what your pet ate" gives a toxicity verdict in seconds (grapes, xylitol gum, onion, chocolate dose by weight) with a clear "call your vet / poison line now" escalation. Then the same camera grades the food bag against your pet's profile (age, breed, weight, allergies). The repeat loop is treats and meals, not the bag: log treats with a photo, track daily treat calories against the 10% guideline, and show a weekly "diet score". Personal pet character (your dog's photo as the avatar) gives the emotional stake the playbook says points alone lack.

## The 2-second clip
Hand holds a chocolate chip cookie next to a beagle. Phone snaps. Screen flashes red: "TOXIC for Biscuit (11 kg): chocolate. Call your vet." Cut to a kibble bag: green ring "82/100, named chicken first ingredient". Second format: "Rating my dog's food" series, owners scanning famous brands with reaction faces.

## Core loop sketch
- Onboarding aha: add pet name, photo, breed, weight (4 questions that visibly pay back in the verdict wording), then scan the food you have at home. First verdict inside 60 seconds.
- Daily action: photo-log treats and meals; one-tap walk and med check.
- Streak/reward: "healthy treat days" streak with two freezes; the pet avatar looks happier as the week score rises.
- Shareable artifact: "Biscuit's Food Report Card" with grade, brand, pet photo, watermark; "my dog's food got a C" is natural comment bait.
- Paywall: soft. Toxicity checks free forever (trust and press); food grading, multi-pet, treat budget and alternatives behind Pro after the first full scan. Price $4.99/week or $29.99 to $39.99/year with 3-day trial. Affiliate links to better-scored foods (Chewy) as a second revenue stream, disclosed.

## Risks
- Veterinary advice: wrong "safe" verdict on a toxin is a real harm and a liability; needs conservative defaults, sourced lists (ASPCA poison control style), clear disclaimers.
- Brand defamation risk from low scores of named brands; scoring method must be published.
- Saturation: about ten look-alike scanners launched in 12 months, all with negligible traction, which suggests either distribution is the bottleneck or willingness to pay is low.
- Retention: food changes every few months, so without the treat/meal loop this is a one-scan app.
- Platform: App Store "AI wrapper" scrutiny is low risk here.

## Scores
| Criterion | 1-5 | Why |
|---|---|---|
| Two-second aha | 5 | Snap a cookie, red TOXIC screen; Yuka proved the format |
| Visual short-video hook | 5 | Pets plus reaction plus "rating my dog's food" series |
| Money already swims | 3 | $68.3B food spend (APPA), but pet apps earn little: 11pets $10K+/mo, scanners near zero (AppGoblin) |
| Daily reason to return | 2 | Bag scans are rare; treat logging is plausible but unproven |
| Shareable moment | 4 | Report card with the pet's face is very shareable |
| Unit economics | 3 | Pet niche CPI is moderate; weak retention caps LTV; affiliate helps |
| **Total** | **22/30** | |

## Verdict
Maybe. The hook and demo are excellent, but the crowded, tractionless 2025-2026 scanner field says the scan alone does not pay. Build only if the emergency "my pet ate this" angle plus a treat-budget habit gives a reason to return, and test with organic TikTok content before heavy build.

## Sources
- https://americanpetproducts.org/news/u.s.-pet-industry-reaches-158-billion-in-2025-poised-for-continued-growth-in-2026
- https://www.petfoodindustry.com/regions/us-and-canada/news/15820734/us-pet-food-industry-returned-to-real-growth-in-2025
- https://appgoblin.info/apps/1092799236
- https://apps.apple.com/us/app/petscan-food-ai/id6761618711
- https://apps.apple.com/us/app/kibble-pet-food-scanner/id6761734073
- https://apps.apple.com/us/app/hapu-cat-dog-food-scanner/id6748929220
- https://appgoblin.info/apps/6748929220
- https://apps.apple.com/us/app/petsydna-ai-dog-assistant/id6749225257
- https://apps.apple.com/us/app/safe-pet-treats/id1023344412
- https://pawsfood.app/
- https://www.maxpet.app/
- https://appgoblin.info/apps/com.m11pets.elevenpets
- https://appgoblin.info/apps/1232470530
- https://adapty.io/paywall-library/pet-care-tracker-dog-cat-log/
- https://reddit.birdcat.cafe/r/Animals/comments/1kx888l/app_for_checking_ingredients_lists
