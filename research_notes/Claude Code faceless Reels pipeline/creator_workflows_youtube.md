# How successful faceless AI short-video creators produce Reels/Shorts/TikToks end to end (2026, YouTube-first evidence)

**Method and evidence notes (read first)**
- Checked on 2026-11-16. I ran 28 YouTube search queries twice: once with the "this year" filter and once sorted by view count for this year. That gave 595 unique videos. Each query pulled the YouTube search-results page and parsed its embedded `ytInitialData`. yt-dlp's search API returned **HTTP 403**. Watch pages redirected to Google's "sorry" captcha page (`google.com/sorry`). Per instructions I did **not** try to get around either block.
- **Exact upload dates, exact view counts and full descriptions** came from each channel's public RSS feed (`youtube.com/feeds/videos.xml?channel_id=…`). That feed only covers a channel's latest 15 uploads. Where a video was not in the feed, the date is approximate: it is worked back from YouTube's relative label (for example "5mo ago" ≈ June 2026, ±1 month) and marked "≈".
- **Method summaries** came from third-party transcript-based summary pages (videohighlight.com and youtubesummary.com) and from video descriptions and chapter lists. Evidence confidence per video:
  - **High** = I read the full transcript. **No video reached High**: transcript sites were behind JS/Cloudflare walls.
  - **Medium** = a transcript-derived summary was available.
  - **Low** = description, chapters or search snippet only.
- Reddit (www and old.reddit JSON) and BlackHatWorld returned **403** to both curl and WebFetch. Community evidence therefore comes from search-engine snippets of those threads, plus the communities the creators themselves link to.
- Raw data is in the scratchpad, not the repo: `/tmp/claude-0/-workspace-gen-ai/1c26cfc5-ea4a-5a7f-a2c5-e9438d60fba6/scratchpad/merged.json` (search results) and `/tmp/claude-0/-workspace-gen-ai/1c26cfc5-ea4a-5a7f-a2c5-e9438d60fba6/scratchpad/rss_out.json` (exact dates and descriptions).

---

## Q1. What end-to-end workflows do faceless AI Reels/Shorts creators demonstrate in 2026, which tools appear at each step, and which are free vs paid?

### Takeaway
The dominant 2026 pipeline, especially from May to November, is **"Claude (or ChatGPT) as producer"**: competitor research, then script, then a scene list with timestamps, then image/video prompts.

Media generation goes to one of two places:
- **A paid all-in-one generator**, Higgsfield (often through its MCP connector or CLI "skill" inside Claude), OpenArt or HeyGen.
- **A free stack**: Google Flow (Nano Banana / Veo / "Omni"), Grok image-to-video, Google AI Studio TTS, ElevenLabs free tier and CapCut.

From October to November 2026 a new branch appeared: **Claude Skills / Claude Code rendering the whole video in code** (Remotion, three.js) with no AI video generator at all. Almost every top tutorial monetizes the viewer through affiliate links (overwhelmingly Higgsfield), Skool communities, or the creator's own tool.

### Cited Findings

**Canonical step order, as demonstrated (with tools)**

