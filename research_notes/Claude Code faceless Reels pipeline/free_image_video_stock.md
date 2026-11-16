# Free visual tooling for a faceless AI Instagram Reels pipeline driven by Claude Code (image gen, video gen, stock, covers), as of 2026-11-16

Scope notes for the report writer:
- Everything below was checked between 2026-11-14 and 2026-11-16. Primary sources (Hugging Face model cards and API, license files, official docs and pricing pages, Meta developer docs) were fetched directly where possible. Facts from third-party blogs are labelled "(3rd-party)", and conflicts are flagged.
- Information from before 2026 is marked [OLDER].
- Licence tags come from the Hugging Face API (`https://huggingface.co/api/models/<repo>`), queried on 2026-11-16.
- Several consumer apps (Kling, PixVerse, Hailuo, Vidu, Ideogram, Leonardo) block bots or render their pricing pages with JavaScript, so their free-tier numbers rest on third-party pages that disagree with each other. Treat them as approximate.

---

## Q0. What can Claude Code do alone, without any generative-image service?

### Takeaway
Claude Code can't produce photorealistic pixels itself. It can still produce a large share of a faceless Reel's visuals deterministically and for free:
- text and quote cards, kinetic typography, charts, and SVG/Canvas/HTML motion graphics
- rendered stills and frames (via Playwright screenshots or Pillow)
- the code that calls free stock APIs and free or local generation APIs
- driving a local ComfyUI server over its HTTP API, or through an MCP server

