# AI Engineering Full Course - Build and Deploy a Real AI App
- URL: https://www.youtube.com/watch?v=XzjSx7u9mGw | Channel: Dave Ebbelaar | Views: 93224 | Length: 11407s (3h10m)
- Sources used: https://learn.datalumina.com/docs/customer-support-automation (the official written companion guide to this video, intro page); https://learn.datalumina.com/ (course index describing the build); https://academy.datalumina.com/ (Ebbelaar/Datalumina background and paid programs); YouTube listing (alt title "Full-Stack AI Engineering Course (FastAPI, LLMs, Docker, Supabase)") via search snippets
- Confidence: medium (the creator's own written guide for the exact project was read, but only its overview page, not every lesson; no transcript)

## Core claims (3-7 bullets, what the video argues)
- Shows an end-to-end "full-stack GenAI project, from an empty folder to a deployed system with a dashboard": an AI customer-support agent for an e-commerce company that reads a Gmail inbox, answers from a knowledge base, or escalates to a human.
- Design philosophy: "The model proposes, code decides." A small model classifies, a larger model drafts with tools, and plain Python makes the final call; guards in code stop the bot from replying to itself.
- Customer support is a good first AI project because "the work is repetitive, the rules are written down, and you can check every reply."
- Evals are part of the build, not an afterthought: a golden set of emails checks every decision.
- Keep infrastructure deliberately simple: polling instead of webhooks/queues/workflow engines, no open web port, nothing reachable except SSH from your own IP.
- Not a beginner course: assumes Python and command-line comfort; a coding agent (Cursor, Claude Code, Codex) is used as a helper, but the build is copy-paste from the guide.

## Specific tactics (concrete, actionable; include numbers, prices, timings, exact UI choices)
- Stack: Python 3.13 + uv, FastAPI, Gmail API via OAuth 2.0, Supabase (free plan) for events/tickets/messages/knowledge base, Anthropic models via Pydantic AI with structured output and tools, Docker Compose on a Hostinger VPS (KVM 1 sufficient since DB is on Supabase; KVM 2 for headroom), firewall + SSH hardening, small React dashboard opened through an SSH tunnel; Node 22+, Git, GitHub.
- Architecture: a poller requests new mail from Gmail on a fixed interval and labels what it handled; every email and event is saved to Supabase; two-model pipeline (small classifier, larger drafter with knowledge-base tools).
- Fictional company for the demo: "Harbor & Pine," an Amazon home/outdoor seller; two best-sellers generate most tickets: inflatable paddle boards (10'6", 11', 12'6" sized by rider weight) and flat-pack shelving (3-shelf, 5-shelf, cube 2x2, cube 3x3, four finishes). Typical emails: "Which size for 90 kg?", "It loses air.", "Panel 4 is cracked.", "Screws are missing."
- Guide conventions: every step names a file and gives full code; "Replace" = overwrite whole file; every page ends with a check you must pass before moving on.
- Safety: use a brand-new Gmail account for the demo, never a personal inbox.
- Sponsor tie-in: Hostinger VPS, code DAVEVPS for 10% off on a first yearly plan.
- Last page covers what a production version adds (webhooks, queues, etc.).

## Named examples (apps/companies cited and what they did)
- Harbor & Pine (fictional e-commerce client used throughout).
- Datalumina (Ebbelaar's company; "50+ custom B2B solutions," consulting for TimescaleDB, ClickUp, n8n per academy page).
- Tools: Gmail, Supabase, Anthropic/Claude, Pydantic AI, FastAPI, uv, Docker Compose, Hostinger, React, Cursor/Claude Code/Codex.
- Related free builds on the same site: Document copilot (RAG Q&A with FastAPI/React/Supabase/Pydantic AI), Invoice review on Azure, Automation backend.

## Numbers & evidence (any stats, revenue, conversion rates, retention figures; mark self-reported vs third-party)
- 3h10m video; course is free with no signup (Datalumina).
- Hostinger KVM 1 is enough; 10% discount code (sponsor terms).
- Ebbelaar background claims: a decade in AI, 50+ B2B solutions delivered (self-reported).
- No performance/accuracy metrics for the agent were published on the pages read.

## Contradictions or caveats (where this disagrees with common advice or other videos)
- Rejects the common "use n8n/Zapier/LangChain/workflow engine" advice for a first agent; argues for a plain Python backend with polling and explicit guards.
- Rejects letting the LLM make final decisions; code owns the decision after the model proposes.
- Video is made "in collaboration with Hostinger," so the VPS choice is sponsored.
- Not a retention/monetization video; relevant to this research mainly as the "build a real AI app" reference.

## Memorable framings (quotable one-liners or named frameworks, verbatim if available)
- "The model proposes, code decides."
- "Kept simple on purpose."
- "From an empty folder to a deployed system with a dashboard."
- "The work is repetitive, the rules are written down, and you can check every reply."
