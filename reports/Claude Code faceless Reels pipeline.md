# Claude Code turns topics into Reels for free

*Research snapshot: 16 November 2026. Scope: faceless Instagram Reels made with Claude Code on an existing Claude subscription, adding only free tools (open-source, local, or usable free tiers). Niche selection and trend hunting are out of scope. Any tool marked **PAID** has a free alternative next to it. **NC** means a non-commercial licence, which you cannot use on a monetised account.*

---

## 1. Executive summary: Claude Code covers most of the pipeline; voice and photoreal pixels need free add-ons

- **Claude Code can run the whole pipeline. The only thing you pay for is the Claude subscription you already have.** It writes the script, builds the visuals as code, installs and runs open-source TTS and Whisper, assembles and exports the video with FFmpeg, draws the cover, and can call Instagram's free official API. Working 2026 examples include LearnWithHasan's MIT-licensed Claude Code shorts factory ([guide](https://learnwithhasan.com/guide/how-to-make-faceless-youtube-shorts-with-claude-code/)), the digitalsamba toolkit ([GitHub](https://github.com/digitalsamba/claude-code-video-toolkit)) and OpenMontage's "zero-key" mode, which uses Piper TTS, free stock footage, Remotion and word-level subtitles ([GitHub](https://github.com/OpenMontageInc/OpenMontage)). Claude Code needs at least the **Pro** plan ($20/mo). The pricing page lists Claude Code as "No" on the Free plan ([claude.com/pricing](https://claude.com/pricing)).
- **What creators actually do.** "Claude as producer" writes the script, scene list and image/video prompts. A media generator makes the visuals, and CapCut does the edit. They record the **voiceover first** and let its timestamps drive the visuals ([zapiwala summary](https://youtubesummary.com/summary/WVT2FCjhDDY), [E'Calm summary](https://youtubesummary.com/summary/srDpvEnGQg4)). In October–November 2026 creators started having **Claude render the whole video in code** with Remotion, HyperFrames or three.js, with no AI video generator ([Mr omi summary](https://youtubesummary.com/summary/OtbLL6OBNE4)).
- **Recommended free stack:** Claude Code, plus **Kokoro-82M** voice (Apache-2.0, runs on CPU), **faster-whisper** word timestamps, **Pexels/Pixabay** stock APIs, **FFmpeg**, and Pillow for covers. For motion graphics, add **HyperFrames** (Apache-2.0) or **Remotion** (free for individuals and companies of up to 3 people). Music comes from **ACE-Step 1.5** (MIT), Pixabay/Mixkit, or Freesound CC0 ([Kokoro](https://huggingface.co/hexgrad/Kokoro-82M), [faster-whisper](https://github.com/SYSTRAN/faster-whisper), [HyperFrames](https://github.com/heygen-com/hyperframes), [Remotion licence](https://www.remotion.dev/docs/license/faq.md), [ACE-Step](https://huggingface.co/ACE-Step/Ace-Step1.5)).
- **Where Claude Code falls short.** It cannot produce photoreal images or AI video by itself.
  - **Images:** run local **Z-Image-Turbo** or **FLUX.2 [klein] 4B** (both Apache-2.0, roughly 13–16 GB VRAM, less when quantised), or use **Cloudflare Workers AI's free 10,000 neurons/day** ([Z-Image](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo), [FLUX.2 klein 4B](https://huggingface.co/black-forest-labs/FLUX.2-klein-4B), [Cloudflare](https://developers.cloudflare.com/workers-ai/platform/pricing/)).
  - **AI video:** local **Wan 2.2 5B** needs about an 8 GB GPU with ComfyUI offload ([ComfyUI](https://docs.comfy.org/tutorials/video/wan/wan2_2.md)). Free hosted video tiers are manual-only and mostly watermarked and non-commercial.
- **Licence traps for a monetised account.** Many "best free" models are NC or revenue-capped:
  - NC: F5-TTS, XTTS-v2, MusicGen, MMAudio, FLUX.2 [dev] and klein 9B, Qwen-Image-2.1, and free Kling/Vidu output.
  - Revenue-capped: Fish Audio Drama 3 (under US$500k), Stable Audio Open (under US$1M), LTX-2.5 (under US$10M).
  - Third-party guides also say ElevenLabs Free allows no commercial use.
  - Sources are in the step tables in section 3.
- **Publishing.** Instagram's official Content Publishing API posts Reels to your own Business or Creator account at no documented cost, without App Review (Standard Access). The limit is 100 posts per 24 h, though the same page also says 50. It has an `is_ai_generated` flag. Trending licensed music cannot be added through the API ([Meta docs](https://developers.facebook.com/docs/instagram-platform/content-publishing/), [media reference](https://developers.facebook.com/docs/instagram-platform/instagram-graph-api/reference/ig-user/media)). Do not use unofficial bots such as instagrapi.
- **The rules punish templated, unoriginal output, not AI itself.**
  - Instagram stopped recommending aggregator/repost accounts on 30 Apr 2026 ([TechCrunch](https://techcrunch.com/2026/04/30/instagram-restricts-reach-of-content-aggregators-in-new-crackdown/)).
  - It limits reach for unlabelled AI-person profiles from 31 Aug 2026 ([Instagram Creators](https://creators.instagram.com/blog/ai-generated-profile-label)).
  - YouTube clarified in July 2026 that "generic, repetitive, or template-based" AI content cannot be monetised ([TechCrunch](https://techcrunch.com/2026/07/20/youtube-clarifies-policies-around-ai-slop-and-upsetting-videos/)).
- **Model mix:**
  - **Opus 5.5** (the Claude Code default) to build and debug the pipeline.
  - **Sonnet 5.5** at low/medium effort for daily scripts.
  - **Haiku 5.5** for prompts, captions and critique subagents.
  - Skip **Fable 5.2**: it costs twice as much as Opus and is billed to usage credits on Pro ([models overview](https://platform.claude.com/docs/en/about-claude/models/overview), [pricing](https://claude.com/pricing)).
  - Free fallbacks to save quota: Gemini API free tier, Groq and Ollama.
- **Money reality, especially in India.** Instagram does not pay per view in India ([Influencermetric](https://influencermetric.in/blog/how-to-monetize-instagram-reels-india)). A 10M-view AI-influencer experiment netted **$157.48** ([Tilbury summary](https://videohighlight.com/v/LlhTEttKcwQ)). Plan around affiliates and brand deals.
- **Beginner path:**
  - **Day 1:** install the tools and make one Reel by hand with Claude Code.
  - **Week 1:** one command from topic to MP4, with human approval gates.
  - **Month 1:** add motion graphics, music and covers, and optionally API posting. Keep a human reviewing every Reel.

---

## 2. Pipeline diagram, and how creators actually work

### 2a. Claude-Code-first pipeline (free tool only where Claude Code can't do the step)

```
TOPIC (you)
   |
   v
[1] SCRIPT ............ Claude Code (Sonnet 5.5 skill) -> work/<slug>/script.json
   |                    beats, narration (~100 words / 40 s), on-screen text,
   |                    b-roll search terms / image prompts, fact-check notes
   |                    >>> HUMAN GATE 1: approve script + facts
   v
[2] VOICEOVER ......... Claude Code runs FREE local TTS: Kokoro-82M (CPU)
   |                    [fallbacks: Chatterbox (GPU), edge-tts >= 7.3.1]
   v
[3] WORD TIMESTAMPS ... Claude Code runs FREE faster-whisper / WhisperX (CPU ok)
   |                    -> captions.json (drives scene cuts AND captions)
   v
[4] VISUALS ........... Claude Code by itself: kinetic text, charts, maps, cards
   |                    (HyperFrames / Remotion / Pillow / Manim code)
   |                    + FREE Pexels/Pixabay API b-roll (portrait)
   |                    + optional FREE local images: ComfyUI + Z-Image-Turbo (GPU)
   |                    + optional FREE local video: Wan 2.2 5B I2V (GPU >= 8 GB)
   v
[5] CAPTIONS .......... Claude Code by itself: FFmpeg ASS karaoke / pycaps /
   |                    Remotion createTikTokStyleCaptions
   v
[6] MUSIC + SFX ....... Claude Code picks from a curated FREE library
   |                    (Pixabay / Mixkit / Freesound CC0) or runs ACE-Step 1.5 (GPU)
   v
[7] ASSEMBLY+EXPORT ... Claude Code by itself: FFmpeg -> 1080x1920, 30 fps, H.264,
   |                    AAC 48 kHz, +faststart; qa.py (ffprobe) hook
   |                    >>> HUMAN GATE 2: watch the MP4
   v
[8] COVER + CAPTION ... Claude Code by itself: Pillow/Playwright 1080x1920 JPEG;
   |                    caption text + hashtags
   v
[9] UPLOAD ............ v1: YOU post in Instagram app / Meta Business Suite (free)
                        v2: Claude Code calls the official Instagram API
                            (is_ai_generated, trial_params) - still human-triggered
                        >>> HUMAN GATE 3: AI label + final publish decision
```

### 2b. How creators actually do it in 2026

The YouTube tutorial ecosystem has settled on one pattern: **Claude (or ChatGPT) as the producer**. Claude studies competitors, writes a ~30-second script, splits it into scenes with voiceover lines, visuals and timestamps, and writes the image prompts ([Sanji summary](https://youtubesummary.com/summary/8Rf0xna31xg)). The media layer then splits into a paid all-in-one generator (most often **Higgsfield**, frequently through its MCP connector inside Claude) or a free stack of Google Flow, Grok, Google AI Studio TTS, the ElevenLabs free tier and CapCut ([E'Calm summary](https://youtubesummary.com/summary/srDpvEnGQg4), [Higgsfield summary](https://youtubesummary.com/summary/wU_bmWb6bhg)). The most consistent craft rule across independent creators is **"voice-over first, scenes second"**. Creators generate the narration, get timestamps (FoziScribe, Turboscribe at 3 free/day, or Whisper), and then make one visual per timestamped line ([zapiwala summary](https://youtubesummary.com/summary/WVT2FCjhDDY), [Danny Why summary](https://videohighlight.com/v/WODnqHPLR38)). A pipeline you build should copy that rule: **audio timing decides scene durations.**

Claude Code shows up in four distinct roles:

- **Scriptwriter and prompt writer.** This is universal.
- **Editor inside a real CapCut project.** Claude "synced every image to the voiceover, added music, sound effects and text, and keyframed each clip for subtle zooms" ([Matt Loui, sponsored by Higgsfield](https://www.youtube.com/watch?v=5N1moUCsVhI)).
- **Motion-graphics coder.** Remotion counters, lists and maps are imported into CapCut ([Matt Loui](https://www.youtube.com/watch?v=8oIFBQ9BhVU)).
- **Full renderer.** Mr omi had Claude analyse 20 reference Shorts frame by frame, write a style bible, and render 3D scenes in three.js plus Remotion with seven critique sub-agents. He admits the first version "looked cheap" ([summary](https://youtubesummary.com/summary/OtbLL6OBNE4)).

LearnWithHasan's written guide (30 July 2026) is the clearest reproducible version. Claude Code writes a plan (beat sheet, narration, fact checks) and **waits for approval**. It then builds the animation as Remotion code, **renders test frames to check itself**, renders the final video, adds narration with word-level timings and SFX, and outputs 1080×1920 at 30 fps. It ships five project skills plus a `brand.md` style contract and `CLAUDE.md` ([LearnWithHasan](https://learnwithhasan.com/guide/how-to-make-faceless-youtube-shorts-with-claude-code/)). One caution: that guide **requires ElevenLabs (PAID)** for voice and caption timestamps. The free substitute is Kokoro plus faster-whisper (section 3).

Two framework families dominate. **Remotion** (React) has had official Agent Skills since January 2026, installed with `npx remotion skills add` ([remotion-dev/skills](https://github.com/remotion-dev/skills)). **HyperFrames** is HeyGen's HTML-to-video framework: Apache-2.0, on npm since March 2026, installed as a Claude Code plugin with `claude plugin marketplace add heygen-com/hyperframes` ([HyperFrames README](https://github.com/heygen-com/hyperframes)). HyperFrames took off in September–November 2026: four HyperFrames tutorials drew 30k–70k views each in October alone ([e.g. Selling With Nas](https://www.youtube.com/watch?v=3sEuuAk-lYc)). A caution on the tutorials themselves: **about 15 of the top 30 faceless-AI tutorials carry Higgsfield affiliate or sponsor links or come from Higgsfield's own channel**, so their "paid tool wins" conclusions are commercially biased (section 8).

**Sources disagree on "Claude free plan" tutorials.** zapiwala's title says "Claude Code (Free Plan)" ([video](https://www.youtube.com/watch?v=WVT2FCjhDDY)), and Nafay 3D's skill runs on the Claude free plan ([description](https://www.youtube.com/watch?v=n1N_ZIP5x3M)). Anthropic's pricing page lists Claude Code as **not included on Free** ([pricing](https://claude.com/pricing)). Those tutorials most likely use Claude chat or skills in the app, not Claude Code. One summary also quotes a "minimum $19/month" subscription ([videohighlight](https://videohighlight.com/v/JhtbnZUU_8E)), but the official price is $20/mo, or $17/mo billed annually.

### 2c. Video styles by what they need

| Style | Claude Code alone (code + open-source it installs) | Needs free tools / GPU / accounts | Really needs PAID | Policy risk |
|---|---|---|---|---|
| Kinetic typography, facts and lists, quote cards | **Yes**. HyperFrames/Remotion/Pillow; local TTS ([HyperFrames](https://github.com/heygen-com/hyperframes)) | Music library | No | Medium if every video uses an identical template ([YouTube policy](https://support.google.com/youtube/answer/1311392?hl=en)) |
| Motion-graphics explainer (counters, maps, charts) | **Yes**. Remotion motion graphics ([Matt Loui](https://www.youtube.com/watch?v=8oIFBQ9BhVU)) | None | No | Low–medium |
| Math/science explainer | **Yes**. Manim ([Medhavy AI](https://www.youtube.com/watch?v=13bpFftt06A), [Manim](https://github.com/ManimCommunity/manim)) | None | No | Low |
| Code-rendered 2D/3D animated story (stickman, "2D in 3D") | **Yes, but setup is heavy**. three.js plus Remotion ([Mr omi summary](https://youtubesummary.com/summary/OtbLL6OBNE4)); 12 code-only examples ([hassancs91 repo](https://github.com/hassancs91/claude-faceless-shorts-creator)) | Free 3D assets | No | Medium (repetitive characters) |
| Narrated stock-footage B-roll with captions | Partly | **Pexels/Pixabay free API keys** ([Pexels](https://www.pexels.com/api/documentation/)) | No | Medium (generic look) |
| Paper-collage / "Vox" style with AI image layers | Partly | Local Z-Image or Cloudflare free tier (the Hasan repo uses Gemini/fal, which are **PAID**) | No | Low–medium |
| AI-image mini-documentary with zooms | Partly (zoom/parallax in FFmpeg) | Local image model (GPU) or manual Gemini app / Google Flow | No | **Highest**. "Image slideshows" are non-monetisable on YouTube ([policy](https://support.google.com/youtube/answer/1311392?hl=en)) |
| Short AI-video clips (stickman, scenic) | No | Local Wan 2.2 5B (GPU ≥8 GB) or manual Google Flow (50 credits/day, 720p) ([Flow](https://labs.google/flow)) | For 1080p, volume, no watermark | Medium |
| Consistent photoreal AI character / AI influencer / talking-animal podcast / lip-sync | No | Barely: free tiers are watermarked or NC | **Yes**: Higgsfield, HeyGen, Kling (**PAID**) ([Jack Craig summary](https://youtubesummary.com/summary/za2VyvLl5T0), [Youri](https://www.youtube.com/watch?v=VVU3GLgk-R0)) | High. Needs the "AI-generated profile" label ([Instagram](https://creators.instagram.com/blog/ai-generated-profile-label)) |
| Ranking/compilation of other people's viral clips | n/a | n/a | n/a | **Avoid**: reused/unoriginal content on Instagram and YouTube ([Tubefilter](https://www.tubefilter.com/2026/04/30/instagram-removes-algorithm-recommendations-repost-content-aggregator/)) |

---

## 3. Step-by-step tables

Ratings are 1–5 (5 = best). Quality and ease ratings are synthesised from the cited sources and are judgements, not benchmarks. Hardware notes refer to local runs.

### 3.1 Scripting (hook, beats, narration, on-screen text, visual prompts)

| Tool | Free? / limits | Quality | Ease of use | How Claude Code drives it | Notes |
|---|---|---|---|---|---|
| **Claude Code by itself: YES** | Included in Pro/Max subscription; uses the shared 5-hour and weekly limits ([support](https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-max-or-ultra-plan)) | 5 | 5 | Native. A `/write-script` skill writes `script.json`; headless `claude -p --json-schema` returns schema-valid output ([headless docs](https://code.claude.com/docs/en/headless)) | Use plan-before-build with beat sheet and fact checks, about 100 words per 40 s, and a hook/setup/reveal/twist/loop grammar ([LearnWithHasan](https://learnwithhasan.com/guide/how-to-make-faceless-youtube-shorts-with-claude-code/)). Fact-check: AI history channels are being called out for errors ([fern summary](https://youtubesummary.com/summary/-Gnrp_caPvo)) |
| Gemini API free tier (only to save Claude quota) | Flash models "Free of charge"; RPM/RPD shown only in AI Studio; free-tier data "used to improve our products" ([Gemini pricing](https://ai.google.dev/gemini-api/docs/pricing)) | 4 | 4 | Python/REST script called by the pipeline | Don't send private data |
| Groq Free | gpt-oss-120b: 30 RPM, 1K RPD, 200K tokens/day ([Groq](https://console.groq.com/docs/rate-limits)) | 3.5 | 4 | OpenAI-compatible REST | Fast fallback |
| Ollama local (gpt-oss:20b, Gemma 4, Qwen 3.x) | Unlimited; gpt-oss:20b is 14 GB and runs in about 16 GB of memory ([Ollama](https://ollama.com/library/gpt-oss)) | 3 | 3 | `ollama run` / local REST | LM Studio recommends 16 GB RAM and 4 GB VRAM ([LM Studio](https://lmstudio.ai/docs/app/system-requirements)) |
| OpenRouter `:free` models | 20 RPM; 50 RPD (1,000 RPD after a one-time $10 purchase) ([OpenRouter](https://openrouter.ai/docs/api-reference/limits)) | varies | 4 | REST | Tightest daily cap |

### 3.2 TTS / voiceover

| Tool | Free? / limits | Quality | Ease of use | How Claude Code drives it | Notes |
|---|---|---|---|---|---|
| **Claude Code by itself: PARTLY** | It cannot speak, but it installs and runs local TTS end to end | — | — | `pip install` plus a ~20-line script | Open TTS is below ElevenLabs in naturalness (compare Elo ranks below); ElevenLabs is the paid add-on most creator repos and tutorials use ([LearnWithHasan](https://learnwithhasan.com/guide/how-to-make-faceless-youtube-shorts-with-claude-code/)) |
| **Kokoro-82M** (default) | Free, local, **Apache-2.0**, commercial OK ([HF](https://huggingface.co/hexgrad/Kokoro-82M)) | 3.5 (AA arena Elo 1060) ([AA](https://artificialanalysis.ai/text-to-speech/leaderboard/provider-voice/open-weights)) | 4 | `pip install kokoro soundfile` + `espeak-ng` ([README](https://github.com/hexgrad/kokoro)) | **CPU works.** 54 voices (20 US and 8 UK English); other languages are thin; no cloning ([yaps.ai](https://www.yaps.ai/blog/best-local-tts-models)). Kokoro-FastAPI returns per-word timestamps ([GitHub](https://github.com/remsky/Kokoro-FastAPI)) |
| **Chatterbox** (Turbo / Nano / Multilingual V3) | Free, **MIT** ([HF](https://huggingface.co/ResembleAI/chatterbox)) | 3.5 (Elo 1020) | 3 | `pip install chatterbox-tts` | Voice cloning; Turbo supports `[laugh]` tags; Multilingual V3 covers 23+ languages; **Nano runs 3x realtime on 8 CPU cores**; others want a GPU ([README](https://github.com/resemble-ai/chatterbox)). "Beats ElevenLabs" claims come from vendor tests |
| **Qwen3-TTS** (0.6B/1.7B) | Free, **Apache-2.0** | 4 | 3 | pip + script | 10 languages, cloning from ~3 s; CUDA GPU recommended ([yaps.ai](https://www.yaps.ai/blog/best-local-tts-models)) |
| **edge-tts** | Free, no key; uses Microsoft's online service (unofficial client) | 3.5 | 5 | One CLI: `edge-tts --text … --write-media out.mp3 --write-subtitles out.srt` ([PyPI](https://pypi.org/project/edge-tts/)) | **Fragile:** versions ≤7.2.7 got HTTP 403 after Microsoft's mid-Oct 2026 change; use ≥7.3.1 ([issue](https://github.com/NousResearch/hermes-agent/issues/140990)). Commercial terms of the service are unverified |
| Google Cloud TTS free tier | 1M chars/mo Chirp 3 HD; 4M WaveNet/Standard; **billing account required** and you're auto-charged beyond the free amount ([Google](https://cloud.google.com/text-to-speech/pricing)) | 4 | 3 | gcloud auth + REST | Official, but needs a card on file |
| Fish Audio Drama 3 (open weights) | Free **only under US$500k annual revenue**; non-commercial otherwise ([LICENSE](https://huggingface.co/fishaudio/drama-3/raw/main/LICENSE)) | 5 (Elo 1277, #1) | 1 | pip + GPU | Needs roughly a **48 GB GPU** (secondary source) ([oflight](https://www.oflight.co.jp/en/columns/fish-audio-drama-3-requirements-license-guide-2026)) |
| ElevenLabs Free / Starter | Free: 10k credits/mo ≈ 10k characters, i.e. a handful of Reels. "Commercial License" starts at **Starter, $6/mo (PAID)** ([ElevenLabs](https://elevenlabs.io/pricing)) | 5 | 5 | Official MCP ([GitHub](https://github.com/elevenlabs/elevenlabs-mcp)) or API | Third-party guides say Free is **NC and needs attribution** ([dupple](https://dupple.com/learn/is-elevenlabs-free)); the official page doesn't say. Free alternative: Kokoro/Chatterbox |
| Avoid on monetised accounts | F5-TTS (weights **CC-BY-NC**), XTTS-v2 (**NC**, Coqui licence [OLDER]) ([yaps.ai](https://www.yaps.ai/blog/best-local-tts-models)) | — | — | — | Piper is GPL with per-voice licences, so commercial status is unclear |

**India note.** This research did not confirm **Hindi** voice quality or support for any free model. Test Hindi/Hinglish before committing. Kokoro's non-English coverage is thin.

### 3.3 Image generation

| Tool | Free? / limits | Quality | Ease of use | How Claude Code drives it | Notes |
|---|---|---|---|---|---|
| **Claude Code by itself: PARTLY** | Free | 3 for designed graphics, 0 for photoreal | 5 | Writes SVG/HTML/CSS/Canvas, renders with Playwright screenshots or Pillow | Strong for text cards, diagrams, charts and kinetic type. It **cannot make photoreal pixels**; for those it drives a local or free image model (rows below) |
| **ComfyUI + Z-Image-Turbo** | Free, local, **Apache-2.0** | 4 | 3 | Python client against ComfyUI's `POST /prompt` / `GET /history` HTTP API ([ComfyUI routes](https://docs.comfy.org/development/comfyui-server/comms_routes.md)) | 6B parameters, 8 steps, "fits comfortably within 16G VRAM" ([HF](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo)); quantised builds run in about 6 GB (3rd-party) |
| **FLUX.2 [klein] 4B** | Free, local, **Apache-2.0** | 4 | 3 | Same ComfyUI route | About 13 GB VRAM (RTX 3090/4070); handles editing and multi-reference ([HF](https://huggingface.co/black-forest-labs/FLUX.2-klein-4B)) |
| **Cloudflare Workers AI** (no GPU needed) | **10,000 neurons/day free**, resets 00:00 UTC; FLUX.1 schnell, FLUX.2 klein 4B ([Cloudflare](https://developers.cloudflare.com/workers-ai/platform/pricing/)) | 3.5 | 4 | REST call from Python | My estimate from published rates is about 150 schnell images/day; verify actual billing |
| Qwen-Image / Qwen-Image-2512 | Free, Apache-2.0 ([HF](https://huggingface.co/api/models/Qwen/Qwen-Image)) | 4 | 2 | ComfyUI | Heavier |
| FastSD CPU | Free | 2 | 3 | CLI | 0.82 s per 512² image on a desktop i7 with SDXS; quality well below FLUX-class ([README](https://github.com/rupeshs/fastsdcpu/blob/main/Readme.md)) |
| Manual web apps: Gemini app, Ideogram, Leonardo, ChatGPT, Bing/Copilot, Meta AI | Gemini ≈20 Nano Banana 2 images/day (3rd-party) ([laozhang](https://blog.laozhang.ai/en/posts/nano-banana-2-limits-daily-quotas-guide)); Ideogram 30 credits/week with Google/Apple/MS signup ([docs](https://docs.ideogram.ai/plans-and-pricing/available-plans)); Leonardo 150 tokens/day ([dev.to](https://dev.to/techsifted/leonardo-ai-pricing-2026-free-credits-paid-plans-and-api-costs-16a2)); ChatGPT ≈2–3/day ([CometAPI](https://www.cometapi.com/how-many-images-can-you-create-with-chatgpt-free-in-2026/)) | 4–5 | 5 | **Can't**: no free API, so manual download into `assets/` | Commercial rights are unclear or restricted: Bing requires an application for commercial use ([Microsoft](https://microsoft.ai/news/introducing-mai-image-2/)); Meta AI output is watermarked |
| Gemini API image models | **PAID**: no free tier on any image model, e.g. Nano Banana 2 at $0.067 per 1K image ([AI Studio pricing](https://aistudio.google.com/docs/pricing)) | 5 | 4 | API | Free alternative: Cloudflare Workers AI or local Z-Image |
| Pollinations | Needs an `sk_` key and "Pollen" credits; free Pollen only via Quests ([APIDOCS](https://raw.githubusercontent.com/pollinations/pollinations/main/APIDOCS.md)) | 3.5 | 4 | OpenAI Images API | No longer keyless; older guides are outdated |
| **NC / restricted, avoid if monetising** | FLUX.2 [dev] and klein 9B (**NC**) ([HF](https://huggingface.co/api/models/black-forest-labs/FLUX.2-dev)); Qwen-Image-2.1 (**research-only**) ([HF](https://huggingface.co/api/models/Qwen/Qwen-Image-2.1)); MiniMax H3-Image (excludes EU/UK/S.Korea/USA, needs written authorisation above $1M revenue, datacenter GPU) ([HF](https://huggingface.co/MiniMaxAI/MiniMax-H3-Image)); FLUX 3 Klein (reportedly free under $5M revenue, licence text gated) ([VentureBeat](https://venturebeat.com/ai/black-forest-labs-opens-flux-3-image-klein-weights-with-free-commercial-use-limited-to-smaller-businesses)) | — | — | — | India is not in H3-Image's excluded list, but its hardware needs rule it out anyway |

### 3.4 Video generation

| Tool | Free? / limits | Quality | Ease of use | How Claude Code drives it | Notes |
|---|---|---|---|---|---|
| **Claude Code by itself: PARTLY** | Free | 4 for motion graphics; 0 for AI footage | 4 | Code-rendered animation (HyperFrames, Remotion, three.js, Manim); FFmpeg zoom/pan on stills | HyperFrames: headless Chrome seeks each frame and FFmpeg encodes; Node 22+ ([README](https://github.com/heygen-com/hyperframes)). Cannot generate AI footage |
| **Wan 2.2 TI2V-5B** (local) | Free, **Apache-2.0** [OLDER, Jul 2025, still the best Apache video model] | 3.5 | 2 | ComfyUI HTTP API or Python script | 720p/24 fps. The official card says 24 GB VRAM; ComfyUI says it "should fit well on 8GB" with offload ([HF](https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B), [ComfyUI](https://docs.comfy.org/tutorials/video/wan/wan2_2.md)). Takes about **5–12 min per 5 s clip on an RTX 3060** (3rd-party) ([localaimaster](https://localaimaster.com/blog/local-text-to-video-low-vram)) |
| Wan 2.2 14B I2V "Rapid" distilled | Free, Apache-2.0 | 4 | 2 | ComfyUI | 111 s per clip on an 8 GB RTX 4060 ([lilting.ch](https://lilting.ch/en/articles/wan22-comfyui-rtx4060-i2v)) |
| HunyuanVideo 1.5 | Free; **Tencent community licence**, so read the terms before monetising | 4 | 2 | ComfyUI / Wan2GP | 14 GB minimum with offload, or 6 GB via Wan2GP; about 75 s for a 480p I2V clip on an RTX 4090 ([HF](https://huggingface.co/tencent/HunyuanVideo-1.5)) |
| LTX-2.5 | Free under **US$10M** revenue ([licence](https://github.com/Lightricks/LTX-2/blob/main/LICENSE-2_x)) | 4 | 1 | ComfyUI | Needs a 32 GB+ GPU (3rd-party) |
| Kaggle (free cloud GPU) | About 30 GPU-hours/week on a P100 16 GB or 2×T4 (3rd-party) ([gpuperhour](https://gpuperhour.com/blog/free-cloud-gpus-and-credits)) | — | 2 | Notebook scripts | Best free option if you have no GPU. Colab free bars web-UI-centric use ([Colab FAQ](https://research.google.com/colaboratory/faq.html)) |
| **Google Flow** (Veo 3.1 / Omni) | 50 credits/day free ([Flow](https://labs.google/flow)), about 2–5 clips; **720p cap**; no visible watermark (3rd-party) ([veo3ai](https://www.veo3ai.io/blog/is-google-flow-free)) | 5 | 5 | **Can't**: manual only; Claude writes the prompts | Free-tier commercial terms are unconfirmed. This is the creators' favourite free route ([Mark Ai Guy](https://www.youtube.com/watch?v=H8FAaKeCguA)) |
| Kling / PixVerse / Hailuo / Vidu free tiers | Kling ≈66 credits/day ≈2 clips; all **watermarked, 720p, NC** on free ([Vidu blog](https://www.vidu.com/blog/free-ai-animation), [marcandrews](https://marcandrews.com/kling-ai-free-plan-2026-what-66-credits-buys/)) | 4–5 | 5 | Can't | **NC: unusable for a monetised account.** Credit figures conflict between sources |
| Grok Imagine | Free video access inconsistent: paywalled 19 Mar 2026, partly restored 21 Aug, some cut off 5 Sep ([roborhythms](https://www.roborhythms.com/is-grok-imagine-free/)) | 4 | 5 | Can't | Older tutorials cite "~10 free/day"; treat that as outdated |
| Sora | **Discontinued** (announced 24 Mar 2026) ([Axios](https://www.axios.com/2026/03/24/openai-discontinue-sora-video-app)) | — | — | — | — |
| Higgsfield, Kling paid, Gemini Omni API | **PAID** (Gemini Omni ≈$0.07/s at 720p, no free tier) ([AI Studio](https://aistudio.google.com/docs/pricing)) | 5 | 4 | Higgsfield MCP/CLI ([Zinho](https://www.youtube.com/watch?v=zXE_PpJ5WUc)) | Free alternative: local Wan 2.2 I2V or code-rendered motion |

**Hardware guide** ([synthesised from cited cards](https://docs.comfy.org/tutorials/video/wan/wan2_2.md)):

| Hardware | Images | Video |
|---|---|---|
| CPU-only laptop | Code graphics; Cloudflare free API; FastSD (low quality) | **No AI video.** Use stock footage plus code motion |
| 8 GB VRAM | Z-Image / klein 4B quantised | Wan 2.2 5B with offload, or 14B Rapid |
| 12–16 GB | Z-Image FP8/bf16 | HunyuanVideo 1.5 at 480p |
| 24 GB | Everything consumer-class | LTX-2.3 int8 |

**Tip:** image-to-video beats text-to-video for control. Make the still locally, then animate it.

### 3.5 Stock footage

| Tool | Free? / limits | Quality | Ease of use | How Claude Code drives it | Notes |
|---|---|---|---|---|---|
| **Claude Code by itself: PARTLY** | It has no footage, but writes and runs the API client the moment you give it a free key | — | 5 | Python `requests` with `orientation=portrait` and min-duration filters | Log source and creator in `sources.json` |
| **Pexels API** | Free key; 200 req/h, 20,000/month; licence allows commercial use, "Attribution is not required" ([API](https://www.pexels.com/api/documentation/), [licence](https://www.pexels.com/license/)) | 4 | 5 | `GET /v1/videos/search` | API terms ask for "a prominent link to Pexels". No identifiable people in a bad light |
| **Pixabay API** | Free key; 100 req/60 s; cache responses 24 h; download, don't hotlink ([API](https://pixabay.com/api/docs/)) | 3.5 | 5 | `/api/videos/` | No attribution; no trademark/brand commercial use ([licence](https://pixabay.com/service/license-summary/)) |
| Coverr | Free API (REST and MCP); free-tier apps must credit Coverr and the creator and report downloads ([licence](https://coverr.co/license)) | 3.5 | 4 | REST or MCP | No Content ID claims allowed on Coverr clips |
| Mixkit | Free licence covers social media commercial use; **"Restricted" clips are NC** ([Mixkit](https://mixkit.co/license/)) | 4 | 3 | Manual download (no API) | Check each clip |

### 3.6 Word-level captions

| Tool | Free? / limits | Quality | Ease of use | How Claude Code drives it | Notes |
|---|---|---|---|---|---|
| **Claude Code by itself: YES** (with open-source ASR it installs) | Free | 4 | 4 | Installs faster-whisper, writes captions.json, then writes an FFmpeg ASS "karaoke" file and burns it in | Since the script is known, the TTS timestamps (Kokoro-FastAPI, edge-tts SRT) or forced alignment (WhisperX) are cheapest ([WhisperX](https://github.com/m-bain/whisperX)) |
| **faster-whisper** | Free, MIT; CPU INT8 OK | 4 | 4 | Python, `word_timestamps=True` | "Up to 4 times faster than openai/whisper" ([README](https://github.com/SYSTRAN/faster-whisper)) |
| WhisperX | Free | 4.5 | 3 | Python | wav2vec2 alignment for accurate word timings ([README](https://github.com/m-bain/whisperX)) |
| whisper.cpp | Free | 4 | 3 | CLI | Good on Mac or CPU-only; used by Remotion's TikTok template ([template](https://github.com/remotion-dev/template-tiktok)) |
| **pycaps** | Free, MIT, alpha; Python 3.10–3.12 + FFmpeg | 4 | 4 | CLI or Python; install from GitHub | CSS-styled word highlighting, pop/fade animations; targets Reels ([README](https://github.com/francozanardi/pycaps)) |
| Remotion `createTikTokStyleCaptions()` | Free for individuals and companies of up to 3 people ([licence](https://www.remotion.dev/docs/license/pricing)) | 5 | 3 | Node/React code | Word-by-word paging ([docs](https://www.remotion.dev/docs/captions/create-tiktok-style-captions)) |
| CapCut auto-captions | **Freemium/partly PAID**. CapCut's own pages conflict ("free automatic captions" vs "exclusive to Pro"); Pro costs $19.99/mo ([AllAble](https://www.allable.ai/blog/capcut-pricing/)) | 4 | 5 | Can't (GUI) | Free alternative: pycaps/FFmpeg. A 2025 ToS controversy over content licensing [OLDER] ([TechRadar](https://www.techradar.com/pro/popular-video-editing-app-capcut-wants-to-use-any-content-you-produce-for-free-forever-heres-what-you-should-know)) |

### 3.7 Royalty-free music and SFX

| Tool | Free? / limits | Quality | Ease of use | How Claude Code drives it | Notes |
|---|---|---|---|---|---|
| **Claude Code by itself: PARTLY** | — | — | — | Can't find licensed music on its own (most libraries need a login and have no API). It can pick from a library you curate, or run a local generator | Bake audio into the MP4; API posts can't tag licensed music ([Meta](https://developers.facebook.com/docs/instagram-platform/instagram-graph-api/reference/ig-user/media)) |
| **ACE-Step 1.5** (music generation) | Free, **MIT**; "You can strictly use the generated music for commercial purposes" ([HF](https://huggingface.co/ACE-Step/Ace-Step1.5)) | 4 | 3 | Transformers/Diffusers script | **Under 4 GB VRAM**; under 10 s per song on an RTX 3090. One review calls it NC, which conflicts with the card ([usefulai](https://usefulai.com/models/music-generation)) |
| HeartMuLa | Free, Apache-2.0 (the MuLaCover variant is **NC**) ([GitHub](https://github.com/HeartMuLa/heartlib)) | 4 | 2 | Python | Lyrics control |
| Stable Audio Open | Free only under **US$1M** revenue; must register ([licence](https://stability.ai/community-license-agreement)) | 3.5 | 3 | Python | Music and SFX up to 47 s |
| **Pixabay music** | Free, no attribution ([licence](https://pixabay.com/service/license-summary/)) | 3.5 | 4 | Manual download into `music/` | **May trigger Content ID claims**; keep your licence proof ([FAQ](https://pixabay.com/service/faq/)) |
| **Mixkit music and SFX** | Free licence, social media commercial use OK ([Mixkit](https://mixkit.co/license/)) | 3.5 | 4 | Manual | — |
| **Freesound** | Free; **CC0** = anything; CC BY = credit; **CC BY-NC = NC** ([FAQ](https://freesound.org/help/faq/#licenses)) | 3 | 3 | API with a free key (unverified) or manual | Filter to CC0 |
| Incompetech (Kevin MacLeod) | Free with credit (CC BY) ([licence](https://incompetech.com/music/royalty-free/licenses/)) | 3.5 | 4 | Manual | Put the credit in the caption |
| Instagram **Sound Collection** | Free, 14,000+ tracks, "royalty free", commercial OK; Instagram/Facebook only ([Instagram Help](https://www.facebook.com/help/instagram/402084904469945)) | 4 | 5 (in-app) | **Can't**: added in the app | The licence doesn't travel to TikTok/YouTube ([Fox Music](https://www.foximusic.com/blog/instagram-reels-music-copyright-legal-guide/)) |
| Uppbeat Free | 3 downloads upfront, then 1/month; needs a credit ([help](https://fastly-f.uppbeat.io/help-center)) | 4 | 3 | Manual | Too small for daily posting |
| YouTube Audio Library | Free on YouTube; **off-YouTube (Instagram) use not granted** by Google's page ([help](https://support.google.com/youtube/answer/3376882)) | 4 | 4 | Manual | Creators use it anyway ([E'Calm](https://youtubesummary.com/summary/srDpvEnGQg4)); risky for Reels |
| MOSS-SoundEffect v2.0 (SFX generation) | Free, Apache-2.0; up to 30 s at 48 kHz; CUDA ([HF](https://huggingface.co/OpenMOSS-Team/MOSS-SoundEffect-v2.0)) | 3.5 | 2 | pip install -e + script | The card is silent on output use |
| **NC: avoid** | MusicGen (**CC-BY-NC**) [OLDER] ([HF](https://huggingface.co/facebook/musicgen-small)); MMAudio (**CC-BY-NC**) ([HF](https://huggingface.co/hkchengrex/MMAudio)); FMA BY-NC tracks ([FMA](https://freemusicarchive.org/License_Guide)) | — | — | — | Epidemic Sound (common affiliate in tutorials) is **PAID**; the free alternative is ACE-Step or Pixabay |

### 3.8 Editing / assembly and 9:16 export

| Tool | Free? / limits | Quality | Ease of use | How Claude Code drives it | Notes |
|---|---|---|---|---|---|
| **Claude Code by itself: YES** | Free | 4 | 4 | Writes and runs FFmpeg/MoviePy/HyperFrames/Remotion; renders test frames to check itself ([LearnWithHasan](https://learnwithhasan.com/guide/how-to-make-faceless-youtube-shorts-with-claude-code/)) | Cuts B-roll to word-timestamp beats, burns captions, ducks music, exports to the Meta spec |
| **FFmpeg** | Free | 4 | 3 (for humans), 5 (for Claude) | Bash | Many FFmpeg MCP servers are stale [OLDER]; Bash is simpler ([video-audio-mcp](https://github.com/misbahsy/video-audio-mcp)) |
| MoviePy 2.2.1 | Free | 3.5 | 4 | Python | Used by MoneyPrinter and ShortGPT ([GitHub](https://github.com/Zulko/moviepy)) |
| **HyperFrames** | Free, **Apache-2.0**, "no per-render fees or commercial thresholds" | 4.5 | 4 | Claude Code plugin with 9 skills; `npx hyperframes init/preview/render` ([README](https://github.com/heygen-com/hyperframes)) | Node 22+ and FFmpeg |
| **Remotion** | Free for individuals and companies of up to 3, including automation; 4+ people **PAID** (from $100/mo for Automators) ([FAQ](https://www.remotion.dev/docs/license/faq.md), [pricing](https://www.remotion.dev/docs/license/pricing.md)) | 5 | 3 | Official Agent Skills ([GitHub](https://github.com/remotion-dev/skills)) | Without skills, Claude "may generate buggy or outdated Remotion code" (3rd-party) ([Nemo Video](https://www.nemovideo.com/blog/remotion-agent-skills-claude-code-guide)) |
| MoneyPrinterTurbo (turnkey) | Free, MIT; 143.8k★ | 3.5 | 4 | Claude Code installs and configures it (Docker/Python) | Topic → 9:16 1080×1920 with Edge TTS, Pexels, Whisper subtitles. Point its LLM at Gemini free or Ollama, **not** an Anthropic API key, which is pay-as-you-go ([README](https://github.com/harry0703/MoneyPrinterTurbo)) |
| CapCut | Freemium; **Pro is PAID** ($19.99/mo) | 4.5 | 5 | Can't drive it directly; one creator's free skill edits CapCut project files ([Matt Loui](https://www.youtube.com/watch?v=5N1moUCsVhI)) | Free alternative: FFmpeg/HyperFrames |

**Export to Instagram's spec** ([Meta media reference](https://developers.facebook.com/docs/instagram-platform/instagram-graph-api/reference/ig-user/media)):

- **Container:** MP4/MOV, with the moov atom at the front and no edit lists.
- **Video:** H.264/HEVC, progressive, closed GOP, 4:2:0, 23–60 fps, max 1920 px, VBR ≤25 Mbps, 9:16 recommended.
- **Audio:** AAC ≤48 kHz, 128 kbps.
- **Length and size:** 3 s to 15 min, ≤300 MB.

A safe command (my derivation from that spec):

```
ffmpeg -i in.mp4 -vf "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2" -r 30 -c:v libx264 -profile:v high -pix_fmt yuv420p -b:v 10M -maxrate 12M -bufsize 20M -c:a aac -b:a 128k -ar 48000 -movflags +faststart out.mp4
```

### 3.9 Thumbnail / Reel cover

| Tool | Free? / limits | Quality | Ease of use | How Claude Code drives it | Notes |
|---|---|---|---|---|---|
| **Claude Code by itself: YES** | Free | 4 | 5 | HTML/CSS template rendered at 1080×1920 with Playwright, or composited with Pillow; uses a Reel frame or Pexels photo as background | Meta spec: JPEG ≤8 MB, sRGB, 9:16. A 1:1 centre crop shows when shared to feed, so **keep the title in the central 1080×1080** ([Meta](https://developers.facebook.com/documentation/instagram-platform/instagram-graph-api/reference/ig-user/media.md)). Profile-grid crop is disputed (3:4 vs 4:5) ([Hootsuite](https://blog.hootsuite.com/instagram-reels-cover/)) |
| Canva free / Photopea | Free (Canva watermark-free without Pro assets, 3rd-party) ([aicomparison](https://aicomparison.ai/free-ai-video-generators/)) | 4 | 5 | Can't (manual) | Manual fallback |
| Local Z-Image background | Free (GPU) | 4 | 3 | ComfyUI API | Optional |

Attach the cover with `cover_url` (a public JPEG) or `thumb_offset` when posting via the API ([Meta](https://developers.facebook.com/documentation/instagram-platform/instagram-graph-api/reference/ig-user/media.md)).

### 3.10 Scheduling / posting

| Tool | Free? / limits | Quality | Ease of use | How Claude Code drives it | Notes |
|---|---|---|---|---|---|
| **Claude Code by itself: PARTLY** | Free | — | 3 | Calls the official API with curl/Python once you set up a Meta app and token. It **cannot** operate the Instagram app or Business Suite | Keep publishing human-triggered (a manual-only skill) |
| **Instagram Content Publishing API** | Free (no fee in the docs); Business or Creator account; **Standard Access is enough for your own account, so no App Review**; 100 posts/24 h (another section says 50; check `content_publishing_limit`); 400 containers/24 h ([Content Publishing](https://developers.facebook.com/docs/instagram-platform/content-publishing/), [Overview](https://developers.facebook.com/docs/instagram-platform/overview)) | 5 | 2 | `POST /media` (REELS, video_url) → poll `status_code` → `POST /media_publish` | Instagram Login needs a **publicly hosted MP4 URL**; resumable upload is only for Facebook Login. Long-lived token lasts 60 days. Supports `is_ai_generated`, `trial_params`, `cover_url` |
| Instagram app scheduler | Free; up to 75 days ahead, about 25/day (secondary sources, unverified) ([Socialbu](https://socialbu.com/blog/schedule-instagram-reels-and-posts)) | 5 | 5 | Can't | **The best v1 choice.** Lets you add trending audio |
| Meta Business Suite / Planner | Free; window disputed (75 vs 29 days); reportedly can't add licensed trending audio ([Sprout](https://sproutsocial.com/insights/schedule-instagram-reels/), [Planable](https://blog.planable.io/blog/schedule-instagram-reels/)) | 4 | 4 | Can't | Desktop batch-friendly |
| Buffer Free | 3 channels, 10 queued posts each, 1 API key ([Buffer](https://buffer.com/pricing)) | 4 | 4 | REST API | Reels support on Free is unconfirmed |
| Metricool Free | 20 posts/month, 1 IG account, **Metricool MCP** ([Metricool](https://metricool.com/pricing/)) | 4 | 4 | MCP | 20/month cap |
| Postiz (self-host) | Free, **AGPL-3.0**; API, webhooks, MCP, CLI ([GitHub](https://github.com/gitroomhq/postiz-app)) | 4 | 2 | API/MCP | Good for cross-posting later; needs Docker, Postgres and Redis |
| Later | No permanent free plan (14-day trial) ([Buffer vs Later](https://buffer.com/resources/buffer-vs-later/)) | — | — | — | Skip |
| Unofficial (instagrapi, browser bots) | Free but **against Instagram's terms on automated access** ([ScrapeOps quoting ToS](https://scrapeops.io/websites/instagram/)) | — | — | — | **Ban risk; never use** |

---

## 4. Claude model comparison: Opus builds, Sonnet writes, Haiku checks

**Official facts** ([models overview](https://platform.claude.com/docs/en/about-claude/models/overview); [Claude Code model config](https://code.claude.com/docs/en/model-config)):

| | Fable 5.2 | Opus 5.5 | Sonnet 5.5 | Haiku 5.5 |
|---|---|---|---|---|
| Positioning | "Demanding reasoning and long-horizon agentic work" | "Long-running agentic coding and knowledge work" | "Best combination of speed and intelligence" | "High-volume, latency-sensitive tasks" |
| API price (input/output per MTok) | $8 / $40 | $4 / $20 | $2 / $10 | From $0.10 / $0.50 |
| Latency label | Moderate | Moderate | Fast | Fastest |
| Released (2026) | 9 Nov | 22 Sep | 28 Sep | 7 Oct |
| On a Pro subscription | **Billed to usage credits = extra spend (PAID)** ([pricing](https://claude.com/pricing)); a temporary launch promo includes it up to 50% of weekly limits ([announcement](https://www.anthropic.com/claude-fable-and-mythos-5-2)) | **Default model** in Claude Code, at medium effort | `/model sonnet` | `/model haiku` |
| Context / max output | 1M / 128K | 1M / 128K | 1M / 128K | 1M / 128K |

Benchmarks: Sonnet 5.5 nearly matches Opus 5.5 on agentic tests (Terminal-Bench 4.0: 70.6% vs 66.4%; OSWorld 2.1: 80.1% vs 81.8%). Anthropic itself says "Opus 5.5 remains clearly stronger at complex, open-ended work requiring sustained judgment" ([Sonnet 5.5](https://www.anthropic.com/claude-sonnet-5-5)). Haiku 5.5 scores 39.2% on Terminal-Bench and "pairs well with Opus 5.5 and Sonnet 5.5 as a subagent" ([Haiku 5.5](https://www.anthropic.com/claude-haiku-5-5)). A third party measured Opus 5.5 at 59.6% on Terminal-Bench against Anthropic's self-reported 66.4% (unverified secondary report) ([mixed-news](https://mixed-news.com/en/?p=32220)). **No official creative-writing or short-script benchmark exists**, so the writing ratings below are inferences from Anthropic's positioning. On speed, Artificial Analysis puts Haiku 5.5 at about 234 tokens/s and Sonnet 5.5 at about 143 tokens/s at top effort ([AA](https://artificialanalysis.ai/providers/anthropic)).

**Per-task recommendation** (Q = quality, S = speed, C = quota/cost burn; ✓ = recommended):

| Pipeline task | Fable 5.2 | Opus 5.5 | Sonnet 5.5 | Haiku 5.5 | Recommended |
|---|---|---|---|---|---|
| Design, build and debug the pipeline (Python/FFmpeg/HyperFrames/Remotion code) | Q5 S2 C5. Overkill | **Q5 S3 C4 ✓** | Q4 S4 C3 | Q2 S5 C1 | **Opus 5.5 at medium; high for hard bugs** ([model config](https://code.claude.com/docs/en/model-config)). Use `opusplan` to plan with Opus and execute with Sonnet |
| Complex animation scenes (three.js/Remotion multi-scene) | Q5. Only if Opus stalls | **✓** | Q4 | Q2 | Opus 5.5 (with Remotion/HyperFrames skills loaded) |
| Daily script (hook, beats, CTA) to a fixed template | Q5 | Q5 | **Q4.5 S4 C2 ✓** | Q3.5 | **Sonnet 5.5, low/medium effort** ([Sonnet 5.5](https://www.anthropic.com/claude-sonnet-5-5)) |
| Fact-check pass on a script | — | ✓ for sensitive topics | **✓** | Q3 | Sonnet; escalate to Opus for history, health or science |
| Hook variants, titles, Instagram caption, hashtags | — | — | Q4 | **Q3.5 S5 C1 ✓** | Haiku 5.5; Sonnet if quality lags |
| B-roll search terms / image or video prompts per beat | — | — | Q4 | **✓** | Haiku 5.5 (`/make-shot-prompts` skill) |
| Script-rules critic / QA subagent | — | — | — | **✓** | Haiku 5.5 subagent, low effort |
| Bulk batch (10+ scripts) | — | — | ✓ | **✓** | Haiku or Sonnet via `claude -p --model …`, or a free LLM (3.1) |

**The most economical mix.** On Pro, Opus 5.5 is the default, so it is already what burns your shared five-hour window. The steps:

1. **Build** in an interactive Opus session.
2. **Pin cheaper models inside the skills.** SKILL.md frontmatter takes `model: sonnet` or `model: haiku` plus `effort: low` ([skills docs](https://code.claude.com/docs/en/skills)). Subagent files take `model: haiku` ([sub-agents](https://code.claude.com/docs/en/sub-agents)).
3. **Make rendering plain Python**, so it uses no Claude quota at all.
4. **Avoid hidden spend:** never select Fable on Pro, never use `/fast` (subscribers pay for it with usage credits only) ([fast mode](https://code.claude.com/docs/en/fast-mode)), keep usage credits off, and keep `ANTHROPIC_API_KEY` unset. If that key is set, Claude Code "will use this API key… resulting in API usage charges" ([support](https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-max-or-ultra-plan)). In `-p` mode, Fable requests that bill to credits are charged **without asking** ([model config](https://code.claude.com/docs/en/model-config)).
5. **Monitor with `/usage`.** Seat-wide limits are shared across models, so switching models doesn't help once one is hit. A model-specific "Opus limit" can be worked around by switching to Sonnet ([costs](https://code.claude.com/docs/en/costs)).

**Free LLM alternatives** to save Claude usage on daily scripts:

| Option | Free limits | Catch |
|---|---|---|
| **Gemini API free tier** (Flash models) | "Free of charge"; limits shown in AI Studio | Free-tier data is used for training ([Gemini pricing](https://ai.google.dev/gemini-api/docs/pricing)) |
| **Groq** (gpt-oss-120b) | 30 RPM / 1K RPD / 200K tokens per day ([Groq](https://console.groq.com/docs/rate-limits)) | — |
| **OpenRouter** `:free` models | 50 RPD without a credit purchase ([OpenRouter](https://openrouter.ai/docs/api-reference/limits)) | Tightest daily cap |
| **Ollama local** (gpt-oss:20b, Gemma 4, Qwen 3.x) | Unlimited | Needs about 16 GB of memory ([Ollama](https://ollama.com/library/gpt-oss)) |
| Cerebras | **No permanent free tier**, only a $5 / 30-day trial ([Cerebras](https://inference-docs.cerebras.ai/support/rate-limits)) | — |

No independent benchmark ranks these for short-form script writing. Keep Claude for the scripts you care most about.

---

## 5. Automation map: render everything, gate the script and the publish

| Step | Status | Reason |
|---|---|---|
| Script writing | **Partly automatable (gate by choice)** | Claude writes reliably, but AI history and fact errors are the genre's "Achilles heel" ([magnify](https://videohighlight.com/v/PSB83EKg_oQ)). A human approves `script.json` |
| Fact-check | Partly | Claude can flag claims; a human verifies sensitive ones |
| Voiceover (local TTS) | **Fully** | Deterministic script → WAV |
| Word timestamps / captions | **Fully** | faster-whisper or TTS timestamps → ASS/pycaps |
| Code-rendered motion graphics | **Fully** (after templates exist) | Deterministic render ([HyperFrames](https://github.com/heygen-com/hyperframes)) |
| Stock B-roll selection | Partly | The API search is automatic, but relevance and visible brands/people need a glance ([Pixabay licence](https://pixabay.com/service/license-summary/)) |
| Local AI images | Fully (with GPU) / Partly | ComfyUI API is scriptable; re-rolls need judgement |
| Local AI video (Wan/Hunyuan) | Partly | Scriptable but slow (minutes per clip) and needs a GPU |
| Hosted free AI video (Flow, Kling…) | **Manual** | No free API; Gemini Omni video API has no free tier ([AI Studio pricing](https://aistudio.google.com/docs/pricing)) |
| Music (curated library / ACE-Step) | **Fully** | Pick by mood tag, or generate |
| Trending licensed Instagram audio | **Manual** | In-app only; the API can't tag licensed music ([Meta](https://developers.facebook.com/docs/instagram-platform/instagram-graph-api/reference/ig-user/media)) |
| Assembly + 9:16 export | **Fully** | FFmpeg plus an ffprobe QA hook |
| Final watch-through | **Manual** | Catches bad cuts, mispronunciations and repetition |
| Cover + caption text | **Fully** | Pillow/Playwright + Haiku |
| AI-label decision | Partly | `is_ai_generated` is settable via the API ([changelog](https://developers.facebook.com/documentation/instagram-platform/changelog)); a human decides when content is photorealistic |
| Upload / schedule | Partly (API) / Manual (app, Business Suite) | API publishing is automatable after app setup; keep a human trigger |
| Comments / community | Manual | Out of scope; automated engagement violates automation terms ([Later](https://later.com/blog/instagram-bots/)) |

---

## 6. Recommended v1 pipeline: one command, two Claude calls, the rest plain Python

### 6.1 Architecture

**Claude Code is the developer and the writer, not the render engine.** Claude Code writes every script in the repo once. After that, each Reel needs Claude for only two small, cheap jobs: writing `script.json` and writing caption/hashtags. Voice, captions, B-roll, assembly, QA and cover run as deterministic Python and FFmpeg, which costs no quota and gives repeatable results. This follows the stage-per-file pattern in the reference repos, where each stage writes a file a human can inspect ([digitalsamba](https://github.com/digitalsamba/claude-code-video-toolkit), [OpenMontage](https://github.com/OpenMontageInc/OpenMontage), [LearnWithHasan](https://learnwithhasan.com/guide/how-to-make-faceless-youtube-shorts-with-claude-code/)).

**v1 style:** narrated stock-footage Reel with word-highlight captions, a title card and background music. It needs **no GPU** (works on a typical Indian laptop) and no Node.js, and it is the same proven recipe MoneyPrinterTurbo automates ([README](https://github.com/harry0703/MoneyPrinterTurbo)).

**v1 stack:**

| Layer | Choice | Why |
|---|---|---|
| Orchestrator | Claude Code (Pro) skills + `claude -p` | Subscription, no API key |
| Script | `/write-script` skill (Sonnet 5.5, low effort) | Cheap and good |
| Voice | Kokoro-82M (fallback: edge-tts ≥7.3.1) | Apache-2.0, CPU |
| Timing / captions | faster-whisper (`small`, CPU int8) → ASS karaoke via FFmpeg (or pycaps) | Free, word-level |
| B-roll | Pexels + Pixabay APIs (portrait) | Free keys, commercial OK |
| Music / SFX | Hand-curated `assets/music/` from Pixabay, Mixkit and Freesound CC0, each with a `LICENSES.csv` row | No Content ID surprises |
| Assembly / export | FFmpeg (Meta-spec command above) | Universal |
| Cover | Pillow (or Playwright HTML template) | Repeatable brand look |
| QA | `qa.py` (ffprobe: 1080×1920, fps, duration, audio present) | Fail fast |
| Upload | **Manual** in the Instagram app (v1) | Allows trending audio and the AI toggle; zero ban risk |

**Fastest working baseline (optional, one afternoon).** Ask Claude Code to install **MoneyPrinterTurbo** (MIT), configured with Edge TTS, Pexels and a Gemini free or Ollama LLM. Use it to see a complete Reel before building your own ([README](https://github.com/harry0703/MoneyPrinterTurbo)). Your own repo is still better long-term: it is smaller, you understand it, and it is easier to make original.

### 6.2 Folder layout

```
reels-factory/
  CLAUDE.md                  # rules: stop after script for approval; never upload; spec; brand voice
  brand.md                   # fonts, colours, caption style, pacing, banned phrases
  config/pipeline.yaml       # size=1080x1920, fps=30, max_seconds=45, tts=kokoro, voice=af_heart
  .env                       # PEXELS_API_KEY, PIXABAY_API_KEY  (NO ANTHROPIC_API_KEY!)
  .claude/
    settings.json            # permission allowlist + hooks
    skills/
      make-reel/SKILL.md     # orchestrator (disable-model-invocation: true)
      write-script/SKILL.md  # model: sonnet, effort: low -> script.json (schema)
      shot-prompts/SKILL.md  # model: haiku -> b-roll queries / image prompts
      publish/SKILL.md       # manual-only, later: official API
    agents/
      script-critic.md       # model: haiku, effort: low - checks rules, length, facts to verify
  schemas/script.schema.json
  scripts/
    tts.py  captions.py  broll.py  music.py  assemble.py  cover.py  qa.py  render.py
  assets/music/  assets/sfx/  assets/fonts/  assets/LICENSES.csv
  work/<slug>/   # script.json, voice.wav, words.json, captions.ass, clips/, render.mp4
  out/<slug>.mp4  out/<slug>_cover.jpg  out/<slug>_caption.txt
  reel.sh        # the one command
```

### 6.3 How the Claude Code features fit

- **Skills** are the packaging unit. Custom commands have been merged into skills, and a skill can bundle scripts and set `model`, `effort`, `allowed-tools` and `disable-model-invocation` ([skills docs](https://code.claude.com/docs/en/skills)). Make `/make-reel` and `/publish` manual-only so Claude never fires them on its own. Optionally install the HyperFrames plugin or Remotion skills for v1.5.
- **Subagents** (`.claude/agents/*.md`) take a `model` and `effort` field ([sub-agents](https://code.claude.com/docs/en/sub-agents)). Use a Haiku `script-critic`, and later parallel "3 hook variants" workers. `context: fork` runs a skill in a subagent ([skills](https://code.claude.com/docs/en/skills)).
- **Hooks** are deterministic guardrails ([hooks guide](https://code.claude.com/docs/en/hooks-guide)):
  - **PostToolUse** on Write of `work/*/script.json` runs a JSON-schema validator.
  - **PostToolUse** after a render runs `qa.py`.
  - **PreToolUse** blocks any `curl` to `graph.instagram.com` outside `/publish`.
  - **Stop** sends a desktop notification when the batch finishes.
- **MCP is not needed for v1.** Bash plus Python is simpler, and most FFmpeg MCPs are stale, e.g. last push May 2025 ([video-audio-mcp](https://github.com/misbahsy/video-audio-mcp)). Add MCP later only where a vendor maintains it, for example Postiz or Metricool for scheduling, or a local ComfyUI MCP ([glama](https://glama.ai/mcp/servers/artokun/comfyui-mcp)).
- **Headless mode.** `claude -p` supports `--model`, `--output-format json`, `--json-schema`, `--allowedTools` and `--permission-mode acceptEdits`. Do **not** use `--bare`: "bare mode doesn't use your subscription login" ([headless docs](https://code.claude.com/docs/en/headless)).
- **Scheduling (later).** Desktop scheduled tasks run on your machine with local files. Cloud scheduled tasks run from a fresh clone and "draw down subscription usage" ([scheduled tasks](https://code.claude.com/docs/en/routines)).
- **Terms.** Subscription limits assume "ordinary, individual usage of Claude Code and the Agent SDK". Personal pipelines are fine, but don't build a service for others on your login ([legal](https://code.claude.com/docs/en/legal-and-compliance)). There is no numeric definition of "ordinary", so keep scheduled batches modest.

### 6.4 The one command

```bash
# reel.sh "why octopuses have three hearts"
claude -p "/make-reel $1 stage=script" --model sonnet \
  --permission-mode acceptEdits \
  --allowedTools "Read,Write,Edit,Bash(python scripts/*)"
echo "Review work/<slug>/script.json, set \"approved\": true, then press Enter"; read
python scripts/render.py work/<slug>    # TTS -> captions -> b-roll -> music -> assemble -> qa -> cover
claude -p "/make-reel $1 stage=caption" --model haiku   # caption + hashtags -> out/<slug>_caption.txt
```

Flags are from [Claude Code headless docs](https://code.claude.com/docs/en/headless). For a fully unattended render, the render half needs no Claude at all.

### 6.5 Human-in-the-loop checkpoints

| Gate | When | What you check |
|---|---|---|
| **Gate 1** | After `script.json` | Facts, hook, originality, no health/finance persona advice ([YouTube policy](https://techcrunch.com/2026/07/20/youtube-clarifies-policies-around-ai-slop-and-upsetting-videos/)) |
| **Gate 2** | After `out/<slug>.mp4` | Pronunciation, caption sync, B-roll relevance, no visible brands or logos, music level |
| **Gate 3** | At publish | AI label (on if photoreal AI video or realistic AI voice; [Meta](https://about.fb.com/news/2024/02/labeling-ai-generated-images-on-facebook-instagram-and-threads/)), caption text, cover crop |

### 6.6 Build plan (ask Claude Code to do each step; Opus in plan mode)

1. **Prerequisites.** Pro login (`/login`), Python 3.10–3.12 (pycaps needs that range) ([pycaps](https://github.com/francozanardi/pycaps)), FFmpeg, Git, `espeak-ng`. Get free Pexels and Pixabay keys. Run `env | grep ANTHROPIC` and make sure nothing is set.
2. **Scaffold.** "Create the reels-factory layout above, with CLAUDE.md rules and a script.json schema: beats[] with narration, on_screen_text, broll_query, sfx; target 35–45 s; ~100 words per 40 s" ([LearnWithHasan](https://learnwithhasan.com/guide/how-to-make-faceless-youtube-shorts-with-claude-code/)).
3. **`tts.py`.** Kokoro to `voice.wav`, with an edge-tts fallback. Listen to 3 voices and pick one in `pipeline.yaml`.
4. **`captions.py`.** faster-whisper `word_timestamps=True` to `words.json`, then an ASS file with 2–4 word pages and the current word highlighted. Fonts and colours come from `brand.md`.
5. **`broll.py`.** For each beat, search Pexels then Pixabay (portrait, duration ≥ beat length), download, and log creator and URL to `sources.json`.
6. **`music.py`.** Pick a track from `assets/music` by mood tag and duck it under the voice.
7. **`assemble.py`.** Cut and crop clips to 1080×1920 on beat boundaries from `words.json`, overlay a title card for the first 2 s, burn captions, mix audio, then run the export command from 3.8.
8. **`qa.py` and hook.** ffprobe checks wired into `.claude/settings.json` as a PostToolUse hook.
9. **`cover.py`.** 1080×1920 JPEG with the title inside the central square.
10. **Skills, critic subagent and `reel.sh`.** Run 3 test topics, fix issues with Opus, and commit to Git.
11. **Post manually** for 2–4 weeks before automating anything on the publish side.

### 6.7 Later upgrades (in order)

- **v1.5: motion graphics.** Install HyperFrames (`claude plugin install hyperframes@hyperframes`) and add 3–5 reusable scene types: animated counter, list reveal, map pin, quote card. This mixes code-made scenes with stock footage, which raises originality ([HyperFrames](https://github.com/heygen-com/hyperframes)). Remotion is the alternative; it is free while you are a team of three or fewer ([FAQ](https://www.remotion.dev/docs/license/faq.md)).
- **v2: AI stills (needs a GPU, or use Cloudflare's free tier).** ComfyUI with Z-Image-Turbo, driven from Python via `/prompt`. Animate stills with zoom/parallax and **keep each image under about 10 s** to avoid "slideshow" flags ([Eizner](https://videohighlight.com/v/8UW7TNr2S5A)).
- **v2.5: generated music.** ACE-Step 1.5 (under 4 GB VRAM), so every track is unique and claim-free ([HF](https://huggingface.co/ACE-Step/Ace-Step1.5)).
- **v3: AI video clips.** Wan 2.2 5B or 14B Rapid image-to-video on a local GPU or Kaggle, for 1–3 hero shots per Reel.
- **v3: API publishing.** Meta app with Instagram Login and Standard Access, tested with your own account. Host the MP4 at a temporary public URL. The manual-only `/publish` skill sets `is_ai_generated` and optionally `trial_params` (Trial Reels shown only to non-followers) ([Content Publishing](https://developers.facebook.com/docs/instagram-platform/content-publishing/)). Refresh the 60-day token on a schedule.
- **v4: batching and cross-posting.** A desktop scheduled task writes tomorrow's scripts for morning approval. Self-hosted Postiz handles YouTube and TikTok cross-posting ([Postiz](https://github.com/gitroomhq/postiz-app)). Don't use Instagram's Sound Collection in the master file, because its licence doesn't travel off Meta ([Fox Music](https://www.foximusic.com/blog/instagram-reels-music-copyright-legal-guide/)).

---

## 7. Risks and platform rules: originality, labels and audio decide reach

**Official Instagram API versus Meta's own tools**

The Content Publishing API works for **professional accounts only** (Business or Creator, not Personal) and offers three login setups. **Instagram Login** needs no Facebook Page ([Overview](https://developers.facebook.com/docs/instagram-platform/overview)). Publishing needs `instagram_business_basic` plus `instagram_business_content_publish`, and **Standard Access** covers app-role users, i.e. your own account. **App Review and Business Verification** are required only to serve accounts without a role on your app ([Overview](https://developers.facebook.com/docs/instagram-platform/overview)).

| Item | Detail |
|---|---|
| Rate limits | **100 posts per 24 h**, contradicted by "50" elsewhere on the same page; 400 containers per 24 h; containers expire after 24 h ([Content Publishing](https://developers.facebook.com/docs/instagram-platform/content-publishing/), [media ref](https://developers.facebook.com/docs/instagram-platform/instagram-graph-api/reference/ig-user/media)) |
| Cost | No fee appears anywhere in Meta's docs, which implies it is free, but there is no explicit statement |
| Hosting | Instagram Login apps must give a public `video_url`; resumable binary upload is only for Facebook Login |
| Recent features | Trial Reels (Dec 2025); `is_ai_generated` (22 Jun 2026); `media_audio_type` (1 Jun 2026); media URLs withheld for copyrighted/flagged video (30 Jul 2026) ([changelog](https://developers.facebook.com/documentation/instagram-platform/changelog)) |
| Meta's own schedulers | The Instagram app and Business Suite are free but UI-only. That makes them the natural v1 choice and the only route to licensed trending audio ([Planable](https://blog.planable.io/blog/schedule-instagram-reels/)) |
| Unofficial bots | Instagram's terms bar automated access "without our prior permission" ([ScrapeOps](https://scrapeops.io/websites/instagram/)). Vendor anecdotes report suspensions ([bot.space](https://www.bot.space/blog/the-dangers-of-unofficial-instagram-dm-apis-why-theyll-get-you-banned)). The official API already covers Reels, so there is no reason to risk an unofficial tool |

**Unoriginal / mass-produced content**

Since **30 April 2026**, accounts that mostly repost others' content are no longer eligible for recommendations, extending protections that already applied to Reels ([TechCrunch](https://techcrunch.com/2026/04/30/instagram-restricts-reach-of-content-aggregators-in-new-crackdown/)). What counts as original: content you create, or third-party content you "materially edit" with commentary or voiceover. Adding a watermark or changing speed does not count ([Tubefilter](https://www.tubefilter.com/2026/04/30/instagram-removes-algorithm-recommendations-repost-content-aggregator/)). A "10+ unoriginal posts in 30 days" threshold circulates, but even the blog repeating it couldn't confirm it ([Gyre](https://gyre.pro/blog/instagram-algorithm-updates-and-tips-to-boost-your-visibility)). Facebook cross-posts face Meta's July 2025 rules [OLDER, still current], under which repeat reusers lose monetisation and reach ([Facebook Creators](https://creators.facebook.com/blog/combating-unoriginal-content)).

If you cross-post to YouTube, its **16 July 2026 clarification** makes three things non-monetisable ([TechCrunch](https://techcrunch.com/2026/07/20/youtube-clarifies-policies-around-ai-slop-and-upsetting-videos/)):

- "generic, repetitive, or template-based" AI content;
- manipulative or distressing content;
- AI people discussing finance, legal or health topics.

YouTube's policy page also names image slideshows and characters "put in the same situation over and over" ([policy](https://support.google.com/youtube/answer/1311392?hl=en)). YPP thresholds rise on **1 Feb 2027**, with Shorts entry going to 20M views in 90 days ([YouTube Help](https://support.google.com/youtube/answer/12843009?hl=en)).

**Where sources disagree.** Creators insist "AI scripts, AI voiceovers, AI images… are not demonetizing channels… The pattern is the content type" ([Eizner](https://www.youtube.com/watch?v=8UW7TNr2S5A)), while the official text explicitly names AI-template content. In practice both point the same way: **vary formats, visuals, thumbnails and titles**, and make sure your one-command pipeline doesn't output the same video 100 times.

**AI labels**

- **Content label.** Meta requires disclosure for "photorealistic video or realistic-sounding audio that was digitally created or altered" and "may apply penalties" if you skip it [OLDER, Feb 2024, still current] ([Meta Newsroom](https://about.fb.com/news/2024/02/labeling-ai-generated-images-on-facebook-instagram-and-threads/)). A 2026 Help Center snippet says the requirement "does not apply to images" ([Meta Help](https://www.meta.com/help/artificial-intelligence/1783222608822690/)).
- **Practical rule.** Label Reels that contain AI video or a realistic AI voice; with the API, set `is_ai_generated=true`. Kokoro narration is realistic-sounding audio, so labelling is the safe default.
- **Profile label.** From **31 Aug 2026**, profiles featuring an AI-generated *person* must add the "AI-generated profile" label or have their reach limited. "Creators who simply use AI tools… don't need to add the label" ([Instagram Creators](https://creators.instagram.com/blog/ai-generated-profile-label)). A purely faceless account needs no profile label.
- **Ranking.** No official source says post-level AI labels reduce reach. Mosseri said "I don't think we should filter out AI content" ([SocialDay](https://socialday.live/features/instagrams-mosseri-tells-users-if-you-dont-like-ai-content-dont-use-the-feed)).

**Music copyright**

Instagram's licensed library is for personal, non-commercial use, and business accounts get the royalty-free Sound Collection ([Instagram Help](https://www.facebook.com/help/instagram/402084904469945)). API posts can tag only original audio ([media ref](https://developers.facebook.com/docs/instagram-platform/instagram-graph-api/reference/ig-user/media)). The safe approach is to **bake royalty-free or self-generated audio into the MP4** and keep licence proof. Pixabay tracks can still draw claims ([Pixabay FAQ](https://pixabay.com/service/faq/)). How Meta Rights Manager treats Pixabay, Mixkit or AI music is undocumented.

**Licence risks for monetisation**

| Category | Tools |
|---|---|
| **NC, never use** | F5-TTS, XTTS-v2, MusicGen, MMAudio, FLUX.2 [dev] and klein 9B, Qwen-Image-2.1, HeartMuLa MuLaCover, Freesound/FMA NC tracks, free Kling/Vidu/PixVerse/Hailuo output (all cited in section 3) |
| **Revenue-capped** | Drama 3 (under $500k), Stable Audio Open (under $1M), MiniMax H3/H3-Image (written authorisation above $1M), FLUX 3 Klein (under $5M, reported), LTX-2.5 (under $10M) |
| **AGPL** | OpenMontage, MoneyPrinterV2, Postiz. Fine to run privately; the obligation is source-sharing if you offer a modified version as a network service ([OpenMontage LICENSE](https://raw.githubusercontent.com/OpenMontageInc/OpenMontage/main/LICENSE)) |
| **Grey** | edge-tts (unofficial use of a Microsoft service), YouTube Audio Library on Instagram, Google Flow free-tier commercial terms |

**Monetisation reality, especially in India**

- **No per-view pay.** Instagram does not pay per view or share Reels ad revenue in India ([Influencermetric](https://influencermetric.in/blog/how-to-monetize-instagram-reels-india)).
- **Gifts** (500 followers) and **Subscriptions** (10k) are reported as available in India, and Creator Marketplace from about 1k followers. These are secondary sources; re-verify in your Professional Dashboard ([Hypee](https://www.hypee.co.in/blog/instagram-monetization-rules-india), [Kudozz](https://www.kudozz.in/blog/instagram-creator-monetization)).
- **Bonuses** are invite-only, and reports on them conflict.
- **Revenue claims are marketing.** Title figures like "$30K/month" are often vidIQ estimates of other channels ([Sanji summary](https://youtubesummary.com/summary/8Rf0xna31xg)). A real 10M-view test netted $157.48 ([Tilbury](https://videohighlight.com/v/LlhTEttKcwQ)). Creators quote Shorts RPMs of $0.07–$0.33 per 1,000.
- **Plan for:** affiliates, brand deals (use `is_paid_partnership` when posting via API; [changelog](https://developers.facebook.com/documentation/instagram-platform/changelog)) and your own products.

---

## 8. Top YouTube videos and resources

Views were observed on 16 Nov 2026. "≈" marks dates estimated from YouTube's relative labels. **Spon** = sponsored, **Aff** = affiliate. Method summaries come from descriptions and third-party transcript summaries; no full transcript was read.

**Claude/Claude Code process videos**

| # | Video | Channel | Views | Date | Method (2–3 lines) | Spon/Aff |
|---|---|---|---|---|---|---|
| 1 | [How to Make Viral Animated Shorts Using Claude (Full Workflow)](https://www.youtube.com/watch?v=OtbLL6OBNE4) | Mr omi | 1,120,816 | 2026-11-01 | Claude analyses 20 reference Shorts at 30 fps into a style bible, then renders 3D scenes in three.js plus Remotion with 7 critique sub-agents; free GitHub skill. The first draft "looked cheap" ([summary](https://youtubesummary.com/summary/OtbLL6OBNE4)). The repo name differs between sources (`claude-animated-shorts` vs a truncated link) | Skool upsell |
| 2 | [Claude Code Just Changed YouTube Forever!](https://www.youtube.com/watch?v=WODnqHPLR38) | Danny Why | 1,737,761 | ≈Jun 2026 | Claude Code with the Higgsfield CLI skill; voiceover, then Turboscribe timestamps, then a master prompt for timestamped images, then edit. Long-form oriented ([summary](https://videohighlight.com/v/WODnqHPLR38)) | **Aff Higgsfield**; Skool |
| 3 | [Claude Code (Free Plan) + YouTube = $77,000/Month](https://www.youtube.com/watch?v=WVT2FCjhDDY) | zapiwala ai | 1,211,088 | 2026-06-11 | Free stickman stack: Claude, ElevenLabs free, FoziScribe timestamps, Google Flow Nano Banana 2 bulk images, timestamp-synced edit. Images are 16:9 ([summary](https://youtubesummary.com/summary/WVT2FCjhDDY)) | Own product (Zapi Flow) |
| 4 | [Claude Edited My Entire CapCut Video](https://www.youtube.com/watch?v=5N1moUCsVhI) | Matt Loui | 984,150 | ≈Oct 2026 | Claude script, Higgsfield voice and images; Claude builds a real CapCut project with sync, music, SFX, text and zoom keyframes; free skill | **Spon Higgsfield** |
| 5 | [Claude + CapCut Completely Changes Everything For Editors](https://www.youtube.com/watch?v=8oIFBQ9BhVU) | Matt Loui | 785,308 | 2026-05-05 | Claude plus Remotion motion graphics (counters, lists, maps, text highlights) imported into CapCut | Own course; CapCut referral |
| 6 | [How To Make Faceless YouTube Shorts with Claude (Free Skill/Automation)](https://www.youtube.com/watch?v=n1N_ZIP5x3M) | Nafay 3D | 714,048 | 2026-11-01 | Free Claude skill: script, visuals, voiceover, word-synced captions; 5 preset styles; Zapier daily auto-posting | **Spon/Aff Zapier** |
| 7 | [I Tried Making a Viral Video Using ONLY Claude AI](https://www.youtube.com/watch?v=kDcxEIDC5NA) | ReachMora | ≈627,000 | 2026-11-03 | Claude skill: 10 story ideas, script, ElevenLabs voice, auto-rendered animated MP4, no CapCut | **Aff moraviral** |
| 8 | [I Made VIRAL Animation Videos Using Claude Code (FREE Plugin)](https://www.youtube.com/watch?v=3tpaWHaiLQ8) | Grow With Kaz | 435,311 | 2026-11-04 | Claude Code plus a free plugin for 2D/3D animation; ElevenLabs voice | **Aff ElevenLabs**; Skool |
| 9 | [My Claude Code System For Viral Instagram Reels](https://www.youtube.com/watch?v=JhtbnZUU_8E) | Oleg Melnikov | 162,258 | ≈Mar 2026 | **Instagram-specific.** A Claude Code app scrapes competitor Reels, analyses them with Gemini, and writes hooks and scripts; 60+ ideas from 23 Reels ([summary](https://videohighlight.com/v/JhtbnZUU_8E)) | Own agency |
| 10 | [Claude Code Can Now Automate Your Videos (Remotion + Opus 5.5)](https://www.youtube.com/watch?v=6_rCyryA6hg) | Roboverse | 126,750 | 2026-10-01 | Claude Code plus Remotion plugin; motion graphics and finished videos from prompts | None seen |
| 11 | [How to make FREE AI Videos with Claude (and Hyperframes) – Full Beginner Tutorial](https://www.youtube.com/watch?v=3sEuuAk-lYc) | Selling With Nas | 70,139 | 2026-10-12 | Install the HyperFrames plugin; prompt-only video creation | None seen |
| 12 | [How I create viral animated reels using HyperFrames + Claude Code](https://www.youtube.com/watch?v=y4YupFxhAog) | Science Based AI | 55,805 | 2026-10-03 | HyperFrames plus Claude for short-form reels at work | **Spon Typeless** |
| 13 | [Claude Code + Blotato = Automated Shorts in Minutes](https://www.youtube.com/watch?v=ZXyjSufezL8) | Koen \| AI Content Systems | 42,240 | 2026-03-29 | Claude Code plus Blotato (a rendering/posting SaaS, not free) | **Aff Blotato** |
| 14 | [Claude Code + HyperFrames = Cheapest AI Video Editor EVER](https://www.youtube.com/watch?v=xbCKxfWlIO0) | Brandon Melville | 38,615 | 2026-10-14 | HyperFrames editing; Fish Audio TTS | **Spon Fish Audio** |
| 15 | [Generate Animated Videos with Claude Code (Remotion Agent Skill Tutorial)](https://www.youtube.com/watch?v=EwKCAgt4aKI) | Snapper AI | 15,636 | 2026-01-22 | First-wave Remotion Agent Skills walkthrough | None seen |
| 16 | [How I Post 20+ Automated Instagram Reels A Day (Claude Code Tutorial)](https://www.youtube.com/watch?v=He3KS1kSwv4) | Emil Faschang | 7,197 | 2026-03-23 | Claude Code system producing and posting 20+ Reels a day. 20+ a day is exactly the volume that risks "mass-produced" flags | Skool funnel |
| 17 | [No Claude Motion? Make Videos with Claude Code + Remotion](https://www.youtube.com/watch?v=btKmUC4sw0c) | Vibe Dojo | 2,962 | 2026-10-15 | **Best beginner Windows walkthrough:** Node.js setup, animated video, prompt revisions, export | None seen |
| 18 | [Build a Quantum Energy Ladder with Claude Code + Manim](https://www.youtube.com/watch?v=13bpFftt06A) | Medhavy AI | 446 | 2026-07-11 | Claude Code writes a Manim physics animation | None seen |

**Broader faceless-AI workflow videos**

| # | Video | Channel | Views | Date | Method | Spon/Aff |
|---|---|---|---|---|---|---|
| 19 | [I Tried The LAZIEST Way to Make Money With AI](https://www.youtube.com/watch?v=LlhTEttKcwQ) | Mark Tilbury | 9,993,418 | 2026-09-21 | 3 AI Instagram influencers (Claude personas, Higgsfield media), 10 posts each; netted $157.48 ([summary](https://videohighlight.com/v/LlhTEttKcwQ)) | **Aff Higgsfield** |
| 20 | [How a Faceless Channel Made $39K With Claude + ChatGPT](https://www.youtube.com/watch?v=8Rf0xna31xg) | Sanji Nai-Chien | 1,691,835 | ≈Sep 2026 | vidIQ plus Claude topics, scene list with timestamps, RankReel voice and clips, 9:16, auto-subs, account warm-up ([summary](https://youtubesummary.com/summary/8Rf0xna31xg)) | Likely Higgsfield (RankReel) |
| 21 | [I BLEW UP a YouTube Channel in 24 Hours with AI](https://www.youtube.com/watch?v=za2VyvLl5T0) | Jack Craig | 1,427,227 | 2026-05-01 | Reverse-engineers a 6-phase "AI pet salon" formula; Higgsfield, Premiere; shows 694K views in 48 h ([summary](https://youtubesummary.com/summary/za2VyvLl5T0)) | **Aff Higgsfield** |
| 22 | [I Copied a Top Faceless Channel's Format With AI in 20 Minutes](https://www.youtube.com/watch?v=wU_bmWb6bhg) | Higgsfield AI | 1,111,713 | ≈Jul 2026 | Claude plus Higgsfield MCP; "borrow the format, not the videos"; upload stays manual ([summary](https://youtubesummary.com/summary/wU_bmWb6bhg)) | **Vendor channel** |
| 23 | [My $75K YouTube Shorts System – Full Course In 19 Minutes](https://www.youtube.com/watch?v=srDpvEnGQg4) | E'Calm | 972,236 | ≈Mar 2026 | Google AI Studio TTS (free), Nano Banana/Whisk images, Grok 9:16 video, CapCut; hook, body, reward ([summary](https://youtubesummary.com/summary/srDpvEnGQg4)) | Paid course/WhatsApp |
| 24 | [How to Create Stickman Animation with AI 100% FREE](https://www.youtube.com/watch?v=H8FAaKeCguA) | Mark Ai Guy | 600,309 | 2026-10-13 | ChatGPT master prompt, Google Flow Agent Mode batch images and 4 s animations, ElevenLabs, CapCut | **Aff Vsub** |
| 25 | [How to Make Viral Stickman Animated Shorts Using FREE AI TOOLS](https://www.youtube.com/watch?v=-fgNFJCQZGk) | Mark Ai Guy | 228,023 | 2026-11-09 | Rick's Clips style with Flow and Omni Flash clips stitched together; CapCut captions | Telegram funnel |
| 26 | [$0–$45,186 In 30 Days With Faceless YouTube Automation](https://www.youtube.com/watch?v=HOEqRYPD7sE) | Chris Barrera | 181,343 | ≈Jun 2026 | **Counterpoint:** full automation "leads to poor quality"; Claude for scripts plus human editors ([summary](https://videohighlight.com/v/HOEqRYPD7sE)) | Coaching |
| 27 | [How To Make $24,937/mo Posting YouTube Shorts (Using Claude AI)](https://www.youtube.com/watch?v=V_t51u1tBJc) | Kellan Henneberry | 1,770,360 | 2026-06-28 | Ranking compilations of viral TikTok clips via Viblo. **Policy-risky** (reused content) ([summary](https://videohighlight.com/v/V_t51u1tBJc)) | Viblo link |

**Policy and critical counterweights**

| Video | Channel | Views | Date | Gist | Spon/Aff |
|---|---|---|---|---|---|
| [The Death of Educational Content on YouTube](https://www.youtube.com/watch?v=-Gnrp_caPvo) | fern | 11,528,272 | 2026-09-02 | AI copycat "slop" networks; hallucinated history ([summary](https://youtubesummary.com/summary/-Gnrp_caPvo)) | **Spon FlexiSpot** |
| [The New Rules For Faceless Channels in 2026](https://www.youtube.com/watch?v=ye2T2FwubI4) | vidIQ | 134,571 | ≈Sep 2026 | Narrator POV, characters, recognisable visual style, expertise | Vendor |
| [YouTube ENDS Faceless AI YouTube Channels?](https://www.youtube.com/watch?v=RSnGnIWUvIQ) | Make Money Matt | 130,134 | ≈Apr 2026 | Reddit-story, celebrity and fake-trailer niches are being hit ([summary](https://youtubesummary.com/summary/RSnGnIWUvIQ)) | Unknown |
| [AI Channels Are Getting Demonetized Again, Here's How to Avoid It](https://www.youtube.com/watch?v=8UW7TNr2S5A) | Eddie Eizner | 75,510 | 2026-02-18 | Triggers: repeated thumbnails and titles, static slideshows; images ≤10 s ([summary](https://videohighlight.com/v/8UW7TNr2S5A)) | **Aff TubeGen** |
| [Creator Insider: inauthentic content clarification](https://www.youtube.com/watch?v=14Vm0CiyUVE) | Creator Insider (YouTube) | n/a | Jul 2026 | Official explainer of the July 2026 clarification | Official |
| [I BLEW UP a YouTube Channel in 7 Days with AI](https://www.youtube.com/watch?v=1r0eyM7suUg) **[OLDER]** | Jack Craig | 2,550,386 | 2025-11-21 | Predecessor of #21 | Aff Higgsfield (likely) |

**Written guides and repositories** (stars from the ungh.cc mirror, 16 Nov 2026)

| Resource | Notes |
|---|---|
| [LearnWithHasan: Faceless Shorts with Claude Code](https://learnwithhasan.com/guide/how-to-make-faceless-youtube-shorts-with-claude-code/) (2026-07-30) | Best written walkthrough. ElevenLabs is **PAID**; swap in Kokoro |
| [hassancs91/claude-faceless-shorts-creator](https://github.com/hassancs91/claude-faceless-shorts-creator) | MIT, 364★ |
| [digitalsamba/claude-code-video-toolkit](https://github.com/digitalsamba/claude-code-video-toolkit) | MIT, 2,586★. Open models on your own cloud GPU; Modal suggested |
| [OpenMontage](https://github.com/OpenMontageInc/OpenMontage) | **AGPL**, 80.7k★. Zero-key mode |
| [HyperFrames](https://github.com/heygen-com/hyperframes) | Apache-2.0, 84.8k★ |
| [remotion-dev/skills](https://github.com/remotion-dev/skills) | Official; no root LICENSE file |
| [remotion-dev/template-tiktok](https://github.com/remotion-dev/template-tiktok) | Remotion's TikTok-captions starter |
| [MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | MIT, 143.8k★. README heavily sponsored by API aggregators |
| [short-video-maker](https://github.com/gyoridavid/short-video-maker) | **[OLDER, stale since Jun 2025]**. Kokoro, Whisper, Pexels, Remotion; good reference design |
| [ShortGPT](https://github.com/RayVentura/ShortGPT) | **[OLDER, stale since Feb 2025]** |
| [awesome-claude-video-skills](https://github.com/zhuyansen/awesome-claude-video-skills) | 180 security-graded repos |
| [pycaps](https://github.com/francozanardi/pycaps) | Caption renderer |
| [Claude Code skills docs](https://code.claude.com/docs/en/skills) and [headless docs](https://code.claude.com/docs/en/headless) | Official |

---

## 9. Sources used and research limits

**What the report relied on most:**

- **Official vendor documentation**, for everything about pricing, limits and policy:
  - Anthropic's models overview, pricing, Claude Code docs (skills, headless, model config, hooks, sub-agents, costs) and support articles. These were the only authoritative source for model prices, plan inclusion and the subscription-versus-API billing trap.
  - Meta's Instagram Platform docs and changelog. These are primary for API setup, specs, rate limits and `is_ai_generated`.
  - The Instagram Creators blog for the AI-profile label.
  - Hugging Face model cards and API licence tags, and LICENSE files. Licence claims here come from these rather than blogs, because blogs frequently get licences wrong; the ACE-Step "non-commercial" claim, for example, conflicts with the MIT card.
- **GitHub READMEs** (HyperFrames, Remotion, MoneyPrinterTurbo, OpenMontage, faster-whisper, pycaps, Kokoro) for how Claude Code can drive each tool.
- **Artificial Analysis leaderboards** for TTS, image and video quality rankings. They are snapshot-dependent, and earlier snapshots show different leaders.
- **Creator evidence:** YouTube metadata plus transcript-based summaries from youtubesummary.com and videohighlight.com. These are used for *what creators do*, never for pricing.
- **Third-party blogs** only where no primary page could be fetched (Kling/PixVerse/Hailuo free tiers, Instagram scheduler limits, India monetisation thresholds). They are labelled "(3rd-party)", and several conflict.

**Method limits:**

- **YouTube bot checks** ("Sign in to confirm you're not a bot" and Google's captcha page) were **not bypassed**. Video evidence therefore comes from search-result metadata, channel **RSS feeds** (exact dates and views for each channel's latest 15 uploads only) and **third-party transcript summaries**. No full transcript was read, so no video evidence is rated high-confidence, and some dates are approximate (≈).
- **Reddit** (www and old.reddit) and BlackHatWorld were **largely unreachable (HTTP 403)**. Community sentiment comes from search snippets and creator-run communities, which skew promotional.
- **GitHub API access was blocked**, so star counts and push dates came via the **ungh.cc mirror** in places. These may lag by hours, and very high counts (HyperFrames 84.8k, OpenMontage 80.7k) weren't cross-checked. Licences were read from raw LICENSE files.
- **Instagram Help Center** pages failed to render. Scheduler limits (75 days, 25/day), music restrictions for business accounts and India monetisation thresholds rely on secondary sources.
- **Not verified:** Hindi TTS quality of any free model; INR pricing of Claude plans; Google Flow free-tier commercial rights; Meta Rights Manager behaviour on Pixabay, Mixkit or AI music; Buffer Free Reels support.

---

## 10. Beginner roadmap

**Day 1: get one Reel out by hand (about 3–4 hours)**

1. Install Claude Code and log in with your Pro account. Confirm no `ANTHROPIC_API_KEY` is set, and run `/usage` to see your limits ([support](https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-max-or-ultra-plan)).
2. Install Python 3.11, FFmpeg and Git. Get free Pexels and Pixabay API keys.
3. In an empty folder, ask Claude Code (Opus, default): "Write a 40-second Reel script about X, then generate the voice with Kokoro, get word timestamps with faster-whisper, fetch 6 portrait clips from Pexels, burn word-highlight captions, add this music file, and export 1080×1920 to Instagram's spec."
4. Watch the result, fix one thing, and post it manually from the Instagram app. Switch to a **Creator** account first if you plan to use the API later ([Overview](https://developers.facebook.com/docs/instagram-platform/overview)).
5. Build a 10-track music folder from Pixabay, Mixkit and Freesound CC0, and write each licence into `LICENSES.csv`.

**Week 1: one command, three gates, daily habit**

1. Turn Day 1's ad-hoc code into the `reels-factory` repo (section 6). Add `/write-script` (Sonnet), the Haiku `script-critic`, the `qa.py` hook and `reel.sh`.
2. Lock your `brand.md`: 2 fonts, 3 colours, one caption style, and a voice. Consistency of style is good; identical videos are not.
3. Make one Reel a day, reviewing at all three gates. Track which hooks hold viewers in Instagram Insights.
4. Optional: install MoneyPrinterTurbo (with a Gemini-free or Ollama LLM) once to compare output.

**Month 1: originality and leverage**

1. **Week 2:** install HyperFrames (or the Remotion skills) and build 3–5 reusable motion-graphic scene types. Mix them with stock footage so each Reel looks designed, not templated.
2. **Week 3:** if you have an 8 GB+ NVIDIA GPU, add ComfyUI with Z-Image-Turbo for custom stills, and optionally Wan 2.2 5B for 1–2 hero clips. If not, try Cloudflare Workers AI's free tier or Kaggle. Optionally swap library music for ACE-Step 1.5.
3. **Week 4:** decide on API publishing. Create a Meta app with Instagram Login and Standard Access, and test-publish one Reel through a manual `/publish` skill with `is_ai_generated` set correctly. Or keep using the in-app scheduler, which is still the only way to add trending licensed audio.
4. **Throughout:**
   - Keep Claude's daily use to scripts and captions; rendering is plain Python.
   - Keep posting to 1–2 Reels a day, not 20+.
   - Never give an AI persona health or finance advice.
   - Never repost others' clips.
   - Plan income around affiliates, brand deals (Creator Marketplace) and your own products, not Instagram payouts, which don't exist per view in India ([Influencermetric](https://influencermetric.in/blog/how-to-monetize-instagram-reels-india)).

**Takeaway.** The 2026 evidence shows the hard part is no longer the tools. With Claude Code, voice, captions, B-roll, assembly and posting are all free and scriptable within a week. What decides whether a faceless account survives Instagram's originality rules and YouTube's inauthentic-content rules is the human layer: fact-checked scripts, a recognisable visual identity built in code, and the discipline not to mass-produce. Build the pipeline to save time, and spend the saved time on what reviewers and algorithms now reward.