### Cited Findings
- The ComfyUI server exposes plain HTTP and WebSocket routes, so a script or agent can run it headlessly:
  - `POST /prompt` queues a workflow
  - `GET /history/{prompt_id}` returns results
  - `GET /view` fetches output images
  - `POST /upload/image` uploads inputs
  - `/ws` gives real-time progress
  — [ComfyUI docs: server routes](https://docs.comfy.org/development/comfyui-server/comms_routes.md)
- **Official Comfy Cloud MCP server:** hosted at `https://cloud.comfy.org/mcp`. It needs no local install, Claude Code can add it with an API-key header, and its `submit_workflow` tool takes API-format workflows. Access is reported as invite-only beta or private preview, so it isn't freely available to a beginner yet. — [Comfy docs: MCP server](https://docs.comfy.org/development/cloud/mcp-server.md); [mcpservers.org listing](https://mcpservers.org/servers/docs-comfy-org-agent-tools-cloud)
- **Community MCP servers for local ComfyUI:** e.g. `comfyui-mcp` and `comfyui-easy-mcp`, launched via `uvx` with `COMFY_URL=http://localhost:8188`. They can discover nodes, build and edit API workflows, run them, and fetch outputs. Gotcha: only workflows saved with "Save (API Format)" can be run this way. — [glama: artokun/comfyui-mcp](https://glama.ai/mcp/servers/artokun/comfyui-mcp); [comfyui-wiki news on Comfy MCP, 2026-06-30](https://comfyui-wiki.com/en/news/2026-06-30-comfy-mcp-agent-integration); [mcp.directory: Comfy MCP 2026](https://mcp.directory/blog/comfy-mcp)
- **Pollinations is no longer keyless.** All generation now needs an `sk_` key from enter.pollinations.ai, and usage is billed in "Pollen" credits ($1 ≈ 1 Pollen). Free Pollen is earned through "Quests"; there is no documented free daily grant. It speaks the OpenAI Images API at `https://gen.pollinations.ai/v1`, and its models include `flux.1-schnell`, `tongyi-mai/z-image-turbo` and `flux.2-klein-4b`. — [Pollinations APIDOCS.md](https://raw.githubusercontent.com/pollinations/pollinations/main/APIDOCS.md); [Pollinations README](https://raw.githubusercontent.com/pollinations/pollinations/main/README.md)
  - Older third-party posts describing an anonymous, keyless tier at 1 request per 15 s are now outdated. — [agentdeals.dev (3rd-party)](https://agentdeals.dev/vendor/pollinations-ai)
- The Meta Graph API lets code set a Reel cover with `cover_url` (a public JPEG) or `thumb_offset` (milliseconds); `cover_url` wins if both are set. A Claude-made cover can therefore be attached programmatically. — [Meta IG User Media reference](https://developers.facebook.com/documentation/instagram-platform/instagram-graph-api/reference/ig-user/media.md)

### Inferences
- **Practical split of work for Claude Code alone, all zero cost:**
  - Pillow: text overlays, cover compositing, resizing to 1080×1920
  - HTML/CSS/SVG plus Playwright `page.screenshot()`: designed cards and covers
  - Canvas, HTML or Remotion-style frames rendered to PNG sequences, then encoded by FFmpeg: animated typography
  - Python `requests`: Pexels, Pixabay and Coverr APIs
  - ComfyUI HTTP API: local diffusion
  
  The Pillow, Playwright and FFmpeg capabilities are standard library behaviour and weren't separately sourced here.
- For a beginner, an MCP server for ComfyUI is optional. Claude Code can write a ~30-line Python client against `/prompt` and `/history` directly, which avoids beta-access problems.

### Gaps
- I found no official Anthropic or Claude Code documentation listing image or video MCP servers. The MCP servers above are community projects of varying quality and weren't installed or tested.

---

## Q1. Image generation: open-weight local models (current leaders, licences, VRAM)

### Takeaway
The top of the Artificial Analysis open-weights board (Nov 2026) is now dominated by models that are either non-commercial or too large for consumer hardware:
- MiniMax H3-Image (33B DiT plus a 66.7 GB text encoder, and territory-restricted)
- Qwen-Image-2.1 (research/non-commercial licence)
- FLUX 3 Image Klein (FLUX Kommunity licence; reported free commercial use only under $5M revenue)

For a beginner who wants to monetise safely on a consumer GPU, the best picks are Apache-2.0 models:
1. **Z-Image-Turbo / Z-Image** (6B; fits 16 GB, and quantised versions fit less)
2. **FLUX.2 [klein] 4B** (~13 GB)
3. **Qwen-Image / Qwen-Image-2512** (Apache 2.0, but heavier)

FLUX.2 [dev] and FLUX.2 klein 9B are **non-commercial**.

### Cited Findings
**Leaderboard: Artificial Analysis AA-Image-T2I v2.1, open weights (fetched 2026-11-16)**

| Rank | Model | Creator | Elo | Released |
|---|---|---|---|---|
| 1 | H3-Image | MiniMax | 1066 | Nov 2026 |
| 2 | Qwen-Image-2.1 | Alibaba | 1047 | Sep 2026 |
| 3 | FLUX 3 Image Klein | BFL | 1041 | Oct 2026 |
| 4 | Fibo 2.0 | Bria | 1037 | Oct 2026 |
| 5 | Ideogram 4.0 (Quality) | Ideogram | 1026 | Jun 2026 |
| 7 | Ming-Image-0.1-Design | InclusionAI | 1001 | Sep 2026 |
| 8 | FLUX.2 [dev] (anchor model) | BFL | 1000 | Nov 2025 |
| 10 | Cosmos3-Super-Text2Image | NVIDIA | 995 | May 2026 |
| 12 | HunyuanImage 3.0 Instruct | Tencent | 986 | Jan 2026 |

— [AA open-weights T2I leaderboard](https://artificialanalysis.ai/image/leaderboard/text-to-image/open-weights)

- **Disagreement:** search snippets of earlier AA snapshots show different leaders, e.g. Qwen-Image-2.1 first at 1035 as of 2026-10-07, and FLUX 3 first at 1,119 on a mixed open and proprietary scale. Leaderboard versions (v2.0 vs v2.1) and dates differ. — [AA leaderboard (open-weights filter)](https://artificialanalysis.ai/image/leaderboard/text-to-image?open-weights=true); [alphasignal: Qwen-Image-2.1 tops two open-weight boards](https://alphasignal.ai/news/alibaba-s-qwen-image-2-1-tops-two-open-weight-image-leaderboards); [theopenweights.com leaderboards](https://theopenweights.com/leaderboards)

**Licences and sizes, verified via the HF API and model cards**
- **MiniMax-H3-Image:** "MiniMax-H3-Image Community License"
  - Size: the DiT is 33.1B parameters (66.28 GB BF16), and the text encoder (66.7 GB) is loaded from MiniMax-H3. It is distilled to 6 steps. The listed hardware is datacenter-class (H200, RTX PRO 6000).
  - Licence terms:
    - It names the EU, UK, South Korea and USA as "Excluded Territories".
    - Use, distribution or display of the model or its Outputs outside the "Applicable Territory" is not authorised.
    - Separate written authorisation is required above $1M annual revenue.
    - Commercial UIs must display "MiniMax-H3-Image".
  — [HF model card](https://huggingface.co/MiniMaxAI/MiniMax-H3-Image); [LICENSE](https://huggingface.co/MiniMaxAI/MiniMax-H3-Image/blob/main/LICENSE)
- **Qwen-Image-2.1** (created 2026-09-14): licence_name `qwen-research`, i.e. non-commercial and research only. This drops the Apache 2.0 licence used by earlier Qwen-Image releases. — [HF API](https://huggingface.co/api/models/Qwen/Qwen-Image-2.1); [aiweekly: drops Apache for research-only licence](https://aiweekly.co/alerts/alibaba-ships-qwen-image-21-7b-dit-with-native-2048x2048-and-rgba-drops-apache)
  - It is a 7B DiT with native 2048×2048 output and RGBA support. — [aiweekly](https://aiweekly.co/alerts/alibaba-ships-qwen-image-21-7b-dit-with-native-2048x2048-and-rgba-drops-apache)
  - VRAM (unofficial): ~11 GB with GGUF and 24 GB with INT8/FP8. — [Unsloth docs](https://unsloth.ai/docs/models/qwen-image-2.1)
- **Qwen-Image (Aug 2025) and Qwen-Image-2512 (Dec 2025):** Apache 2.0. — [HF API Qwen-Image](https://huggingface.co/api/models/Qwen/Qwen-Image); [HF API Qwen-Image-2512](https://huggingface.co/api/models/Qwen/Qwen-Image-2512)
- **FLUX 3 Image Klein** (BFL, repo created 2026-10-13): licence `flux-kommunity-license`, with gated access on HF. — [HF API](https://huggingface.co/api/models/black-forest-labs/flux-3-image-klein)
  - It is reported as 5.6B parameters, with free commercial use for individuals and businesses under $5M annual revenue. — [VentureBeat](https://venturebeat.com/ai/black-forest-labs-opens-flux-3-image-klein-weights-with-free-commercial-use-limited-to-smaller-businesses); [BFL blog](https://bfl.ai/blog/flux-3-image-klein)
  - I could not read the licence text itself because the repo is gated.
  - Community GGUF and FP8 builds exist (`unsloth/flux-3-image-klein-GGUF`, `-FP8`). — [HF search](https://huggingface.co/models?search=flux-3)
- **FLUX.2 [klein] 4B** (Jan 2026): **Apache 2.0**. "Runs on consumer GPUs (~13GB VRAM)" such as the RTX 3090 or 4070. It is distilled for sub-second generation and does generation, editing and multi-reference in one model. — [HF model card](https://huggingface.co/black-forest-labs/FLUX.2-klein-4B)
- **FLUX.2 [klein] 9B and FLUX.2 [dev]:** `flux-non-commercial-license`. — [HF API klein-9B](https://huggingface.co/api/models/black-forest-labs/FLUX.2-klein-9B); [HF API FLUX.2-dev](https://huggingface.co/api/models/black-forest-labs/FLUX.2-dev)
- **FLUX.1 [schnell]** [OLDER, 2024]: Apache 2.0. — [HF API](https://huggingface.co/api/models/black-forest-labs/FLUX.1-schnell)
- **Z-Image-Turbo** (Nov 2025) and **Z-Image base** (Jan 2026), from Tongyi-MAI/Alibaba: **Apache 2.0**.
  - 6B parameters with 8-step inference (NFEs). It "fits comfortably within 16G VRAM consumer devices" and has strong photorealism plus English/Chinese text rendering.
  — [HF model card](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo); [HF API Z-Image](https://huggingface.co/api/models/Tongyi-MAI/Z-Image)
  - Quantised FP8 and NF4 community builds run in about 6 GB. — [qubrid (3rd-party)](https://qubrid.com/models/z-image-turbo-lora); [civitai mirror: low-VRAM quant](https://civitai-proxy.pages.dev/models/2169712/z-image-turbo-quantized-for-low-vram)
- **HunyuanImage 3.0:** `tencent-hunyuan-community` licence. — [HF API](https://huggingface.co/api/models/tencent/HunyuanImage-3.0)
- **Stable Diffusion 3.5 Large** [OLDER, 2024]: `stabilityai-ai-community` licence. — [HF API](https://huggingface.co/api/models/stabilityai/stable-diffusion-3.5-large)
- **SDXL base** [OLDER, 2023]: `openrail++`. — [HF API](https://huggingface.co/api/models/stabilityai/stable-diffusion-xl-base-1.0)
- **HiDream-I1-Full** [OLDER, Apr 2025]: MIT. — [HF API](https://huggingface.co/api/models/HiDream-ai/HiDream-I1-Full)
- **Bria FIBO:** licence "other" (Bria's own). — [HF API](https://huggingface.co/api/models/briaai/FIBO)

**CPU-only image generation**
- FastSD CPU's README reports 0.82 s per 512×512 image for one-step SDXS-512 on OpenVINO on a Core i7-12700 desktop. A laptop Core i7 took about 20 s per image with LCM-Dreamshaper (4 steps). Quality is well below FLUX- or Z-Image-class models. — [FastSD CPU README](https://github.com/rupeshs/fastsdcpu/blob/main/Readme.md); [sibany blog (3rd-party, Oct 2025) [OLDER]](https://mail.sibany.com/magazine/2025-10/free-image-generative-ai-pc-without-gpu)
- stable-diffusion.cpp has a CPU build and supports Z-Image, but "no one — including its authors — publishes CPU timings." — [localaimaster (3rd-party)](https://localaimaster.com/blog/image-generation-without-gpu)

### Inferences
- **Recommended local stack for a beginner who intends to monetise:** ComfyUI + Z-Image-Turbo (default) or FLUX.2 klein 4B (for editing and multi-reference). Both are Apache 2.0, both are fast (8 steps or fewer), and both fit 12–16 GB, or about 8 GB quantised with offload.
- Avoid FLUX.2 [dev] and klein 9B (non-commercial) and Qwen-Image-2.1 (research-only) for a monetised account.
- Avoid H3-Image both on licence and on hardware. Its text encoder alone is larger than any consumer GPU, and US, EU, UK and South Korean users are excluded from the open licence.
- FLUX 3 Klein looks fine for a small creator under $5M revenue, but the exact terms are unverified.
- **Quality vs ease (my rating, 5 = best):**

  | Model | Quality | Ease |
  |---|---|---|
  | Z-Image-Turbo | 4 | 4 |
  | FLUX.2 klein 4B | 4 | 4 |
  | FLUX 3 Klein | 4.5 | 3 (gated, newer) |
  | Qwen-Image | 4 | 3 (large) |
  | SDXL | 2.5 | 5 |

### Gaps
- No primary-source Elo exists specifically for Z-Image-Turbo or FLUX.2 klein 4B on the current AA v2.1 open-weights board. They weren't in the top 15 fetched.
- I couldn't read the FLUX Kommunity licence text.
- I found no official minimum VRAM for Qwen-Image-2.1 or FLUX 3 Klein.

---

## Q2. Image generation: free cloud tiers and APIs (limits, watermark, rights, API)

### Takeaway
Free *API* image generation has largely disappeared in 2026:
- The Gemini API has **no free tier for any image model**.
- Hugging Face gives free users **no** inference credits.
- Pollinations requires paid or earned Pollen.

The main remaining free *API* is **Cloudflare Workers AI: 10,000 neurons/day**, which covers FLUX.1 schnell, FLUX.2 klein 4B/9B and FLUX.2 dev. Free *web apps* still exist (Gemini app, Google Flow, Ideogram, Leonardo, Bing/Copilot, Meta AI, ChatGPT), but they're manual-only, often watermarked, and commercial rights on them are unclear or restricted.

### Cited Findings
**Google**
- **Gemini API pricing page:** every image model shows the Free Tier as "Not available":
  - Nano Banana 2.1: $0.0336 per 1K image
  - Gemini 3.1 Flash Image (Nano Banana 2): $0.067 per 1K image
  - Nano Banana 2 Lite: $0.0336 per 1K image
  - Gemini 3 Pro Image (Nano Banana Pro): $0.134 per 1K/2K image
  - Gemini 2.5 Flash Image: $0.039 per image (deprecated, shuts down 2027-03-15)
  
  Text models such as Gemini 3.x Flash and Flash-Lite are still free. — [Google AI Studio pricing](https://aistudio.google.com/docs/pricing) **PAID** for images.
  - [OLDER] early-2026 claims of "500 free images/day" via the API are outdated. — [aifreeapi (3rd-party)](https://www.aifreeapi.com/en/posts/gemini-image-free-tier-2026)
- **Gemini app:** Google's help page gives no numeric limits, only "Standard limits" for no plan, with AI Plus 2×, Pro 4× and Ultra 5×/20× of Pro. — [Gemini Apps limits help](https://support.google.com/gemini/answer/16275805?hl=en)
  - A third-party source says Gemini Basic (free) gets up to 20 Nano Banana 2 images/day. Older posts say 100. — [laozhang blog (3rd-party)](https://blog.laozhang.ai/en/posts/nano-banana-2-limits-daily-quotas-guide); [aifreeapi (3rd-party)](https://www.aifreeapi.com/en/posts/nano-banana-free-use)

**Cloudflare Workers AI** (free API; good for Claude Code)
- The free allocation is "10,000 Neurons per day at no charge" and resets at 00:00 UTC. Image model pricing:
  - FLUX.1 schnell: 4.80 neurons per 512² tile + 9.60 per step
  - FLUX.2 klein 4B: 5.37 per input tile and 26.05 per output tile
  - FLUX.2 klein 9B: 1363.64 for the first megapixel
  - FLUX.2 dev: 37.50 per output tile per step
  - Leonardo Phoenix 1.0: 530 per tile + 10 per step
  - Leonardo Lucid Origin: 636 per tile + 12 per step
  
  — [Cloudflare Workers AI pricing](https://developers.cloudflare.com/workers-ai/platform/pricing/)

**Hugging Face**
- Free users: "None" monthly Inference Provider credits (credit purchase required). PRO gets $2.00/month. — [HF Inference Providers pricing](https://huggingface.co/docs/inference-providers/pricing)
- ZeroGPU Spaces are mentioned as a quota-based compute service, but the free quota wasn't stated on this page. — same source

**Pollinations**
- Key required; Pollen credits; free Pollen only via Quests. See Q0. — [APIDOCS.md](https://raw.githubusercontent.com/pollinations/pollinations/main/APIDOCS.md)

**Ideogram**
- Official docs (via search snippet) say free accounts get 30 credits/week if they sign up with Google, Apple or Microsoft, and none for email/password signups. Free images are public, and downloads are JPG only. Third-party pages still say 10 slow credits/week (outdated). — [Ideogram docs: available plans](https://docs.ideogram.ai/plans-and-pricing/available-plans) (page returned 403 to the fetcher; content taken from the search snippet); [eesel (3rd-party)](https://www.eesel.ai/blog/ideogram-pricing)
- Ideogram 4.0 open weights rank #5 and #6 on the AA open-weights board (Jun 2026). — [AA leaderboard](https://artificialanalysis.ai/image/leaderboard/text-to-image/open-weights)

**Leonardo**
- 150 tokens/day (reset at midnight UTC, no rollover). Sources conflict on whether free output may be used commercially or is watermarked. — [dev.to (3rd-party)](https://dev.to/techsifted/leonardo-ai-pricing-2026-free-credits-paid-plans-and-api-costs-16a2); [Leonardo pricing (403 to fetcher)](https://leonardo.ai/pricing/)

**Microsoft Bing Image Creator / Copilot (MAI-Image 2)**
- MAI Image 2 is rolling out on Copilot and Bing Image Creator. For commercial use, Microsoft asks users to "fill out an application". — [Microsoft AI: Introducing MAI Image 2](https://microsoft.ai/news/introducing-mai-image-2/)
- [OLDER, 2023] A Microsoft community thread says Bing Image Creator output is for personal, non-commercial use. — [Microsoft Tech Community](https://techcommunity.microsoft.com/discussions/bing/confused-about-commercial-use-of-microsoft-ai-images/4005234/replies/4010034)
- Third-party 2026 guides disagree on commercial rights. — [morphed.app (3rd-party)](https://morphed.app/blog/bing-ai-image-generator)
- There is no free public API.

**ChatGPT free tier**
- About 2–3 images per rolling 24 h. OpenAI doesn't publish a fixed quota. — [CometAPI (3rd-party)](https://www.cometapi.com/how-many-images-can-you-create-with-chatgpt-free-in-2026/)
- I couldn't verify this against an OpenAI help page.

**Meta AI**
- Basic image generation is still $0 as of July 2026.
- Meta One, a paid subscription with higher "Muse Image" limits, launched 2026-05-27.
- Output is watermarked, and regional availability varies. Exact free limits are unknown.
— [tech-insider (3rd-party)](https://tech-insider.org/how-to-use-meta-ai-muse-image-2026/); [morphed.app (3rd-party)](https://morphed.app/blog/meta-ai-image-generator)

**Together / fal free credits**
- Not verified in this session. See Gaps.

### Inferences
- **Ranking for a Claude-Code-driven pipeline (automatable and free):**
  1. Local ComfyUI with Z-Image-Turbo or FLUX.2 klein 4B (if a GPU is available)
  2. Cloudflare Workers AI free 10k neurons/day. By my arithmetic from the published rates, one 1024×1024 FLUX.1 schnell image at 4 steps is ~4 tiles × 4.8 + 4 × 9.6 ≈ 58 neurons, so roughly 150+ images/day. Verify actual billing.
  3. Pollinations, only if you have earned Pollen
- **Manual-only free web apps** (Claude Code can't call them): Gemini app, Ideogram (good text rendering), Leonardo, Bing/Copilot, Meta AI, ChatGPT.
- **Commercial-use safety:** with the open-weights Apache models run locally, you own the output. For free web apps, the terms are unclear or non-commercial (Bing, Leonardo-free, Meta), so they're risky for a monetised account.

### Gaps
- I couldn't fetch official free-tier pages for Ideogram, Leonardo, ChatGPT or Meta AI (403s, JS rendering, or no page).
- Together AI and fal.ai new-account credit amounts for 2026 weren't verified.
- The Hugging Face ZeroGPU free quota for Spaces wasn't verified.
- My per-image neuron estimate for Workers AI is my own calculation, not a published figure.

---

## Q3. Video generation: open-weight local models (leaders, VRAM, speed, licences)

### Takeaway
- **Quality leader:** among open weights the top model is **MiniMax H3 (768p)**, at AA T2V Elo 1159 (overall #3). It is a 33B model and isn't licensed for the US, EU, UK or South Korea without separate authorisation. Next are Pika H3 Flex and **LTX-2.5** (needs a 32 GB+ GPU; LTX-2.x Community License, free under $10M revenue).
- **Consumer GPU, free and commercial:** the practical picks are **Wan 2.2 TI2V-5B** (Apache 2.0, 720p@24fps, ~8 GB with ComfyUI offload, minutes per clip) and **HunyuanVideo 1.5** (8.3B, 14 GB minimum with offload, ~75 s for a 480p I2V clip on an RTX 4090 with the step-distilled model; Tencent community licence).
- **CPU-only video is not viable.**

### Cited Findings
**Leaderboard: AA-Video-T2V v2.1 (fetched 2026-11-16)**
- Overall: #1 Wan 3.0 (Alibaba, Aug 2026, **not** open weights), #2 Utopai X, #3 MiniMax H3 (768p, open), #4 Seedance 2.5, #5 FLUX 3 Max, #6 Gemini Omni Flash 1.2.
- Open-weights ranking: MiniMax H3 (1159), Pika H3 Flex (1124), LTX-2.5 Fast (939), LTX-2.5 Pro (938), LTX-2.3 Pro (885).

— [AA text-to-video leaderboard](https://artificialanalysis.ai/video/leaderboard/text-to-video?open-weights=true)
- Wan 2.5/2.6/3.0 have **no** open weights on HF. A search for official Wan-AI repos returned only Wan 2.2. — [HF search API](https://huggingface.co/api/models?search=Wan2.5)

**MiniMax H3** (Jul 2026)
- 33B dense single-stream transformer. 4–15 s video with native stereo audio, 768p by default (2K via the regenerate pass), 24 fps.
- Licence: "MiniMax H3 Community License". The open-weight licence is currently limited for the EU, UK, South Korea and US, with an application form for those regions.
— [HF model card](https://huggingface.co/MiniMaxAI/MiniMax-H3); [License Q&A](https://huggingface.co/MiniMaxAI/MiniMax-H3/raw/main/docs/QA-about-License.md)
- One vendor timing: 559.67 s for a 5 s 1344×768 clip at 50 steps on two RTX 5090s. The INT8 model is 20.97 GB. — [vdf.ai roundup, 2026-11-04 (3rd-party, citing MiniMax guide)](https://vdf.ai/blog/best-local-video-generation-models/)

**LTX-2.5** (Lightricks, weights 2026-07/08)
- Licence: `ltx-2.x-community-license-agreement`. Commercial entities with annual revenue of at least $10,000,000 need a paid Commercial Use Agreement. — [HF API](https://huggingface.co/api/models/Lightricks/LTX-2.5); [LICENSE-2_x](https://github.com/Lightricks/LTX-2/blob/main/LICENSE-2_x)
- Hardware: "NVIDIA GPU with 32 GB or more"; no published timings. — [vdf.ai (3rd-party)](https://vdf.ai/blog/best-local-video-generation-models/)
- Other sources give 24 GB as the minimum with int8 and block-swap for LTX 2.3. — [ltx.io blog](https://ltx.io/blog/best-open-source-video-generation-models)

**Wan 2.2 TI2V-5B** (Jul 2025) [OLDER but still the best Apache video model]
- Apache 2.0. Text- and image-to-video at 720P/24fps.
- The official script needs "at least 24GB VRAM (e.g, RTX 4090)" with offload flags.
— [HF model card](https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B)
- ComfyUI docs say the 5B version "should fit well on 8GB vram with the ComfyUI native offloading." — [ComfyUI Wan2.2 tutorial](https://docs.comfy.org/tutorials/video/wan/wan2_2.md)
- Speed:
  - Wan states under 9 minutes for 5 s of 720p on one consumer GPU. — [vdf.ai](https://vdf.ai/blog/best-local-video-generation-models/)
  - RTX 3060 12GB: ~5–12 min. — [localaimaster (3rd-party)](https://localaimaster.com/blog/local-text-to-video-low-vram)
  - ~3 min with a 4-step workflow. — [GitHub Cordux workflow](https://github.com/Cordux/ComfyUI-Wan2.2-workflow)
- **Wan 2.2 14B I2V on an 8 GB RTX 4060:** 111 s per clip using a "Rapid" distilled checkpoint. — [lilting.ch](https://lilting.ch/en/articles/wan22-comfyui-rtx4060-i2v)
- Wan 2.2 A14B T2V/I2V are Apache 2.0 but need ~80 GB for the reference script, or 14.29 GB per expert in FP8. — [HF API](https://huggingface.co/api/models/Wan-AI/Wan2.2-T2V-A14B); [vdf.ai](https://vdf.ai/blog/best-local-video-generation-models/)

**HunyuanVideo 1.5** (Nov 2025)
- 8.3B parameters. "Minimum GPU Memory: 14 GB (with model offloading enabled)".
- The step-distilled 480p I2V model generates "within 75 seconds" on a single RTX 4090.
- The Wan2GP app runs it in "as low 6 GB of VRAM".
- Licence: `tencent-hunyuan-community`.
— [HF model card](https://huggingface.co/tencent/HunyuanVideo-1.5); [HF API](https://huggingface.co/api/models/tencent/HunyuanVideo-1.5)

**Kandinsky 6.0 Lite/Pro** (Sep 2026)
- MIT licence. Lite transformer 7.48 GB, Pro 69.73 GB, plus a 16.60 GB encoder. — [vdf.ai](https://vdf.ai/blog/best-local-video-generation-models/); [HF kandinskylab](https://huggingface.co/kandinskylab/Kandinsky-6.0-Lite-distill-5s-Diffusers)

**Older models**
- **Mochi 1** [OLDER]: Apache 2.0. — [HF API](https://huggingface.co/api/models/genmo/mochi-1-preview)
- **CogVideoX 1.5** [OLDER]: custom licence. — [HF API](https://huggingface.co/api/models/zai-org/CogVideoX1.5-5B)
- Neither is a 2026 leader.

**Free cloud GPU for running these**
- **Google Colab:** free GPUs are "heavily restricted", and limits are unpublished. Sessions last "at most 12 hours". Free users may not "bypass the notebook UI to interact primarily via a web UI" (relevant to running the ComfyUI web UI) or use SSH or remote desktops. — [Colab FAQ](https://research.google.com/colaboratory/faq.html)
- **Kaggle:** ~30 GPU-hours/week on a P100 16 GB or 2×T4. Sessions are 12 h for GPU per Kaggle docs as read Sep 2026, but some sources say 9 h. — [gpuperhour (3rd-party)](https://gpuperhour.com/blog/free-cloud-gpus-and-credits); [thundercompute](https://www.thundercompute.com/blog/google-colab-alternatives)

### Inferences
- **Hardware guidance (my synthesis of the above):**

  | Hardware | Images | Video |
  |---|---|---|
  | CPU-only laptop | SD-Turbo/SDXS-class images in seconds (low quality); Z-Image via sd.cpp is untested and slow | Not viable; use stock footage or Ken-Burns/parallax animation of stills via FFmpeg or HTML |
  | 8 GB VRAM | Z-Image-Turbo / FLUX.2 klein 4B quantised (GGUF/FP8) | Wan 2.2 5B with offload, or 14B distilled GGUF I2V (~2–12 min per 5 s clip) |
  | 12 GB VRAM | Z-Image-Turbo FP8 or FLUX.2 klein 4B comfortably | Wan 2.2 5B, HunyuanVideo 1.5 via Wan2GP |
  | 16 GB | Z-Image-Turbo bf16, FLUX.2 klein 4B | HunyuanVideo 1.5 480p I2V (14 GB min) |
  | 24 GB (RTX 3090/4090) | Everything consumer-class | Wan 2.2 official script, HunyuanVideo 1.5 (~75 s for 480p I2V), LTX-2.3 with int8 and block-swap; LTX-2.5 wants 32 GB |

- **Kaggle** (P100 16 GB / 2×T4) is the best free cloud GPU for Claude Code to drive by script. Running Wan 2.2 5B or HunyuanVideo 1.5 there is plausible. Colab's free terms discourage web-UI-centric use such as the ComfyUI interface, though headless scripted runs inside a notebook appear allowed.
- **Image-to-video beats text-to-video for faceless Reels.** Generating a still locally with Z-Image, then animating it with Wan 2.2 5B or HunyuanVideo I2V, gives better control.

### Gaps
- I found no independent 2026 benchmarks of generation times on 8, 12 or 16 GB cards for LTX-2.5 or MiniMax H3.
- Pika H3 Flex's licence and VRAM weren't checked.
- Kaggle's official quota page wasn't fetched directly.

---

## Q4. Video generation: free consumer and cloud tiers (credits, watermark, resolution, rights)

### Takeaway
- **Most useful free hosted video:** **Google Flow**, at about 50 credits/day, 720p cap on free, Veo 3.1 / Omni access. Several sources say it has no visible watermark (SynthID invisible), but I couldn't confirm that officially.
- **Other free tiers** (Kling ~66 credits/day, PixVerse daily credits, Vidu ~40/month, Hailuo trial) are all **watermarked and non-commercial** on free plans.
- **Sora is discontinued:** OpenAI announced the end of the Sora app and API on 2026-03-24.
- **Grok Imagine:** free video access is inconsistent.
- **No hosted video tool offers a free API** that Claude Code can call. The Gemini API's video models (Gemini Omni Flash) have no free tier.

### Cited Findings
**Google Flow**
- 50 daily Flow credits on the free plan, with Veo 3.1 access, Text-to-Video and Frames-to-Video. AI Plus adds 200/month, AI Pro 1,000/month, Ultra 10,000/month. — [labs.google/flow](https://labs.google/flow)
- About 5 Veo 3.1 Lite clips or 2 Fast clips per day. Free output is capped at 720p (paid 1080p+). — [veo3ai.io (3rd-party)](https://www.veo3ai.io/blog/is-google-flow-free); [justghostwriter (3rd-party)](https://www.justghostwriter.com/blog/google-flow-pricing-2026-plans-credits-real-value); [saascrmreview (3rd-party)](https://saascrmreview.com/google-flow-review/)
- Watermark: no visible on-frame mark, only an invisible SynthID (third-party, unconfirmed). — [aicomparison.ai (3rd-party)](https://aicomparison.ai/free-ai-video-generators/)

**Gemini API video**
- Gemini Omni 1.2 Flash and Omni 1.1 Flash show Free Tier "Not available". Paid is ~$0.07/s at 720p. — [Google AI Studio pricing](https://aistudio.google.com/docs/pricing) **PAID**

**Sora — DISCONTINUED**
- OpenAI announced on 2026-03-24 that it would "discontinue Sora in the consumer app and API". — [Axios](https://www.axios.com/2026/03/24/openai-discontinue-sora-video-app); [Engadget](https://engadget.com/ai/openai-is-shutting-down-its-sora-video-generation-app-211023358.html)
- A single source says the app closed on 2026-04-26 and the API on 2026-09-24. — [CometAPI](https://www.cometapi.com/is-sora-ai-free-now/)

**Kling**
- About 66 credits per 24 h, at ~25 credits per 5 s clip. Free plan output is 720p, watermarked, and not for commercial use. — [marcandrews (3rd-party)](https://marcandrews.com/kling-ai-free-plan-2026-what-66-credits-buys/); [rescroll, Sep 2026 (3rd-party)](https://www.rescroll.ai/blog/best-free-ai-video-generators-2026)
- **Conflict:** some accounts receive a monthly grant instead, and Costbench says daily login credits go to subscribers only. — [marcandrews](https://marcandrews.com/kling-ai-free-plan-2026-what-66-credits-buys/); [costbench](https://costbench.com/software/ai-video-generators/kling/)

**PixVerse**
- Watermarked, non-commercial, 540p–720p cap. Credits conflict: "90 signup + 60/day" vs "60 initial + 30/day". — [atlascloud (3rd-party)](https://www.atlascloud.ai/id/blog/guides/pixverse-ai-free); [costbench (3rd-party)](https://costbench.com/software/ai-video-generators/pixverse/free-plan/)

**Hailuo (MiniMax)**
- **Conflict:** "one-time welcome credits that expire after 3 days", or "200 credits once", vs "~3–5 generations/day". Free output is 720p, watermarked, ~6 s, and not commercial. — [aicomparison (3rd-party)](https://aicomparison.ai/free-ai-video-generators/); [rescroll](https://www.rescroll.ai/blog/best-free-ai-video-generators-2026); [costbench](https://costbench.com/software/ai-video-generators/hailuo-ai/free-plan/)

**Vidu**
- Vidu's own blog says the free tier is capped at 720p, carries a lower-right watermark, and "free plan videos on Vidu cannot be used commercially". Costbench lists 40 credits/month. — [Vidu blog](https://www.vidu.com/blog/free-ai-animation); [costbench](https://www.costbench.com/software/ai-video-generators/vidu/free-plan/)

**Pika**
- Free tier is "limited". One roundup says the free tier "permits commercial use" at lower resolution. — [rescroll (3rd-party)](https://www.rescroll.ai/blog/best-free-ai-video-generators-2026)
- Not verified on Pika's site.

**Runway / Luma**
- Free tiers give limited one-time or monthly credits and are not for commercial use. — [rescroll (3rd-party)](https://www.rescroll.ai/blog/best-free-ai-video-generators-2026)

**Grok Imagine**
- **Conflicting reports:**
  - Video went behind the SuperGrok paywall on 2026-03-19.
  - A partial free return on 2026-08-21 offered ~1 video/day.
  - Since 2026-09-05, some free accounts have been cut off.
  
  — [roborhythms (3rd-party)](https://www.roborhythms.com/is-grok-imagine-free/); [doolly](https://www.doolly.com/blog/grok-ai-video-no-longer-free-best-alternatives); [aliteq](https://aliteq.com/is-grok-imagine-free)

**Meta AI / Vibes**
- One blog claims up to 20 s free clips. I found no official limits. — [rescroll/aicomparison roundups (3rd-party)](https://aicomparison.ai/free-ai-video-generators/)

**Watermark-free alternatives**
- Canva AI video exports are watermark-free if you avoid Pro assets. Adobe Firefly doesn't watermark output. — [aicomparison.ai (3rd-party)](https://aicomparison.ai/free-ai-video-generators/)

### Inferences
- **For a monetised faceless Reels account, the free hosted video tools are mostly unusable as-is.** Free output is watermarked and non-commercial. Google Flow is the exception worth testing: it has no visible watermark and free daily credits, but its commercial terms on the free tier still need checking.
- **The safest free route** is local Wan 2.2 5B or HunyuanVideo 1.5 (own GPU, or Kaggle), or stock footage plus programmatic motion.
- **Claude Code can't automate any of the consumer apps**, since none has a free API.

### Gaps
- No official Google statement on Flow free-tier commercial-use rights or watermarking was found.
- Kling, PixVerse and Hailuo official pricing pages weren't fetchable, so all figures are third-party and conflicting.
- YouTube Shorts' Veo integration and Meta Vibes free limits were not verified.

---

## Q5. Free stock footage and images (APIs, rate limits, licences, monetised Reels)

### Takeaway
**Pexels** and **Pixabay** are the two free, keyed APIs Claude Code can call immediately. Both permit commercial use with no attribution required (with the usual bans on trademarks and on reselling unaltered files), and both are fine for monetised Reels.
- **Coverr:** also has a free API (with REST and MCP); free-tier API apps must credit Coverr and the creator.
- **Mixkit:** free licence permits YouTube and social media commercial use, but watch for clips marked "Restricted" (non-commercial).

### Cited Findings
**Pexels API**
- Free key on signup. Defaults are "200 requests per hour and 20,000 requests per month", and unlimited free usage is possible on request if terms are met.
- You must "show a prominent link to Pexels" when using the API.
- Video search endpoint: `GET https://api.pexels.com/v1/videos/search`.
— [Pexels API docs](https://www.pexels.com/api/documentation/)

**Pexels licence**
- Commercial use OK and editing OK. "Attribution is not required."
- Don't sell unaltered copies, imply endorsement, or show identifiable people in a bad light.
— [Pexels license](https://www.pexels.com/license/)

**Pixabay API**
- "100 requests per 60 seconds" per key. Responses "must be cached for 24 hours". Permanent hotlinking of images isn't allowed (download first).
- Show users where content is from.
- Videos endpoint: `https://pixabay.com/api/videos/` (large/medium/small/tiny renditions).
— [Pixabay API docs](https://pixabay.com/api/docs/)

**Pixabay Content License**
- Free use, no attribution, modification OK.
- No standalone redistribution, and no commercial use of content showing recognisable trademarks or brands in relation to goods and services.
— [Pixabay license summary](https://pixabay.com/service/license-summary/)

**Coverr**
- "Everything Coverr publishes is free for commercial and personal projects." No attribution is needed for downloads.
- The API (REST and MCP) is licensed for commercial use on every tier. Free/Demo API apps must credit Coverr and the creator, and must report downloads via `PATCH /videos/:id/stats/downloads`.
- Restrictions:
  - No AI training on Coverr content.
  - No Content ID claims.
  - Sponsored Shutterstock/iStock items are excluded.
— [Coverr license](https://coverr.co/license)

**Mixkit**
- The Free License covers commercial projects (YouTube videos, social media marketing, ads) with no attribution. The "Restricted" licence is personal and non-commercial, so check each clip. — [Mixkit official info](https://mixkit.co/llm-info/); [Mixkit license page](https://mixkit.co/license/)
- A Swarmify post saying attribution is required contradicts Mixkit's own statement. — [swarmify (3rd-party)](https://swarmify.com/blog/best-free-b-roll-websites/)
- Mixkit has no public API (none was found).

### Inferences
- **Recommended setup:** Claude Code queries Pexels and Pixabay video search with `orientation=portrait` and min-duration filters, downloads MP4s, and logs the source and creator for safety even though attribution isn't required.
- **Rate limits are ample** for a daily Reels cadence: 200 req/h on Pexels and 100 req/min on Pixabay.
- **Main legal risks:** visible brands or logos and recognisable people in a negative context, plus the fact that YouTube/IG Content ID isn't governed by these licences.
- **Ease rating:** Pexels 5/5, Pixabay 5/5, Coverr 4/5 (download-tracking requirement), Mixkit 3/5 (manual, per-clip licence check).

### Gaps
- Videvo free, NASA and Wikimedia Commons terms were **not researched in this session**, for budget reasons.
  - My general knowledge: NASA media is generally not copyrighted but has logo and endorsement restrictions, and Wikimedia licences vary per file (CC-BY-SA, PD). This needs sourcing.
- Mixkit's full free-licence legal text is rendered by JavaScript and wasn't read directly.

---

## Q6. Thumbnails and Reel covers (specs and tools)

### Takeaway
Meta's official Reels cover spec:
- JPEG, ≤8 MB, sRGB, 9:16 recommended
- Instagram centre-crops a 9:16 rectangle, and a **1:1 square** when the reel is shared to the feed

Design at **1080×1920**, keep title and subject inside the centre square (and centre 3:4, for the profile grid per third-party guides), and render with Pillow or HTML+Playwright. Upload via the app, or via the Graph API `cover_url`.

### Cited Findings
- **Reels cover photo spec (Meta):**
  - Format: JPEG; file size: 8MB maximum; colour space: sRGB.
  - "We recommend 9:16 to avoid cropping… If the aspect ratio of the original image is not 9:16, we crop the image and use the middle most 9:16 rectangle as the cover photo for the reel. If you share a reel to your feed, we crop the image and use the middle most 1:1 square as the cover photo for your feed post."
  
  — [Meta IG User Media reference](https://developers.facebook.com/documentation/instagram-platform/instagram-graph-api/reference/ig-user/media.md)
- **Reels video spec (Meta API):** HEVC or H264; 23–60 FPS; max 1920 px wide; 9:16 recommended; ≤25 Mbps; AAC ≤48 kHz; 3 s to 15 min; ≤300 MB. — same source
- `cover_url` must be a publicly reachable image. `thumb_offset` is in milliseconds (default 0). — same source
- **Profile grid crop:** third-party guides disagree (3:4 vs 4:5 vs 1:1). Several say the 2025+ grid shows a ~3:4 crop and recommend checking the in-app "Profile grid" preview. The help-centre figure of 420×654 (1:1.55) is cited as a minimum. — [Hootsuite](https://blog.hootsuite.com/instagram-reels-cover/); [hopperhq](https://www.hopperhq.com/blog/instagram-reel-size/); [oktopost](https://www.oktopost.com/blog/instagram-grid-size-guide/); [adaptlypost](https://adaptlypost.com/blog/instagram-reel-cover-size)
- **Canva** AI video exports are watermark-free if no Pro assets are used (applies to the free tier). — [aicomparison.ai (3rd-party)](https://aicomparison.ai/free-ai-video-generators/)

### Inferences
- **Best free cover pipeline with Claude Code:**
  1. Generate or choose a background (a Z-Image frame, a still from the Reel, or a Pexels photo).
  2. Composite it with Pillow, or with an HTML/CSS template rendered by Playwright at 1080×1920. Use bold text inside the central 1080×1080 safe zone.
  3. Export JPEG in sRGB under 8 MB.
  
  This is fully scriptable and repeatable for a consistent brand look.
- Canva free and Photopea (free browser editor) are good manual fallbacks for beginners but can't be automated by Claude Code.
- **Ease rating:** Pillow 4/5 (code-only), HTML+Playwright 5/5 (easy to iterate on design), Canva free 5/5 manual, Photopea 3/5 manual.

### Gaps
- I didn't fetch a Meta Help Center (help.instagram.com) page for the in-app grid crop; that figure is third-party only.
- Canva free-tier limits for 2026 and Photopea's terms weren't verified from primary sources.

---

## Q7. Overall ranking per step and where sources disagree

### Takeaway
**Best free stack for a beginner using Claude Code**, from most to least automatable and commercially safe:

| Step | Free option | Notes |
|---|---|---|
| Stock | Pexels + Pixabay APIs | |
| Images | Local Z-Image-Turbo or FLUX.2 klein 4B in ComfyUI (if GPU) | Otherwise Cloudflare Workers AI free 10k neurons/day (FLUX schnell / klein 4B) |
| Video | Local Wan 2.2 5B or HunyuanVideo 1.5 I2V (GPU ≥8–14 GB, or Kaggle) | Otherwise stock footage plus code-driven motion; Google Flow free for occasional manual Veo clips |
| Covers | Pillow / HTML+Playwright at 1080×1920 JPEG | |

### Cited Findings
- **Gemini API image free tier:** was "available" early 2026; now "Not available".
  — [AI Studio pricing](https://aistudio.google.com/docs/pricing) vs [aifreeapi early-2026 (3rd-party)](https://www.aifreeapi.com/en/posts/gemini-image-free-tier-2026)
- **Qwen-Image licence:** Apache 2.0 for Qwen-Image/2512, but research-only for 2.1.
  — [HF API Qwen-Image](https://huggingface.co/api/models/Qwen/Qwen-Image); [HF API 2.1](https://huggingface.co/api/models/Qwen/Qwen-Image-2.1)
- **Wan 2.2 5B VRAM:** 24 GB per the official card vs 8 GB with ComfyUI offload.
  — [HF card](https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B); [ComfyUI docs](https://docs.comfy.org/tutorials/video/wan/wan2_2.md)
- **LTX-2.x VRAM:** 32 GB vs 24 GB with int8 and block-swap.
  — [vdf.ai](https://vdf.ai/blog/best-local-video-generation-models/); [ltx.io](https://ltx.io/blog/best-open-source-video-generation-models)
- **Kling free credits:** daily vs monthly.
  — [marcandrews](https://marcandrews.com/kling-ai-free-plan-2026-what-66-credits-buys/)
- **Grok Imagine free video:** removed vs partially restored.
  — [roborhythms](https://www.roborhythms.com/is-grok-imagine-free/)
- **AA image leaderboard leader:** varies by snapshot. H3-Image is #1 on the current v2.1 open-weights board; earlier snapshots had Qwen-Image-2.1 first.
  — [AA](https://artificialanalysis.ai/image/leaderboard/text-to-image/open-weights)

### Inferences
- **Changes in 2026 a beginner must know:**
  1. Sora is gone.
  2. The Gemini API no longer offers free images.
  3. Hugging Face gives free users no inference credits.
  4. Pollinations now needs a key and Pollen.
  5. The newest open-weight leaders (Qwen-Image-2.1, FLUX.2 dev/klein-9B, MiniMax H3 and H3-Image) carry non-commercial, revenue-capped or territory-restricted licences, while Z-Image, FLUX.2 klein 4B, Wan 2.2 and FLUX.1 schnell remain Apache 2.0.
- **Without any GPU,** a fully free, fully automated pipeline of high visual quality is realistic only with stock footage, Cloudflare Workers AI stills, and code-generated motion graphics. AI video then has to come from manual free tiers (Google Flow) or from Kaggle's ~30 GPU-hours/week.

### Gaps
- No 2026 YouTube comparison videos were reviewed, due to budget.
- Fal and Together sign-up credits, HF ZeroGPU quotas, Videvo, NASA and Wikimedia, and official Canva/Photopea terms remain unverified.
