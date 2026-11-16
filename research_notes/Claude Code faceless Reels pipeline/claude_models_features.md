# Claude models, Claude Code plans/limits, automation features, and free LLM alternatives (as of 2026-11-16)

Scope: which Claude model to use for each task in an automated short-video (faceless Reels) pipeline; how subscription plans and usage limits apply to Claude Code; which Claude Code features automate repeated steps; and free LLM alternatives for repetitive scripting. Primary sources are Anthropic docs (platform.claude.com, code.claude.com, support.claude.com, claude.com/pricing, anthropic.com announcements), fetched 2026-11-16. Third-party sources are labelled as such.

## Q1. Model comparison: Claude Fable 5.2, Opus 5.5, Sonnet 5.5, Haiku 5.5

### Takeaway
The four current models all have a 1M-token context window and 128K max output (sync API). They differ mainly in price and speed: Fable 5.2 costs $8/$40 per million input/output tokens, Opus 5.5 $4/$20, Sonnet 5.5 $2/$10 and Haiku 5.5 from $0.10/$0.50. Anthropic's own guidance is to start with Opus 5.5 for most work. Use Fable 5.2 only for the hardest long-horizon work. Use Sonnet 5.5 for well-scoped everyday tasks and Haiku 5.5 for high-volume, narrow tasks such as summarizing, classifying, and acting as a subagent.

### Cited Findings

