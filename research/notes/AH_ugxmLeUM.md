# 7 UI/UX mistakes that SCREAM you’re a beginner
- URL: https://www.youtube.com/watch?v=AH_ugxmLeUM | Channel: Kole Jain | Views: 494705 | Length: 437s
- Sources used: https://sozai.app/transcript/ui-ux-mistakes-beginner (full transcript plus key takeaways); https://recapio.com/digest/7-ui-ux-mistakes-that-scream-youre-a-beginner-by-kole-jain (page found but content did not render)
- Confidence: high (full transcript read)

## Core claims (3-7 bullets, what the video argues)
- Beginner designs are recognizable by seven recurring mistakes; the video fixes each one on a recipe-app redesign, before/after.
- 1 Poor user flow (missing search, skip, nav links, hidden states) "quietly ruins your UX."
- 2 Overused effects (gradients, glows, harsh shadows) read as amateur; "less visual noise equals a better design."
- 3 Cramped spacing; fix with grids and auto layout, and more vertical space than you think on mobile.
- 4 Inconsistent components (mixed corner radii, mismatched back/skip buttons) are easy to fix and "kill" polish.
- 5 Bad icons: missing on cards, mismatched fill/stroke, unlabeled; good icons speed browsing.
- 6 Redundant elements (arrows where swipe exists, unnecessary strokes) are clutter.
- 7 Missing interactive feedback makes an interface feel unresponsive; bonus 8: over-designed charts are unreadable.

## Specific tactics (concrete, actionable; include numbers, prices, timings, exact UI choices)
- Onboarding allergy screen: six preset options need a search bar for "anything else" and a Skip button for users with no allergies; sketch flows as boxes on paper to catch gaps; add small touches like a filter icon on the search bar and a Save button up top.
- Gradients: if you must, use variations of the same hue (darker/lighter green), not blue-to-green; usually remove entirely.
- Shadows: Figma defaults are too harsh; instead of lowering opacity, change the shadow color to light gray and increase blur significantly, or remove.
- Spacing: set a 3-column grid on one screen and a 2-column grid on another; align closely but allow balanced grid breaks; increase vertical spacing on stacked content; use Figma auto layout with vertical trim off for pixel-perfect spacing on cards and chips.
- Consistency: make the two search bars identical except placeholder text; set corner radius of all smaller components to 10px; match Skip and Back buttons in size, radius, and style; use color styles, measurement variables, and components.
- Icons: add icons to cards and replace "Save" text with an icon; use one library (Flaticon interface icons sorted by stroke width and corner; or Phosphor / Feather Figma plugins); download SVG; label unfamiliar icons or add tooltip pop-ups during onboarding; house/bookmark/user icons need no labels; different icon styles are fine if visually separated by area (nav vs food vs recipe icons).
- Redundancy: remove arrows where swipe is available; dim button color; remove strokes on elements or dim them for contrast compliance.
- Feedback: gray out a button on tap while the next screen loads; add a loading wheel for long waits; on Save, fill the icon and add a red dot badge on the Save tab so the user knows a recipe was added.
- Charts: avoid Dribbble-style charts with no vertical axis, rounded bar tops (unclear endpoint), and 16 bars for 7 days; simple charts "convey so much more useful information."

## Named examples (apps/companies cited and what they did)
- A recipe app (the author's own redesign subject, with allergy onboarding, save tab, cards, chips).
- Figma (auto layout, defaults, plugins), Flaticon, Phosphor Icons, Feather Icons, Dribbble (source of the unreadable chart).
- Kole Jain's separate video on interactive feedback and micro-interactions.

## Numbers & evidence (any stats, revenue, conversion rates, retention figures; mark self-reported vs third-party)
- Design constants only: 10px corner radius for small components; 3-column and 2-column grids; 16 bars vs 7 days chart example.
- Self-reported: "I've spent years making bad designs."
- No user metrics; practitioner heuristics.

## Contradictions or caveats (where this disagrees with common advice or other videos)
- Against the "stuff everywhere" trend and against Dribbble aesthetics: readability beats aesthetics in charts.
- Allows breaking the grid when balanced, unlike strict grid advice.
- Says mixing icon styles is acceptable when visually separated, contrary to the usual "one icon set only" rule.
- Covers onboarding only as flow completeness (search, skip, tooltips), not conversion or paywall design.

## Memorable framings (quotable one-liners or named frameworks, verbatim if available)
- "Let's start with something that quietly ruins your UX: user flow."
- "These are things you will miss if you don't plan out your flow, but users, they'll feel it instantly."
- "Most of the time, less visual noise equals a better design."
- "Especially on mobile screens, you'll need more space than you think."
- "Which one do you think I got from Dribbble?"
- "Just try not to have bizarre icons everywhere."
