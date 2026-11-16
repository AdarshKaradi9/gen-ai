# Free audio, captions and music tools for a Claude Code-driven faceless Instagram Reels pipeline (as of 2026-11-16)

Method note: GitHub API (`gh api` / api.github.com) was blocked in this session, so star counts and last-push dates are not given. Popularity and recency come from the Hugging Face API instead (likes, downloads, lastModified, license tag, queried 2026-11-16, e.g. `https://huggingface.co/api/models/hexgrad/Kokoro-82M`). Project READMEs were read through raw.githubusercontent.com.

## Q1. TTS / voiceover: can Claude Code do it alone, and what are the best free options?

### Takeaway
Claude Code cannot produce speech itself, but it can `pip install` and run a local open-weight TTS model end to end. For a beginner the strongest free and commercially safe defaults are **Kokoro-82M** (Apache-2.0, runs on CPU, no cloning) and **Chatterbox / Chatterbox-Turbo** (MIT, voice cloning, wants a GPU; the 110M Nano version runs on CPU). **edge-tts** gives free Microsoft neural voices and writes subtitles, but it is an unofficial use of a Microsoft service and broke in Oct 2026. The top open-weights quality model is **Fish Audio Drama 3**, but its license is not OSI open source (commercial use only under US$500k revenue) and it needs a large GPU. Many popular models (F5-TTS, XTTS-v2) are **non-commercial**.

