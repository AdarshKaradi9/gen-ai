# Claude Code for Automated Short-Video (Reels/Shorts/TikTok) Pipelines — 2026

Observation date for all star counts, push dates and view counts: **2026-11-16**.

Method notes (read before using numbers):
- `gh api` and direct `api.github.com` / `github.com` requests were **blocked by this session's GitHub access policy** (HTTP 403 "GitHub access to this repository is not enabled for this session"). Live stars and `pushed_at` were therefore taken from the **ungh.cc** public GitHub mirror API (`https://ungh.cc/repos/OWNER/REPO`, run by the UnJS project), which returns GitHub's own stars and pushedAt fields. Licenses were read from each repo's `LICENSE` file on `raw.githubusercontent.com`. Confidence: High for licenses, Medium-High for stars/dates (mirror may lag by hours).
- YouTube metadata came from `yt-dlp` (metadata only, no download). Several videos returned YouTube's "Sign in to confirm you're not a bot" check; I did **not** bypass it. For those, only the view count from a `ytsearch` flat listing is given (no upload date). "Sponsored?" is based on description text only (affiliate/sponsor links); YouTube's "paid promotion" flag was not visible. Confidence for each row is marked.
- No Reddit threads or X threads surfaced in my searches (see Gaps).

---

## Q1. Real 2026 examples: YouTube videos, blog posts and tutorials showing Claude Code / Claude making short videos