**Lineup table (official)**
- Official comparison (Fable 5.2 / Opus 5.5 / Sonnet 5.5 / Haiku 5.5) — [Models overview](https://platform.claude.com/docs/en/about-claude/models/overview):
  - Description: "For demanding reasoning and long-horizon agentic work" / "For long-running agentic coding and knowledge work" / "The best combination of speed and intelligence" / "For high-volume, latency-sensitive tasks such as classification, extraction, and routing".
  - Comparative latency: Moderate / Moderate / Fast / Fastest.
  - Price per MTok input/output: $8/$40, $4/$20, $2/$10, and "From $0.10 / From $0.50".
  - Thinking: Adaptive, always on (Fable 5.2, Opus 5.5); Adaptive (Sonnet 5.5, Haiku 5.5).
  - Default API effort: `high`, `medium`, `high`, `medium`.
  - Context window: 1M tokens for all four. Max output: 128K tokens for all four.
  - Reliable knowledge cutoff: Jun 2026 for all four.
  - Retirement no sooner than: Nov 9 2027, Sep 22 2027, Sep 28 2027, and Oct 7 2027 respectively.
- API model IDs are `claude-fable-5-2`, `claude-opus-5-5`, `claude-sonnet-5-5` and `claude-haiku-5-5`. Each ID is a pinned snapshot — [Models overview](https://platform.claude.com/docs/en/about-claude/models/overview).
- Anthropic's guidance: "If you're unsure which model to use, start with Claude Opus 5.5 for most workloads. Use Claude Fable 5.2 for demanding reasoning and long-horizon agentic work, or when your evals on Claude Opus 5.5 at higher effort still fall short." — [Models overview](https://platform.claude.com/docs/en/about-claude/models/overview)
- Discounts: Batch API requests are 50% off. Prompt-cache reads cost 10% of the base input price. Exceptions: 2.5% on Fable 5.2/5.1 and 5% on Opus 5.5 and Sonnet 5.5 — [Models overview](https://platform.claude.com/docs/en/about-claude/models/overview).
- On the Message Batches API, Opus 5.5, Sonnet 5.5 and Haiku 5.5 support up to 300k output tokens with the `output-300k-2026-03-24` beta header — [Models overview](https://platform.claude.com/docs/en/about-claude/models/overview).
- Haiku 5.5 tiered pricing: $0.10/$0.50 per MTok for prompts of 100K tokens or fewer, and $0.50/$2.50 above that. Cache reads are $0.01/MTok for prompts of 100K tokens or fewer — [claude.com/pricing (API tab)](https://claude.com/pricing); [Claude Haiku 5.5 announcement](https://www.anthropic.com/claude-haiku-5-5).

**Release dates (all 2026)**
- Opus 5.5: launched **September 22, 2026**, at $4/$20 (Opus 5 was $5/$25) — [Release notes](https://platform.claude.com/docs/en/release-notes/overview).
- Sonnet 5.5: launched **September 28, 2026** — [Release notes](https://platform.claude.com/docs/en/release-notes/overview).
- Haiku 5.5: launched **October 7, 2026**, described as "our most capable model tuned for high-volume and latency-sensitive work" — [Release notes](https://platform.claude.com/docs/en/release-notes/overview).
- Fable 5.2 (and the verified-orgs-only Mythos 5.2, which is the same model): launched **November 9, 2026** at $8/$40. Fable 5.1 was $10/$50 — [Release notes](https://platform.claude.com/docs/en/release-notes/overview); [Fable 5.2 announcement](https://www.anthropic.com/claude-fable-and-mythos-5-2).

**Opus 5.5 positioning and benchmarks**
- Anthropic says Opus 5.5 "performs at the level of Claude Fable 5.1 on most work and costs 40% less to run than Opus 5." Cache reads are $0.20/MTok, 60% less than Opus 5 — [Opus 5.5 announcement](https://www.anthropic.com/claude-opus-5-5).
- Anthropic-reported benchmarks. Columns are Opus 5.5 / Fable 5.1 / Opus 5 / GPT-6 Astra / GPT-5.6 Sol; scores are at max effort unless noted, and Terminal-Bench uses xhigh — [Opus 5.5 announcement](https://www.anthropic.com/claude-opus-5-5):
  - Terminal-Bench 4.0: 66.4% / 55.8% / 52.3% / 57.9% / 37.3%.
  - FrontierCode v1.1: 54.4% / 50.3% / 48.0% / 53.3% / 47.5%.
  - CursorBench 4.0: 57.8% / 51.8% / 46.6% / — / 41.7%.
  - GDPval-AA v2.1: 1846 / 1735 / 1708 / 1542 / 1588 Elo.
  - OSWorld 2.1 (partial credit): 81.8%.
  - Humanity's Last Exam (with tools): 67.7%.
- Internal inconsistency: the Opus 5.5 announcement text gives FrontierCode at default (medium) effort as 54.6%, while the table shows 54.4% — [Opus 5.5 announcement](https://www.anthropic.com/claude-opus-5-5).
- Third-party check: secondary coverage reports that Artificial Analysis measured Opus 5.5 at 59.6% on Terminal-Bench 4.0, against Anthropic's self-reported 66.4%. I did not verify this on the Artificial Analysis site — [mixed-news.com (third-party)](https://mixed-news.com/en/?p=32220).
- Writing quality: Anthropic says Opus 5.5's writing is "clearer and easier to follow", that it "puts the most important information up front", and that it "follows the writing rules you give" — [Opus 5.5 announcement](https://www.anthropic.com/claude-opus-5-5).
- Fast mode for Opus 5.5 is available in Claude Code and on the Claude Platform. It runs up to 2.5x faster at $8/$40 per MTok — [Opus 5.5 announcement](https://www.anthropic.com/claude-opus-5-5).

**Sonnet 5.5 positioning and benchmarks**
- Positioning: "runs 30%+ faster, and costs up to 30% less for most work" than Sonnet 5. It is "strongest at well-scoped everyday tasks, fixing bugs, and creating polished documents, slides, and spreadsheets." Its writing is clearer than the previous generation's — [Sonnet 5.5 announcement](https://www.anthropic.com/claude-sonnet-5-5).
- Benchmarks (Sonnet 5.5 vs Opus 5.5) — [Sonnet 5.5 announcement](https://www.anthropic.com/claude-sonnet-5-5):
  - Terminal-Bench 4.0: 70.6% vs 66.4%; Sonnet 5 scored 10.3%.
  - CursorBench 4.0: 55.5% vs 57.8%.
  - GDPval-AA: 1844 vs 1846.
  - OSWorld 2.1: 80.1% vs 81.8%.
  - FrontierCode: 52.1% (xhigh) vs 54.4%.
- Anthropic's own caveat: "Opus 5.5 remains clearly stronger at complex, open-ended work requiring sustained judgment." — [Sonnet 5.5 announcement](https://www.anthropic.com/claude-sonnet-5-5)
- Default effort is Medium in Claude Code and the Claude apps, but High on the Claude Platform API — [Sonnet 5.5 announcement](https://www.anthropic.com/claude-sonnet-5-5).
- Sonnet 5.5 cache reads were halved to $0.10/MTok at the Haiku 5.5 launch, which Anthropic says makes Sonnet 5.5 about 20% cheaper on most agentic work — [Haiku 5.5 announcement](https://www.anthropic.com/claude-haiku-5-5).

**Haiku 5.5 positioning and benchmarks**
- Positioning: "designed for high-volume, cost-sensitive tasks... summaries, compactions, database queries, and classification"; "pairs well with Opus 5.5 and Sonnet 5.5 as a subagent"; "our fastest model to date". It costs about 75% less to run than Haiku 4.5 on average — [Haiku 5.5 announcement](https://www.anthropic.com/claude-haiku-5-5).
- Benchmarks (Haiku 5.5 vs Haiku 4.5) — [Haiku 5.5 announcement](https://www.anthropic.com/claude-haiku-5-5):
  - Terminal-Bench 4.0: 39.2% vs 0.0%; Sonnet 5.5 scores 70.6%.
  - GDPval-AA: 1620 vs 735.
  - OSWorld 2.1 offline subset: 72.4%.
  - FrontierCode: 46.4%.
- Anthropic says Sonnet 5.5 and Opus 5.5 "remain better choices for complex agentic coding tasks". Haiku 5.5 is "best suited to more narrowly scoped tasks" — [Haiku 5.5 announcement](https://www.anthropic.com/claude-haiku-5-5).
- Haiku 5.5 has adaptive thinking that is on by default, with effort from low to max (default `medium`). A newer tokenizer counts the same text as about 30% more tokens than Haiku 4.5 did — [Haiku 5.5 announcement](https://www.anthropic.com/claude-haiku-5-5); [Models overview](https://platform.claude.com/docs/en/about-claude/models/overview).

**Fable 5.2 positioning and benchmarks**
- Positioning: "best for the most ambitious, open-ended technical work. For most coding and knowledge tasks, we recommend that users start with Claude Opus 5.5". It can act as an Advisor or Orchestrator for smaller models — [Fable 5.2 announcement](https://www.anthropic.com/claude-fable-and-mythos-5-2).
- Speed and price: it generates outputs up to 30% faster than Fable 5.1. Fast mode is $16/$80 per MTok and up to 2.5x faster — [Fable 5.2 announcement](https://www.anthropic.com/claude-fable-and-mythos-5-2).
- Benchmarks (Fable 5.2 vs Opus 5.5) — [Fable 5.2 announcement](https://www.anthropic.com/claude-fable-and-mythos-5-2):
  - FrontierCode 2.0: 49.1% (xhigh) vs 45.5%.
  - FrontierSWE v2: 69.9% vs 62.3%.
  - AutomationBench: 51.4% vs 42.5%.
  - Terminal-Bench-Science 0.1: 74.6% vs 58.7%.
- Default effort is Medium in Claude apps and Claude Code — [Fable 5.2 announcement](https://www.anthropic.com/claude-fable-and-mythos-5-2); [Claude Code model config](https://code.claude.com/docs/en/model-config). The API default is `high` — [What's new in Fable 5.2](https://platform.claude.com/docs/en/models/fable-5-2/whats-new-fable-5-2).
- Blocked requests: Fable 5.2's safety classifiers block high-risk cyber and most research-biology tasks. Blocked queries are answered by Opus 4.8 (cyber) or Opus 5 (biology) instead — [Fable 5.2 announcement](https://www.anthropic.com/claude-fable-and-mythos-5-2).
- Data retention: Fable 5.2 requires 30-day data retention and is not available under zero data retention — [What's new in Fable 5.2](https://platform.claude.com/docs/en/models/fable-5-2/whats-new-fable-5-2).

**Speed (third-party)**
- Artificial Analysis (third-party) lists Haiku 5.5 at about 234 output tokens/s at max effort, the fastest Anthropic model on its provider page. Sonnet 5.5 tops out around 143 t/s at xhigh. Head-to-head pages show Haiku 5.5 (medium) at 137 t/s vs Sonnet 5.5 (xhigh) at 101 t/s — [Artificial Analysis – Anthropic provider page](https://artificialanalysis.ai/providers/anthropic); [AA Sonnet 5.5 release page](https://www.artificialanalysis.ai/models/releases/claude-sonnet-5-5); [AA Haiku vs Sonnet comparison](https://artificialanalysis.ai/models/comparisons/claude-haiku-5-5-medium-vs-claude-sonnet-5-5-xhigh). DeepLearning.AI reported 237 t/s (Haiku 5.5) and 127.5 t/s (Sonnet 5.5) — [The Batch](https://www.deeplearning.ai/the-batch/claude-fills-out-its-model-family/). The figures vary with effort and source; treat them as approximate. These numbers came from search-result summaries, and I did not open the pages.

**Deprecations and changes to flag**
- Fast mode on Opus 4.8 was deprecated on Oct 30, 2026 and will be removed on Nov 30, 2026 — [Release notes](https://platform.claude.com/docs/en/release-notes/overview); [Claude Code fast mode](https://code.claude.com/docs/en/fast-mode).
- API requests that send `temperature`/`top_p`/`top_k` return a 400 error on API version 2026-10-21 — [Release notes](https://platform.claude.com/docs/en/release-notes/overview) (also covered in Anthropic's bundled API reference skill). This matters for any old pipeline code.
- Opus 5.5: thinking can't be disabled; effort is the only control.
- Sonnet 5.5: `thinking: {type: "disabled"}` returns a 400; use `between_tools` instead.
- Opus 5.5 and Sonnet 5.5: forced `tool_choice` returns a 400.
- All current models: assistant prefill is removed. Use structured outputs to get JSON.
- Source for the thinking, tool_choice and prefill changes: [Models overview](https://platform.claude.com/docs/en/about-claude/models/overview); [What's new in Fable 5.2](https://platform.claude.com/docs/en/models/fable-5-2/whats-new-fable-5-2); Anthropic's bundled API reference skill (claude-api skill, cached 2026-11-03).

### Inferences
- For a video pipeline, all four models' 1M context is far more than script or prompt writing needs, so context window is not a differentiator. Price per task, speed, and writing quality are.
- Opus 5.5 and Sonnet 5.5 have near-identical headline numbers on several benchmarks (GDPval, OSWorld, Terminal-Bench). Anthropic itself says Opus is better at open-ended judgment. For building and debugging a pipeline (open-ended), Opus 5.5 is the safer pick. For recurring writing to a fixed template, Sonnet 5.5 or Haiku 5.5 should be enough.
- Fable 5.2 is likely overkill for this use case. It is 2x Opus price, needs usage credits on Pro, and is aimed at multi-day engineering work.

### Gaps
- **SWE-bench Verified / SWE-bench Pro**: none of the four official announcements report SWE-bench. Anthropic now reports Terminal-Bench 4.0, FrontierCode, CursorBench and FrontierSWE. Third-party SWE-bench figures conflict, so I excluded them.
- **No official creative-writing / short-form-script benchmark** exists for any model. The only official writing-quality evidence is the qualitative claims quoted above.
- **No official latency numbers**: Anthropic gives only relative labels (Moderate/Fast/Fastest), the "30%+ faster" claim for Sonnet 5.5, and the "up to 30% faster" claim for Fable 5.2 vs Fable 5.1.

## Q2. How subscription plans and usage limits apply to Claude Code

### Takeaway
Claude Code is included on Pro ($20/mo, or $17/mo billed annually), Max ($100), Ultra ($200), Team and Enterprise. It is **not** included on the Free plan. Usage is shared with claude.ai chat. Limits run on a rolling 5-hour session window plus a weekly limit; verified Ultra accounts have no 5-hour limit. Max and Ultra also have a separate weekly Fable limit. The default model in Claude Code on Pro, Max, Ultra, Team, Enterprise and the API is **Opus 5.5** at **medium** effort. Fast mode on subscriptions is billed only to usage credits.

### Cited Findings

**Plans and prices** — [claude.com/pricing](https://claude.com/pricing)
- Free ($0): "Limited usage every 5 hours and every week"; Claude Code: **No**; Opus: No; Sonnet and Haiku: Yes.
- Pro ($20/mo, or $17/mo billed annually): Claude Code: Yes. Includes "Hand off and schedule tasks". Fable is "paid with usage credits".
- Max ($100/mo): "5x Pro usage every 5 hours and every week". Fable is "included, up to half your weekly limit". Includes "$100 a month in API credits to build on the Claude Platform".
- Ultra ($200/mo): "No 5-hour limit" for verified accounts; "10x Pro usage every week"; $200/mo in API credits.
- Team: Standard seat $20/seat/mo annually ($25 monthly); Premium seat $100 annually ($125 monthly), with 5x the usage of a standard seat. Up to $500/mo in pooled API credits.
- Pricing-page footnote: "How fast you reach a limit depends on the model you use, how long your chats are, and how large your files are."
- Docs conflict on the Free plan: the Claude Code legal page says OAuth is "intended exclusively for purchasers of Claude Free, Pro, Max, Ultra, Team, and Enterprise subscription plans" — [Legal and compliance](https://code.claude.com/docs/en/legal-and-compliance). But the pricing page lists Claude Code as **No** on Free — [claude.com/pricing](https://claude.com/pricing). The authentication docs list only Pro/Max/Ultra/Team/Enterprise, Console, and cloud providers as Claude Code account types — [Claude Code authentication](https://code.claude.com/docs/en/iam). Treat Free as not usable for Claude Code.

**Usage limits** — [Use Claude Code with your Pro, Max, or Ultra plan](https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-max-or-ultra-plan); [How do usage and length limits work?](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work)
- "Pro and Max plans have a five-hour session limit and a weekly limit. Ultra plans have a weekly limit, and verified Ultra accounts don't have a five-hour session limit. Max and Ultra plans also have a separate weekly limit for Fable."
- Limits are "shared across Claude and Claude Code, meaning all activity in both tools counts against the same limits." IDE usage counts too.
- The 5-hour period "starts when you send your first message, and your limit resets in full five hours later."
- Weekly limits "reset at a fixed time each week that is assigned to your account".
- Usage depends on conversation length and complexity, features used, model, and effort level.
- Anthropic "may limit your usage with weekly and monthly caps or model and feature usage."
- "Usage limit reached · wrapping up": Claude Code may finish a step already in progress after the 5-hour limit is hit. On Pro this applies up to once per weekly period; on Max, each time the 5-hour limit is hit. It is rolling out gradually.
- Claude Code error messages distinguish two kinds of limit — [Claude Code costs](https://code.claude.com/docs/en/costs):
  - Seat-wide limits ("You've hit your session limit" / "weekly limit") are "shared across all models", so switching with `/model` doesn't help.
  - **Model-specific** limits ("You've hit your Opus limit" / "Sonnet limit"): "switching to a model outside that family with `/model` does keep the developer working."
- Team and Enterprise: each member's usage "draws from a per-seat allowance that resets on a rolling five-hour window and a weekly window", shared with chat and Cowork — [Claude Code costs](https://code.claude.com/docs/en/costs).
- Recent changes to limits:
  - A promotion ran May 13 – Sep 13, 2026 that raised Claude Code weekly limits by 50%. From Sep 14, 2026, weekly Claude Code limits are permanently 25% higher than before the promotion — [Weekly limits promotion](https://support.claude.com/en/articles/15910845-claude-code-may-august-2026-weekly-limits-promotion).
  - With Opus 5.5 (Sep 22), Anthropic increased five-hour limits on Pro, Max, Team and seat-based Enterprise, and gave subscribers a saved "rate limit reset" — [Opus 5.5 announcement](https://www.anthropic.com/claude-opus-5-5).
- Fable 5.2 launch promotion ("this week"): Fable is included for up to 50% of weekly limits on Pro plans and Team standard seats, plus 1–3 Fable resets — [Fable 5.2 announcement](https://www.anthropic.com/claude-fable-and-mythos-5-2). This is temporary; the standing pricing page says Pro's Fable is paid with usage credits.
- Usage credits let you keep working past a limit at standard API rates. Turn them on at claude.ai/settings/usage or with `/usage-credits` in Claude Code. A monthly spend limit can be set — [Manage usage credits](https://support.claude.com/en/articles/12429409-manage-usage-credits-for-paid-claude-plans); [Claude Code costs](https://code.claude.com/docs/en/costs).
- Monitoring: `/usage` shows plan usage bars and a breakdown of what counts against limits, with fix recommendations — [Claude Code costs](https://code.claude.com/docs/en/costs).
- No official numbers: Anthropic does not publish absolute message or token counts per window, only multipliers (Max = 5x Pro; Ultra = 10x Pro weekly) — [claude.com/pricing](https://claude.com/pricing).

**Default model, /model, aliases, opusplan** — [Claude Code model configuration](https://code.claude.com/docs/en/model-config)
- The `default` setting resolves to **Opus 5.5** on Pro, Max, Ultra, Team, Enterprise and the Anthropic API. Before v2.1.280 it was Sonnet 5 on Pro and Team Standard, and Opus 5 on Max and others.
- No Fable model is the default on any plan; select it explicitly with `/model fable`.
- On the Anthropic API, the aliases resolve to `opus` → Opus 5.5, `sonnet` → Sonnet 5.5, `haiku` → Haiku 5.5, and `fable` → Fable 5.2.
- Switching: `/model <alias|name>` switches mid-session; `claude --model …` sets the model at launch; the `ANTHROPIC_DEFAULT_*_MODEL` environment variables pin a version.
- Minimum Claude Code versions: Opus 5.5 needs v2.1.280+, Sonnet 5.5 v2.1.284+, Haiku 5.5 v2.1.293+, Fable 5.2 v2.1.321+.
- `opusplan`: "uses `opus` during plan mode, then switches to `sonnet` for execution".
- Fable billing in Claude Code:
  - Depending on plan and seat, Fable may bill to usage credits, and `/model` then shows "Requires usage credits".
  - **In `-p` (headless) mode, "Claude Code never asks for consent. When a Fable request there would bill to usage credits, Claude Code bills it without asking."**
- Haiku 5.5 runs with a 1M context on every plan. Sessions auto-compact at about 967K tokens.

**Effort** — [Claude Code model configuration](https://code.claude.com/docs/en/model-config)
- Levels are low/medium/high/xhigh/max on all four models. In Claude Code, Fable 5.2, Opus 5.5, Sonnet 5.5 and Haiku 5.5 all default to `medium`.
- Ways to set it, in precedence order: the `CLAUDE_CODE_EFFORT_LEVEL` environment variable, then `/effort` in the session, then `--effort` at launch, then settings (`modelSettings`/`effortLevel`), then the model default. Skill and subagent frontmatter can also set `effort`.
- Guidance from the same page:
  - `low` is for "quick exchanges where you review each result".
  - `medium` "fits day-to-day engineering work with a clear scope".
  - `high` suits bug-fixing in existing code.
  - `max` "may show diminishing returns and is prone to overthinking".
- "In Anthropic's testing, Opus 5.5 at `medium` matches or exceeds Opus 5 at `high`."
- `ultrathink` in a prompt raises a single turn to deeper reasoning. `ultracode` is a separate setting that orchestrates dynamic workflows.
- Lower effort also stretches subscription limits: "Choose a lower effort level for routine tasks... Higher effort uses more tokens" — [Usage and length limits](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work).

**Fast mode** — [Claude Code fast mode](https://code.claude.com/docs/en/fast-mode)
- Toggled with `/fast`. Up to 2.5x faster, same quality.
- Supported on Fable 5.2, Opus 5.5, Opus 5 and Opus 4.8. Not on Sonnet or Haiku.
- Prices per MTok: $16/$80 (Fable 5.2), $8/$40 (Opus 5.5).
- "For Claude Code users on subscription plans (Pro/Max/Ultra/Team/Enterprise), fast mode is available via usage credits only and not included in the subscription rate limits."

### Inferences
- A beginner on Pro gets Opus 5.5 by default, so the expensive model is already what burns the shared 5-hour window. Switching routine turns to Sonnet or Haiku (`/model sonnet` or `/model haiku`) and keeping effort at low or medium should stretch the window.
- Avoid `/fast` and Fable on a budget. Both silently draw on usage credits rather than plan limits, and in `-p` runs Fable can bill credits without asking. Keep usage credits off, or set a monthly spend limit, if "no extra spend" is a hard rule.

### Gaps
- There is no official per-model weekly cap table (for example, whether Pro has a separate Opus-only weekly bucket). The docs mention "Opus limit" and "Sonnet limit" messages but publish no numbers.
- No absolute numbers exist for the 5-hour or weekly allowances on any plan.

## Q3. Recommended model mix for the pipeline (build once vs. run daily)

### Takeaway
Use Opus 5.5 (the Claude Code default) at medium or high effort for architecting, building and debugging the pipeline. Escalate to Fable 5.2 only if Opus stalls on a hard problem; it needs credits on Pro. For daily script, caption and image/video prompt writing, use Sonnet 5.5 at low or medium effort. Use Haiku 5.5 for bulk or variant generation and as a subagent model. Run these through headless `claude -p --model haiku|sonnet` with structured JSON output, or through free external LLMs (Q6), so the build model's quota is saved for engineering work.

### Cited Findings
- Anthropic's recommended ladder: "start with Claude Opus 5.5... switch... upward to Fable or Mythos, or downward to Claude Sonnet 5.5 or Claude Haiku 5.5" depending on scope and complexity — [Fable 5.2 announcement](https://www.anthropic.com/claude-fable-and-mythos-5-2).
- Sonnet 5.5 is "strongest at well-scoped everyday tasks" and "well suited to fast iteration on less complex tasks" — [Sonnet 5.5 announcement](https://www.anthropic.com/claude-sonnet-5-5).
- Haiku 5.5 "reliably handles quick and repetitive workloads" and "pairs well with Opus 5.5 and Sonnet 5.5 as a subagent" — [Haiku 5.5 announcement](https://www.anthropic.com/claude-haiku-5-5).
- `opusplan` uses Opus in plan mode and Sonnet for execution — [Model configuration](https://code.claude.com/docs/en/model-config).
- Headless per-run model choice: `claude -p` accepts CLI flags such as `--model`, and `--output-format json` with `--json-schema` returns schema-valid output in a `structured_output` field — [Run Claude Code programmatically](https://code.claude.com/docs/en/headless).
- Subagent model selection — [Subagents](https://code.claude.com/docs/en/sub-agents):
  - The `model` field in an agent file's frontmatter accepts `sonnet`, `opus`, `haiku`, `fable`, a full ID such as `claude-opus-5-5`, or `inherit`.
  - Resolution order: the per-invocation model parameter, then the frontmatter `model`, then the `CLAUDE_CODE_SUBAGENT_MODEL` environment variable.
  - A user/project subagent named `Explore` with `model: haiku` makes exploration run on the cheaper model.
  - `CLAUDE_CODE_SUBAGENT_MODEL` together with `CLAUDE_CODE_SUBAGENT_MODEL_FORCE=1` forces one model onto every subagent (v2.1.257+).
  - An `effort` frontmatter field sets the subagent's effort level.
- Skills can also pin `model:` and `effort:` in SKILL.md frontmatter. The override lasts for the rest of the turn; with `context: fork` it applies to the forked subagent — [Skills](https://code.claude.com/docs/en/skills).
- Advisor option: the advisor tool lets a cheaper executor consult a stronger model mid-task. For a Sonnet 5.5 executor, the advisor can be Opus 5.5 — [Model configuration](https://code.claude.com/docs/en/model-config) (links to advisor docs); [Fable 5.2 announcement](https://www.anthropic.com/claude-fable-and-mythos-5-2).

### Inferences
- **Suggested mapping:**

  | Pipeline task | Suggested model and effort |
  |---|---|
  | Pipeline design, code, debugging (one-off) | Opus 5.5 at medium; high or xhigh for hard bugs |
  | Daily script writing (hook, body, CTA) | Sonnet 5.5 at low or medium |
  | Image/video generation prompts, captions, hashtags, titles | Haiku 5.5, or Sonnet 5.5 if quality lags |
  | Topic research / summarizing sources | Haiku 5.5 subagent |
  | QA or "does this script follow the rules" check | Haiku 5.5 |

- **Example daily cost if called via API (pay-as-you-go, not the subscription).** Rough arithmetic from list prices, assuming 5 scripts/day at about 3K input and 1.5K output tokens each:
  - Haiku 5.5: about $0.0015 input + $0.0038 output ≈ under $0.01/day.
  - Sonnet 5.5: about $0.03 + $0.075 ≈ $0.11/day.
  - Thinking tokens bill as output, so real numbers will be higher.
  - Source for prices: [Models overview](https://platform.claude.com/docs/en/about-claude/models/overview).
- Headless runs with a cheaper model make sense when the step is deterministic and template-driven, its output is machine-parsed (JSON schema), and it runs on a schedule or in a loop. Keep interactive Opus sessions for changing the pipeline itself.

### Gaps
- No official guidance targets creative or short-form video scripting specifically. The mapping above is an inference from Anthropic's general positioning.

## Q4. Claude Code features for automating repeated pipeline steps

### Takeaway
Claude Code offers several layers for codifying repeated steps:

| Feature | Use in the pipeline |
|---|---|
| Skills (SKILL.md; custom commands are now merged into skills) | Reusable procedures such as "/write-reel-script" |
| Subagents (`.claude/agents/*.md` with per-agent model and effort) | Cheap specialist workers |
| Hooks (PostToolUse etc.) | Deterministic post-processing |
| MCP servers (`claude mcp add`) | External tools and APIs |
| Headless `claude -p` with JSON/schema output | Scripts and cron jobs |
| Agent SDK (Python/TS) | Embedding the agent in pipeline code |
| GitHub Actions | CI triggers |
| Cloud scheduled tasks (formerly routines) / Desktop tasks / `/loop` | Recurring runs |
| Output styles | Session-wide tone and format |

### Cited Findings

**Skills**
- "Custom commands have been merged into skills." `.claude/commands/` files still work. A skill lives at `.claude/skills/<name>/SKILL.md`, and the folder name becomes the `/command` — [Skills](https://code.claude.com/docs/en/skills).
- Frontmatter fields — [Skills](https://code.claude.com/docs/en/skills):
  - `name`, `description`, `argument-hint`.
  - `disable-model-invocation` (manual-only skills).
  - `allowed-tools` (pre-approve tools for the turn).
  - `model` and `effort` (per-skill overrides).
  - `context: fork` with `agent` (run the skill in a subagent).
  - `hooks`, and `paths` (auto-activate on matching files).
- Skills, commands, memory and plugins load in Agent SDK sessions too. Plugins "package skills, agents, hooks, and MCP servers" — [Agent SDK overview](https://code.claude.com/docs/en/agent-sdk/overview).

**Subagents**
- Defined as markdown with frontmatter: `name`, `description`, `tools`, `disallowedTools`, `model`, `permissionMode`, `maxTurns`, `skills` (preloaded), `memory`, `background`, `effort` — [Subagents](https://code.claude.com/docs/en/sub-agents).
- Built-in Explore and Plan subagents exist, and a same-named custom agent overrides them — [Subagents](https://code.claude.com/docs/en/sub-agents).

**Hooks**
- Events include SessionStart, UserPromptSubmit, PreToolUse ("Can block it"), PostToolUse ("After a tool call succeeds"), PostToolUseFailure, Notification, SubagentStop, Stop and StopFailure. Matchers select tool names such as `Edit|Write` or `mcp__.*` — [Hooks guide](https://code.claude.com/docs/en/hooks-guide).
- The official example runs Prettier on every file Claude edits through a PostToolUse hook: `f=$(jq -r '.tool_input.file_path') && npx prettier --write ...` — [Hooks guide](https://code.claude.com/docs/en/hooks-guide).

**MCP servers**
- Remote servers: `claude mcp add --transport http <name> <url>`, for example `claude mcp add --transport http notion https://mcp.notion.com/mcp`. Use `--transport sse` for SSE-only servers. For stdio servers, put `--` before the server command — [MCP](https://code.claude.com/docs/en/mcp).
- Scopes: local by default; `--scope project` writes a shared `.mcp.json`, and `--scope user` is also available — [MCP](https://code.claude.com/docs/en/mcp).

**Headless / print mode** — [Run Claude Code programmatically](https://code.claude.com/docs/en/headless)
- Basic call: `claude -p "<prompt>" --allowedTools "Read,Edit,Bash"`. The exit code is 0 on success.
- Output formats: `--output-format text|json|stream-json`. Use `--json-schema` for validated `structured_output`.
- Sessions: `--continue` resumes a conversation.
- Permissions: `--permission-mode auto|dontAsk|acceptEdits`. `--permission-prompts none` is for unattended runs (v2.1.259+).
- `--bare` skips hooks, skills, MCP and CLAUDE.md for reproducible CI, but "bare mode doesn't use your subscription login". It needs `ANTHROPIC_API_KEY`.
- Without `--bare`, a `-p` session runs the project's hooks and MCP servers even in untrusted folders. Security note: a `-p` run shows no trust dialog.

**Agent SDK** — [Agent SDK overview](https://code.claude.com/docs/en/agent-sdk/overview)
- "The same tools, agent loop, and context management that power Claude Code, programmable in Python and TypeScript."
- Capabilities: built-in tools, hooks, subagents, MCP, permissions, sessions, skills/commands/memory, plugins.
- Other languages can run `claude -p --output-format json` as a subprocess.

**GitHub Actions** — [GitHub Actions](https://code.claude.com/docs/en/github-actions)
- Authenticates with either `ANTHROPIC_API_KEY` (Console key) or `CLAUDE_CODE_OAUTH_TOKEN`. The OAuth token comes from `claude setup-token` and is "available on Pro, Max, Ultra, Team, and Enterprise plans".
- The example workflow file is `examples/claude.yml` (responds to `@claude` mentions).
- An OAuth token "is tied to the subscription of the person who ran `claude setup-token`".

**Scheduling** — [Cloud scheduled tasks (formerly routines)](https://code.claude.com/docs/en/routines); [Run prompts on a schedule](https://code.claude.com/docs/en/scheduled-tasks)

Three scheduling options:

| | Cloud scheduled tasks | Desktop tasks | `/loop` |
|---|---|---|---|
| Runs on | Anthropic cloud | Your machine | Your machine, inside an open session |
| Access to local files | No (fresh clone) | Yes | Yes |
| Minimum interval | 1 hour | 1 minute when Claude sets it; 1 hour in the forms | 1 minute |
| Lifetime | Persistent | Persistent | Recurring loops expire after 7 days |

- Cloud scheduled tasks:
  - Status: research preview.
  - Plans: Pro, Max, Ultra, Team and Enterprise.
  - Triggers: Schedule (hourly, nightly, weekly or one-off), API (HTTP POST with a bearer token), or GitHub events.
  - Where to manage them: claude.ai/code/routines, or `/schedule` in the CLI.
  - They "draw down subscription usage the same way interactive sessions do". Hourly caps apply, for example 100 scheduled runs per hour per account.
  - Permission prompts are handled in auto mode by default.

**Output styles**
- An output style sets "Claude's role, tone, and response format for every response in a session". There are four built-ins plus custom styles. A custom style "can also turn Claude into something other than a software engineer, such as a writing assistant" — [Output styles](https://code.claude.com/docs/en/output-styles).

### Inferences
Example applications to a faceless Reels pipeline. These are my design suggestions, not official examples.
- **Skill `/write-reel-script`**: a SKILL.md holding the house script template (hook in 2s, 6–8 beats, CTA), banned phrases, length rules and a JSON output contract. Frontmatter: `model: sonnet`, `effort: low`, `allowed-tools: Read Write`. A companion skill `/make-shot-prompts` with `model: haiku` turns script beats into image or video-generator prompts.
- **Subagents**:
  - `.claude/agents/topic-researcher.md` (`model: haiku`, tools: WebSearch, WebFetch, Read) returns 5 trend-based topics.
  - `script-critic.md` (`model: haiku`, `effort: low`) checks scripts against the rules.
  - The main Opus session orchestrates both.
- **Hooks**:
  - PostToolUse on `Write` matching `scripts/*.json`: run a validator (jq schema check), auto-render TTS, or kick off `ffmpeg` assembly.
  - Stop hook: send a desktop or phone notification when the day's batch is done.
  - PreToolUse: block `rm -rf` or uploads.
- **MCP**: add servers for storage (Google Drive or Notion content calendar), image or video generation APIs that expose MCP, or a browser. Use `claude mcp add --scope project` so the config is committed with the repo.
- **Headless**: a cron or Task Scheduler job runs `claude -p "/write-reel-script topic=..." --model sonnet --output-format json --json-schema schema.json --permission-mode acceptEdits` and then a plain Python script calls TTS/ffmpeg. No API key is needed if the run uses the subscription login (see Q5).
- **Cloud scheduled task**: a nightly task in the repo that writes tomorrow's 3 scripts and opens a PR. Desktop scheduled tasks suit steps that need local files or GPU (rendering).
- **GitHub Actions**: an `@claude` comment on an issue such as "Make 5 Reels about X" produces script files via a PR.
- **Output style**: a custom "Reels copywriter" style for writing sessions.

### Gaps
- I did not verify specific MCP servers for TikTok, Instagram or YouTube upload, or for particular video generators. Availability varies, and another researcher may cover video tools.

## Q5. API (pay-as-you-go) vs. subscription use; headless with subscription login

### Takeaway
Two billing systems are separate. Calling the Claude API (Anthropic SDK or curl with an `ANTHROPIC_API_KEY` from the Console) bills pay-as-you-go per token, separate from any Pro/Max subscription. Claude Code logged in with a claude.ai subscription draws on plan limits. Interactive and headless (`claude -p`) runs both use the subscription login unless an API key is present. A set `ANTHROPIC_API_KEY` silently takes precedence and causes API charges. Anthropic's terms say subscription OAuth is for "ordinary use of Claude Code and other native Anthropic applications". Developers building products, including Agent SDK apps, should use API keys. Advertised limits assume "ordinary, individual usage of Claude Code and the Agent SDK".

### Cited Findings
- Precedence warning: "If you have an ANTHROPIC_API_KEY environment variable set on your system, Claude Code will use this API key for authentication instead of your Claude subscription... resulting in API usage charges rather than using your subscription's included usage." — [Use Claude Code with your Pro, Max, or Ultra plan](https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-max-or-ultra-plan)
- Auth precedence order — [Claude Code authentication](https://code.claude.com/docs/en/iam):
  1. Cloud provider credentials.
  2. `ANTHROPIC_AUTH_TOKEN`.
  3. `ANTHROPIC_API_KEY`.
  4. `apiKeyHelper`.
  5. `CLAUDE_CODE_OAUTH_TOKEN` (from `claude setup-token`).
  6. Anthropic profile.
  7. Subscription OAuth from `/login`, the default for Pro/Max/Ultra/Team/Enterprise.
- `claude setup-token` generates a one-year OAuth token for "CI pipelines and scripts where browser login isn't available". `--bare` does not read it — [Claude Code authentication](https://code.claude.com/docs/en/iam).
- Separate systems: the help center says Claude Console API credits and plan usage are "separate systems". To stay within the plan, "Decline the API credit option when presented" and log in with plan credentials only — [Use Claude Code with your Pro, Max, or Ultra plan](https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-max-or-ultra-plan).
- Max and Ultra include $100 and $200 per month in API credits, but these "can't be used in Claude Code or the Claude apps, including for usage credits". They are for building on the Claude Platform (API) — [Use Claude Code with your Pro, Max, or Ultra plan](https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-max-or-ultra-plan); [Haiku 5.5 announcement](https://www.anthropic.com/claude-haiku-5-5).
- Terms (Usage policy section) — [Legal and compliance](https://code.claude.com/docs/en/legal-and-compliance):
  - "Advertised usage limits for Pro, Max, and Ultra plans assume ordinary, individual usage of Claude Code and the Agent SDK."
  - "OAuth authentication is intended exclusively for purchasers of Claude Free, Pro, Max, Ultra, Team, and Enterprise subscription plans and is designed to support ordinary use of Claude Code and other native Anthropic applications."
  - "Developers building products or services that interact with Claude's capabilities, including those using the Agent SDK, should use API key authentication... Anthropic does not permit third-party developers to offer Claude.ai login into their own applications, or to route requests through Free, Pro, Max, or Ultra plan credentials on behalf of their users."
  - The same page says this does not prevent "an end user from signing in to the unmodified Claude Code binary with their own Claude subscription".
  - Free, Pro, Max and Ultra users fall under the Consumer Terms; Team, Enterprise and API users under the Commercial Terms.
- Agent SDK note: "Unless previously approved, Anthropic does not allow third party developers to offer claude.ai login or rate limits for their products, including agents built on the Claude Agent SDK." — [Agent SDK overview](https://code.claude.com/docs/en/agent-sdk/overview)
- Scheduled tasks and GitHub Actions officially support subscription auth:
  - Cloud scheduled tasks "draw down subscription usage the same way interactive sessions do" — [Scheduled tasks](https://code.claude.com/docs/en/routines).
  - GitHub Actions accepts `CLAUDE_CODE_OAUTH_TOKEN` "that authenticates with your Claude subscription" — [GitHub Actions](https://code.claude.com/docs/en/github-actions).
- Pitfall: in `-p` mode, Fable requests that would bill to usage credits are billed without a consent prompt — [Model configuration](https://code.claude.com/docs/en/model-config).
- Plan view: `/usage` shows plan bars for subscribers. The session dollar figure "isn't relevant for billing purposes" on Pro, Max and Ultra — [Claude Code costs](https://code.claude.com/docs/en/costs).

### Inferences
- For a "no paid subscriptions" beginner: Claude Code itself requires at least Pro, since Free does not include it per the pricing page. Calling the Claude API from Python pipeline code requires a Console account with prepaid credits, billed separately.
- If the beginner refuses every paid plan, Claude can't be part of the automated loop at all. Use free LLMs (Q6) for scripting, and the free claude.ai chat manually for occasional help.
- With Pro, the officially documented way to automate on the subscription is `claude -p` (or a cloud scheduled task, or GitHub Actions with `CLAUDE_CODE_OAUTH_TOKEN`) for personal use. Keep `ANTHROPIC_API_KEY` unset, don't use `--bare`, keep usage credits off, and don't select Fable.
- Running a personal pipeline in your own repo looks like "ordinary, individual usage" under the terms. Building a product for others, or routing other users' requests through your subscription, is not allowed.
- I found no official quantitative definition of "ordinary" usage. A daily scheduled script job is a gray area to keep modest.

### Gaps
- There is no official statement quantifying how much automated `claude -p` use counts as "ordinary, individual usage". The terms are qualitative.

## Q6. Free LLM alternatives for repetitive scripting

### Takeaway
The best free API option for daily script and prompt generation is the Google Gemini API free tier. Flash-class models (Gemini 3.8 Flash, 3.6 Flash, 3.5 Flash-Lite, Gemma 4) are "Free of charge" for input and output. Per-model RPM/RPD limits are shown only in AI Studio, and free-tier data "is used to improve our products". Other options:
- **Groq** has a permanent free plan (for example gpt-oss-120b/20b and qwen3.8-27b at 30 RPM / 1K RPD / 200K tokens/day).
- **OpenRouter** `:free` models allow 20 RPM, and 50 RPD rising to 1,000 RPD after a one-time purchase of $10 or more in credits.
- **Cerebras** has no permanent free tier, only a $5 / 30-day trial.
- **Mistral's** free Experiment plan exists, but exact limits are console-only.
- **Local models** via Ollama or LM Studio (gpt-oss:20b at 14GB, Gemma 4, Qwen3.5/3.6/3.8) are free and unlimited, given about 16GB RAM and a 4GB+ GPU.

### Cited Findings

**Google Gemini API (AI Studio)**
- Free tier qualification: an "Active project or free trial; some projects need verification". Limits are per project, not per API key. RPD resets at midnight Pacific time. Limits are "more restricted for experimental and preview models". Active limits are viewed in AI Studio — [Gemini API rate limits](https://ai.google.dev/gemini-api/docs/rate-limits) (redirects to aistudio.google.com/docs/rate-limits).
- Free availability by model — [Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing):
  - Free tier input and output "Free of charge": Gemini 3.8 Flash, Gemini 3.6 Flash, Gemini 3.5 Flash-Lite, Gemini 4 Hydrogen, Gemma 4, Gemini 2.5 Flash, Gemini 2.5 Pro.
  - "Gemini 4 Carbon is not available on the Free tier", and the same applies to Gemini 4 Argon.
  - Paid price for comparison: Gemini 3.8 Flash is $0.75 input / $3.75 output per 1M tokens through Dec 31, 2026, doubling to $1.50 / $7.50 from Jan 1, 2027.
  - "Used to improve our products": Yes on the Free tier, No on the Paid tier for most models.
- The pricing page did not show specific free-tier RPM/RPD numbers per model; they appear in AI Studio. One published free-tier table covers Gemini Decision 1 only (200 RPM / 50K TPM / 10K RPD), which is not relevant to text generation — [Gemini API rate limits](https://ai.google.dev/gemini-api/docs/rate-limits).

**Gemini app (consumer, free)**
- Usage limits are compute-based. The "limit refreshes every 5 hours until you reach your weekly limit". Paid AI plans get 2x–20x higher limits. "If capacity changes, limits for users without a Google AI plan may be limited before users with a plan" — [Gemini Apps limits & feature availability](https://support.google.com/gemini/answer/16275805?hl=en).

**Groq**
- Free Plan limits (RPM / RPD / TPM / TPD) — [Groq rate limits](https://console.groq.com/docs/rate-limits):

  | Model | RPM | RPD | TPM | TPD |
  |---|---|---|---|---|
  | openai/gpt-oss-120b | 30 | 1K | 8K | 200K |
  | openai/gpt-oss-20b | 30 | 1K | 8K | 200K |
  | qwen/qwen3.8-27b | 30 | 1K | 8K | 200K |
  | whisper-large-v3 / -turbo | 20 | 2K | — | — |

- llama-3.3-70b-versatile and llama-3.1-8b-instant appear in Groq's model list but were not in the Free Plan table I fetched — [Groq models](https://console.groq.com/docs/models).

**Cerebras**
- "Is there a permanently free tier? No. The Free Trial is time- and credit-bounded: $5 in credits that expire 30 days after they're granted." The trial requires a verified payment method — [Cerebras rate limits](https://inference-docs.cerebras.ai/support/rate-limits).

**OpenRouter**
- Free model variants have IDs ending in `:free`. Limits: 20 requests/minute. Daily cap is 50 requests/day if you have bought fewer than 10 credits all-time, and 1,000/day if you have bought 10 or more. A negative credit balance can cause errors even on free models — [OpenRouter API limits](https://openrouter.ai/docs/api-reference/limits). The numbers were read from the page's embedded constants (`FREE_MODEL_RATE_LIMIT_RPM=20`, `FREE_MODEL_NO_CREDITS_RPD=50`, `FREE_MODEL_HAS_CREDITS_RPD=1e3`, `FREE_MODEL_CREDITS_THRESHOLD=10`).

**Mistral**
- A free "Experiment" plan exists for evaluation and prototyping. It needs phone verification, and its requests may be used for training. Exact limits appear only in the console's Limits page.
- Third-party aggregators cite 1 request/second, 500K tokens/minute and 1B tokens/month, but these are **unverified** — [free-llm-api-resources (third-party)](https://mintlify.com/cheahjs/free-llm-api-resources/providers/free/mistral-plateforme); [TechCrunch 2024 launch of the free tier](https://techcrunch.com/2024/09/17/mistral-launches-a-free-tier-for-developers-to-test-its-ai-models).
- Mistral's official tier doc and help-center articles returned 404 when I fetched them — [docs.mistral.ai tier page](https://docs.mistral.ai/deployment/laplateforme/tier).

**ChatGPT Free**
- OpenAI's help page (help.openai.com/en/articles/9275245) returned 403 to automated fetch.
- Third-party reports (unverified) say:
  - OpenAI removed the text-message counter for Free and Go users around Aug 6–7, 2026.
  - Free accounts use GPT-5.6 Luna.
  - Tools such as image generation and file uploads keep separate caps.
  - Sources: [Help Net Security (third-party)](https://helpnetsecurity.com/2026/08/07/openai-gpt-5-6-sol-luna-chatgpt-free-limits); [Engadget (third-party)](https://engadget.com/2234173/chatgpt-free-features-2026).
- The help page itself says the default model and limits "can change over time" (per search snippet) — [OpenAI Help: ChatGPT Free Tier](https://help.openai.com/en/articles/9275245-chatgpt-free-tier).

**Local models (Ollama / LM Studio)**
- Model sizes on Ollama:

  | Model | Download size | Context | Notes |
  |---|---|---|---|
  | gpt-oss:20b | 14GB | 128K | Text |
  | gpt-oss:120b | 65GB | 128K | Text |
  | gemma4 e2b | 4.6–7.5GB | 128K | Text and image |
  | gemma4 e4b (latest) | 6.6–9.5GB | 128K | Text and image |
  | gemma4 26b / 31b | about 16–20GB | — | Larger variants |
  | qwen3.8:27b | 18GB | 256K | Text and image; updated about 1 week ago |
  | qwen3.6 | 27b, 35b | — | — |
  | qwen3.5 | 0.8b–122b | — | Multimodal; 2b about 2.7–3.1GB |
  | qwen3 | 0.6b–235b | — | — |

  Sources: [Ollama gpt-oss](https://ollama.com/library/gpt-oss); [Ollama gemma4](https://ollama.com/library/gemma4); [Ollama qwen3.8](https://ollama.com/library/qwen3.8); [Ollama qwen3.5](https://ollama.com/library/qwen3.5); [Ollama library](https://ollama.com/library).
- gpt-oss MXFP4 quantization "enables the smaller model to run on systems with as little as 16GB memory, and the larger model to fit on a single 80GB GPU" — [Ollama gpt-oss](https://ollama.com/library/gpt-oss).
- Ollama's newest listings in Oct–Nov 2026 include agentic and coding models such as flint (40B MoE), muse-spark-open (816B, cloud) and kimi-k3.1-pro (cloud). Large ones are offered as Ollama "cloud" models rather than local — [Ollama search, newest](https://ollama.com/search?o=newest).
- LM Studio system requirements — [LM Studio system requirements](https://lmstudio.ai/docs/app/system-requirements):
  - "At least 16GB of RAM is recommended"; "at least 4GB of dedicated VRAM is recommended".
  - AVX2 is required on x64.
  - Apple Silicon Macs are supported (8GB Macs only for small models); Intel Macs are not.
  - It can run fully offline.

### Inferences
- The cheapest robust setup for a beginner:
  - Gemini 3.x Flash (free API tier) or local Gemma 4 / Qwen 3.5–3.8 / gpt-oss-20b via Ollama for daily script, caption and prompt drafts.
  - Groq free gpt-oss-120b as a fast fallback.
  - Claude Code (on Pro) reserved for building and fixing the pipeline.
  - All of Gemini, Groq, OpenRouter and Ollama expose OpenAI-compatible or simple REST APIs, so the pipeline can switch providers through a config file.
- Free tiers on Gemini and Mistral use your prompts to improve or train models. Avoid sending anything private.
- At 5–10 scripts/day, every free API tier above has ample headroom. OpenRouter's no-purchase 50 RPD is the tightest.
- For "best small local models" in Nov 2026, Ollama listings and pull counts favor Qwen3.5/3.6/3.8, Gemma 4 and gpt-oss. I found no authoritative 2026 quality ranking for creative scripting among them.

### Gaps
- Per-model Gemini free-tier RPM/RPD numbers are not on the public docs page (AI Studio only).
- Official ChatGPT Free limits could not be retrieved (403).
- Official Mistral free-tier numbers could not be retrieved (404s; console-only).
- No independent benchmark of small local models on short-form script writing.