1. **Research and idea.** Find 3–5 competitor channels, then connect vidIQ to Claude and run a "competition breakdown". It asks for the 5 best-performing topics with links.
   - Sanji Nai-Chien, ≈Sep 2026 — [youtubesummary](https://youtubesummary.com/summary/8Rf0xna31xg), [video](https://www.youtube.com/watch?v=8Rf0xna31xg).
   - Kellan Henneberry, 2026-06-28: install the free vidIQ Chrome extension, then paste the competitor channel ID into Claude via vidIQ — [videohighlight](https://videohighlight.com/v/V_t51u1tBJc).
   - vidIQ now sells a "free vidIQ MCP" that you paste into Claude/ChatGPT for niche checks — [vidIQ video description, 2026-11-09](https://www.youtube.com/watch?v=rStytOzzLwo).
   - Oleg Melnikov built a Claude Code tool for Instagram Reels. It needs three API keys (a social-media scraper, Gemini for video analysis, and Anthropic/OpenAI for scripts) and produced 60+ ideas from 23 analysed competitor Reels — [videohighlight](https://videohighlight.com/v/JhtbnZUU_8E) ([video](https://www.youtube.com/watch?v=JhtbnZUU_8E), ≈Mar 2026).
2. **Script.** Claude turns a "proven" topic into a new ~30-second Shorts script, then breaks it into scenes with voiceover line, on-screen visual and timestamps — [youtubesummary 8Rf0xna31xg](https://youtubesummary.com/summary/8Rf0xna31xg).
   - Mr omi had Claude derive a script formula from 20 reference Shorts: paradox or odd claim, then escalating detail, then explanatory pivot, then payoff/twist. Claude also fact-checks the story — [youtubesummary](https://youtubesummary.com/summary/OtbLL6OBNE4).
   - Sanji (2026-11-11) teaches a "4-part viral script formula", with Claude writing and fact-checking — [description](https://www.youtube.com/watch?v=quTKGJQnZLg).
3. **Voiceover first, visuals second.** This is an explicit, repeated principle.
   - zapiwala ai: "Voice-over first, scenes second". The steps are: ElevenLabs free plan (voice "Raunak"), then FoziScribe for pause-accurate timestamps, then Claude writes one image prompt per timestamped line — [youtubesummary](https://youtubesummary.com/summary/WVT2FCjhDDY) ([video](https://www.youtube.com/watch?v=WVT2FCjhDDY), 2026-06-11).
   - Danny Why records or generates the voiceover, transcribes it with Turboscribe (3 free transcriptions/day), and uses the timestamps to drive image generation — [videohighlight](https://videohighlight.com/v/WODnqHPLR38).
   - E'Calm: "Import voiceover first and edit audio pacing (remove dead time)", using Google AI Studio TTS (free) — [youtubesummary](https://youtubesummary.com/summary/srDpvEnGQg4).
4. **Visuals.**
   - *Free route.* Google Flow with the Nano Banana 2 image model, bulk-generated through the "Zapi Flow" Chrome extension. That extension is zapiwala's own product — [youtubesummary WVT2FCjhDDY](https://youtubesummary.com/summary/WVT2FCjhDDY).
   - Google Flow Agent Mode for batch images, then batch animation into 4-second clips; Omni Flash also appears — [Mark Ai Guy description, 2026-10-13](https://www.youtube.com/watch?v=H8FAaKeCguA).
   - Nano Banana Pro or Whisk for images, then Grok for vertical image-to-video. Grok gives "~10 free generations/day" (creator observation) — [youtubesummary srDpvEnGQg4](https://youtubesummary.com/summary/srDpvEnGQg4).
   - *Paid route.* Higgsfield through Claude's Settings → Connectors (MCP). It "breaks the video into clips… generates visuals, editing, voice-over and music", for example a 5-minute Pompeii documentary in ~10 minutes — [youtubesummary wU_bmWb6bhg](https://youtubesummary.com/summary/wU_bmWb6bhg).
   - OpenArt plus GPT Image 2 — [Youri van Hofwegen description](https://www.youtube.com/watch?v=XX3JzfYo1Rk). Seedance 2.0, Nano Banana Pro and GPT Image 2 for consistent kids' characters — [Jack Vs. AI description](https://www.youtube.com/watch?v=NnvRMs_0UQ8).
   - *Code route (new, Oct–Nov 2026).* Claude plus three.js plus Remotion renders frame by frame, "No AI video generator". It uses free 3D assets and procedural textures, with seven specialist sub-agents comparing frames against the references — [youtubesummary OtbLL6OBNE4](https://youtubesummary.com/summary/OtbLL6OBNE4).
   - "Claude writes and fact-checks the script, builds the entire 3D scene in code, and assembles the final video, while Higgsfield… generates the characters… 3D models, and voiceover" — [Sanji, 2026-11-11](https://www.youtube.com/watch?v=quTKGJQnZLg).
5. **Captions.**
   - Auto-subtitles from the voiceover inside RankReel, then restyle font, colour and shadow — [youtubesummary 8Rf0xna31xg](https://youtubesummary.com/summary/8Rf0xna31xg).
   - CapCut auto-captions — [Mark Ai Guy](https://www.youtube.com/watch?v=-fgNFJCQZGk).
   - Word-synced captions generated by the Nafay 3D Claude skill — [description](https://www.youtube.com/watch?v=n1N_ZIP5x3M).
6. **Music/SFX.**
   - YouTube Audio Library background music plus SFX and transitions in CapCut — [youtubesummary srDpvEnGQg4](https://youtubesummary.com/summary/srDpvEnGQg4).
   - Premiere Pro with background music — [youtubesummary za2VyvLl5T0](https://youtubesummary.com/summary/za2VyvLl5T0).
   - Epidemic Sound affiliate links are common — [Isaac description](https://www.youtube.com/watch?v=KhQTKG3Xtbs), [Natalie Fong description](https://www.youtube.com/watch?v=QxZR0gOC-dg).
   - Claude added music, SFX and text to a real CapCut project — [Matt Loui description](https://www.youtube.com/watch?v=5N1moUCsVhI).
7. **Editing/assembly.**
   - Drop the voiceover on the timeline, then trim each image to the timestamp embedded in its filename — [youtubesummary WVT2FCjhDDY](https://youtubesummary.com/summary/WVT2FCjhDDY).
   - Claude "synced every image to the voiceover, added music, sound effects and text, and keyframed each clip for subtle zooms" inside a real CapCut project. In other words, the Ken Burns effect is automated — [Matt Loui, ≈Oct 2026, sponsored by Higgsfield](https://www.youtube.com/watch?v=5N1moUCsVhI).
   - Claude plus Remotion generates motion graphics (counters, stacked lists, map animations, text highlights) that are then imported into CapCut — [Matt Loui, 2026-05-05](https://www.youtube.com/watch?v=8oIFBQ9BhVU).
   - Human-in-loop editing in Premiere: "remove dead air", sync voiceover, captions — [youtubesummary za2VyvLl5T0](https://youtubesummary.com/summary/za2VyvLl5T0).
8. **9:16 export.** "Maintain aspect ratio 9:16" when generating each scene clip — [youtubesummary 8Rf0xna31xg](https://youtubesummary.com/summary/8Rf0xna31xg). Grok is used for "vertical 9:16" image-to-video — [youtubesummary srDpvEnGQg4](https://youtubesummary.com/summary/srDpvEnGQg4).
   - Note: the zapiwala stickman flow generates **16:9** images. It is a long-form tutorial — [youtubesummary WVT2FCjhDDY](https://youtubesummary.com/summary/WVT2FCjhDDY).
9. **Packaging/upload.**
   - Claude writes the title, description, tags and 5 thumbnail prompts — [youtubesummary WVT2FCjhDDY](https://youtubesummary.com/summary/WVT2FCjhDDY).
   - Claude generates an upload package with thumbnail variants for A/B testing. Upload and scheduling are still manual — [youtubesummary wU_bmWb6bhg](https://youtubesummary.com/summary/wU_bmWb6bhg).
   - Fully automated daily posting through Zapier (sponsor) — [Nafay 3D](https://www.youtube.com/watch?v=n1N_ZIP5x3M).
   - Upload hygiene that creators repeat:
     - Warm up a new account (about 30 minutes of Shorts scrolling a day for 2 days, or 5–7 days) or reuse an old account; verify by phone — [youtubesummary 8Rf0xna31xg](https://youtubesummary.com/summary/8Rf0xna31xg), [youtubesummary srDpvEnGQg4](https://youtubesummary.com/summary/srDpvEnGQg4).
     - Use #shorts, set "not made for kids", no VPNs, 1–3 Shorts/day maximum — [youtubesummary srDpvEnGQg4](https://youtubesummary.com/summary/srDpvEnGQg4).
     - Post 1–2 Shorts every day without skipping — [videohighlight V_t51u1tBJc](https://videohighlight.com/v/V_t51u1tBJc).
     - Use an account older than 7 days; hold the next upload until analytics flatline for ~12 hours — [youtubesummary za2VyvLl5T0](https://youtubesummary.com/summary/za2VyvLl5T0).

**All-in-one / "one-click" tools pushed in 2026 tutorials (almost all paid, usually affiliate)**
- RankReel by Higgsfield (`rankreel.higgsfield.app`): paste viral TikTok clips, name the ranks, shuffle the playback order, one-click vertical Short — [Sanji description](https://www.youtube.com/watch?v=iJiBJAJRRkk).
- Viblo.ai for ranking Shorts — [Kellan description](https://www.youtube.com/watch?v=V_t51u1tBJc).
- Vsub — [Mark Ai Guy](https://www.youtube.com/watch?v=H8FAaKeCguA), [E'Calm](https://www.youtube.com/watch?v=ZxTudE4T5fw). Kutly — [E'Calm](https://www.youtube.com/watch?v=Sp83h2FqOH0). moraviral — [ReachMora](https://www.youtube.com/watch?v=kDcxEIDC5NA). TubeGen — [Eddie Eizner](https://www.youtube.com/watch?v=8UW7TNr2S5A). HeyGen digital twin — [Joshua Mayo](https://www.youtube.com/watch?v=72dGWuCMUyI). OpenArt Director — [Joshua Mayo](https://www.youtube.com/watch?v=4LryAnzFLMw). Swagga AI — [Jennifer Turner](https://www.youtube.com/watch?v=fjbE7EnM0bo).
- TubeGen run end to end: a 20,000-word script became a 2h47m video, cost "10,000–15,000 credits", using a 5:1 image-to-B-roll ratio plus an AI-avatar intro. Its built-in editor handles videos up to 20 minutes only — [videohighlight 8UW7TNr2S5A](https://videohighlight.com/v/8UW7TNr2S5A).

**Free vs paid, as demonstrated**
- *Shown as free:*
  - Claude free plan: [zapiwala](https://www.youtube.com/watch?v=WVT2FCjhDDY), [Nafay 3D](https://www.youtube.com/watch?v=n1N_ZIP5x3M), [Brunoe AI](https://www.youtube.com/watch?v=73uCC76-D50).
  - ElevenLabs free plan; Google Flow plus Nano Banana 2: [zapiwala](https://www.youtube.com/watch?v=WVT2FCjhDDY).
  - FoziScribe, Turboscribe (3 a day): [videohighlight WODnqHPLR38](https://videohighlight.com/v/WODnqHPLR38).
  - Google AI Studio TTS, Whisk, Grok (~10 a day), YouTube Audio Library: [youtubesummary srDpvEnGQg4](https://youtubesummary.com/summary/srDpvEnGQg4).
  - CapCut ("Just Use Capcut, It's Free"): [Romayroh description](https://www.youtube.com/watch?v=zxFZE_-w54Y).
  - Google Vids: [Jacksons AI](https://www.youtube.com/watch?v=zocKB90jZZg).
  - Free video generators Pavo AI, Digen, AI Free Video, ModelScope and Google Vids were compared, then contrasted with paid Higgsfield. That video is sponsored by Higgsfield — [Youri van Hofwegen](https://www.youtube.com/watch?v=nmpHMBnZHWQ).
  - BytePlus Seedance 1.5 Pro free credits at 480p — [Youri](https://www.youtube.com/watch?v=I9EvujHJm3o).
  - Open-source local video generation — [Kevin Stratvert, ≈Feb 2026](https://www.youtube.com/watch?v=G2Ec3h5CfA8).
- *Paid:*
  - Higgsfield, advertised with "Up to 60% OFF premium plans" and a 3-day MCP trial that "renews to a paid plan" — [Higgsfield description](https://www.youtube.com/watch?v=YP8D2_j3_Hc).
  - Claude Code via a paid subscription ("minimum $19/month" per the summary) — [videohighlight JhtbnZUU_8E](https://videohighlight.com/v/JhtbnZUU_8E).
  - HeyGen, OpenArt, TubeGen and Kling, all via affiliate links (see above). Kling affiliate — [FILM CRUX](https://www.youtube.com/watch?v=PzOH1v5GaW0).

### Inferences
- The "producer LLM plus media generator plus CapCut" triad is now the default. In 2026 the scripting LLM shifted visibly from ChatGPT toward **Claude**: 12 of the top on-topic titles name Claude, and many tutorials ship a free "Claude skill". ChatGPT remains common in the free/stickman tutorials.
- **"Voiceover first, then timestamp-driven visuals"** is the most consistent craft rule across independent creators (zapiwala, Danny Why, E'Calm). It is the key design point for any pipeline: audio timing drives scene durations.
- From October to November 2026, "render in code" (Remotion/three.js driven by Claude) is spreading. It sidesteps per-clip generator costs. This is the most relevant style for a Claude-Code-based pipeline.

### Gaps
- No full transcripts (High confidence) were obtained, so exact prompts, settings and timings inside the videos are unverified beyond the summaries.
- Current 2026 prices for Higgsfield, ElevenLabs, Kling and others were not verified from vendor pricing pages. The only figures are creator claims.
- Instagram- and TikTok-specific upload and export steps are rarely shown. Most tutorials are YouTube-first and say "works for Reels/TikTok too".

---

## Q2. What are the main styles of AI short video, and what tools, cost, labour and performance does each involve?

### Takeaway
Seven styles dominate 2026 tutorials:
1. Stickman / 2D-in-3D animated explainers (the hottest by count, Oct–Nov 2026).
2. AI-image "mini-documentary" slideshows with zooms.
3. Fully generated AI video clips (Veo, Kling, Seedance, Grok, Higgsfield).
4. Ranking/compilation Shorts built from viral TikTok clips.
5. Recurring AI characters and AI influencers (Instagram-led).
6. Motion-graphics / kinetic-text and commentary Shorts.
7. Code-rendered 3D animation via Claude.

**Reddit-story-over-gameplay and quiz formats are nearly absent from 2026 tutorial results.** This is consistent with their being the formats YouTube's policy text names as non-monetizable.

### Cited Findings

**1. Stickman / 2D characters in 3D worlds ("Rick's Clips" style)**
- Tools: ChatGPT or Claude free for the master prompt and script, Google Flow / Omni Flash for images and animation, ElevenLabs, CapCut — [Mark Ai Guy, 2026-11-09, 228,023 views](https://www.youtube.com/watch?v=-fgNFJCQZGk).
- Other versions: Claude free, Google Flow, ElevenLabs, CapCut — [Brunoe AI, 2026-11-10](https://www.youtube.com/watch?v=73uCC76-D50). Claude free plus Google Vids "on autopilot" — [Jacksons AI, 2026-11-04](https://www.youtube.com/watch?v=zocKB90jZZg). OpenCode or Claude Code for 3D stickman — [Jacksons AI, 2026-11-15](https://www.youtube.com/watch?v=Gu9lO8oqGYU).
- Cost: free-tier capable. Labour: low to medium.
- Performance claims: the example stickman channel had "7.5 million views on one video… 14 videos, 137,000 subscribers… first upload 2 months ago" — [youtubesummary WVT2FCjhDDY](https://youtubesummary.com/summary/WVT2FCjhDDY). Treat as an unverified creator claim.
- Search saturation: 30 stickman tutorials in my 2026 sample. The top one has 857,399 views — [AI4Next, ≈Mar 2026](https://www.youtube.com/watch?v=QQVmuuSqv18).

**2. AI-image mini-documentary / slideshow with zoom (Ken Burns)**
- Pipeline: Claude script, then timestamped image prompts, then Nano Banana / Higgsfield images, then CapCut with keyframed zooms — [Matt Loui](https://www.youtube.com/watch?v=5N1moUCsVhI), [zapiwala](https://www.youtube.com/watch?v=WVT2FCjhDDY), [Danny Why](https://www.youtube.com/watch?v=WODnqHPLR38).
- Cost: free to low. Labour: low.
- **Policy risk is highest here.**
  - YouTube lists "Image slideshows, templated storylines, or scrolling text with minimal or no narrative, commentary, or educational value" as not allowed to monetize — [YouTube channel monetization policies](https://support.google.com/youtube/answer/1311392?hl=en).
  - Eddie Eizner names "slideshow videos where long static images make up most of the runtime" as one of three demonetization triggers. He suggests ≤10 seconds per image — [description](https://www.youtube.com/watch?v=8UW7TNr2S5A), [videohighlight](https://videohighlight.com/v/8UW7TNr2S5A).
  - [OLDER, 2025, still applies] A creator's Substack says AI slideshow videos struggle to compete with fast-paced Shorts and pivoted to longer videos — [automatedincomelifestyle](https://automatedincomelifestyle.substack.com/p/90-days-into-my-faceless-automated).

**3. Fully AI-generated video clips (Veo / Kling / Seedance / Grok / Higgsfield)**
- AI pet-salon transformation Shorts: ChatGPT for structure, Higgsfield for reference images, per-phase images, animation and voiceover, then Premiere for assembly.
  - Result: 694K views and 2,000 subscribers within 48 hours; average viewed 82–88% on a 59-second Short — [youtubesummary za2VyvLl5T0](https://youtubesummary.com/summary/za2VyvLl5T0) ([Jack Craig, 2026-05-01, 1,427,227 views](https://www.youtube.com/watch?v=za2VyvLl5T0)).
- "Talking cat and dog podcast" with consistent characters, voices, locations and camera cuts — [Youri van Hofwegen, 2026-10-29, sponsored by Higgsfield](https://www.youtube.com/watch?v=VVU3GLgk-R0).
- Tutorials: Kling 4.0 — [FILM CRUX, ≈Oct 2026, 1,115,315 views, Kling affiliate](https://www.youtube.com/watch?v=PzOH1v5GaW0). Kling 3.0 consistent characters — [Dan Kieft, ≈Apr 2026](https://www.youtube.com/watch?v=0CjArtUh_Wg).
- Cost: medium to high, credit-based, paid. Labour: medium, because of re-rolls and consistency work.
- Policy risk: YouTube bars "videos that stitch together unrelated or inconsistent AI clips to surprise or shock viewers" — [YouTube policy](https://support.google.com/youtube/answer/1311392?hl=en).

**4. Ranking / compilation Shorts from viral TikTok clips**
- Claude plus vidIQ for topics, then RankReel (Higgsfield) or Viblo to assemble ranked clips with a "custom playback order".
- Claims: "$30K/month"; one Short got 17M views and $3.8K — [videohighlight V_t51u1tBJc](https://videohighlight.com/v/V_t51u1tBJc), [videohighlight iJiBJAJRRkk](https://videohighlight.com/v/iJiBJAJRRkk).
- Cost: low (tool subscription). Labour: very low (5–10 minutes per video, claimed).
- **Conflict:** this re-uses other people's clips, which falls under YouTube's separate "reused content" policy covering "clips, compilations" — [YouTube policy](https://support.google.com/youtube/answer/1311392?hl=en). Instagram removed recommendations for accounts that mostly post unoriginal content (April 30, 2026) — [Tubefilter](https://tubefilter.com/2026/04/30/instagram-removes-algorithm-recommendations-repost-content-aggregator), [Instagram Creators blog](https://creators.instagram.com/blog/rewarding-original-creators-on-instagram).

**5. Recurring AI character / AI influencer (Instagram-led)**
- Mark Tilbury built three AI influencers with Claude (personas and scripts) and Higgsfield (photos, voice, video). He launched them on Instagram with 10 posts each.
  - Best account: one video hit 250K views.
  - Monetized by selling a $12 workbook: 23 sales, $276 revenue, **$157.48 profit** after a $118.52 cost — [videohighlight LlhTEttKcwQ](https://videohighlight.com/v/LlhTEttKcwQ) ([video, 2026-09-21, 9,993,418 views](https://www.youtube.com/watch?v=LlhTEttKcwQ)).
- Indian Instagram "Sheru Bhai" lion-character AI reels are a November 2026 trend:
  - Tutorials: [Tarun Editz, 1,776,166 views, ≈Nov 10](https://www.youtube.com/watch?v=LFDKWwM-txo) and [Chitransh Asthana, 1,009,315 views, ≈Nov 7, ChatGPT](https://www.youtube.com/watch?v=Kasq1e8rmyc).
  - Example output: [AaluToons Sheru short, 10,472,506 views, ≈Oct](https://www.youtube.com/watch?v=Aa8flbAH23Y).
- AI influencer monetization with a Higgsfield affiliate — [DIGITAL INCOME PROJECT, ≈Mar 2026](https://www.youtube.com/watch?v=gXaF4t4B4ss). HeyGen "digital twin" AI host — [Joshua Mayo, 2026-09-28](https://www.youtube.com/watch?v=72dGWuCMUyI).
- Policy risk:
  - YouTube does not monetize "Videos where characters are put in the same situation over and over again with the same outcome".
  - It also bars "AI personas… on topics such as health, legal issues, finances", for example an AI doctor or an AI finance podcast host — [YouTube policy](https://support.google.com/youtube/answer/1311392?hl=en).
  - Tilbury's best persona was a health influencer ("Amos") — [videohighlight](https://videohighlight.com/v/LlhTEttKcwQ).

**6. Motion graphics / kinetic text / commentary Shorts**
- Claude plus Remotion produces motion graphics (counters, lists, maps, text highlight) for CapCut — [Matt Loui, 785,308 views](https://www.youtube.com/watch?v=8oIFBQ9BhVU).
- Also: "Claude + CapCut… color grading, motion graphics and animation from a text prompt" — [Sanji, ≈Sep 2026, 695,736 views](https://www.youtube.com/watch?v=j4FzO2fF1kg). A free master prompt for motion graphics — [ReachMora, ≈Oct, 506,950 views](https://www.youtube.com/watch?v=n50KkoucMpU).
- Commentary Shorts: download a viral clip, write an original commentary script in Claude, voice it with ElevenLabs, edit in CapCut — [Krish, 2026-07-21](https://www.youtube.com/watch?v=xeng_HQjLIE). Text-commentary Shorts — [Jonas Rankl, ≈Jun](https://www.youtube.com/watch?v=QfbGKfkGP8U).
- Cost: free to low. Labour: medium.

**7. Claude-coded 3D/2D animation (no video generator)**
- [Mr omi, 2026-11-01, 1,120,816 views](https://www.youtube.com/watch?v=OtbLL6OBNE4): three.js plus Remotion, with a free skill on GitHub (`github.com/mromidev/claude-animated-shorts`).
- "Kaz Short Films" Claude Code skill for no-voiceover cinematic shorts — [Grow With Kaz, 2026-11-10](https://www.youtube.com/watch?v=Ock60o-Glh4).
- Sanji with Higgsfield assets plus Claude 3D assembly, claiming "2–3 high-retention Shorts a day" once the asset library exists — [2026-11-11](https://www.youtube.com/watch?v=quTKGJQnZLg).
- "Viral animated Shorts using only Claude", with a Claude skill plus ElevenLabs producing an MP4 — [ReachMora, 2026-11-03, 626,924 views](https://www.youtube.com/watch?v=kDcxEIDC5NA).
- Cost: low marginal cost, but a high one-time setup. The first version "looked cheap" and needed multi-agent fixes — [youtubesummary](https://youtubesummary.com/summary/OtbLL6OBNE4).
- Nafay 3D's free Claude skill ships five preset styles: "Deep Dive 3D", "Night File 3D" (mysteries), "Inside Out" (2D x-ray), "Stick Story", and "Paper Atlas" (cut-paper history maps) — [description](https://www.youtube.com/watch?v=n1N_ZIP5x3M).

**Absent or rare formats**
- Reddit-story-over-gameplay: my 2026 sample (595 videos) had no 2026 tutorial for it. The "reddit" hits were Smosh Pit live reading shows and unrelated content.
- Quiz/trivia: no 2026 tutorials in the sample.
- Make Money Matt lists "Reddit-story / revenge-story channels that mass-produce content with AI" among those getting hit — [youtubesummary RSnGnIWUvIQ](https://youtubesummary.com/summary/RSnGnIWUvIQ) ([video, ≈Apr 2026](https://www.youtube.com/watch?v=RSnGnIWUvIQ)).
- A blog calls untransformed AI narration of scraped Reddit stories "the classic pattern that fails" — [Medium](https://mateostarcevicfilipovic.medium.com/youtube-quietly-demonetizes-faceless-ai-channels-since-july-2025-30b3d2daaf2e) (commentary, low authority).

### Inferences
- Cheapest and most automatable: stickman, slideshow and ranking compilations. These also carry the most policy risk (template, slideshow and reused-content language).
- The styles that 2026 creators frame as "safe" add a visible creative layer: an original story, a recurring stylized world, code-built animation, or real commentary.
- Reddit-gameplay and quiz formats seem to have dropped out of the tutorial ecosystem. This is inferred from their absence in 595 results, not from a direct source.

### Gaps
- No independent, systematic performance comparison between styles was found. Performance figures are creator self-reports or vidIQ estimates.
- I could not verify the claimed earnings of example channels (vidIQ estimates as shown on screen).

---

## Q3. Ranked list: most-viewed and most process-revealing 2026 YouTube videos

Ranking: on-topic relevance × views × how much process is revealed. Views were observed 2026-11-16. Dates are exact (from RSS) unless marked ≈. Abbreviations: Aff = affiliate, Spon = sponsored, Conf = evidence confidence.

| # | Video | Channel | Views | Uploaded | Method shown (2–3 lines) | Sponsor / affiliate | Conf |
|---|---|---|---|---|---|---|---|
| 1 | [I Tried The LAZIEST Way to Make Money With AI](https://www.youtube.com/watch?v=LlhTEttKcwQ) | Mark Tilbury | 9,993,418 | 2026-09-21 | 7-day test of AI Instagram influencers: Claude for personas and scripts, Higgsfield for photos, voice and video, 10 posts per account, sold a $12 workbook. Net profit $157.48 ([summary](https://videohighlight.com/v/LlhTEttKcwQ)). | Aff: Higgsfield ("This is an affilliate link") | Medium |
| 2 | [How I Make $24,937/mo Posting YouTube Shorts (Using Claude AI)](https://www.youtube.com/watch?v=V_t51u1tBJc) | Kellan Henneberry | 1,770,360 | 2026-06-28 | Ranking Shorts from viral TikTok clips. vidIQ extension plus Claude for competitor topics, Viblo.ai to assemble, 1–2 Shorts a day. Claims 17M views earned $3.8K ([summary](https://videohighlight.com/v/V_t51u1tBJc)). | Viblo link (affiliate status not stated) | Medium |
| 3 | [Claude Code Just Changed YouTube Forever!](https://www.youtube.com/watch?v=WODnqHPLR38) | Danny Why | 1,737,761 | ≈Jun 2026 | Clones a "Zen" channel. Claude Code with the Higgsfield CLI skill, voiceover, Turboscribe timestamps, a master prompt for timestamped images, then editing ([summary](https://videohighlight.com/v/WODnqHPLR38)). Long-form oriented. | Aff: Higgsfield; Skool | Medium |
| 4 | [How a Faceless Channel Made $39K With Claude + ChatGPT](https://www.youtube.com/watch?v=8Rf0xna31xg) | Sanji Nai-Chien | 1,691,835 | ≈Sep 2026 | ~30-second mini-docs: vidIQ plus Claude for topics, Claude for script and scene list, RankReel for voice, clips/AI shots, 9:16 and auto-subs. ChatGPT for branding; account warm-up ([summary](https://youtubesummary.com/summary/8Rf0xna31xg)). | Likely Higgsfield-affiliated (RankReel is a Higgsfield app; full description not seen) | Medium |
| 5 | [The $30K/Month AI Faceless Shorts Method…](https://www.youtube.com/watch?v=iJiBJAJRRkk) | Sanji Nai-Chien | 1,537,609 | ≈Aug 2026 | Ranking Shorts: Claude plus vidIQ, then RankReel (paste TikTok clips, shuffle order, one-click vertical), 1–2 a day ([summary](https://videohighlight.com/v/iJiBJAJRRkk)). | Higgsfield/RankReel links | Medium |
| 6 | [I BLEW UP a YouTube Channel in 24 Hours with AI](https://www.youtube.com/watch?v=za2VyvLl5T0) | Jack Craig | 1,427,227 | 2026-05-01 | Reverse-engineers a channel's 6-phase formula into "AI pet salon". ChatGPT, Higgsfield (images, animation, voiceover), Premiere. Shows real analytics: 694K views and 2K subscribers in 48 hours ([summary](https://youtubesummary.com/summary/za2VyvLl5T0)). | Aff: Higgsfield; coaching | Medium |
| 7 | [Claude Code (Free Plan) + YouTube = $77,000/Month](https://www.youtube.com/watch?v=WVT2FCjhDDY) | zapiwala ai | 1,211,088 | 2026-06-11 | Free stickman stack: Claude free, ElevenLabs free, FoziScribe timestamps, Claude image prompts, Google Flow Nano Banana 2 via the Zapi Flow bulk extension, timestamp-synced edit ([summary](https://youtubesummary.com/summary/WVT2FCjhDDY)). | Own product (Zapi Flow); all links via zapiwala.ai shortlinks | Medium |
| 8 | [How to Make Viral Animated Shorts Using Claude (Full Workflow)](https://www.youtube.com/watch?v=OtbLL6OBNE4) | Mr omi | 1,120,816 | 2026-11-01 | Claude analyses 20 Shorts at 30 fps into a style bible. three.js plus Remotion render; 7 critique agents; free GitHub skill ([summary](https://youtubesummary.com/summary/OtbLL6OBNE4)). | Paid Skool upsell; no generator affiliate | Medium |
| 9 | [I Copied a Top Faceless Channel's Format With AI in 20 Minutes](https://www.youtube.com/watch?v=wU_bmWb6bhg) | Higgsfield AI (vendor) | 1,111,713 | ≈Jul 2026 | Claude plus Higgsfield MCP connector. "Borrow the format, not the videos". One prompt gives a 5-minute documentary plus Shorts and thumbnail variants ([summary](https://youtubesummary.com/summary/wU_bmWb6bhg)). | Vendor-owned channel | Medium |
| 10 | [How to Create AI YouTube Videos That Make Money in 2026](https://www.youtube.com/watch?v=72dGWuCMUyI) | Joshua Mayo | 1,000,189 | 2026-09-28 | HeyGen digital twin as AI host, niche framework, monetization (description). | Aff: HeyGen | Low |
| 11 | [Claude Edited My Entire CapCut Video](https://www.youtube.com/watch?v=5N1moUCsVhI) | Matt Loui | 984,150 | ≈Oct 2026 | Claude script, Higgsfield voice and images, Claude builds a real CapCut project (sync, music, SFX, text, zoom keyframes); free skill (description). | Spon: Higgsfield | Low |
| 12 | [My $75K YouTube Shorts System – Full Course In 19 Minutes](https://www.youtube.com/watch?v=srDpvEnGQg4) | E'Calm | 972,236 | ≈Mar 2026 | Recreate viral emotional-story Shorts: rewrite the transcript, Google AI Studio TTS, Nano Banana Pro/Whisk, Grok 9:16, CapCut, YouTube Audio Library. Hook–body–reward; 1–3 a day ([summary](https://youtubesummary.com/summary/srDpvEnGQg4)). | Gumroad course, paid WhatsApp group | Medium |
| 13 | [How To Grow A Faceless YouTube Channel In 2026 – FULL COURSE](https://www.youtube.com/watch?v=Bbjv9-00tv0) | Fabio Morena | 885,781 | 2026-04-12 | 1h42m fundamentals course: niche, sourcing, scripts, AI voices, editing, hiring. Long-form focus (description). | Skool community | Low |
| 14 | [I Blew Up a Shorts Channel in 7 Days!](https://www.youtube.com/watch?v=QXfugR3ZIAs) | Isaac | 848,234 | ≈Oct 2026 | New Shorts channel aiming for 1M views on one Short in 7 days: niche, scripts, animation, "secret sauce" (description). | Spon: .store domain; Aff: ElevenLabs | Low |
| 15 | [AI Video Workflow – Faceless Channel From Zero](https://www.youtube.com/watch?v=FAW6AuzT1Uw) | Faisal Shabbir | 820,149 | ≈Aug 2026 | Idea, AI script, voiceover, scenes, animation, edit, export, with a master prompt (description). | Aff: Hostinger | Low |
| 16 | [Claude + CapCut Completely Changes Everything For Editors](https://www.youtube.com/watch?v=8oIFBQ9BhVU) | Matt Loui | 785,308 | 2026-05-05 | Claude plus Remotion motion graphics (LUTs, counters, lists, maps, text highlights) imported into CapCut (description and chapters). | Own course; CapCut referral | Low |
| 17 | [How To Make Faceless YouTube Shorts with Claude (Free Skill/Automation)](https://www.youtube.com/watch?v=n1N_ZIP5x3M) | Nafay 3D | 714,048 | 2026-11-01 | Free Claude skill on the free plan: script, visuals, voiceover, word-synced captions; 5 styles; Zapier daily auto-posting (description). | Spon: Zapier | Low |
| 18 | [Forget After Effects: Claude + CapCut…](https://www.youtube.com/watch?v=j4FzO2fF1kg) | Sanji Nai-Chien | 695,736 | ≈Sep 2026 | Claude editing inside CapCut: grading, motion graphics, animation from text (snippet). | Not checked | Low |
| 19 | [I Tried Making a Viral Video Using ONLY Claude AI](https://www.youtube.com/watch?v=kDcxEIDC5NA) | ReachMora | 626,924 | 2026-11-03 | Claude skill: 10 story ideas, script, ElevenLabs voiceover, auto-rendered animated MP4. No CapCut (description). | Aff: moraviral (40% off link) | Low |
| 20 | [How to Create Stickman Animation with AI 100% FREE](https://www.youtube.com/watch?v=H8FAaKeCguA) | Mark Ai Guy | 600,309 | 2026-10-13 | ChatGPT master prompt, Google Flow Agent Mode batch images, batch 4-second animations (Omni Flash), ElevenLabs, CapCut (description). | Aff: Vsub; "comment for prompt" | Low |
| 21 | [How to Create AI Animated Stories That Make Money… 2026](https://www.youtube.com/watch?v=4LryAnzFLMw) | Joshua Mayo | 585,899 | 2026-08-12 | OpenArt Director: consistent characters, animation, narration, hybrid AI plus real footage (description). | Aff: OpenArt | Low |
| 22 | [How to Make YouTube Shorts with AI (Full Guide)](https://www.youtube.com/watch?v=XX3JzfYo1Rk) | Youri van Hofwegen | 387,175 | ≈Jul 2026 | Under 15 minutes per Short: Claude ideas and script, ElevenLabs, OpenArt / GPT Image 2, CapCut (description). | Aff: OpenArt | Low |
| 23 | [How to Build a Kids Animation Channel with AI](https://www.youtube.com/watch?v=NnvRMs_0UQ8) | Jack Vs. AI | 350,344 | ≈Jul 2026 | Nano Banana Pro world style, GPT Image 2 character sheets, Seedance 2.0 animation, music and lip-sync (description). | Aff: Higgsfield | Low |
| 24 | [How to Make Viral Stickman Animated Shorts Using FREE AI TOOLS](https://www.youtube.com/watch?v=-fgNFJCQZGk) | Mark Ai Guy | 228,023 | 2026-11-09 | Rick's Clips style: ChatGPT, Google Flow plus Omni Flash 10-second clips stitched, ElevenLabs, CapCut. Appeared in 12 of my 28 queries (description). | Telegram; comment-for-prompt | Low |
| 25 | [$0–$45,186 In 30 Days With Faceless YouTube Automation](https://www.youtube.com/watch?v=HOEqRYPD7sE) | Chris Barrera | 181,343 | ≈Jun 2026 | Anti "full automation": Claude adapts scripts, Upwork/onlinejobs.ph freelancers edit, 1–2 hours a day; body-cam niche ([summary](https://videohighlight.com/v/HOEqRYPD7sE)). | Coaching | Medium |
| 26 | [How to Build a Faceless Channel YouTube Won't Demonetize (Claude Fable 5.2)](https://www.youtube.com/watch?v=YP8D2_j3_Hc) | Higgsfield AI (vendor) | 178,336 | 2026-11-11 | Claude plus Higgsfield MCP: 5-minute documentary, then fix bad shots, then thumbnails, then Shorts (chapters). | Vendor; trial auto-renews | Low |
| 27 | [My Claude Code System For Viral Instagram Reels](https://www.youtube.com/watch?v=JhtbnZUU_8E) | Oleg Melnikov | 162,258 | ≈Mar 2026 | Claude Code app scrapes competitor Reels and analyses them with Gemini, then writes hooks and scripts; 60+ ideas from 23 Reels ([summary](https://videohighlight.com/v/JhtbnZUU_8E)). | Own agency | Medium |
| 28 | [How I edit viral commentary shorts with Claude AI and CapCut](https://www.youtube.com/watch?v=xeng_HQjLIE) | Krish | 158,675 | 2026-07-21 | Viral clip, Claude commentary script, ElevenLabs, CapCut pacing and SFX (description). | Spon/aff: Filmora; own SFX pack | Low |
| 29 | [How to Make YouTube Shorts with AI](https://www.youtube.com/watch?v=VVU3GLgk-R0) | Youri van Hofwegen | 135,842 | 2026-10-29 | Recurring talking cat-and-dog podcast characters: consistent voices and locations, camera cuts, SFX, auto-captions (description). | Spon: Higgsfield | Low |
| 30 | [How To Build a Faceless YouTube Channel with Claude (Full Automation)](https://www.youtube.com/watch?v=zXE_PpJ5WUc) | Zinho Automates | 115,755 | 2026-10-30 | Claude plus Higgsfield MCP: niche, identity, first video, refine, "virality predictor", Shorts (chapters). | Aff: Higgsfield | Low |

**Critical / policy videos (high views, important counterweight)**

| Video | Channel | Views | Uploaded | Gist | Conf |
|---|---|---|---|---|---|
| [The Death of Educational Content on YouTube](https://www.youtube.com/watch?v=-Gnrp_caPvo) | fern | 11,528,272 | 2026-09-02 | Investigation of AI "slop" copycat channels: thumbnail/format cloning, hallucinated history (including Holocaust-content errors), tool vendors as accelerants ([summary](https://youtubesummary.com/summary/-Gnrp_caPvo)). Sponsored by FlexiSpot. | Medium |
| [A Big Problem With AI "History" Videos](https://www.youtube.com/watch?v=PSB83EKg_oQ) | magnify | 1,006,026 | ≈Jun 2026 | Factual and visual errors as the "Achilles heel" of AI history content ([description](https://videohighlight.com/v/PSB83EKg_oQ)). | Low |
| [AI Slop Could Bankrupt YouTube](https://www.youtube.com/watch?v=iVE2ogxKE3s) | Siliconversations | 264,655 | ≈May 2026 | Argues YouTube embracing AI slop threatens its business (snippet). | Low |
| [How to Build a Faceless Channel YouTube Won't Demonetize](https://www.youtube.com/watch?v=d_csri5M9xw) | vidIQ | 233,944 | ≈Aug 2026 | AI sleep channels versus the crackdown on mass-produced content (description). | Low |
| [Why AI STORY Channels Keep Getting Demonetized](https://www.youtube.com/watch?v=QxZR0gOC-dg) | Natalie Fong | 164,802 | 2026-06-06 | Reused and repetitive-content triggers for AI story channels (description). | Low |
| [The New Rules For Faceless Channels in 2026](https://www.youtube.com/watch?v=ye2T2FwubI4) | vidIQ | 134,571 | ≈Sep 2026 | Five rules: narrator POV, characters/conflict, recognizable visual style, writing, expertise (description). | Low |
| [YouTube ENDS Faceless AI YouTube Channels?](https://www.youtube.com/watch?v=RSnGnIWUvIQ) | Make Money Matt | 130,134 | ≈Apr 2026 | AI moderation false positives. Reddit-story, celebrity, fake-trailer and MMO niches are hit. Advice: use an avatar/character as the "face" ([summary](https://youtubesummary.com/summary/RSnGnIWUvIQ)). | Medium |
| [New YouTube Monetization Update: Inauthentic Content Has Gone!](https://www.youtube.com/watch?v=JvZ0MXl70fc) | vidIQ | 103,328 | ≈Aug 2026 | Explains the new "unsatisfying or off-putting" label (description). | Low |
| [AI Channels Are Getting Demonetized Again, Here's How to Avoid It](https://www.youtube.com/watch?v=8UW7TNr2S5A) | Eddie Eizner | 75,510 | 2026-02-18 | Three triggers: repeated thumbnails, repeated title phrasing, static slideshows; plus monthly upload hours. Lost "$70,000 a month" over 12 channels ([summary](https://videohighlight.com/v/8UW7TNr2S5A)). Aff: TubeGen. | Medium |
| [YouTube Just Started a War on AI Channels](https://www.youtube.com/watch?v=F0dvK0MOrfM) | Thinkverse AI | 67,383 | 2026-10-25 | Target is mass-produced repetitive content, not AI itself (description). | Low |

**[OLDER] still relevant**
- [I BLEW UP a YouTube Channel in 7 Days with AI](https://www.youtube.com/watch?v=1r0eyM7suUg), Jack Craig: 2,550,386 views, uploaded 2025-11-21. It is the predecessor of #6 and still ranks top for "faceless AI" queries.

### Takeaway
The most-viewed 2026 videos sit in the "make money with AI" genre (Tilbury) rather than pure tutorials. The most process-revealing ones are Sanji (#4/#5), Jack Craig (#6), zapiwala (#7), Mr omi (#8), E'Calm (#12) and Higgsfield (#9). **Roughly 15 of the top 30 carry Higgsfield affiliate or sponsor links or are made by Higgsfield itself**, a strong commercial bias in the tutorial ecosystem.

### Cited Findings
- Higgsfield affiliate/sponsor links appear in:
  - [Tilbury](https://www.youtube.com/watch?v=LlhTEttKcwQ), [Danny Why](https://www.youtube.com/watch?v=WODnqHPLR38), [Jack Craig](https://www.youtube.com/watch?v=za2VyvLl5T0), [Sanji](https://www.youtube.com/watch?v=iJiBJAJRRkk), [Sanji 2](https://www.youtube.com/watch?v=quTKGJQnZLg).
  - [Matt Loui (Spon)](https://www.youtube.com/watch?v=5N1moUCsVhI), [Youri (Spon)](https://www.youtube.com/watch?v=VVU3GLgk-R0), [Jack Vs. AI](https://www.youtube.com/watch?v=NnvRMs_0UQ8), [Zinho](https://www.youtube.com/watch?v=zXE_PpJ5WUc), [Make Money Matt](https://www.youtube.com/watch?v=0lTLOyB7QUE), [DIGITAL INCOME PROJECT](https://www.youtube.com/watch?v=gXaF4t4B4ss).
  - Plus Higgsfield's own channel: [1](https://www.youtube.com/watch?v=wU_bmWb6bhg), [2](https://www.youtube.com/watch?v=YP8D2_j3_Hc).
- Iman Gadzhi's [How To Make $10,000/Month With Higgsfield](https://www.youtube.com/watch?v=vOBKA8n15vg) has 1,361,831 views (2026-10-28) but little process (description only).
- Many free-prompt offers are gated behind "comment X" or a Telegram/Skool join:
  - [Mark Ai Guy](https://www.youtube.com/watch?v=-fgNFJCQZGk), [Jacksons AI](https://www.youtube.com/watch?v=Gu9lO8oqGYU), [Grow With Kaz](https://www.youtube.com/watch?v=Ock60o-Glh4), [Fabio Morena](https://www.youtube.com/watch?v=Bbjv9-00tv0).

### Inferences
- Treat revenue claims in titles ($24,937/mo, $30K/mo, $39K, $77,000/mo) as marketing. Several are **vidIQ estimates of other people's channels**, not the presenter's own revenue — [youtubesummary 8Rf0xna31xg](https://youtubesummary.com/summary/8Rf0xna31xg), [youtubesummary wU_bmWb6bhg](https://youtubesummary.com/summary/wU_bmWb6bhg).
- The 2026 corpus is dominated by "Claude + X" titles from June to November. Process demos converge, but the media layer is vendor-driven.

### Gaps
- Sanji #4, Danny Why #3, Higgsfield #9 and vidIQ: these were not in the RSS feed window, so the upload date is approximate and full-description affiliate checks are partial.
- No full transcripts were available for any video, so nothing reached High confidence.
- I did not get comment-section sentiment because watch pages were blocked.

---

## Q4. Which communities are most active, and what do practitioners report (what works, what fails, monetization reality, abandoned tools)?

### Takeaway
The active hubs are creator-owned **Skool communities**, **Telegram/WhatsApp channels**, vendor **Discords** (Higgsfield, vidIQ), and **BlackHatWorld** threads. Reddit is surely active, but I could not access it (403).

Practitioner consensus in 2026:
- AI tooling itself is not what gets channels demonetized; templated, repetitive or reused output is.
- Shorts ad revenue is thin (cents per 1,000 views).
- Real income tends to come from long-form, products, affiliates or selling courses to other aspiring creators.

### Cited Findings

**Where the activity is**

| Community | Run by | Source |
|---|---|---|
| skool.com/faceless | Fabio Morena | [desc](https://www.youtube.com/watch?v=Bbjv9-00tv0) |
| skool.com/creatorprofits | Danny Why | [summary page](https://videohighlight.com/v/WODnqHPLR38) |
| skool.com/ai-launchpad | Zinho | [desc](https://www.youtube.com/watch?v=zXE_PpJ5WUc) |
| skool.com/mromi | Mr omi | [desc](https://www.youtube.com/watch?v=OtbLL6OBNE4) |
| skool.com/views-for-income-7713 | Romayroh | [desc](https://www.youtube.com/watch?v=zxFZE_-w54Y) |
| skool.com/monetize-society-8126 | Money Groot | [desc](https://www.youtube.com/watch?v=_e3wkQpPQnw) |
| skool.com/jack-vs-ai-workflows-8360 | Jack Vs. AI | [desc](https://www.youtube.com/watch?v=NnvRMs_0UQ8) |
| Kaz Skool | Grow With Kaz | [desc](https://www.youtube.com/watch?v=Ock60o-Glh4) |
| Telegram t.me/markaiguyHQ | Mark Ai Guy | [desc](https://www.youtube.com/watch?v=H8FAaKeCguA) |
| Jacksons AI Telegram | Jacksons AI | [desc](https://www.youtube.com/watch?v=zocKB90jZZg) |
| WhatsApp channels | E'Calm, Waseem Automation, Faisal Shabbir | [E'Calm](https://www.youtube.com/watch?v=Sp83h2FqOH0), [Waseem](https://www.youtube.com/watch?v=NP1aZVpNGTo), [Faisal](https://www.youtube.com/watch?v=FAW6AuzT1Uw) |
| Higgsfield Discord (discord.gg/higgsfield) | Higgsfield | [desc](https://www.youtube.com/watch?v=YP8D2_j3_Hc) |
| vidIQ Discord and Facebook group | vidIQ | [desc](https://www.youtube.com/watch?v=rStytOzzLwo) |

**BlackHatWorld threads (2026)**
- [AI YouTube channel monetization in 2026](https://www.blackhatworld.com/seo/ai-youtube-channel-monetization-in-2026.1805126/) and [AI shorts video will be monetized??](https://www.blackhatworld.com/seo/ai-shorts-video-will-be-monetized.1826372/). Both pages returned 403; the content below is from search-engine summaries.
- Posters say originality matters. Fully automated or repetitive AI content "will likely result in demonetization or reduced visibility". The problem "is usually generic content, not AI itself". One reply says the bigger money is in CPA affiliate offers.
- A journey thread for a faceless AI storytelling channel, started September 2025 [OLDER], reported 120 subscribers, 104 watch hours and **$0** by November 2025. Some prompts were rejected by AI image tools' copyright filters — [BHW](https://www.blackhatworld.com/seo/from-cpa-crash-to-ai-creation-my-journey-to-50-day-through-youtube-monetization.1769025/).

**What practitioners say works**
- Original story or format "borrowing", not copying — [Jack Craig summary](https://youtubesummary.com/summary/za2VyvLl5T0), [Higgsfield summary](https://youtubesummary.com/summary/wU_bmWb6bhg).
- Human-in-loop edits — [Jack Craig](https://youtubesummary.com/summary/za2VyvLl5T0); quality control of the script and voiceover — [Romayroh desc](https://www.youtube.com/watch?v=zxFZE_-w54Y).
- Consistent daily posting; hook in the first ~3 seconds — [E'Calm summary](https://youtubesummary.com/summary/srDpvEnGQg4).
- Freelancers rather than full automation — [Chris Barrera summary](https://videohighlight.com/v/HOEqRYPD7sE).
- A recurring visual identity, narrator POV and characters — [vidIQ desc](https://www.youtube.com/watch?v=ye2T2FwubI4).

**What fails**
- Templated thumbnails and titles, and static slideshows. Example: the "Boring History" channel reportedly made $170K in about 6 months, then was demonetized; Eizner says 12 of his channels were terminated — [videohighlight 8UW7TNr2S5A](https://videohighlight.com/v/8UW7TNr2S5A).
- Channels stuck in "view jail". E'Calm restarted 3 times before success — [youtubesummary srDpvEnGQg4](https://youtubesummary.com/summary/srDpvEnGQg4).
- Reddit-story spam, celebrity AI, fake trailers, MMO keywords — [youtubesummary RSnGnIWUvIQ](https://youtubesummary.com/summary/RSnGnIWUvIQ).

**Monetization reality**
- Shorts RPMs cited by creators:
  - $0.07–$0.20 per 1,000, US ~$0.33 — [Sanji summary](https://youtubesummary.com/summary/8Rf0xna31xg).
  - Kellan: 17M views → $3.8K. That works out to about $0.22 per 1,000, although the summary labels it "42 cents"; flagged as internally inconsistent — [videohighlight](https://videohighlight.com/v/V_t51u1tBJc).
  - Blogs: $0.01–$0.12 — [aishortgen](https://aishortgen.com/blog/youtube-shorts-monetization-ai-content), [video-to-prompt](https://video-to-prompt.com/blog/youtube-shorts-ai-monetization-real-revenue-2026) (vendor blogs).
- Tilbury's 10M-view experiment netted **$157.48** — [videohighlight](https://videohighlight.com/v/LlhTEttKcwQ).
- E'Calm's own framing: "YouTube automation is rarely the easy money machine people claim" — [desc](https://www.youtube.com/watch?v=Sp83h2FqOH0).

**Official YouTube Partner Program changes announced 2026, effective 2027-02-01** — [YouTube Help: Changes to YPP](https://support.google.com/youtube/answer/12843009?hl=en)
- New-creator entry rises to 1K subscribers plus 8,000 watch hours in 365 days, **or 20M Shorts views in 90 days** (up from 10M).
- Earning from the Shorts Creator Pool requires **10M qualified Shorts views per 90 days**, even for channels already in the program.
- New: 45% revenue share on Shorts ads targeted to five or fewer channels.
- Secondary coverage dates the announcement 2026-08-10 — [Newsshooter](https://www.newsshooter.com/2026/08/10/youtube-updates-its-partner-program/).
- Higgsfield's description pushes viewers to start "before YouTube's monetization bar doubles for new channels" — [desc](https://www.youtube.com/watch?v=YP8D2_j3_Hc).

**TikTok**
- Faceless AI on the Creator Rewards Program is contested. Some guides say AI videos qualify if labelled; others say "fully AI-generated content cannot qualify". Commonly cited thresholds are 10K followers and 100K views in 30 days, with videos over 1 minute — [Clippie](https://clippie.ai/blog/tiktok-creator-rewards-faceless-ai-videos), [virvid](https://virvid.ai/blog/tiktok-monetization-alternatives-2026-ai-content-ban) (third-party blogs, unverified).
- A Nigerian creator's video shows monetizing via a "UK account" — [Buzz, 2026-02-14, 293,018 views](https://www.youtube.com/watch?v=0eQDpN4lmNE). This implies geo-workaround practices.

**Abandoned or declining tools and formats**
- Creators abandoned Blender for three.js — [youtubesummary OtbLL6OBNE4](https://youtubesummary.com/summary/OtbLL6OBNE4).
- Video tutorials pivoting "NO CLAUDE CODE" for simpler free stacks — [Mark Ai Guy title](https://www.youtube.com/watch?v=-fgNFJCQZGk); "Stop Learning n8n in 2026" — [Nate Herk, ≈Apr, 529,900 views](https://www.youtube.com/watch?v=ZeJXI2MAhj0) (title only).
- 15.ai's 15.dev closed 2026-05-28 — [Wikipedia](https://en.wikipedia.org/wiki/15.ai).

### Inferences
- The community layer is heavily monetized by the same creators who publish the tutorials (Skool, Gumroad, coaching). Independent practitioner voice is mostly on Reddit and BHW, which I could not access directly. The "what fails" evidence leans on policy explainers.
- The n8n-style "automation" pipelines common in 2025 [OLDER] seem to be giving way to Claude skills/MCP in 2026 tutorials. This is inferred from title frequency, not measured usage.

### Gaps
- **No direct Reddit thread content.** r/NewTubers, r/youtubeautomation, r/PartneredYoutube and r/SideProject all returned 403 to curl and WebFetch, and search engines returned no Reddit URLs for 2026 queries.
- X/Twitter accounts were not researched (no access path tested).
- BHW thread content is known only from search summaries.
- No verified Instagram Reels monetization data for faceless AI accounts. The only data point is that Tilbury monetized via a digital product, not Reels payouts.

---

## Q5. Where do sources disagree?

### Takeaway
The main conflicts:
- "AI isn't the problem, templates are" (most creators) versus official policy text that explicitly names AI-template content and slideshows.
- "Fully automated channels make $30K/month" versus documented demonetizations, a $157 real-world result, and rising thresholds.
- "Ranking/compilation Shorts are the best niche" versus YouTube's and Instagram's reused/unoriginal-content rules.
- Wildly different Shorts RPM figures.

### Cited Findings
- **AI versus template.**
  - Creators: "AI scripts, AI voiceovers, AI images, and AI avatars are not demonetizing channels… The pattern is the content type, not the tool" — [Eizner desc](https://www.youtube.com/watch?v=8UW7TNr2S5A). "YouTube cares about value, not whether AI was used" — [Higgsfield summary](https://youtubesummary.com/summary/wU_bmWb6bhg).
  - YouTube's policy does permit "using AI to visualize a unique character and narrative you invented". It also lists as non-monetizable: "AI-generated content made with generic or unoriginal templates giving the impression of mass production"; "Image slideshows"; "characters… put in the same situation over and over again"; and channels relying on "emotionally manipulative themes, like… animals in exaggerated distress" — [YouTube policy](https://support.google.com/youtube/answer/1311392?hl=en).
  - The July 15, 2025 rename from "repetitious" to "inauthentic content" [OLDER, still in force] is on the same page.
  - Several creators describe a newer "unsatisfying or off-putting" category — [vidIQ desc](https://www.youtube.com/watch?v=JvZ0MXl70fc), [youtubesummary fern](https://youtubesummary.com/summary/-Gnrp_caPvo). It appears on the live policy page.
  - Third-party blogs date that clarification to July 13 or 16, 2026 — [outlierkit](https://outlierkit.com/blog/youtube-updates-july-2026). The exact date is unconfirmed.
- **"Fully automated" money versus reality.**
  - Claims: Nafay 3D says a Zapier autopilot posts "a new Short to your channel every single day" — [desc](https://www.youtube.com/watch?v=n1N_ZIP5x3M). Sanji says ranking Shorts bring "a monetized channel within a few weeks" — [desc](https://www.youtube.com/watch?v=iJiBJAJRRkk).
  - Counter-evidence:
    - Chris Barrera: full automation "leads to poor quality content", so hire freelancers — [summary](https://videohighlight.com/v/HOEqRYPD7sE).
    - Jack Craig: human edits are needed and AI output is "not perfect" — [summary](https://youtubesummary.com/summary/za2VyvLl5T0).
    - Tilbury's $157 net — [summary](https://videohighlight.com/v/LlhTEttKcwQ); Eizner's 12 terminated channels — [summary](https://videohighlight.com/v/8UW7TNr2S5A).
    - Higher 2027 YPP entry bar — [YouTube Help](https://support.google.com/youtube/answer/12843009?hl=en).
    - A blog reports that in January 2026 YouTube terminated 16 channels with 35M combined subscribers — [earnfacts](https://earnfacts.com/demonetization-2026-ai-rules/). This is unverified secondary reporting.
- **"Competition is down" versus "slop flood".**
  - Kellan and Sanji argue Google Trends interest in "YouTube automation" is near a 5-year low, so competition is low — [summary](https://youtubesummary.com/summary/8Rf0xna31xg).
  - Kapwing found 104 of the first 500 Shorts (21%) shown to a new account were AI-generated, and 33% were "brainrot" — [Kapwing](https://www.kapwing.com/blog/ai-slop-report-the-global-rise-of-low-quality-ai-videos/), [The Decoder](https://the-decoder.com/one-in-five-youtube-shorts-shown-to-new-users-is-ai-generated-slop-study-finds/). The report is likely November 2025 [OLDER]; its date is reported inconsistently.
  - fern's 11.5M-view investigation documents AI copycat networks — [summary](https://youtubesummary.com/summary/-Gnrp_caPvo).
- **Ranking/compilations versus reused content.**
  - Kellan and Sanji recommend compiling viral TikTok clips — [summary](https://videohighlight.com/v/V_t51u1tBJc).
  - YouTube's reused-content policy covers "clips, compilations" without significant original commentary — [YouTube policy](https://support.google.com/youtube/answer/1311392?hl=en).
  - Instagram no longer recommends accounts that mostly post unoriginal Reels, photos or carousels (from 2026-04-30) — [Tubefilter](https://tubefilter.com/2026/04/30/instagram-removes-algorithm-recommendations-repost-content-aggregator).
  - A blog claims that since October 1, 2026 YouTube cut Shorts reach for channels that mostly re-upload clips — [via outlierkit/vidpal search results](https://outlierkit.com/blog/youtube-updates-july-2026) (single-source, unverified).
- **RPM.** Figures range from $0.01–$0.05 per 1,000 (Mediacube, cited by blogs) to $0.33 US per 1,000 (Sanji) to "$50–$500 per million" — [aishortgen](https://aishortgen.com/blog/youtube-shorts-monetization-ai-content), [youtubesummary 8Rf0xna31xg](https://youtubesummary.com/summary/8Rf0xna31xg).
- **AI personas.** Tilbury's most promising persona was a health influencer — [summary](https://videohighlight.com/v/LlhTEttKcwQ). YouTube bars monetization of "AI personas… [giving] health… advice" — [YouTube policy](https://support.google.com/youtube/answer/1311392?hl=en). That was on Instagram rather than YouTube, but it shows the gap.
- **Free versus paid.**
  - "100% free" tutorials (zapiwala, Mark Ai Guy, Nafay 3D) rely on free tiers with rate limits: Grok ~10 a day, Turboscribe 3 a day — [summaries](https://youtubesummary.com/summary/srDpvEnGQg4).
  - Sponsored comparisons conclude the paid tool wins: Youri's free-generator comparison ends with Higgsfield and is sponsored by Higgsfield — [desc](https://www.youtube.com/watch?v=nmpHMBnZHWQ).

### Inferences
- The safest reading for a pipeline designer:
  - Treat AI as allowed, but vary format, visuals, thumbnails and titles.
  - Avoid static-image slideshows, same-outcome character loops, and re-uploaded clip compilations.
  - Never put an AI persona in health or finance advice.
  - Plan for Shorts ad revenue being small and harder to reach from February 2027.
- Revenue claims and vendor-sponsored "free vs paid" comparisons are systematically biased toward the paid tool.

### Gaps
- No official YouTube statement quantifies AI-channel demonetization rates in 2026; the figures are from blogs.
- The exact date of the July 2026 policy clarification and the October 2026 reach claim are unconfirmed.
- I could not confirm current TikTok Creator Rewards AI eligibility from an official TikTok source.