### Cited Findings
**Leaderboards (current leaders)**
- Artificial Analysis TTS arena, 2026 snapshot (the page is labelled "All models", so it is not filtered to open weights). Ranks with Elo: #1 Fish Audio Drama 3, 1277 (Oct 2026); Drama 3 Preview 1238; Breeze TTS 2, 1229 (Aug 2026); Ant Ming-3.0-tts 1183; Gradium Phonon 31M 1111; Fish S2 Pro 1104; StepFun Step Audio EditX 1100; Mistral Voxtral TTS 1093; NVIDIA Magpie-Multilingual 357M 1062; **Kokoro 82M v1.0, 1060** (Jan 2025); Maya1 1048; OpenAudio S1 Mini 1043; Higgs Audio V3 1038 (Jun 2026); **Chatterbox 1020**; Zonos 1000; VibeVoice 1.5B 955; **XTTS v2 915**. — [Artificial Analysis](https://artificialanalysis.ai/text-to-speech/leaderboard/provider-voice/open-weights)
- Sources disagree on which open model is "top". A blog says Breeze TTS 2 leads open weights but its weights are non-commercial, so the best shippable model is Step Audio EditX (Apache-2.0). Another article (Oct 10 2026) places Chatterbox highest among clearly open-weight models on TTS Arena (#28 of 39, 1481±19), with Kokoro at #29 (1478±22, "Retired"), statistically tied. — [WebSearch summary of AA/yaps](https://artificialanalysis.ai/text-to-speech/leaderboard); [yaps.ai, Oct 10 2026](https://www.yaps.ai/blog/best-local-tts-models)

**Local open-weight models (license → commercial use)**
- **Kokoro-82M**: Apache-2.0; 82M params; 7,433 HF likes and about 12.9M downloads. Installs with `pip install kokoro>=0.9.4 soundfile` plus `espeak-ng`, and the README says it "can be deployed anywhere from production environments to personal projects." — [HF API](https://huggingface.co/hexgrad/Kokoro-82M); [kokoro README](https://github.com/hexgrad/kokoro)
- Kokoro runs on CPU or GPU and has no voice cloning. It has 54 voices (20 US English and 8 UK English); other languages are thin (1 French, 2 Italian voices). Apple Silicon needs an MPS fallback flag. — [yaps.ai](https://www.yaps.ai/blog/best-local-tts-models)
- Kokoro word timestamps: the core library offers none, according to the search. Kokoro-FastAPI has a `/dev/captioned_speech` endpoint that returns per-word start and end times, and the Rust port Kokoros has `--timestamps`, which writes a word/start/end TSV. The Replicate wrapper notes timestamps work for English voices only. — [Kokoro-FastAPI](https://github.com/remsky/Kokoro-FastAPI); [Kokoros](https://github.com/cybernagle/Kokoros); [Replicate](https://replicate.com/siegerts/kokoro-tts-82m/readme)
- **Chatterbox family (Resemble AI)**: MIT license (HF tag); 1,914 likes, about 2.5M downloads; card updated 2026-06-10. Installs with `pip install chatterbox-tts`. **Chatterbox Multilingual V3** (0.5B, 23+ languages) does cross-language voice cloning. **Chatterbox-Turbo** (350M, English) has native paralinguistic tags (`[laugh]`, `[cough]`, `[chuckle]`) and one-step decoding. **Chatterbox-Nano** (110M, English) runs "3x faster than realtime on 8 CPU cores." — [HF API](https://huggingface.co/ResembleAI/chatterbox); [Chatterbox README](https://github.com/resemble-ai/chatterbox); [HF card](https://huggingface.co/ResembleAI/chatterbox)
- Chatterbox's "beats ElevenLabs" figures are vendor-run tests: Resemble cites 63.75% preference in a Podonos test without naming the version, and a widely repeated "65.3%" figure could not be found on any Resemble page. — [yaps.ai](https://www.yaps.ai/blog/best-local-tts-models)
- **Fish Audio Drama 3** (open weights released Oct 13 2026): a 35B mixture-of-experts model with about 3B parameters active. — [MarkTechPost](https://www.marktechpost.com/2026/10/14/fish-audio-drama-3-open-weight-tts-model/)
- Drama 3 license (official LICENSE file): free for research and non-commercial use. Commercial use is free "only while Your Annual Revenue is less than USD 500,000". A "Hosted Service" (offering TTS or voice cloning to third parties) always needs a separate license. Generating narration for your own content is explicitly not a Hosted Service. — [fishaudio/drama-3 LICENSE](https://huggingface.co/fishaudio/drama-3/raw/main/LICENSE)
- Secondary sources say Drama 3 needs about a 48 GB GPU as a practical floor; no official minimum is published. — [search summary citing explainx/oflight](https://www.oflight.co.jp/en/columns/fish-audio-drama-3-requirements-license-guide-2026)
- Fish S2 Pro: Fish Audio Research License (separate license needed for commercial use); 5B params; the card lists an H200. — [yaps.ai](https://www.yaps.ai/blog/best-local-tts-models); [HF](https://huggingface.co/fishaudio/s2-pro)
- **Qwen3-TTS** (Jan 2026): Apache-2.0; 0.6B and 1.7B sizes; 10 languages; voice cloning from about a 3-second sample; a CUDA GPU is recommended and it is slow without one. 2,233 likes, about 1.19M downloads. — [yaps.ai](https://www.yaps.ai/blog/best-local-tts-models); [HF](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice)
- **Pocket TTS (Kyutai)**: CC-BY-4.0, so commercial use requires attribution; 100M params; runs on 2 CPU cores; 6 languages; cloning through a gated repo. — [yaps.ai](https://www.yaps.ai/blog/best-local-tts-models); [HF](https://huggingface.co/kyutai/pocket-tts)
- **Supertonic 3**: OpenRAIL-M (commercial use allowed with use restrictions); about 99M params; designed for CPU; 31 languages; no cloning in the open release. — [yaps.ai](https://www.yaps.ai/blog/best-local-tts-models); [HF](https://huggingface.co/Supertone/supertonic-3)
- **Piper**: GPL-3.0 engine and per-voice licenses that vary, so commercial status is unclear; CPU or small devices; 44 locales; no cloning. — [yaps.ai](https://www.yaps.ai/blog/best-local-tts-models)
- **F5-TTS**: code MIT but **weights CC-BY-NC-4.0** (non-commercial). — [HF API](https://huggingface.co/SWivid/F5-TTS); [yaps.ai](https://www.yaps.ai/blog/best-local-tts-models)
- **XTTS-v2 (Coqui)**: Coqui Public Model License, non-commercial; HF card unchanged since 2023-12 [OLDER]. Coqui the company shut down [OLDER; no 2026 source found]. — [yaps.ai](https://www.yaps.ai/blog/best-local-tts-models); [HF](https://huggingface.co/coqui/XTTS-v2)
- **Orpheus 3B**: Apache-2.0 on the card, but it is built on Llama 3.2 3B, so Meta's terms also apply; needs a GPU. **Dia 1.6B**: Apache-2.0; about 4.4 GB VRAM; English only. **IndexTTS-2.5**: bilibili model license, and commercial use requires contacting bilibili. **Sesame CSM-1B**: Apache-2.0. **NeuTTS Air**: Apache-2.0, cloning from 3 s. **VibeVoice**: MIT, but Microsoft removed the long-form TTS code in Sept 2025. **Kyutai TTS 1.6B**: CC-BY-4.0. **Higgs Audio**: appears on the AA board (V3, Jun 2026). — [yaps.ai](https://www.yaps.ai/blog/best-local-tts-models); [HF API Kyutai](https://huggingface.co/kyutai/tts-1.6b-en_fr); [AA](https://artificialanalysis.ai/text-to-speech/leaderboard/provider-voice/open-weights)

**Free cloud options**
- **edge-tts** (Python, LGPLv3): latest version 7.3.1 (Oct 13 2026). Writes SRT subtitles with `edge-tts --text "..." --write-media out.mp3 --write-subtitles out.srt`. Custom SSML was removed because "Microsoft prevents the use of any SSML that could not be generated by Microsoft Edge itself." — [PyPI edge-tts](https://pypi.org/project/edge-tts/); [README](https://github.com/rany2/edge-tts)
- edge-tts risk: Microsoft tightened Sec-MS-GEC token validation around mid-Oct 2026. Versions up to 7.2.7 get HTTP 403 on every synthesis, and 7.3.0/7.3.1 fix it. A separate endpoint-migration failure was reported around Oct 24 for other clients. — [hermes-agent #140990](https://github.com/NousResearch/hermes-agent/issues/140990); [#137944](https://github.com/NousResearch/hermes-agent/issues/137944); [ekko-studio #3524](https://github.com/EKKOLearnAI/ekko-studio/issues/3524)
- **Google Cloud TTS** free tier (official pricing page, read 2026-11-16). Monthly free characters: Chirp 3 HD 1M, then $30/1M; WaveNet 4M, then $4/1M; Standard 4M, then $4/1M; Neural2 1M, then $16/1M; Studio 1M, then $160/1M; Polyglot 1M. Gemini TTS models have no free usage and are billed per token (Gemini 3.8 Flash TTS preview prices double on Jan 1 2027). Billing must be enabled, and you are "automatically charged if your usage exceeds" the free amount. — [Google Cloud TTS pricing](https://cloud.google.com/text-to-speech/pricing)
- **ElevenLabs Free**: "10k credits per month", 1 credit per character for TTS, so about 10,000 characters. "Commercial License" first appears under Starter ($6/mo, 30k credits), and instant voice cloning also starts at Starter. — [ElevenLabs pricing](https://elevenlabs.io/pricing)
- Third-party sources say the ElevenLabs Free plan requires attribution and allows no commercial use. They disagree on the wording ("Made with ElevenLabs" vs "Voice by ElevenLabs"), and the official pricing page does not mention attribution. — [dupple](https://dupple.com/learn/is-elevenlabs-free); [licenseorg](https://licenseorg.com/blog/elevenlabs-licensing-guide-ai-voices)
- PAID tools for comparison: ElevenLabs Starter $6/mo (free alternatives: Chatterbox or Kokoro). Fish Audio's API is reported at $15 per 1M characters for Drama 3. — [ElevenLabs](https://elevenlabs.io/pricing); [AlphaSignal](https://alphasignal.ai/news/fish-audio-s-drama-3-tops-open-weight-voice-rankings-at-15-per-million)

### Inferences
- Beginner ranking (free, commercial-safe, Claude Code-installable):
  1. Kokoro: CPU, Apache-2.0, fastest to set up.
  2. Chatterbox-Turbo or Multilingual V3: MIT, cloning and expressive tags; GPU preferred, Nano for CPU.
  3. Qwen3-TTS: Apache-2.0, multilingual plus cloning; needs a GPU.
  4. edge-tts: zero hardware and built-in SRT, but ToS-grey and breakage-prone.
  5. Google Cloud TTS free tier: official and generous, but needs a billing account.
- Avoid for a monetised account: F5-TTS, XTTS-v2, ElevenLabs Free (non-commercial). Treat Drama 3 and Pocket TTS as "commercial with conditions" (revenue cap, or CC-BY attribution).
- Instagram Reels voiceovers are short (about 100–250 words), so ElevenLabs' roughly 10k characters a month covers only a handful of Reels. Local models remove per-character limits.
- Claude Code drives all local models via `pip` plus a short Python script. edge-tts is a single CLI command. Google needs `gcloud` auth plus the REST API.

### Gaps
- GitHub stars and last-push dates could not be fetched (GitHub API blocked in this session).
- No official Microsoft statement on edge-tts permissibility was found. It is an unofficial client of the Edge "Read Aloud" endpoint, and that it is unsanctioned is inferred, not documented.
- Exact VRAM needs for Chatterbox-Turbo and Qwen3-TTS were not stated in the sources read.
- ElevenLabs' official attribution wording for Free was not verified on an official help page.

## Q2. Word-level captions: can Claude Code do it alone, and which ASR and caption-rendering tools are best?

### Takeaway
Yes, Claude Code can do this entirely alone: install faster-whisper, WhisperX, whisper.cpp or stable-ts, get word timestamps, then burn TikTok-style captions with FFmpeg (ASS subtitles), **pycaps** (Python, MIT, CSS-styled, Reels-oriented) or **Remotion** (`createTikTokStyleCaptions`; free for individuals and companies of up to 3 people). Because the script is already known in a TTS pipeline, the cheapest path is often TTS-provided timestamps (edge-tts SRT, Kokoro-FastAPI) or forced alignment (WhisperX's wav2vec2 alignment) rather than full ASR. CapCut should be marked **freemium/partly paywalled**: auto captions are limited on the free tier, and sources and CapCut's own pages conflict.

### Cited Findings
**ASR engines**
- **faster-whisper**: "up to 4 times faster than openai/whisper for the same accuracy while using less memory". Supports CPU INT8 (`device="cpu", compute_type="int8"`) and `word_timestamps=True`. — [faster-whisper README](https://github.com/SYSTRAN/faster-whisper)
- **WhisperX**: "70x realtime with large-v2" batched; "Accurate word-level timestamps using wav2vec2 alignment"; optional pyannote diarization. — [WhisperX README](https://github.com/m-bain/whisperX)
- **whisper.cpp**: C/C++ with Apple Silicon Metal/Core ML and Vulkan GPU support, a good fit for CPU-only or Mac machines. — [whisper.cpp README](https://github.com/ggml-org/whisper.cpp)
- **stable-ts**: a Whisper wrapper with an alignment mode (align known text to audio) and a faster-whisper backend. — [stable-ts README](https://github.com/jianfch/stable-ts)
- Whisper large-v3-turbo: MIT; 3,552 HF likes. — [HF API](https://huggingface.co/openai/whisper-large-v3-turbo)
- 2026 ASR accuracy leaders: Cohere Transcribe (2B, Apache-2.0, Mar 2026) topped the Open ASR Leaderboard at 5.42% average WER, and IBM Granite Speech 4.1 2B followed at 5.33%. A Nov 2026 source cites English averages of 6.10% for NVIDIA Nemotron 3.5 Transcribe, 6.14% for Qwen3-ASR 1.7B, and 8.18% for Whisper large-v3. Rankings vary by source and snapshot. — [MarkTechPost, Jul 23 2026](https://www.marktechpost.com/2026/07/23/best-open-speech-recognition-asr-models-in-2026-wer-languages-latency-and-license-compared/); [ThinkScribe](https://thinkscribe.ai/en/blog/open-speech-recognition-models-2026); [Northflank](https://northflank.com/blog/best-open-source-speech-to-text-stt-model-in-2026-benchmarks)
- Licenses (HF API): Cohere Transcribe 03-2026 Apache-2.0; Qwen3-ASR 1.7B and 0.6B Apache-2.0; Granite Speech 4.1 2B Apache-2.0; Parakeet TDT 0.6B v3 CC-BY-4.0; Canary-Qwen-2.5B CC-BY-4.0; Nemotron 3.5 Transcribe 30B-A4B "other" (NVIDIA license). — [HF Cohere](https://huggingface.co/CohereLabs/cohere-transcribe-03-2026); [HF Qwen3-ASR](https://huggingface.co/Qwen/Qwen3-ASR-1.7B); [HF Granite](https://huggingface.co/ibm-granite/granite-speech-4.1-2b); [HF Parakeet](https://huggingface.co/nvidia/parakeet-tdt-0.6b-v3); [HF Canary](https://huggingface.co/nvidia/canary-qwen-2.5b); [HF Nemotron](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B)
- Parakeet TDT 0.6B v3 is the throughput leader among multilingual open models (RTFx about 3333, 25 European languages). Canary-Qwen-2.5B: 5.63% WER at RTFx 418. Whisper "remains the correct default" because of its runtime ecosystem (whisper.cpp, faster-whisper, WhisperX). — [Open ASR Leaderboard paper](https://arxiv.org/html/2510.06961v1); [search summary of Northflank/MarkTechPost](https://northflank.com/blog/best-open-source-speech-to-text-stt-model-in-2026-benchmarks)

**Avoiding ASR when the script is known**
- edge-tts writes an SRT directly from the TTS run (`--write-subtitles`). — [edge-tts](https://pypi.org/project/edge-tts/)
- Kokoro-FastAPI returns per-word timestamps, and Kokoros writes a word-level TSV. — [Kokoro-FastAPI](https://github.com/remsky/Kokoro-FastAPI); [Kokoros](https://github.com/cybernagle/Kokoros)
- CTC forced alignment of known text to TTS audio with Wav2Vec2 works with any TTS (Wikimedia prototype). WhisperX's aligner is the same wav2vec2 approach. — [Wikimedia Phabricator T427488](https://phabricator.wikimedia.org/T427488); [WhisperX](https://github.com/m-bain/whisperX)

**Caption rendering**
- **pycaps**: MIT; "alpha"; Python 3.10–3.12; needs FFmpeg; installed from GitHub (`pip install "git+https://github.com/francozanardi/pycaps.git#egg=pycaps[all]"`), not on PyPI. It has CSS styling (e.g. `.word-being-narrated`), templates, built-in animations (pop, fade, slide), emoji and SFX effects, Whisper or faster-whisper word timestamps, and a CLI plus Python API. It is "Offline-first" and explicitly targets TikTok, Shorts and Reels. Sibling project tscaps is a browser editor (engine MIT, app AGPL-3.0) with a cloud API that has a free tier. — [pycaps README](https://github.com/francozanardi/pycaps)
- **Remotion**: `createTikTokStyleCaptions()` (v4.0.216+) groups word-level `Caption[]` into pages and tokens. Setting `combineTokensWithinMilliseconds` small gives word-by-word animation, and `breakOnSilenceAfterMilliseconds` was added in 4.0.514. — [Remotion docs](https://www.remotion.dev/docs/captions/create-tiktok-style-captions)
- Remotion license: "completely free to use for any individual or small company"; Free License is "for individuals and companies of up to 3 people … unlimited commercial use." Larger companies pay ($25/seat/mo Creators, or $0.01/render with a $100/mo minimum). — [Remotion License & Pricing](https://www.remotion.dev/docs/license/pricing)
- Remotion also ships a TikTok captions template using Whisper.cpp. — [Remotion TikTok template](https://remotion.dev/templates/tiktok)

**CapCut (free vs paid)**
- CapCut's own pages conflict. A March 2026 page promises "free automatic captions," while a Sept 2026 Standard vs Pro guide says the auto caption generator "is exclusive to Pro users." — [search summary citing AllAble/CapCut](https://www.allable.ai/blog/capcut-pricing/)
- Reported free caps vary: "10 minutes of auto-captions per video" (fluxnote via AllAble), or "5 auto caption generations per rolling 30-day window" (unverified third-party tracker). CapCut publishes no number. — [AllAble, Oct 8 2026](https://www.allable.ai/blog/capcut-pricing/); [ReelVideoCaptions, Jun 12 2026 (competitor)](https://reelvideocaptions.com/blog/capcut-auto-captions-not-free-anymore.html)
- CapCut Pro is $19.99/mo or $179.99/yr in the US. The annual price rose from about $77.99 to $179.99 in a Feb–Mar 2026 restructure (Newsweek, via secondary sources), and a paid "Standard" tier is $9.99/mo on the US App Store. — [AllAble](https://www.allable.ai/blog/capcut-pricing/); [ReelVideoCaptions](https://reelvideocaptions.com/blog/capcut-auto-captions-not-free-anymore.html)
- ToS controversy [2025]: the June 12 2025 terms update was read as granting a perpetual, worldwide, royalty-free license to user content. CapCut told TechRadar the disputed section "has not changed." — [TechRadar](https://www.techradar.com/pro/popular-video-editing-app-capcut-wants-to-use-any-content-you-produce-for-free-forever-heres-what-you-should-know); [CapCut "About CapCut's Terms of Service"](https://capcut.com/resource/about-capcut-terms-of-service)
- Several "CapCut isn't free" articles come from competitors (Descript, ReelVideoCaptions, AEJuice), so treat their framing with caution. — [Descript](https://www.descript.com/blog/article/capcut-captions-arent-free-anymore-heres-a-better-option)

### Inferences
- Best beginner path (all free and local):
  1. TTS with word timestamps (edge-tts SRT, or Kokoro then WhisperX alignment).
  2. pycaps (Python, one CLI command) or an FFmpeg ASS karaoke file written by Claude Code.
  3. Remotion if the user is comfortable with Node/React.
- On CPU, faster-whisper small/medium INT8 or whisper.cpp is enough for 30–90 s Reels. Parakeet v3 is the fastest but English/European-only, and CC-BY attribution applies to the model, not to your captions.
- CapCut should be listed as "Freemium – auto captions limited/paywalled on some plans and platforms in 2026; verify in-app," not as free.

### Gaps
- Montreal Forced Aligner and aeneas licenses and 2026 maintenance status were not verified in this session.
- No benchmark comparing word-timestamp accuracy across ASR models was found.
- No measured CPU real-time factors for a 60-second Reel were found from a primary source (the faster-whisper README benchmark used an i7-12700K, but the numbers were not extracted).

## Q3. Music and SFX: free royalty-free sources and open AI generators usable on Instagram

### Takeaway
Claude Code cannot "find" licensed music by itself (most libraries have no free API, or need a login). It can download from sources with clear terms, or **generate** music and SFX locally. The safest commercially usable free generators are **ACE-Step 1.5** (MIT, under 4 GB VRAM, outputs usable commercially), **HeartMuLa** (Apache-2.0) and **MOSS-SoundEffect v2.0** (Apache-2.0 SFX). Stable Audio Open is free only under US$1M revenue. MusicGen and MMAudio are **non-commercial**. Among libraries, Pixabay (no attribution; occasional Content ID claims), Mixkit (free license, no attribution), Freesound CC0/CC-BY, Incompetech (CC-BY) and Instagram's own Sound Collection (commercial-cleared) are the main free options. Uppbeat free is tiny (3 downloads, then 1 per month) and needs a credit.

### Cited Findings
**Libraries**
- **YouTube Audio Library**: Google's help page covers only YouTube use. It says "YouTube can't give legal guidance, including guidance on issues with music that can occur off the platform", that Audio Library music "won't be claimed by a rights holder through the Content ID system", and that CC tracks need credit in the description. Off-YouTube (Instagram) use is not granted by this page. — [YouTube Help](https://support.google.com/youtube/answer/3376882)
- **Pixabay** Content License: free use without attribution, modification allowed. You cannot sell or distribute content "on a Standalone basis" or use it in trademarks. — [Pixabay license summary](https://pixabay.com/service/license-summary/)
- Pixabay's FAQ says some music "might trigger Content ID claims … usually resolved by showing your Pixabay license". A guide says contributors can now flag tracks for Content ID. — [Pixabay FAQ](https://pixabay.com/service/faq/); [search summary](https://www.foximusic.com/blog/need-background-music-that-wont-trigger-content-id/)
- **Mixkit**: separate "Stock Music Free License" and "Sound Effects Free License". Secondary sources say commercial use including social media and ads is allowed with no attribution, but games, CDs/DVDs and TV/radio broadcast are excluded. Mixkit's own LLM-info page contained prompt-injection-like instructions and was disregarded. — [Mixkit license](https://mixkit.co/license/); [creativeentrepreneurs](https://creativeentrepreneurs.co/journal/six-brilliant-stock-music-websites-clear-licensing-terms/); [hellothematic](https://hellothematic.com/thematic-vs-mixkit/)
- **Uppbeat free**: Uppbeat's help center says the free plan gives "30% of our music, sound effects … library, with 3 free downloads upfront, restored by 1 each month", and free downloads need a credit (with a license code). An Uppbeat comparison says free downloads are covered on YouTube, TikTok and Instagram with attribution. Some sites cite 10 per month, which looks outdated. — [Uppbeat help center](https://fastly-f.uppbeat.io/help-center); [Uppbeat blog](https://uppbeat.io/blog/royalty-free-and-copyright-free-music/uppbeat-vs-artlist-how-do-they-compare); [Uppbeat free](https://uppbeat.io/free)
- **Freesound**: CC0 (anything, even selling); CC BY (credit required); CC BY-NC (no commercial use); legacy Sampling+ (no commercial ads; being removed). — [Freesound FAQ](https://freesound.org/help/faq/#licenses)
- **Incompetech (Kevin MacLeod)**: "Creative Commons — Free. No charge. Requires that you credit the music." A paid Standard License is for cases where attribution is impossible. — [Incompetech licenses](https://incompetech.com/music/royalty-free/licenses/)
- **Free Music Archive**: per-track CC licenses. BY-NC variants forbid advertising or "promoting a product", and ND variants forbid putting the song in a video. — [FMA License Guide](https://freemusicarchive.org/License_Guide)
- **Instagram in-app audio**: "certain business accounts and certain types of posts do not have access to the library"; licensed music is "intended for personal, non-commercial use". **Sound Collection** has over 14,000 songs and sounds, is "entirely royalty free and safe to use in Reels and Instagram Stories," and "can be used for commercial purposes like ads." — [Instagram Help](https://www.facebook.com/help/instagram/402084904469945)

**AI music generation (local)**
- **ACE-Step 1.5** (Feb 2026): MIT. The card says "You can strictly use the generated music for commercial purposes" and that training data is licensed, royalty-free or synthetic. It runs locally in under 4 GB VRAM, makes a full song in under 10 s on an RTX 3090, covers 50+ languages, and is installable via Transformers or Diffusers. 971 likes, about 104k downloads. — [HF ACE-Step 1.5](https://huggingface.co/ACE-Step/Ace-Step1.5)
- One review claims ACE-Step is non-commercial, which conflicts with the MIT card. — [usefulai](https://usefulai.com/models/music-generation) vs [HF card](https://huggingface.co/ACE-Step/Ace-Step1.5)
- **HeartMuLa** (Jan 2026): Apache-2.0 repo and weights; self-described as the best open model for lyrics control and quality. The HeartMuLa MuLaCover variant is CC-BY-NC-4.0. — [heartlib GitHub](https://github.com/HeartMuLa/heartlib); [HF HeartMuLa-oss-3B](https://huggingface.co/HeartMuLa/HeartMuLa-oss-3B)
- **YuE v1**: Apache-2.0 [OLDER, Jan–Mar 2025]; the newer YuE2 reportedly has a stricter license. — [HF YuE](https://huggingface.co/m-a-p/YuE-s1-7B-anneal-en-cot); [it-jim](https://www.it-jim.com/blog/best-open-source-ai-music-generator/)
- **MusicGen (AudioCraft)** weights: CC-BY-NC-4.0, non-commercial [OLDER, 2023]. — [HF musicgen-small](https://huggingface.co/facebook/musicgen-small)
- **Stable Audio Open 1.0 and Small**: Stability AI Community License (gated). It allows free commercial use for those "generating annual revenue of less than US $1,000,000"; commercial users must register; the license terminates above $1M. Stable Audio Open small was updated 2026-11-05. — [HF stable-audio-open-small](https://huggingface.co/stabilityai/stable-audio-open-small); [Stability Community License](https://stability.ai/community-license-agreement)
- **LeVo 2**: non-commercial. **DiffRhythm 1.2**: no license tag on HF. — [search summary](https://arxiv.org/pdf/2606.30642); [HF DiffRhythm](https://huggingface.co/ASLP-lab/DiffRhythm-1_2)

**AI SFX generation**
- **MOSS-SoundEffect v2.0** (May 2026): Apache-2.0; text to SFX up to 30 s (default 10 s) at 48 kHz; CUDA plus bf16 example; installed via the MOSS-TTS repo with `pip install -e`. The card does not address commercial use of outputs. — [HF MOSS-SoundEffect v2.0](https://huggingface.co/OpenMOSS-Team/MOSS-SoundEffect-v2.0)
- **Stable Audio Open** makes samples and SFX up to 47 s (Community License as above). — [Stability AI](https://stability.ai/news-updates/introducing-stable-audio-open)
- **MMAudio** (video-to-audio Foley): CC-BY-NC-4.0, non-commercial. — [HF MMAudio](https://huggingface.co/hkchengrex/MMAudio)
- Mixkit's site navigation now includes "Generate Sounds with AI" (terms not inspected). — [Mixkit](https://mixkit.co/license/)

### Inferences
- Lowest-risk free stack for a monetised faceless account:
  1. Background music generated locally with ACE-Step 1.5 (MIT; no third party can claim it, though AI outputs may have weak copyright protection).
  2. Instagram Sound Collection inside the app, for business accounts.
  3. Pixabay or Mixkit downloads, keeping the license page or certificate.
  4. Freesound CC0 SFX, or MOSS-SoundEffect generation.
- Avoid for commercial or brand accounts: Instagram's licensed (non-Sound-Collection) library, MusicGen, MMAudio, FMA/Freesound NC tracks, and Uppbeat free if you dislike credit lines.
- Content ID mainly matters for YouTube cross-posting. Instagram uses Meta's Rights Manager, and no source here documents how Pixabay or Mixkit tracks fare there.
- Claude Code can drive Freesound via its API (needs a free API key; not verified here), Pixabay via its API (music coverage not verified), and the generators via Python. Mixkit, Uppbeat and Instagram Sound Collection are manual or browser-only.

### Gaps
- Whether YouTube Audio Library tracks may be used on Instagram is not answered by official Google pages. Many tracks are "attribution not required," but off-platform permission is unclear.
- Meta Rights Manager claim behaviour for Pixabay, Mixkit or AI-generated music was not found.
- Uppbeat's pricing page returned HTTP 429. The free-plan terms come from the help center and blog search snippets, and whether free covers commercial or ads use could not be confirmed (one competitor claims Pro is required).
- Pixabay API support for music downloads was not verified.
- No 2026 independent quality ranking of open music models was found; leadership claims are self-reported.

## Q4. How Claude Code drives each tool, and ease of use for a beginner

### Takeaway
Nearly every recommended free tool is a `pip install` package or a single CLI command, which Claude Code can install and script. Only CapCut, Instagram Sound Collection, Mixkit and Uppbeat require manual GUI or browser steps.

### Cited Findings
- `pip install kokoro` plus `apt install espeak-ng` — [kokoro](https://github.com/hexgrad/kokoro)
- `pip install chatterbox-tts` — [chatterbox](https://github.com/resemble-ai/chatterbox)
- `edge-tts --write-media … --write-subtitles …` — [edge-tts](https://pypi.org/project/edge-tts/)
- `faster-whisper` Python API with `word_timestamps=True` — [faster-whisper](https://github.com/SYSTRAN/faster-whisper)
- pycaps CLI plus Python `CapsPipelineBuilder`, installed from GitHub — [pycaps](https://github.com/francozanardi/pycaps); [dev.to tutorial](https://dev.to/francozanardi/adding-animated-subtitles-to-videos-with-python-4hml)
- Remotion `@remotion/captions` (Node) — [Remotion](https://www.remotion.dev/docs/captions/create-tiktok-style-captions)
- ACE-Step 1.5 via Transformers or Diffusers — [HF](https://huggingface.co/ACE-Step/Ace-Step1.5)
- MOSS-SoundEffect via `pip install -e` from the MOSS-TTS repo — [HF](https://huggingface.co/OpenMOSS-Team/MOSS-SoundEffect-v2.0)
- Google Cloud TTS via REST or gcloud with billing enabled — [Google](https://cloud.google.com/text-to-speech/pricing)

### Inferences
- Ease ranking for beginners (1 = easiest):
  1. edge-tts (no GPU, one command, built-in SRT)
  2. Kokoro (CPU)
  3. faster-whisper plus pycaps
  4. Chatterbox (GPU recommended)
  5. ACE-Step 1.5 (GPU, 4 GB+)
  6. Remotion (Node/React knowledge helps)
  7. Drama 3 / MOSS SFX (large GPU or CUDA-specific setup)
- Quality ratings (subjective synthesis from leaderboards):
  - TTS: Drama 3 > Step Audio EditX / S2 Pro > Kokoro ≈ Chatterbox > XTTS-v2.
  - Edge neural voices sound good but generic (no source rating found).

### Gaps
- No MCP servers for these specific tools were researched or verified. Claude Code can use them directly via Bash and Python, so MCP is not required.
