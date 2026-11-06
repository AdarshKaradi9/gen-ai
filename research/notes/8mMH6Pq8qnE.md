# How I Make Apps FEEL 10x Better (5 Design Secrets)
- URL: https://www.youtube.com/watch?v=8mMH6Pq8qnE | Channel: Chris Raroque | Views: 240580 | Length: 699s (~12 min)
- Sources used: https://youtubeds.com/@raroque/how-i-make-apps-feel-10x-better-5-design-secrets (full auto-transcript); https://lilys.ai/en/notes/lilysai-20260813/10x-better-app-design-secrets (structured notes of the video); https://podwise.ai/episodes/6187655 (summary of the related Greg Isenberg episode, context only)
- Confidence: high (full transcript read)

## Core claims (3-7 bullets, what the video argues)
- Chris builds productivity apps (Mogul, Ellie, Luna, Lily) and gets compliments that they "feel different, more polished, more fun"; the feel comes from many small details, not one big thing.
- Five secrets: (1) animation and interaction, (2) custom illustrations especially for empty states, (3) haptic feedback, (4) deliberate icon style and consistency, (5) constant exposure to good design to build taste.
- Default Apple apps are static and sparing (serving a billion users, accessibility/motion-sickness reasons); indie apps are "not Apple" and can go further.
- AI coding tools (Claude Code) make complex animation cheap if you break the interaction into sub-steps instead of one-shotting it.

## Specific tactics (concrete, actionable; include numbers, prices, timings, exact UI choices)
- Animate tab/page changes: in Luna (budgeting app) pages slide over from the previous page rather than appearing instantly. Took him ~5 days pre-AI; "now with Claude Code ... less than an hour."
- Ellie dictation sequence: send button rotates into a checkmark, background expands outward from the microphone, "listening" text fades with a spring animation. Fully "vibe coded" with Claude Code without writing code. Prompt tip: do not ask "animate this"; ask for each sub-animation separately ("make the arrow rotate into the check mark", "have the background expand from the microphone", "add fade in/out for the text"). Apple's animation API is well represented in AI training data.
- "If you do this 100 times throughout your app, it's going to add up to this very premium experience."
- Empty states: replace "no tasks for today" text with a custom illustration or animation. Lily (meeting assistant) has a ghost mascot; feed the base mascot to ChatGPT to generate infinite variants (Lily searching for tasks on the search page, taking notes during a live meeting, sleeping, drinking coffee, walking his dog). Commission an artist for the base illustration if possible; otherwise generate with diverse reference images and tweaked prompts for uniqueness. Next step: animate illustrations with Rive.
- Haptics: Apple default apps rarely use them; control vibration strength in code - light haptic for frequent actions (entering a transaction in Luna), heavier for significant ones (changing tabs). Correct, well-placed haptics feel "addictive, like clicking a pen"; wrong ones make the app worse.
- Icons: avoid default SF Symbols look; use a pack (Hero Icons mentioned as clean and free) and pick one style - thin/minimal, filled/heavy, or complex - and never mix. Use style to show state: Luna's tab bar shows thin icons, switching to the heavier filled version when selected, rather than only changing colour (the Apple Phone app only changes colour).
- Taste: follow designers on Twitter/X and bookmark; browse Mobbin (sponsor; thousands of app screenshots) a few minutes a day or even once a week, and search specific components like "tab bar" to choose an aesthetic.

## Named examples (apps/companies cited and what they did)
- Luna (budgeting): animated tab transitions, thin icons with filled selected state, light haptics on transactions.
- Ellie (planner with AI assistant): custom dictation animation sequence.
- Lily (meeting assistant): ghost mascot used across empty states.
- Mogul (listed in description). Apple default apps (Phone app) as the baseline. Tools: Claude Code, ChatGPT, Rive, Hero Icons, SF Symbols, Mobbin, Twitter/X.

## Numbers & evidence (any stats, revenue, conversion rates, retention figures; mark self-reported vs third-party)
- "5 days" to build the Luna page animation pre-AI vs "less than an hour" now (self-reported).
- "100 times" small interactions compound (heuristic). No retention or revenue data in this video.

## Contradictions or caveats (where this disagrees with common advice or other videos)
- Encourages more motion and haptics than Apple's HIG defaults; the transcript acknowledges Apple's restraint may be for accessibility/motion sickness, and viewers in comments reportedly warn against too many animations.
- Mobbin recommendation is sponsored (disclosed in the video).
- This is a "feel"/polish video with no acquisition or monetisation claims - polish is framed as differentiation, not as a measured conversion lever.

## Memorable framings (quotable one-liners or named frameworks, verbatim if available)
- "We're not Apple."
- "It's not one big thing. It's actually a bunch of small things that when you put them together really do add up."
- "Don't try to one-shot this ... break it down into steps."
- "If I can make something like a finance app feel fun to use, you can definitely do it for your own app, too."
