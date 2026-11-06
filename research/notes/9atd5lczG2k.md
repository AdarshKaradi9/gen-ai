# How I Vibe Coded a Recipe App using Claude Code (Full Build + Marketing)
- URL: https://www.youtube.com/watch?v=9atd5lczG2k | Channel: Jason Lee | Views: 165310 | Length: 2011s
- Sources used: https://videohighlight.com/v/9atd5lczG2k (sectioned summary); https://youtubesummary.com/summary/9atd5lczG2k (structured summary with tool/stack list). Both are AI summaries that render the app name as "ResuMe"; the video description says ReciMe.
- Confidence: medium (two detailed summaries, no transcript)

## Core claims (3-7 bullets, what the video argues)
- ReciMe (a recipe-organizer app) makes ~$800k/month; the idea is validated, so clone-and-niche rather than invent.
- Recipe libraries are "sticky": the more recipes a user saves, the higher the switching cost, which reduces churn and supports subscription revenue.
- The full app can be built with no coding via Claude Design (UI) + Claude Code (backend/wiring), React Native/Expo, OpenAI API.
- Marketing matters more than building; the playbook is TikTok UGC at volume, then scale winners with ads.
- Apps like this sell for 2-4x annual profit (acquire.com, Flippa, "Trust MRR" cited), so there is exit value.

## Specific tactics (concrete, actionable; include numbers, prices, timings, exact UI choices)
- Feature set copied from ReciMe: universal import (paste a URL incl. YouTube -> AI extracts ingredients/instructions), scan a physical/handwritten recipe photo -> structured recipe card, manual entry, library, cook mode with timers, shopping list, calorie estimate (modeled on "Calorie AI"/Cal AI), "Make it healthier" button (heavy cream -> Greek yogurt, spaghetti -> whole grain).
- Build workflow: Claude Code desktop app ($20/month plan minimum); use Opus 4.7 for planning, switch to Sonnet 4.6 for execution to save tokens; prompt Claude with the competitor's App Store URL to generate feature list and page structure; generate hi-fi UI in Claude Design using a Pinterest reference screenshot and global "theme tweaks" for palette; export zip into project; have Claude Code build with Expo React Native + TypeScript; preview on phone via Expo Go QR code; click-to-edit annotations (e.g., progress bar color to green).
- AI cost: GPT-5.4 Mini at ~half a cent per image scan, ~100 scans for $1; pay-as-you-go credits at platform.openai.com; key stored in .env and proxied through a small Node/Express backend so users can't drain it.
- Production stack: Supabase for recipes/settings, RevenueCat for subscriptions, Apple developer account ~$99/year; an 18-item App Store rejection checklist is referenced (vibe-coded apps get rejected for missing reliability/security layers).
- Marketing: check competitors' TikTok (ReciMe posts UGC "hack" videos); three options: (1) run your own TikTok posting UGC-style videos (slow, organic), (2) pay UGC creators a one-time fee for content that keeps driving traffic, (3) AI UGC avatar tools (named as "ArKads"/"Hixfil" in summaries) to run multiple persona accounts at high volume, then put ad spend behind whatever goes viral. Principle: many videos -> find winners -> scale spend.

## Named examples (apps/companies cited and what they did)
- ReciMe: ~$800k/month recipe organizer (claimed; per Cravotta's video in this corpus Sensor Tower-type estimates put it at ~$500k/month and 300k downloads/month).
- Cookpad: niche example, Japan-focused, ~$900k/month (claimed).
- Cal AI / "Calorie AI": calorie-estimate feature inspiration.
- Tools: Claude Code, Claude Design, OpenAI API, Expo Go, Supabase, RevenueCat, acquire.com, Flippa.

## Numbers & evidence (any stats, revenue, conversion rates, retention figures; mark self-reported vs third-party)
- ReciMe $800k/month, Cookpad $900k/month: creator's claims, source not stated (likely Sensor Tower/AppFigures estimates).
- Exit multiples 2-4x annual profit (creator's claim citing marketplaces).
- OpenAI cost ~$0.005 per scan (creator's estimate).
- Apple dev account $99/yr; Claude plan $20/mo (third-party list prices).
- No downloads, revenue or conversion data for the creator's own clone.

## Contradictions or caveats (where this disagrees with common advice or other videos)
- Encourages cloning a top app; counters with "don't only clone, niche down" (Cookpad/Japan).
- Early build stores data on-device only; summaries note the edit-recipe flow didn't fully save in the demo.
- The AI-persona UGC approach (multiple fake accounts) is presented as a tactic without discussing platform policy risk.
- Summaries garble names (ResuMe/Cloud Code/Superbase); treat tool names as approximate.

## Memorable framings (quotable one-liners or named frameworks, verbatim if available)
- "Sticky" retention via accumulated recipe collections / switching costs (summary wording).
- "Generate many videos -> identify what works -> scale spend" (summary wording of the marketing loop).