### Takeaway
By mid–late 2026 the dominant pattern is "Claude Code + a code-based renderer + a TTS service": either **Remotion** (React; official Remotion Agent Skills since Jan 2026) or **HyperFrames** (HeyGen's HTML-to-video framework, Apache-2.0, first on npm March 2026, very popular Sept–Nov 2026). Most high-view YouTube videos are creator-economy tutorials ("faceless channel", "viral animated shorts") that often carry affiliate links; the most technically useful sources are a few written guides and open repos (LearnWithHasan, digitalsamba toolkit).

### Cited Findings

**Written guides / blog posts (2026)**
- LearnWithHasan, "How to Make Faceless YouTube Shorts With Claude Code (Free Project)" by Hasan Aboul Hasan, published 2026-07-30. Claude Code first writes a plan (beat sheet, narration lines, fact checks), waits for approval, then builds the animation as Remotion code, renders test frames to self-check, renders, generates narration with word-level timings for captions, adds SFX; output 1080x1920 30 fps MP4. Uses 5 project skills in `.claude/skills/` (`make-short` code-only animation, `make-vox` paper-collage with AI image layers, `make-ai-short` video-model character, `suggest-sfx`, `vidtsx-2d-generator`), a `brand.md` style contract and `CLAUDE.md`. Recommends a six-beat script grammar (hook, setup, optional quiz, reveal, twist, loop) and ~100 words per 40-s short. Needs ElevenLabs (paid, per character); Gemini and fal.ai optional. Caption timing comes from ElevenLabs timestamps, not Whisper. — [LearnWithHasan](https://learnwithhasan.com/guide/how-to-make-faceless-youtube-shorts-with-claude-code/)
- Beginners in AI, "Build a YouTube Shorts Factory with Claude Code + Remotion": Claude Code does scripting/orchestration, Remotion renders; pitched at 10–50 Shorts/week. (Date not verified.) — [beginnersinai.org](https://beginnersinai.org/youtube-shorts-factory-claude-remotion/)
- MindStudio, "How to Generate AI Videos with Claude Code, HyperFrames, and ElevenLabs: Full Workflow" (search snippet dated May 2026; not fetched). — [MindStudio](https://www.mindstudio.ai/blog/generate-ai-videos-claude-code-hyperframes-elevenlabs-workflow)
- René Zander, "Automate YouTube Shorts with CapCut: The CLI + Claude Pipeline" — deterministic steps scripted, Claude does creative parts (not fetched). — [renezander.com](https://renezander.com/guides/automate-youtube-shorts-capcut-cli/)
- Remotion Agent Skills tutorials: Apidog "How To Turn Claude Code into a Video Director with Remotion" (Jan 23, 2026) — [Apidog](https://apidog.com/blog/claude-code-remotion); Tella guide — [Tella](https://www.tella.com/blog/how-to-use-remotion-agent-skills-with-claude-code); mer.vin (May 2026) — [mer.vin](https://mer.vin/2026/05/remotion-agent-skills-install-remotion-dev-skills-for-claude-code-and-cursor/); aividpipeline "Remotion Agent Skills Guide 2026" — [aividpipeline](https://aividpipeline.com/blog/remotion-agent-skills-guide-2026). A Japanese article dates the Remotion skills release to **2026-01-20** — [issoh.co.jp](https://www.issoh.co.jp/tech/details/12300/) (via search snippet; Medium confidence).
- AITuber vendor blog describes a hosted "YouTube Shorts MCP" tested Sept 2026 that lets Claude script, voice, generate visuals, caption, render 9:16 and publish (vendor claim; Low confidence). — [aituber.app](https://aituber.app/blog/youtube-shorts-mcp-claude/)

**YouTube videos (metadata via yt-dlp unless noted)**

| Date | Channel | Views | Title / URL | Method (from description) | Sponsored / affiliate? | Conf. |
|---|---|---|---|---|---|---|
| 2026-11-01 | Nafay 3D | 714,048 | [How To Make Faceless YouTube Shorts with Claude (Free Skill/Automation)](https://www.youtube.com/watch?v=n1N_ZIP5x3M) | A Claude skill writes script, makes visuals, voiceover and word-synced captions; Zapier used to auto-post Shorts | Zapier affiliate link at top of description | High |
| 2026-11-01 | Mr omi | 1,120,816 | [How to Make Viral Animated Shorts Using Claude (Full Workflow)](https://www.youtube.com/watch?v=OtbLL6OBNE4) | Claude studied a channel's 20 latest shorts frame-by-frame at 30 fps, then built an animated short (2D characters in a 3D world, three.js-style); links a GitHub repo `mromidev/claude-an…` | Description has sponsor/affiliate-style wording (unverified which) | Medium |
| 2026-11-04 | Grow With Kaz | 435,311 | [I Made VIRAL Animation Videos Using Claude Code (FREE Plugin)](https://www.youtube.com/watch?v=3tpaWHaiLQ8) | Claude Code + free plugin to make 3D/2D animated videos; ElevenLabs voice | ElevenLabs affiliate link; paid Skool community | High |
| 2026-10-30 | Zinho Automates | 115,755 | [How To Build a Faceless YouTube Channel with Claude (Full Automation)](https://www.youtube.com/watch?v=zXE_PpJ5WUc) | Claude + Higgsfield MCP for generated visuals | Higgsfield affiliate links | High |
| 2026-10-01 | Roboverse | 126,750 | [Claude Code Can Now Automate Your Videos (Remotion + Opus 5.5)](https://www.youtube.com/watch?v=6_rCyryA6hg) | Claude Code + Remotion plugin, motion graphics and finished videos from prompts | None seen | High |
| 2026-10-03 | Science Based AI | 55,805 | [How I create viral animated reels using HyperFrames + Claude Code](https://www.youtube.com/watch?v=y4YupFxhAog) | Claude + HyperFrames for short-form reels at work | **Yes — explicit sponsor (Typeless)** | High |
| 2026-10-12 | Selling With Nas | 70,139 | [How to make FREE AI Videos with Claude (and Hyperframes) – Full Beginner Tutorial](https://www.youtube.com/watch?v=3sEuuAk-lYc) | Install HyperFrames plugin in Claude, prompt-only video creation | None seen | High |
| 2026-10-14 | Brandon Melville | 38,615 | [Claude Code + HyperFrames = Cheapest AI Video Editor EVER](https://www.youtube.com/watch?v=xbCKxfWlIO0) | Claude Code + HyperFrames editing; Fish Audio TTS | **Yes — Fish Audio promo** | High |
| 2026-10-15 | Vibe Dojo | 2,962 | [No Claude Motion? Make Videos with Claude Code + Remotion](https://www.youtube.com/watch?v=btKmUC4sw0c) | Beginner Windows tutorial: Node.js setup → animated video → prompt revisions → export | None seen | High |
| 2026-11-13 | Enkay Studio | 89 | [How to Edit Videos with Claude Code (Step-by-Step)](https://www.youtube.com/watch?v=pSf6bMA7wQs) | Claude Code + Remotion to edit real footage | None seen | High |
| 2026-08-10 | Sorav Jain | 947 | [How to Make Animated Videos With Claude Code and Remotion](https://www.youtube.com/watch?v=fK0weT1XW5k) | Plain-English prompts → Remotion animations (maps, logos, pins) | None seen | High |
| 2026-07-11 | Medhavy AI | 446 | [Build a Quantum Energy Ladder with Claude Code + Manim](https://www.youtube.com/watch?v=13bpFftt06A) | Claude Code writes Manim physics animation | None seen | High |
| 2026-05-04 | Danny Why | 111,221 | [How I Use Claude Code to Create 2D Animations](https://www.youtube.com/watch?v=rSrs6Tighq4) | Claude Code + Golpo for 2D animation | Golpo affiliate link | High |
| 2026-03-29 | Koen \| AI Content Systems | 42,240 | [Claude Code + Blotato = Automated Shorts in Minutes](https://www.youtube.com/watch?v=ZXyjSufezL8) | Claude Code + Blotato (posting/rendering SaaS) | Blotato referral link | High |
| 2026-03-23 | Emil Faschang | 7,197 | [How I Post 20+ Automated Instagram Reels A Day (Claude Code Tutorial)](https://www.youtube.com/watch?v=He3KS1kSwv4) | Claude Code system producing 20+ Reels/day incl. posting; template on Skool | Skool funnel | High |
| 2026-01-22 | Snapper AI | 15,636 | [Generate Animated Videos with Claude Code (Remotion Agent Skill Tutorial)](https://www.youtube.com/watch?v=EwKCAgt4aKI) | First wave of Remotion Agent Skill tutorials | None seen | High |
| n/a (bot check) | George Clicks | 50,348 | [How My Faceless Channel Made $300/day in 2 Weeks (Claude Only)](https://www.youtube.com/watch?v=v_poyKo4prk) | Title only; income claim unverified | Unknown | Low |
| n/a | Grow With Kaz | 80,853 | [This AI YouTube Niche Is EXPLODING! (Make Videos With Claude Code/Free Plugin)](https://www.youtube.com/watch?v=Ock60o-Glh4) | Title only | Unknown | Low |
| n/a | ReachMora | 627,022 | [I Tried Making a Viral Video Using ONLY Claude AI](https://www.youtube.com/watch?v=kDcxEIDC5NA) | Title only | Unknown | Low |
| n/a | HyperFrames (official) | 6,484 | [Recreate Any Video With Claude, Then Make It Yours](https://www.youtube.com/watch?v=IWqJhESAbKU) | Official HyperFrames channel ("reverse-any-video" skill) | Vendor | Low |
| n/a | Nafay 3D | 52,420 | [How To Make Faceless YouTube Shorts with Claude (Free Skill with 50+ Styles)](https://www.youtube.com/watch?v=GNGDI1yEG-Q) | Title only | Unknown | Low |

Search source for the "n/a" rows: `yt-dlp ytsearch8` flat listings for "claude code youtube shorts automation", "claude code faceless reels", "claude code hyperframes video" (2026-11-16). Other Remotion tutorials found but blocked by bot check: [qcV1W3uGHXE](https://www.youtube.com/watch?v=qcV1W3uGHXE), [6yndvwhxygE](https://www.youtube.com/watch?v=6yndvwhxygE), [dh-oUJLkbAk](https://www.youtube.com/watch?v=dh-oUJLkbAk).

### Inferences
- The highest-view videos (Nafay 3D, Mr omi, Grow With Kaz) are monetization/creator-funnel content; many have affiliate links to the TTS/visual vendor they demo. Treat their "free" claims and income claims skeptically.
- A clear shift happened in Sept–Nov 2026 toward HyperFrames (4 HyperFrames tutorials with 30k–70k views in October alone), while Remotion remains the most-documented option.
- The best beginner-to-intermediate references are written: LearnWithHasan guide + its MIT repo, and the digitalsamba toolkit README.

### Gaps
- No Reddit or X/Twitter threads surfaced in searches (one Reddit-targeted search returned only GitHub/blog results). Not verified whether X threads exist.
- Upload dates for bot-checked videos unknown; YouTube "paid promotion" flags not observable.
- The Mr omi GitHub repo link is truncated in the description (`github.com/mromidev/claude-an...`); `mromidev/claude-animation-skills` did not resolve in the mirror.

---

## Q2. GitHub repos for automated short-video generation (live stats 2026-11-16)

### Takeaway
Two families exist: (1) older "MoneyPrinter-style" Python pipelines (stock footage + TTS + subtitles via MoviePy/FFmpeg) that are self-contained apps, and (2) newer 2026 "agent-native" toolkits where Claude Code itself is the orchestrator using skills (claude-faceless-shorts-creator, digitalsamba toolkit, OpenMontage, HyperFrames, Remotion skills). For a Claude Code user, family (2) is the better fit; MoneyPrinterTurbo is the most mature turnkey app in family (1).

### Cited Findings
Stars/pushed date from [ungh.cc mirror](https://ungh.cc); license from each repo's LICENSE file.

**Agent-native / Claude Code–driven (2026)**
- **hassancs91/claude-faceless-shorts-creator** — 364★, pushed 2026-08-18, MIT (©2026). Faceless Shorts factory driven by Claude Code: pure-TSX Remotion visuals, ElevenLabs voice with word-exact captions, library-first sound design; 12 example shorts; 3 tracks (code-only, Vox-style collage, AI-video character). Paid: ElevenLabs required; Gemini/fal.ai optional; Remotion free ≤3 people. — [GitHub](https://github.com/hassancs91/claude-faceless-shorts-creator); [guide](https://learnwithhasan.com/guide/how-to-make-faceless-youtube-shorts-with-claude-code/)
- **digitalsamba/claude-code-video-toolkit** — 2,586★, pushed 2026-11-16, MIT. "Tell Claude Code what video you want: it writes the script, generates the voiceover, music, and visuals, and renders the MP4." Ships skills (e.g. `remotion`), commands `/setup`, `/video`, `/template`. Uses open-source models deployed to your own cloud GPU (Qwen3-TTS voice, FLUX.2 images, ACE-Step music); recommends Modal ($30/month free compute on Starter). Has a 9:16 Short example with burned captions. Requires Node 22+; uv for Python tools. — [GitHub README](https://github.com/digitalsamba/claude-code-video-toolkit)
- **OpenMontageInc/OpenMontage** (formerly calesthio/OpenMontage) — 80,732★, pushed 2026-11-09, **AGPL-3.0**. "Open-source, agentic video production system. 12 production pipelines, 100+ tools, 700+ agent skill" files; works with Claude Code, Cursor, Copilot, Windsurf, Codex. Zero-key mode: Piper TTS narration, free stock (Pexels/Pixabay/Unsplash keys are free), Remotion composer, word-level burned subtitles; optional paid keys: Kling, ElevenLabs, OpenAI, Google, fal. — [GitHub README](https://github.com/OpenMontageInc/OpenMontage)
- **heygen-com/hyperframes** — 84,770★, pushed 2026-11-16, Apache-2.0; npm `hyperframes` created 2026-03-23, latest 0.9.56 ([npm registry](https://registry.npmjs.org/hyperframes)). See Q3/Q4. — [GitHub README](https://github.com/heygen-com/hyperframes)
- **remotion-dev/skills** — 7,271★, pushed 2026-11-11 (no LICENSE file at root). Official Remotion Agent Skills: `/remotion-best-practices`, `/remotion-create`, `/remotion-markup`, `/remotion-studio`, `/remotion-render`; install via `npx remotion skills add`, `npx skills add remotion-dev/skills`, or `npx create-video@latest --skills`. **Status: active and official** (verified). — [GitHub README](https://github.com/remotion-dev/skills); [Remotion docs](https://www.remotion.dev/docs/ai/skills)
- **zhuyansen/awesome-claude-video-skills** — 2,159★, pushed 2026-11-15. Curated list: "Open-source skills and toolkits that let Claude Code, Codex and other coding agents make video. 180 repos by type, each security-graded." Best discovery index. — [GitHub](https://github.com/zhuyansen/awesome-claude-video-skills)
- **AgriciDaniel/claude-youtube** — 778★, pushed 2026-04-10. Claude Code skill for YouTube creators (audits, SEO, retention scripts, thumbnails, Shorts optimization); does not render video. — [GitHub](https://github.com/AgriciDaniel/claude-youtube)

**Turnkey pipelines (topic → MP4)**
- **harry0703/MoneyPrinterTurbo** — 143,839★, pushed 2026-11-13, MIT. Topic/keyword → HD short video. LLMs: OpenAI, Anthropic Claude, Kimi, DeepSeek, Gemini, Ollama and many aggregators. TTS: **Edge TTS (free, no key)**, Azure, Gemini, MiniMax, ElevenLabs, Chatterbox, Kokoro, Fish Audio, VoxCPM. Visuals: Pexels/Pixabay (free), local media, optional text-to-video (MiniMax H3, Seedance, Wan). Subtitles from TTS timestamps or local Whisper (faster-whisper). Outputs 9:16 1080×1920, 16:9, 1:1. Batch generation; Docker. README heavily sponsored by Chinese API aggregators. Claude Code can run/modify (Python). — [GitHub README](https://github.com/harry0703/MoneyPrinterTurbo)
- **FujiwaraChoki/MoneyPrinter** — 14,204★, pushed 2026-03-26, MIT. MoviePy-based Shorts; now "Ollama-first" (local LLM) with DB-backed queue (API + worker + Postgres in Docker). — [GitHub README](https://github.com/FujiwaraChoki/MoneyPrinter)
- **FujiwaraChoki/MoneyPrinterV2** — 32,450★, pushed 2026-09-15, **AGPL-3.0**. "Automate the process of making money online" (broader: Shorts + Twitter bot + affiliate). — [GitHub](https://github.com/FujiwaraChoki/MoneyPrinterV2)
- **RayVentura/ShortGPT** — 8,176★, **last push 2025-02-10** [OLDER; effectively stale ~21 months], MIT. MoviePy editing, OpenAI scripting, ElevenLabs or free EdgeTTS, Pexels footage, captions, translation/dubbing engine; Docker or Colab. Still runs but likely needs dependency fixes. — [GitHub README](https://github.com/RayVentura/ShortGPT)
- **gyoridavid/short-video-maker** — 1,499★, **last push 2025-06-21** [OLDER; stale ~17 months], MIT. MCP + REST server: Kokoro TTS (English only) → Whisper (whisper.cpp) captions → Pexels background video (free key) → Remotion composition/render. "Free alternative" to paid APIs; Docker images (tiny uses `tiny.en` whisper + q4 Kokoro); ≥3 GB RAM. Example n8n workflows. — [GitHub README](https://github.com/gyoridavid/short-video-maker)
- **unconv/shortrocity** — 271★, last push 2024-06-04 [OLDER; abandoned]. — [GitHub](https://github.com/unconv/shortrocity)

**Long-video → clips (repurposing, not topic→video)**
- **mutonby/openshorts** — 8,509★, pushed 2026-11-15, MIT. OpusClip alternative: Gemini (or Ollama/OpenAI-compatible) moment detection, MediaPipe+YOLOv8 face-tracked 9:16 crop, faster-whisper word-level subtitles, ElevenLabs dubbing; self-host Docker 8 GB+ RAM; exposes an `/mcp` endpoint. — [GitHub README](https://github.com/mutonby/openshorts)
- **Anil-matcha/AI-Youtube-Shorts-Generator** (redirected from SamurAIGPT/…) — 6,108★, pushed 2026-11-12, MIT. Long YouTube video → 9:16 shorts. — [GitHub](https://github.com/Anil-matcha/AI-Youtube-Shorts-Generator)

**Rendering frameworks / templates**
- **remotion-dev/remotion** — 73,464★, pushed 2026-11-15, custom Remotion License (see Q5); `@remotion/cli` latest 4.0.544 ([npm](https://registry.npmjs.org/@remotion/cli/latest)). — [GitHub](https://github.com/remotion-dev/remotion)
- **remotion-dev/template-tiktok** — 308★, pushed 2026-11-09. "Generate TikTok-style captions with Whisper.cpp." Good starter for 9:16 captioned video. — [GitHub](https://github.com/remotion-dev/template-tiktok)
- **ManimCommunity/manim** — 42,597★, pushed 2026-11-14; PyPI `manim` 0.22.1 ([PyPI](https://pypi.org/pypi/manim/json)). **3b1b/manim** — 96,568★, pushed 2026-09-09. — [GitHub](https://github.com/ManimCommunity/manim), [GitHub](https://github.com/3b1b/manim)
- **motion-canvas/motion-canvas** — 19,953★, pushed 2026-07-02, MIT. — [GitHub](https://github.com/motion-canvas/motion-canvas)
- **Zulko/moviepy** — 15,150★, pushed 2026-08-26; PyPI 2.2.1. — [GitHub](https://github.com/Zulko/moviepy), [PyPI](https://pypi.org/pypi/moviepy/json)

**Speech building blocks (all open-source, runnable by Claude Code)**
- faster-whisper 26,775★ (pushed 2026-11-12) — [GitHub](https://github.com/SYSTRAN/faster-whisper); WhisperX 25,354★ (word-level timestamps) — [GitHub](https://github.com/m-bain/whisperX); whisper.cpp 55,226★ — [GitHub](https://github.com/ggml-org/whisper.cpp).
- TTS: Kokoro (hexgrad/kokoro 10,136★, last push 2025-08-06) — [GitHub](https://github.com/hexgrad/kokoro); Kokoro-FastAPI 5,686★ (pushed 2026-11-13) — [GitHub](https://github.com/remsky/Kokoro-FastAPI); Chatterbox 27,852★ — [GitHub](https://github.com/resemble-ai/chatterbox); edge-tts 12,554★ (uses Microsoft's online service, no key) — [GitHub](https://github.com/rany2/edge-tts); sherpa-onnx 15,975★ — [GitHub](https://github.com/k2-fsa/sherpa-onnx).

### Inferences
- All MIT/Apache repos above can be cloned, run and modified by Claude Code (Python or Node). AGPL-3.0 (OpenMontage, MoneyPrinterV2) is fine for personal use but imposes source-sharing if you offer a modified version as a network service.
- A fully free pipeline is possible: Claude (subscription) + Edge TTS or Kokoro/Piper + faster-whisper + Pexels + FFmpeg/MoviePy or HyperFrames. ElevenLabs is the most common paid add-on for voice quality.
- ShortGPT, short-video-maker and shortrocity should be flagged as stale; short-video-maker is still a good reference design (Kokoro→Whisper→Pexels→Remotion).

### Gaps
- Star counts come from a mirror, not `gh api` (blocked); numbers for HyperFrames (84.8k) and OpenMontage (80.7k) are very high for 2026 projects—accurate per the mirror but not cross-checked.
- Did not verify license of remotion-dev/skills (no root LICENSE) or AI-Youtube-Shorts-Generator backends in detail.

---

## Q3. MCP servers relevant to video work

### Takeaway
Video MCPs are mostly small community projects; the mature, maintained ones are the official ElevenLabs MCP and the Blender MCP. For rendering, the 2026 consensus is **skills + CLI** (Remotion skills, HyperFrames plugin) rather than an MCP server; Claude Code can also just call `ffmpeg` via Bash, which makes FFmpeg MCPs largely unnecessary.

### Cited Findings
- **ElevenLabs MCP (official)** — elevenlabs/elevenlabs-mcp 1,551★, pushed 2026-08-20; PyPI `elevenlabs-mcp` 0.12.2. TTS, voice, SFX via API (paid/free-tier ElevenLabs account required). — [GitHub](https://github.com/elevenlabs/elevenlabs-mcp); [PyPI](https://pypi.org/pypi/elevenlabs-mcp/json)
- **Blender MCP** — ahujasid/mcp-for-blender (renamed from blender-mcp) 34,550★, pushed 2026-11-15; "Community plugin to control Blender 3D with any LLM… Not affiliated with the official Blender Foundation." Free. — [GitHub](https://github.com/ahujasid/blender-mcp)
- **FFmpeg MCPs (community, low maturity)**: Kush36Agrawal/Video_Editor_MCP 52★, last push 2025-01-04 [OLDER, stale] — trim, merge, convert, speed, audio, subtitles, filters via natural language — [mcpservers.org](https://mcpservers.org/servers/Kush36Agrawal/Video_Editor_MCP); misbahsy/video-audio-mcp 90★, last push 2025-05-24 [OLDER, stale] — [GitHub](https://github.com/misbahsy/video-audio-mcp); christopher-stevers video-mcp exposes an `execute_ffmpeg` tool — [LobeHub](https://lobehub.com/mcp/christopher-stevers-video-mcp); burningion/video-editing-mcp 295★ (Video Jungle SaaS) pushed 2025-10-09 — [GitHub](https://github.com/burningion/video-editing-mcp).
- **short-video-maker** exposes MCP + REST (stale since 2025-06). — [GitHub](https://github.com/gyoridavid/short-video-maker)
- **OpenShorts** exposes `/mcp` self-hosted, or hosted at mcp.openshorts.app (paid plans from $12/mo; free 20 min/mo with watermark). — [GitHub README](https://github.com/mutonby/openshorts)
- **Higgsfield MCP** (commercial generative video) is promoted in creator videos with affiliate links. — [YouTube description](https://www.youtube.com/watch?v=zXE_PpJ5WUc)
- **HyperFrames** ships as a Claude Code plugin (`claude plugin marketplace add heygen-com/hyperframes`; `claude plugin install hyperframes@hyperframes`) and 9 skills, not an MCP. — [HyperFrames README](https://github.com/heygen-com/hyperframes)
- No official "Remotion MCP" repo was found (remotion-dev/remotion-mcp does not exist per mirror lookup); Remotion's agent integration is via skills. — [remotion-dev/skills](https://github.com/remotion-dev/skills)

### Inferences
- For a beginner, MCPs add config surface without much benefit for FFmpeg/rendering; Bash + skills are simpler. MCPs are worth it for paid generative services (ElevenLabs, image/video gen) where the vendor maintains the server.

### Gaps
- Did not verify Remotion's "Remotion plugin" referenced by Roboverse's video (may be a Claude Code plugin packaging of skills).
- Image-generation MCPs (Replicate, fal, OpenAI images) not individually checked.

---

## Q4. What Claude Code can do alone at each pipeline step (via code)

### Takeaway
Claude Code can perform **every step without paid APIs except the LLM itself** (Claude subscription): it writes scripts, generates visuals as code (Remotion/HyperFrames/Manim/Canvas), installs and runs open-source TTS and Whisper for captions, assembles with FFmpeg/MoviePy, renders thumbnails with Pillow/HTML, and exports Meta-compliant 9:16 MP4. Quality gaps are voice naturalness (open TTS < ElevenLabs) and "illustrative" imagery (code-generated motion graphics are strong for kinetic text, charts, diagrams; weak for photoreal scenes without stock/AI images).

### Cited Findings
- **Scripting / planning**: plan-before-build with beat sheet and fact checks; six-beat grammar; ~100 words per 40 s. — [LearnWithHasan](https://learnwithhasan.com/guide/how-to-make-faceless-youtube-shorts-with-claude-code/)
- **Code-generated visuals**:
  - Remotion skills teach compositions, animation, layout, typography, media, effects, audio, fonts, timing; without them "Claude may generate buggy or outdated Remotion code" (secondary source). — [remotion-dev/skills](https://github.com/remotion-dev/skills); [Nemo Video](https://www.nemovideo.com/blog/remotion-agent-skills-claude-code-guide)
  - HyperFrames: "Write HTML. Render video. Built for agents." Headless Chrome seeks each frame, FFmpeg encodes; deterministic output; requires Node 22+ and FFmpeg; `npx hyperframes init/preview/render`; skills include `/hyperframes`, `/media-use` (voiceover, transcripts), `/reverse-any-video`, `/remotion-to-hyperframes`; kinetic captions as a use case. — [HyperFrames README](https://github.com/heygen-com/hyperframes)
  - Code-only Remotion track produces finished shorts with no stock footage (12 examples). — [claude-faceless-shorts-creator](https://github.com/hassancs91/claude-faceless-shorts-creator)
  - Manim used with Claude Code for physics/math explainers. — [YouTube: Medhavy AI](https://www.youtube.com/watch?v=13bpFftt06A); [ManimCommunity](https://github.com/ManimCommunity/manim)
- **Voiceover (open source, local)**: Kokoro (used by short-video-maker, q4 model in Docker), Piper (OpenMontage zero-key mode), Edge TTS (free, no key, online), Chatterbox, Qwen3-TTS on own GPU. — [short-video-maker](https://github.com/gyoridavid/short-video-maker); [OpenMontage](https://github.com/OpenMontageInc/OpenMontage); [MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo); [digitalsamba toolkit](https://github.com/digitalsamba/claude-code-video-toolkit)
- **Captions**: whisper.cpp in Remotion's TikTok template; faster-whisper word-level subtitles (OpenShorts, MoneyPrinterTurbo); or TTS-provider timestamps (ElevenLabs) for "word-exact" captions with no ASR. — [template-tiktok](https://github.com/remotion-dev/template-tiktok); [openshorts](https://github.com/mutonby/openshorts); [claude-faceless-shorts-creator](https://github.com/hassancs91/claude-faceless-shorts-creator)
- **Editing/assembly**: MoviePy (ShortGPT, MoneyPrinter), FFmpeg (all), Remotion composition (short-video-maker, OpenMontage). — [ShortGPT](https://github.com/RayVentura/ShortGPT); [MoneyPrinter](https://github.com/FujiwaraChoki/MoneyPrinter)
- **Self-QA**: Claude renders test frames and checks them before full render. — [LearnWithHasan](https://learnwithhasan.com/guide/how-to-make-faceless-youtube-shorts-with-claude-code/)
- **Thumbnails**: Playwright + Pillow used in the collage track (HTML/Python render). — [LearnWithHasan](https://learnwithhasan.com/guide/how-to-make-faceless-youtube-shorts-with-claude-code/)
- **Instagram Reels spec (Meta Graph API, Reel specifications)**: container MOV or MP4, "no edit lists, moov atom at the front of the file"; audio AAC, ≤48 kHz, mono/stereo, 128 kbps; video HEVC or H.264, progressive, closed GOP, 4:2:0; 23–60 fps; max 1920 horizontal pixels; aspect 0.01:1–10:1 but **9:16 recommended**; VBR ≤25 Mbps; duration 3 s–15 min; file ≤300 MB. — [Meta developers: IG User Media](https://developers.facebook.com/docs/instagram-platform/instagram-graph-api/reference/ig-user/media)
- **YouTube Shorts**: square or vertical uploads up to **3 minutes** count as Shorts (from 15 Oct 2024). — [YouTube Help](https://support.google.com/youtube/answer/15424877?hl=en)

### Inferences
- Safe universal export (inference from Meta spec): 1080×1920, 30 fps, H.264 High, yuv420p, VBR ~8–12 Mbps (≤25), AAC 128 kbps 48 kHz stereo, `-movflags +faststart` (moov atom at front). Example: `ffmpeg -i in.mp4 -vf "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2" -r 30 -c:v libx264 -profile:v high -pix_fmt yuv420p -b:v 10M -maxrate 12M -bufsize 20M -c:a aac -b:a 128k -ar 48000 -movflags +faststart out.mp4`. libx264 uses closed GOPs by default (open-gop off) — from general x264 knowledge, not cited.
- Keep shorts 20–60 s for cross-posting to TikTok/Shorts/Reels even though limits are higher.
- Code-generated motion graphics are the strongest "Claude-only" visual style (kinetic typography, data viz, explainers); photoreal or character content needs stock footage or paid gen-video APIs.

### Gaps
- TikTok's current upload specs were not checked.
- No quantitative quality comparison of Remotion vs HyperFrames vs Manim output found.

---

## Q5. Licensing: Remotion and other non-standard licenses

### Takeaway
Remotion is free (including commercial use and automation) for individuals and organizations with ≤3 people; larger companies pay. HyperFrames (Apache-2.0) has no thresholds. Watch AGPL (OpenMontage, MoneyPrinterV2).

### Cited Findings
- Remotion Free License: "For individuals and companies of up to 3 people." Company License: "Remotion for Automators" $0.01 per render, billed in blocks of 1,000 ($10), minimum $100/month; "Remotion for Creators" $25/month per seat; Enterprise from $500/month. — [Remotion pricing](https://www.remotion.dev/docs/license/pricing.md)
- FAQ: free license covers "an individual, whether for personal or commercial use"; "If you are eligible for the Free License, you can also run an automation"; teams "as long as your total headcount is 3 or less"; qualifying non-profits free "regardless of your headcount" (educational/government need written permission). — [Remotion License FAQ](https://www.remotion.dev/docs/license/faq.md)
- LearnWithHasan summarizes the same: free for individuals/teams up to 3, paid for 4+. — [LearnWithHasan](https://learnwithhasan.com/guide/how-to-make-faceless-youtube-shorts-with-claude-code/)
- HyperFrames: Apache 2.0, README states no per-render fees or commercial thresholds. — [HyperFrames README](https://github.com/heygen-com/hyperframes)
- AGPL-3.0: OpenMontage, MoneyPrinterV2 (LICENSE files). — [OpenMontage LICENSE](https://raw.githubusercontent.com/OpenMontageInc/OpenMontage/main/LICENSE); [MoneyPrinterV2 LICENSE](https://raw.githubusercontent.com/FujiwaraChoki/MoneyPrinterV2/main/LICENSE)
- MIT: MoneyPrinterTurbo, MoneyPrinter, ShortGPT, short-video-maker, claude-code-video-toolkit, claude-faceless-shorts-creator, openshorts, AI-Youtube-Shorts-Generator, motion-canvas (LICENSE files on raw.githubusercontent.com). — e.g. [MoneyPrinterTurbo LICENSE](https://raw.githubusercontent.com/harry0703/MoneyPrinterTurbo/main/LICENSE)
- Edge TTS uses Microsoft's online service (not a local model) — [edge-tts](https://github.com/rany2/edge-tts); terms of commercial use of that service not verified.

### Inferences
- A solo creator automating a faceless channel can use Remotion free; if the project grows to a 4+ person company, expect $100+/month (Automators) — a reason some 2026 creators moved to HyperFrames.

### Gaps
- Voice-model licenses (Kokoro: Apache-2.0 per its HF card, not verified here; Piper; Chatterbox; Qwen3-TTS) and stock-footage licenses (Pexels) were not individually verified.

---

## Q6. Recommended beginner-friendly architecture ("topic in → finished MP4 out")

### Takeaway
Use Claude Code as the orchestrator with a small repo of **skills + deterministic scripts**: Node/TypeScript renderer (HyperFrames or Remotion) for visuals and composition, small Python helpers for TTS and Whisper, FFmpeg for final export. Make each stage write a file (script.json → audio.wav → captions.json → render.mp4 → final.mp4) so a human can review between stages, and expose one entry point (`/make-short <topic>` interactively or `claude -p "/make-short <topic>"` headless).

### Cited Findings
- Reference repo structures: `.claude/skills/` with track skills + `brand.md` style contract + `CLAUDE.md`, plan approval before build — [LearnWithHasan](https://learnwithhasan.com/guide/how-to-make-faceless-youtube-shorts-with-claude-code/); `/setup`, `/video`, `/template` commands and skills — [digitalsamba toolkit](https://github.com/digitalsamba/claude-code-video-toolkit); `pipeline_defs/` + stage director skills in `skills/pipelines/` + tool registry — [OpenMontage](https://github.com/OpenMontageInc/OpenMontage).
- Language mix: Remotion/HyperFrames require Node (HyperFrames Node 22+); TTS/Whisper tooling is Python (faster-whisper, Kokoro); digitalsamba uses Node 22+ plus uv-managed Python. — [HyperFrames](https://github.com/heygen-com/hyperframes); [digitalsamba](https://github.com/digitalsamba/claude-code-video-toolkit)
- Pure-Python alternative stack (MoviePy + Edge TTS/Kokoro + faster-whisper + Pexels) is proven by MoneyPrinterTurbo/ShortGPT. — [MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo); [ShortGPT](https://github.com/RayVentura/ShortGPT)

### Inferences (proposed design, not from a single source)
```
shorts-factory/
  CLAUDE.md                 # pipeline rules, brand voice, "always stop for approval after script"
  brand.md                  # colors, fonts, caption style, pacing
  config/
    pipeline.yaml           # voice, fps=30, size=1080x1920, max_seconds=45, tts=kokoro|edge|elevenlabs
    .env.example            # optional keys: ELEVENLABS_API_KEY, PEXELS_API_KEY
  .claude/
    skills/
      make-short/SKILL.md   # orchestrator: topic -> runs stages in order (disable-model-invocation: true)
      write-script/SKILL.md # beat sheet + narration -> work/<slug>/script.json
      build-visuals/SKILL.md# HyperFrames/Remotion composition rules
      publish/SKILL.md      # upload step, manual-only
    settings.json           # permissions allowlist (ffmpeg, node, python scripts), hooks
  scripts/
    tts.py                  # script.json -> voice.wav (+ word timestamps if provider gives them)
    captions.py             # faster-whisper word timestamps -> captions.json
    export.sh               # ffmpeg final encode to Meta spec
    qa.py                   # ffprobe checks: 1080x1920, fps, duration<=limit, loudness
  video/                    # Remotion or HyperFrames project
  work/<slug>/              # per-video artifacts (script.json, voice.wav, captions.json, render.mp4)
  out/<slug>.mp4
```
- One command: `claude -p "/make-short 'why octopuses have 3 hearts'" --permission-mode acceptEdits --allowedTools "Bash(python scripts/*),Bash(npx hyperframes *),Bash(ffmpeg *)"` (flags per Claude Code docs, cited in Q7), or a `make short TOPIC=...` wrapper.
- Human review: stage gate after `script.json` (Claude stops and asks; or headless run ends after script and a second run renders), plus a final review of `out/<slug>.mp4` before a manual-only `/publish` skill. Keep publishing out of automated runs initially.
- Python vs TS: choose HyperFrames/Remotion (TS) if you want motion-graphics quality and Claude's strong HTML/React fluency; choose pure Python (MoviePy) if you only need stock-footage + subtitles and want one language.

### Gaps
- No source benchmarks render times/costs per short for these stacks.

---

## Q7. How Claude Code features help (skills, commands, hooks, subagents, headless, Agent SDK, scheduling, CI)

### Takeaway
Skills (SKILL.md with bundled scripts) are the main packaging unit — custom slash commands have been merged into skills; headless `claude -p` + Agent SDK make the pipeline scriptable; scheduled tasks/routines and GitHub Actions (`anthropics/claude-code-action`) make it recurring.

### Cited Findings
- Skills: a directory with `SKILL.md` (YAML frontmatter + instructions); invoked automatically when relevant or via `/skill-name`; body loads only when used. Locations: `~/.claude/skills/`, project `.claude/skills/`, plugins (`/plugin-name:skill-name`). Frontmatter: `description`, `disable-model-invocation: true` (manual-only, for side-effect workflows like deploys), `user-invocable: false`, `allowed-tools` (e.g. `Bash(${CLAUDE_SKILL_DIR}/scripts/render.sh *)`), `context: fork` (runs in a subagent), `arguments`, `model`, `hooks`. Skills can bundle `scripts/` that are executed, not loaded; keep SKILL.md <500 lines. "Custom commands have been merged into skills"; `.claude/commands/*.md` still work. Dynamic context injection with `` !`command` ``. — [Claude Code docs: Skills](https://code.claude.com/docs/en/skills)
- Headless: `claude -p "<prompt>"`; `--output-format text|json|stream-json`; `--json-schema` for structured output; `--allowedTools` with permission rule syntax (e.g. `Bash(git diff *)`); `--permission-mode auto|dontAsk|acceptEdits`; `--permission-prompts none` for unattended runs; `--continue` / `--resume <session_id>`; `--bare` recommended for scripts/CI (skips auto-discovery; needs `ANTHROPIC_API_KEY`); user-invoked skills work in `-p` by including `/skill-name` in the prompt; JSON output includes `total_cost_usd`. — [Claude Code docs: Run programmatically](https://code.claude.com/docs/en/headless)
- Agent SDK: "same tools, agent loop, and context management that power Claude Code," as CLI or Python/TypeScript packages. — [Claude Code docs: headless](https://code.claude.com/docs/en/headless); [Agent SDK overview](https://code.claude.com/docs/en/agent-sdk/overview.md)
- Scheduling: skills docs link to session scheduled tasks, cloud routines and desktop scheduled tasks. — [Skills docs](https://code.claude.com/docs/en/skills) → [scheduled-tasks](https://code.claude.com/docs/en/scheduled-tasks), [routines](https://code.claude.com/docs/en/routines.md)
- GitHub Actions: headless docs link "GitHub Actions: use the Agent SDK in GitHub workflows"; anthropics/claude-code-action 9,970★, pushed 2026-11-14. — [Claude Code docs: GitHub Actions](https://code.claude.com/docs/en/github-actions.md); [GitHub](https://github.com/anthropics/claude-code-action)
- Hooks and subagents: hooks can be attached in skill frontmatter; `context: fork` runs a skill in a subagent; subagent messages appear in stream-json with `parent_tool_use_id`. — [Skills docs](https://code.claude.com/docs/en/skills); [headless docs](https://code.claude.com/docs/en/headless)
- Plugins: HyperFrames distributes as a Claude Code plugin via `claude plugin marketplace add` / `claude plugin install`. — [HyperFrames README](https://github.com/heygen-com/hyperframes)

### Inferences
- Hooks are useful as guardrails: e.g. a PostToolUse/Stop hook that runs `qa.py` (ffprobe resolution/fps/duration check) after any render, so non-compliant MP4s fail fast.
- Subagents (`context: fork`) suit parallel stages such as "research facts" or "generate 3 hook variants" while keeping the main context small.
- For scheduled daily runs, GitHub Actions needs FFmpeg/Chrome/Node on the runner and an API key (bare mode doesn't use subscription login); local scheduled tasks are simpler for a beginner.

### Gaps
- Did not fetch the hooks, subagents, scheduled-tasks or GitHub Actions pages in full; details above come from links and summaries within the skills and headless pages.
- Whether a Claude Pro/Max subscription can power unattended GitHub Actions runs (vs API key) was not verified.
