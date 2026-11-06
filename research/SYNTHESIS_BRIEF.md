# Synthesis brief (read fully before writing)

You are writing ONE chapter of a research document titled "What Makes Apps Spread, Stick, and Sell: a synthesis of 120 YouTube videos on viral apps, onboarding, gamification, hooks, retention and monetization".

Inputs:
- All per-video notes are in /tmp/claude-0/-home-user-gen-ai/6504a663-f93f-59d7-b0af-1cc144734ade/scratchpad/research/notes/<id>.md (one file per video; header has title, URL, channel, sources, confidence).
- /tmp/claude-0/-home-user-gen-ai/6504a663-f93f-59d7-b0af-1cc144734ade/scratchpad/research/INDEX.md lists every note with its theme and confidence.
- Read EVERY note file (grep across all of them for your chapter's keywords first, then read the relevant ones in full; many videos touch several chapters, so do not limit yourself to one theme tag).

Writing rules:
- Write for a solo founder who is building a consumer habit app. Plain, confident prose. Short paragraphs. No em-dashes. No hype.
- Organize the chapter as NAMED PATTERNS (give each pattern a memorable 2-5 word name of your own, e.g. "The 3-Second Aha", "Weekly Is The New Monthly"). For each pattern: what it is, why it works, concrete examples with numbers from the notes, how to apply it, and caveats or counter-evidence.
- Every factual claim or number must carry an inline citation in this exact form: [vid:<video id>]. Multiple ids allowed: [vid:abc123][vid:def456]. Use ONLY ids that exist in the notes directory.
- Mark self-reported founder numbers as self-reported. Prefer results-backed claims (A/B tests, studies of many apps, platform data) over opinion, and say which is which.
- Include a short "Where sources disagree" section at the end of the chapter if there are real contradictions.
- End with a "Checklist" of 6-12 one-line actions a founder can take, each with a citation.
- Length: 1,500 to 3,000 words. Markdown. Start with "## <Chapter title>" as the first line. Do not write an introduction to the whole document, only this chapter.
- Never invent examples, numbers or quotes that are not in the notes. If the notes are thin on something, say so.

Output: write your chapter to the file path given in your task. Then reply with a 5-line summary of the patterns you named.
