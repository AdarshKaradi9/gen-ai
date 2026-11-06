# Watch Me Vibe Code an Animated App with Claude Opus 5.5 (It's Super Smooth)
- URL: https://www.youtube.com/watch?v=Rk6t9Uq1y9M | Channel: Jason Lee | Views: 328690 | Length: 1256s (~21 min)
- Sources used: https://www.ai.joaoqueiros.com/blog/claude-opus-5-5-animated-app-waterllama-mobbin-higgsfield-expo (detailed third-party write-up with a timestamped segment table; the creator's own prompt pack at "The Breadcrumb" is email-gated and was not read)
- Confidence: medium (one detailed, timestamped third-party summary; no transcript; Jason's exact prompts not reproduced anywhere public)

## Core claims (3-7 bullets, what the video argues)
- A three-pass build loop is the way to vibe-code a polished animated consumer app: (1) get the functional skeleton working, (2) replace the character motions that look stiff, (3) add a separate on-device interactive scene (phone tilt).
- The key lesson is division of labor across media: code for anything that must respond instantly to input (water level, slider, bubbles, buttons), generated video (Higgsfield) for expressive character actions (sipping, leaping, swimming), and a static SVG character inside a code-animated scene where the figure itself does not need complex body motion.
- Reference apps should be mapped as a set of states and interactions (onboarding, home, paywall) before prompting, using Mobbin's screen library/MCP plus a real screen recording of the original app, rather than a single screenshot.
- Feedback to the agent works best as a narrated screen recording pointing at concrete failures, not a vague list of complaints.
- The demo is a prototype workflow, not a shipped product: the trial paywall is explicitly a mockup, and no retention, conversion or performance numbers are shown.

## Specific tactics (concrete, actionable; include numbers, prices, timings, exact UI choices)
- Reference app: Waterllama (one-purpose hydration tracker with a daily target, beverage logging, characters and progress feedback). Jason names his clone "Brownie" and swaps the llama for a capybara mascot taken from a Pinterest image.
- Research step (02:20): inspect Waterllama's onboarding, home and paywall screens via Mobbin's screen library and Mobbin MCP (available on Mobbin Pro/Team plans, per the write-up), then record the real app on a phone so the agent can see how it responds to taps.
- First build prompt scope (06:26): onboarding + home screen with code-made motion. Result: working drink picker, volume slider, water level that rises, bubbles, settings, onboarding. Failures observed: cannot swipe to more drinks, some challenge controls are placeholders, jumping/swimming capybara is stiff, one water animation glitches, paywall is a mockup.
- Motion repair (10:33): ask Claude to call Higgsfield for sipping, leaping and swimming clips (Seedance 2.5 for video-from-reference, "Genjutsu" presented as motion transfer); request a green background so the character can be keyed out for compositing in the app. Jason reports different Higgsfield credit amounts per clip (demo-account observations, not a stable per-app price).
- Revision method: record the prototype while speaking and pointing at problems (untouched buttons should invite a tap, kill the water glitch, remove a capybara icon, make the drink row swipeable), hand Claude the recording path, ask it to integrate the new character clips. Second build (15:25): leaping/swimming smoother, glitch gone, swipe reveals more drinks.
- Tilt scene (16:22): a separate Expo React Native screen. Inputs given to Claude: an SVG character, a pool reference image, layout instructions, desired touch and tilt behavior. Code positions the float, draws water and ripples, responds to finger and phone motion (Expo DeviceMotion). Tested on a real phone via Expo Go using the dev-server QR code.
- Write-up's production caveats for the tilt screen: ask for motion permission in context, fall back to touch when the sensor is unavailable or denied, respect reduced-motion preferences.

## Named examples (apps/companies cited and what they did)
- Waterllama: the reference hydration app (custom drinks, hydration ratios, daily target, characters). Jason repeats an approximately $100,000/month revenue claim for it in the video (not independently verified by the write-up).
- Mobbin / Mobbin MCP: used to pull onboarding, home and paywall reference screens into the agent's context.
- Higgsfield (Seedance 2.5, Genjutsu motion transfer): generated the character video clips.
- Expo / Expo Go / Expo DeviceMotion: the tilt-responsive native scene.
- Gamma: sponsor segment at 05:09.
- Claude Opus 5.5: the coding agent; the write-up notes Jason does not run a controlled comparison against other models.

## Numbers & evidence (any stats, revenue, conversion rates, retention figures; mark self-reported vs third-party)
- Waterllama ~$100K/month revenue: repeated by Jason in the video, unverified (third-party write-up explicitly flags it).
- Video segment timestamps (from the write-up): 00:00 intro, 00:47 app and reference, 02:20 structure and Mobbin, 05:09 Gamma sponsor, 06:26 first build, 10:33 improving character motion, 15:25 second build, 16:22 phone-tilt scene.
- No conversion, retention or performance measurements are presented; the paywall processes no money.

## Contradictions or caveats (where this disagrees with common advice or other videos)
- Unlike "one prompt, whole app" vibe-coding demos, the video shows that code-only character animation looked "puppet-like" and needed a separate video-generation tool; the win comes from assigning jobs to the right medium, not from the model alone.
- Copying another app's character (Pinterest image) and screen flow is fine for a private learning exercise but a commercial app needs original or licensed art, copy and motion (write-up's caveat).
- Generated video clips introduce compositing, looping, file-size, load-time and rights checks that the video does not measure.
- The write-up stresses this proves nothing about Opus 5.5 vs other models and nothing about a hydration business; account persistence, accessibility, offline behavior, store approval and device performance are all out of scope.

## Memorable framings (quotable one-liners or named frameworks, verbatim if available)
- Three-pass build: "make the hydration tracker work, replace the character motions that look stiff, then build a phone-tilt scene" (write-up's summary of the structure).
- "Give code and generated video different jobs" (section heading in the write-up describing Jason's approach).
- "Turn a screen recording into a precise revision" (the narrated-recording feedback loop).
- Missing: Jason's verbatim prompts (gated behind an email signup at The Breadcrumb) and any direct quotes from the video.
