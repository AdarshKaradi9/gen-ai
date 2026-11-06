# How to make vibe coding not suck…
- URL: https://www.youtube.com/watch?v=PLKrSVuT-Dg | Channel: Fireship | Views: 961581 | Length: 344s
- Sources used: https://rosetta.to/u/fireship/how-to-make-vibe-coding-not-suck (caption-generated full transcript plus Q&A summary)
- Confidence: high (full caption transcript read; single source but complete)

## Core claims (3-7 bullets, what the video argues)
- AI coding "does suck" in a specific way: it is like gambling — a dopamine rush when a prompt works, then the "prompt treadmill of hell" where you keep burning credits without getting what you need.
- The way to make AI coding "more reliable and quasi deterministic" is Model Context Protocol (MCP) servers: "a standardized way for your coding agent to talk to external systems" (local app, remote server, or third-party API).
- "If you don't already have a couple of MCP servers hooked up to Claude Code, Cursor, OpenCode, or whatever you prefer, you're falling behind."
- Most programmers now use AI, but very few use it to its full potential; the gap is in grounding the model with real docs, data, and tooling rather than prompting harder.
- The video is a Code Report episode dated October 14, 2025, listing seven MCP servers every dev should know.

## Specific tactics (concrete, actionable; include numbers, prices, timings, exact UI choices)
- Svelte MCP server: install in Claude Code, start prompts with `/svelte` so Claude fetches the correct Svelte 5 docs and runs the Svelte autofixer (static analysis that removes hallucinated React code).
- Figma MCP server: connect the local desktop or cloud Figma app; pull a design file and auto-implement it in HTML/CSS, React components, Tailwind, or iOS UI elements.
- Stripe (and other API) MCP servers: fetch documentation for the exact API version in use plus tools to act on live data — with the warning that this opens the door to "accidentally refunding 10,000 customers with a single prompt."
- Sentry MCP server: after deploy, tell the assistant to "query the Sentry issues and fix them on the fly" instead of reading the errors yourself.
- Atlassian / GitHub MCP servers: pull Jira tickets and GitHub issues automatically; prompt the AI to fix the issue and close the ticket.
- Cloud MCP servers (AWS, Cloudflare, Vercel): let the AI provision cloud resources; in theory a robot won't forget to shut down an EC2 instance, "but don't quote me on that."
- Build your own MCP server for custom data sources or smart-home control; there is "an MCP framework for every major programming language."
- Sponsor segment: deploy on Sevalla (Heroku successor on GKE + Cloudflare), $50 free credits, with preview/staging/production pipelines.

## Named examples (apps/companies cited and what they did)
- Coding Garden (streamer) — cited as having "completely destroyed the grift" by showing AI coding is "not fun at all."
- Nvidia — Jensen Huang clip: "Every one of our engineers 100% is now assisted by AI coders and our productivity has gone up incredibly."
- Tools named: Claude Code, Cursor, OpenCode; Svelte MCP, Figma MCP, Stripe MCP, Sentry MCP, Atlassian MCP, GitHub MCP, AWS/Cloudflare/Vercel MCPs; Sevalla (sponsor).

## Numbers & evidence (any stats, revenue, conversion rates, retention figures; mark self-reported vs third-party)
- Opening anecdote (satirical, self-reported): found a $10 app that solved the problem, instead spent 3 days and $500 in Claude credits and missed his kids' baseball game to build "a crappier version from scratch."
- Date stamp: October 14, 2025.
- No retention/conversion data; the video is a tooling roundup.

## Contradictions or caveats (where this disagrees with common advice or other videos)
- Opposes the "just prompt better" school of vibe coding: argues reliability comes from external grounding (MCP), not prompt craft.
- Acknowledges both camps: some devs are "becoming less productive and ditching AI altogether" while others see "productivity gains like never before."
- Warns that MCP tools with live write access (Stripe, cloud provisioning) create real financial risk; all third-party servers require trusting the vendor ("you have to trust us").
- Framing is comedic/hyperbolic ("you're not going to make it"), so the "falling behind" claim is opinion rather than evidence.

## Memorable framings (quotable one-liners or named frameworks, verbatim if available)
- "The prompt treadmill of hell where you keep burning through credits but never actually get what you need."
- "The truth is that AI does suck. It's like gambling."
- "A model context protocol server... in one sentence, it's a standardized way for your coding agent to talk to external systems."
- "Opening the door to all sorts of possibilities, like accidentally refunding 10,000 customers with a single prompt."
- "Instead of trying to understand the slop you rolled out a few minutes ago, you just tell it to query the Sentry issues and fix them on the fly."
- "Vibe engineer" (self-mocking title).
