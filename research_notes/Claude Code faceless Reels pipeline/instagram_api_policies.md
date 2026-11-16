# Instagram Reels publishing options and platform rules for a faceless AI-generated Reels account (as of Nov 2026)

Research date: 2026-11-16. Official Meta developer docs were fetched directly. The help.instagram.com and meta.com/help pages returned errors to both WebFetch and curl ("Sorry, something went wrong"), so Instagram Help Center claims below come from Meta newsroom/creator-blog posts or from secondary sources, and are marked as such. [OLDER] marks pre-2026 information; each one says whether it still appears current.

## 1. Programmatic publishing: Instagram API (Content Publishing) for Reels

### Takeaway
Reels can be published to your own Business or Creator account for free through Meta's official Content Publishing API. The flow is: create a container (`media_type=REELS`), poll its status, then call `media_publish`. To serve only your own account, you need Standard Access (app-role users), not Advanced Access. App Review and Business Verification are required only to serve accounts that don't hold a role on the app. The documented limit is 100 API-published posts per rolling 24 hours, but one section of the same page says 50, so check it per account. The 2025–2026 additions that matter most for an AI pipeline are `trial_params` (Trial Reels), `is_ai_generated` (self-disclosed AI label at publish time), up to 3 `collaborators`, and the read-only `media_audio_type` field.

### Cited Findings
**Three API setups (2026 docs)**
- Meta now documents three setups:
  - **Unified Login**, which Meta says is "recommended for new integrations." Users log in with Instagram or Facebook, no Facebook Page is required, and it uses graph.facebook.com with Business Integration System User tokens.
  - **Instagram Login** (Business Login for Instagram), for professional accounts without a linked Page. It uses graph.instagram.com.
  - **Facebook Login**, for IG accounts linked to a Page. It uses graph.facebook.com.
  - Source: [Meta Dev – Instagram Platform Overview](https://developers.facebook.com/docs/instagram-platform/overview)
- Account type: "An Instagram professional account can represent a business or creator." Both Business and Creator accounts work. Personal accounts are not supported. — [Overview](https://developers.facebook.com/docs/instagram-platform/overview); [Content Publishing](https://developers.facebook.com/docs/instagram-platform/content-publishing/)
- Instagram API with Instagram Login launched July 23, 2024. It uses graph.instagram.com and the new `instagram_business_*` permissions, and a Facebook Page is "no longer required." [OLDER, still current] — [Changelog](https://developers.facebook.com/documentation/instagram-platform/changelog)
- The Instagram Basic Display API was deprecated on Dec 4, 2024, and all its requests now return errors. It never supported publishing anyway. [OLDER, still current] — [Changelog](https://developers.facebook.com/documentation/instagram-platform/changelog)

**Permissions by setup**
- Instagram Login: `instagram_business_basic` + `instagram_business_content_publish` (Instagram User token, graph.instagram.com). — [Content Publishing](https://developers.facebook.com/docs/instagram-platform/content-publishing/)
- Facebook Login: `instagram_basic` + `instagram_content_publish` + `pages_read_engagement`. Add `ads_management`/`ads_read` if the user has a Business Manager role on the Page. Uses a Page access token. — [Content Publishing](https://developers.facebook.com/docs/instagram-platform/content-publishing/)
- Unified Login: `instagram_basic` + `instagram_content_publish`, using a Business Integration System User token. — [Content Publishing](https://developers.facebook.com/docs/instagram-platform/content-publishing/)
- Either "Advanced or Standard" access is listed as valid for publishing under every setup. — [Content Publishing](https://developers.facebook.com/docs/instagram-platform/content-publishing/)

**Access levels, App Review and Business Verification**
- Standard Access is the default. It "is meant for people with roles on the app, such as during development and testing," and Meta warns that some features may not work properly under it. — [Overview](https://developers.facebook.com/docs/instagram-platform/overview)
- Advanced Access "requires App Review and Business Verification." It is needed to serve accounts you don't own or manage, or users without a role on the app or claiming business portfolio. Business Verification is required "if your app will be used by app users who do not have a Role on the app itself." — [Overview](https://developers.facebook.com/docs/instagram-platform/overview)

**Tokens**
- The authorization code and the short-lived token are each valid for 1 hour. The long-lived token is valid for 60 days and can be refreshed before it expires. — [Overview](https://developers.facebook.com/docs/instagram-platform/overview)

**Container → publish flow**
1. `POST /<IG_ID>/media` creates a container. For Reels, pass `media_type=REELS` and `video_url`.
2. `POST /<IG_ID>/media_publish` with `creation_id` returns the media ID.
3. If no media ID comes back, check `GET /<CONTAINER_ID>?fields=status_code`. Meta recommends checking "once per minute, for no more than 5 minutes."
4. Media "must be hosted on a publicly accessible server at the time of the attempt."
5. A published reel returns `media_type=VIDEO`. Use `media_product_type` to identify it as a reel.
- Source: [Content Publishing](https://developers.facebook.com/docs/instagram-platform/content-publishing/)

**Resumable upload**
- `upload_type=resumable` sends the file to `https://rupload.facebook.com/ig-api-upload/<API_VERSION>/<CONTAINER_ID>`. A local file uses `offset`/`file_size` headers. A hosted file uses a `file_url` header.
- The publishing guide says resumable upload is "available only to apps using Facebook Login for Business." Instagram Login apps must use a public `video_url`.
- Source: [Content Publishing](https://developers.facebook.com/docs/instagram-platform/content-publishing/)

**Rate limits and expiry**
- The publishing limit is "100 API-published posts within a 24-hour moving period," enforced on `media_publish`, with a carousel counting as one post. The Carousel section of the same page says "50 published posts within a 24-hour period." Meta's page does not reconcile the two, so query `GET /<IG_ID>/content_publishing_limit` for your account. — [Content Publishing](https://developers.facebook.com/docs/instagram-platform/content-publishing/); third-party analysis noting the same contradiction: [Reel Uploader blog](https://reeluploader.com/blog/instagram-api-publishing-limits)
- Container limit: 400 containers per rolling 24 hours. Containers expire after 24 hours (status `EXPIRED`). — [IG User Media reference](https://developers.facebook.com/docs/instagram-platform/instagram-graph-api/reference/ig-user/media)

**Reels video specs (official)**
- Container: MOV or MP4, with no edit lists and the moov atom at the front.
- Video: HEVC or H.264, progressive scan, closed GOP, 4:2:0 chroma subsampling, 23–60 fps, max 1920 px wide, VBR up to 25 Mbps.
- Aspect ratio: 0.01:1 to 10:1 allowed. 9:16 is recommended.
- Audio: AAC, max 48 kHz, mono or stereo, 128 kbps.
- Duration and size: 3 s to 15 min, max 300 MB.
- Cover image: JPEG, max 8 MB, sRGB, 9:16 recommended.
- Source: [IG User Media reference](https://developers.facebook.com/docs/instagram-platform/instagram-graph-api/reference/ig-user/media)

**Reels parameters**
- `share_to_feed`: shows the reel in Feed and the Reels tab. Placement in the Reels tab is still not guaranteed.
- `cover_url`, `thumb_offset` (ms): set the cover or thumbnail frame.
- `audio_name`: names the reel's audio. It can be renamed only once.
- `collaborators`: up to 3 usernames.
- `trial_params`: Trial Reels, with `graduation_strategy` set to `MANUAL` or `SS_PERFORMANCE`.
- `is_ai_generated`: AI self-disclosure.
- `location_id`, `user_tags`.
- Limitations: music tagging only for original audio, and no reels inside carousels.
- Sources: [IG User Media reference](https://developers.facebook.com/docs/instagram-platform/instagram-graph-api/reference/ig-user/media); [Content Publishing](https://developers.facebook.com/docs/instagram-platform/content-publishing/)
- Trial Reels are shown only to non-followers. — [Content Publishing](https://developers.facebook.com/docs/instagram-platform/content-publishing/)

**2025–2026 changelog items (official)**
- **Dec 3, 2025:** Trial Reels via `trial_params`; collaboration invite endpoints; media deletion (requires `instagram_manage_contents`); new metrics `reels_skip_rate`, `reposts`, `crossposted_views`.
- **Feb 6, 2026:** `enable_fb_login` parameter added to Instagram OAuth.
- **Apr 22, 2026:** Collaborative Media API; paid-partnership label at publish time (`branded_content_sponsor_ids`, `is_paid_partnership`); `shares_count`/`saved_count`/`reposts_count`.
- **Jun 1, 2026:** Instagram Audio API launched (Facebook Login apps only); `media_audio_type` field added (`MUSIC` or `ORIGINAL_SOUND`).
- **Jun 22, 2026:** `is_ai_generated` added as a container parameter and as a media field.
- **Jul 30, 2026:** `media_url` omitted for copyrighted or flagged video.
- Source: [Changelog](https://developers.facebook.com/documentation/instagram-platform/changelog)
- **Date conflict:** a search-engine summary of the same changelog put Trial Reels at May 15, 2026. The fetched changelog lists `trial_params` under Dec 3, 2025, and May 15, 2026 is the oEmbed no-token change. The fetched changelog is treated as authoritative here. — [Changelog](https://developers.facebook.com/documentation/instagram-platform/changelog)
- A third-party guide (April 2026) states that the core publishing flow is unchanged in 2026. — [postproxy.dev guide](https://postproxy.dev/blog/instagram-reels-api-publishing-guide/)

### Inferences
- **Lowest-friction route for a single owned account:** create a Meta app and use Instagram Login (no Facebook Page needed). Give your own IG account a role on the app (e.g., Instagram tester), stay on Standard Access, and refresh the 60-day long-lived token on a schedule.
- **Video hosting:** because Instagram Login cannot use resumable upload, the pipeline must host each MP4 at a public URL during publish, e.g., S3/R2/GCS presigned URLs or a temporary public bucket. The Facebook Login setup with a linked Page allows direct binary upload through rupload.
- **What Claude Code can drive:** plain HTTPS calls (curl/python) to graph.instagram.com, covering upload, poll, publish, the limit check, and setting `is_ai_generated=true` and `trial_params`.
- **Volume:** 100 posts/day (or 50) is far beyond what a sensible Reels cadence needs, so rate limits are not a practical constraint.
- **Cost:** the API appears free. I found no fee in Meta's docs; see Gaps.

### Gaps
- I found no explicit Meta statement that the Content Publishing API is free of charge. No pricing appears anywhere in the docs, which implies it is free.
- The exact current steps for adding an "Instagram Tester" role and dev-mode behaviour for Instagram Login could not be fetched; the docs only say Standard Access is for app-role users.
- The 100 vs. 50 posts/24h discrepancy is unresolved in Meta's own docs.
- I did not determine whether `is_ai_generated` is available on both Instagram Login and Facebook Login. The reference lists it without restriction.

## 2. Free manual and scheduled alternatives, and which Claude Code can drive

### Takeaway
Native options (the Instagram app scheduler and Meta Business Suite/Planner) are free but are UI-only, so Claude Code cannot drive them except through brittle browser automation. Free third-party tiers are small: Buffer gives 3 channels with 10 queued posts each and includes an API key, and Metricool gives 20 posts/month with an MCP server. Postiz (AGPL, self-hosted) has a public API and an MCP server and uses the official Meta APIs, which makes it the most Claude-Code-friendly scheduler. The direct official API (section 1) is the simplest option of all.

### Cited Findings
**Native Instagram and Meta tools**
- **Instagram app scheduling:** posts and Reels can be scheduled up to 75 days ahead, with a reported daily cap of 25 scheduled posts. These figures come from secondary sources citing the Help Center; I could not verify them on Meta's site. — [Socialbu guide](https://socialbu.com/blog/schedule-instagram-reels-and-posts); [Mumbrella](https://mumbrella.com.au/instagram-introduces-in-app-scheduling-tool-for-reels-and-posts-764134)
- **Meta Business Suite/Planner:** it is free and schedules Reels from desktop. Sources disagree on the window: most say 75 days, while Postplanner and Sprout say 29 days. One guide says Business Suite can't add trending (licensed) audio and has no batch upload. — [Sprout Social](https://sproutsocial.com/insights/schedule-instagram-reels/); [Postplanner](https://www.postplanner.com/blog/how-to-schedule-and-publish-instagram-reels); [Planable](https://blog.planable.io/blog/schedule-instagram-reels/)
- **Edits app (Meta's free video editor):**
  - In June 2026 Meta previewed an AI assistant and a "coming soon" desktop version. — [The Next Web, Jun 11 2026](https://thenextweb.com/news/meta-edits-ai-assistant-desktop-capcut); [AlternativeTo](https://alternativeto.net/news/2026/6/meta-is-adding-an-ai-assistant-and-a-new-desktop-version-to-its-edits-video-editing-app/)
  - A third-party guide says Edits shipped "schedule-to-publish" and one-tap publishing, plus AI B-roll generation. This is unverified against Meta. — [inro.social](https://www.inro.social/blog/edits-new-meta-app)

**Third-party schedulers**
- **Buffer Free:**
  - Plan limits: "Connect up to 3 channels" and "10 scheduled posts per channel - refill anytime."
  - Includes 1 API key with 1,000 requests/channel/month (max 3,000), 150 per 15 min, and 600 per 24 h.
  - Automatic publishing is listed for IG Business/Creator accounts; Reels are not mentioned explicitly for Free.
  - Source: [Buffer pricing](https://buffer.com/pricing)
- **Metricool Free:** 1 brand, "Schedule up to 20 posts per month," 1 Instagram account, auto-publication, and the "Metricool MCP." The Metricool API (Zapier, Make) is only on the Advanced plan. — [Metricool pricing](https://metricool.com/pricing/)
- **Later:** most 2026 sources say there is no permanent free plan, only a 14-day trial. One outlier review claims a free plan. — [Buffer vs Later](https://buffer.com/resources/buffer-vs-later/); [Rework 2026 comparison](https://resources.rework.com/tools/social-media/later-vs-metricool-vs-buffer)
- **Postiz:**
  - Licensing and hosting: open source (AGPL-3.0) and self-hostable (Docker, Coolify, Railway, VPS) with Postgres and Redis. About 41.7k GitHub stars.
  - Automation surface: "Public API & webhooks" in both the cloud and self-hosted editions. It also lists "Agentic surfaces (MCP, CLI, Claude / ChatGPT / Codex ... connectors)," a NodeJS SDK and an n8n node.
  - Instagram is supported, but the README doesn't specify the login type.
  - Source: [Postiz GitHub](https://github.com/gitroomhq/postiz-app)
- **Mixpost:** not researched in depth (see Gaps).

### Inferences
- **Easiest for Claude Code:**
  - Call the official API directly (curl/python).
  - Or call Buffer's API on the free tier (3 channels, 10 queued posts).
  - Or self-host Postiz and use its API/MCP. This also enables cross-posting to YouTube and TikTok.
  - Metricool's free MCP is an option, but its 20 posts/month cap limits it.
- **Native schedulers:** Meta Business Suite and in-app scheduling are free, but only a person can operate them. Use them as a manual fallback or to add licensed trending audio, which API posts can't do anyway.

### Gaps
- I couldn't fetch the official Instagram Help Center page on scheduling, so the 75-day window and the 25/day cap are unverified.
- I did not verify the free-tier limits of Mixpost (open-source "Lite"), SocialBee, Publer, or Later.
- I did not confirm whether Buffer Free's automatic publishing includes Reels or only feed and image posts.

## 3. Risks of unofficial automation (instagrapi, browser bots)

### Takeaway
Instagram's terms bar automated access and data collection without permission. Unofficial libraries such as instagrapi use the private mobile API with username/password login. Vendor sources consistently describe action blocks and suspensions, though the evidence is anecdotal. Since the official API supports Reels, trial reels and AI labels, there is no functional reason to use unofficial tools for publishing.

### Cited Findings
- **Instagram's terms (quoted by a third party):** "You may not access or collect data from our Products using automated means (without our prior permission) or attempt to access data you do not have permission to access." The terms also cover "creating accounts or collecting information in an automated way without our express permission." These quotes come via secondary sources; I could not render instagram.com/legal/terms. — [ScrapeOps](https://scrapeops.io/websites/instagram/); [Later – Instagram bots](https://later.com/blog/instagram-bots/)
- **Meta's Automated Data Collection Terms:** reported effective Oct 7, 2024, prohibiting "web scrapers, bots, crawlers, and other automated mechanisms without Meta's express written permission." This is a third-party summary I did not verify on Meta's site. — [Storrito](https://storrito.com/resources/instagram-penalizes-aggressive-automation/)
- **How unofficial tools work and why they get caught:** they "log in with your username and password to mimic human taps," which makes them more detectable. Vendors report permanent suspensions, e.g., a 120K-follower account; these are anecdotes from competitors. — [bot.space](https://www.bot.space/blog/the-dangers-of-unofficial-instagram-dm-apis-why-theyll-get-you-banned); [Gain blog](https://blog.gainapp.com/why-automated-instagram-posting-tools-arent-worth-the-risk/)

### Inferences
- A faceless account with no human identity and no 2FA history is likely at higher risk of checkpoint or ban if it logs in from datacenter IPs via instagrapi. Use only the official API or Meta-approved partners.

### Gaps
- I found no Meta primary statement or data on instagrapi detection or ban rates. The current Instagram ToS text could not be fetched directly (the page is JS-rendered).

## 4. Unoriginal content, AI labels, and recommendation eligibility (2024–2026)

### Takeaway
Instagram's ranking penalty targets unoriginal content: reposts or aggregation without meaningful transformation. On April 30, 2026 it was extended from Reels to photos and carousels, so aggregator accounts are no longer recommendable. AI-generated content is not itself demoted. Meta requires a disclosure label for photorealistic AI video or realistic AI audio and may penalize failure to disclose. New on Aug 31, 2026: profiles that feature an AI-generated person must add an "AI-generated profile" label, or their reach is limited. Creators who only use AI tools don't need it.

### Cited Findings
**Originality rules**
- **Apr 30, 2026:** Instagram said accounts that regularly repost content they didn't create, or mainly share others' photos and carousels, are no longer eligible for recommendations, including Feed and Discover. Followers still see their posts. Protections that "already applied to Reels" now extend to photos and carousels. — [TechCrunch, Apr 30 2026](https://techcrunch.com/2026/04/30/instagram-restricts-reach-of-content-aggregators-in-new-crackdown/); [Tubefilter, Apr 30 2026](https://www.tubefilter.com/2026/04/30/instagram-removes-algorithm-recommendations-repost-content-aggregator/)
- **What counts as original:**
  - Original: content you fully created or that reflects your perspective, or third-party content you "materially edit." Memes and clips with added humor, commentary, unique text, creative edits or voiceover qualify.
  - Not original: adding a watermark, changing speed, or screenshotting another post even with credit.
  - No numeric threshold was disclosed.
  - Sources: [TechCrunch](https://techcrunch.com/2026/04/30/instagram-restricts-reach-of-content-aggregators-in-new-crackdown/); [Tubefilter](https://www.tubefilter.com/2026/04/30/instagram-removes-algorithm-recommendations-repost-content-aggregator/)
- A blog claims "10+ unoriginal posts in 30 days" makes an account non-recommendable. This is unverified; Gyre itself says it couldn't confirm it against an Instagram source. — [Gyre](https://gyre.pro/blog/instagram-algorithm-updates-and-tips-to-boost-your-visibility)
- **[OLDER, Jul 14 2025, Facebook]:** Meta's crackdown on unoriginal content on Facebook.
  - Repeat reusers lose monetization "for a period of time" and get "reduced distribution on everything they share."
  - Duplicate copies are demoted.
  - "Simply stitching together clips or adding your watermark does not qualify as meaningful enhancement."
  - Meta advises avoiding visible third-party watermarks.
  - Still current. It is relevant if Reels are cross-posted to Facebook.
  - Source: [Facebook Creators blog](https://creators.facebook.com/blog/combating-unoriginal-content)

**AI labels**
- **[OLDER, Feb 2024]:** Meta detects "AI generated" information in the C2PA and IPTC standards and applies invisible watermarks plus IPTC metadata to Meta AI images. It will "require people to use this disclosure and label tool when they post organic content with a photorealistic video or realistic-sounding audio that was digitally created or altered" and "may apply penalties if they fail to do so." Still current per the Meta Help Center summary below. — [Meta Newsroom, Feb 2024](https://about.fb.com/news/2024/02/labeling-ai-generated-images-on-facebook-instagram-and-threads/)
- **[OLDER, 2024 updates]:**
  - Jul 1, 2024: "Made with AI" was renamed "AI info."
  - Sep 12, 2024: content only edited with AI has its label moved to the post menu, while detected AI-generated content keeps a visible label and indicates whether it came from industry signals or self-disclosure.
  - Since July 2024, Meta labels rather than removes content under the manipulated-media policy unless it violates other rules.
  - Source: [Meta Newsroom, Apr 2024 (updated)](https://about.fb.com/news/2024/04/metas-approach-to-labeling-ai-generated-content-and-manipulated-media/)
- **Meta Help Center (2026, via search snippet):** Meta may require an AI label for "photorealistic video or realistic-sounding audio that was digitally created, modified or altered," but "this requirement does not apply to images," and there "may be penalties" for unlabeled content. I could not render the page directly. — [Meta Help: How to identify AI content](https://www.meta.com/help/artificial-intelligence/1783222608822690/); [Instagram Help](https://help.instagram.com/761121959519495)
- **API disclosure (Jun 22, 2026):** `is_ai_generated` can now be set at publish time through the API, which "supports self-disclosure of AI-generated content at publish time." — [Changelog](https://developers.facebook.com/documentation/instagram-platform/changelog); [IG User Media reference](https://developers.facebook.com/docs/instagram-platform/instagram-graph-api/reference/ig-user/media)

**AI profile label**
- **May 2026:** Instagram tested an opt-in "AI creator" profile label. Instagram said ranking, distribution and recommendations were unchanged by it. — [SocialDay, Jul 31 2026](https://socialday.live/features/instagrams-mosseri-tells-users-if-you-dont-like-ai-content-dont-use-the-feed)
- **Aug 31, 2026 (official):**
  - Instagram renamed the label to "AI-generated profile," for profiles that feature an AI-generated person rather than a human.
  - Instagram will "limit the reach of profiles that feature an AI-generated person and do not add this label." It will notify detected profiles, which can add the label or appeal via Account Status.
  - "Creators who simply use AI tools as part of their creative process don't need to add the label."
  - Proactive labelers see no change in reach.
  - The profile label appears alongside content only if the media doesn't already carry an AI label.
  - Source: [Instagram Creators blog, Aug 31 2026](https://creators.instagram.com/blog/ai-generated-profile-label)

**Mosseri statements (secondary reports)**
- "I don't think we should filter out AI content." Instagram "should let you know if content is AI content or not." Users who want it could have a feed that's "just AI town." These come from a July 2026 podcast. His year-end 2025 post said "authenticity is becoming infinitely reproducible" and suggested shifting toward "fingerprinting real media." — [SocialDay](https://socialday.live/features/instagrams-mosseri-tells-users-if-you-dont-like-ai-content-dont-use-the-feed); [Engadget](https://www.engadget.com/social-media/instagram-chief-ai-is-so-ubiquitous-it-will-be-more-practical-to-fingerprint-real-media-than-fake-media-202620080.html)

### Inferences
- **Originality:** a faceless pipeline that generates its own AI visuals, script and voiceover is "original" under Instagram's definitions. Risk comes from reusing third-party clips, stock footage with watermarks, or near-identical templated outputs (duplicate detection).
- **Labeling:**
  - Set `is_ai_generated=true` whenever the Reel contains photorealistic AI video or realistic AI voice/audio. AI generators that embed C2PA metadata will likely trigger an automatic label anyway.
  - If the account fronts a synthetic AI person or avatar as its "host," add the AI-generated profile label to avoid reach limits.
  - A purely faceless account (no AI human persona) appears not to need the profile label.

### Gaps
- Instagram's official April 30, 2026 blog post URL was not found, so the originality rules are cited via TechCrunch and Tubefilter.
- I found no official statement that AI-labeled posts are or aren't down-ranked. Meta says the profile label itself doesn't affect ranking, but I found nothing comparable for post-level "AI info."
- The current recommendation guidelines page (help.instagram.com/313829416281232) failed to load.

## 5. Monetization on Instagram in 2026 (incl. India)

### Takeaway
Instagram has no broadly available per-view Reels revenue share. Bonuses are invite-only, and their 2026 status is reported inconsistently. Gifts (500+ followers) and Subscriptions (10k+ followers) are reported as available in India. For most creators, especially in India, the realistic income is brand deals, affiliate and Creator Marketplace. Official confirmation of 2026 thresholds and of India availability could not be fetched.

### Cited Findings
- **Gifts:** reported to need 500 followers, a professional account and age 18+, at about US$0.01 per Star. India is reported on the Gifts and Subscriptions country lists (49 countries per some sources; "40+" per others). — [Influencer Marketing Hub](https://influencermarketinghub.com/instagram-subscriptions-gifts/); [Lilach Bullock](https://www.lilachbullock.com/instagram-monetization-tools/); [Hypee (India)](https://www.hypee.co.in/blog/instagram-monetization-rules-india)
- **Subscriptions:** 10,000 followers, a professional account and age 18+; India is listed. — [Hypee](https://www.hypee.co.in/blog/instagram-monetization-rules-india); [Finology Insider](https://insider.finology.in/business/instagram-subscriptions)
- **Bonuses:** invite-only. Sources disagree on India; one says bonuses are limited to the US, Japan and South Korea, and another says India has not been publicly listed. — [Influencermetric.in](https://influencermetric.in/blog/how-to-monetize-instagram-reels-india); [Lilach Bullock](https://www.lilachbullock.com/does-instagram-pay-creators-for-reels/)
- **Unverified 2026 bonus claims:** one blog says that from June 15, 2026 Meta paused Reels bonuses for Facebook Reels creators and US Instagram creators, with an invite-only replacement. Other blogs claim an August 2026 bonus expansion to photos and carousels and an October 2026 "Reels Royalties" launch. None cite a Meta source. — [Meta Music Media](https://metamusicmedia.com/blogs/news/meta-ends-reels-bonuses-us-creators-2026); [Creator Newsdesk](https://www.creatornewsdesk.com/platforms/instagram-reels-monetization-in-2026-ads-revenue-gifts-and-subscriptions-replace-play-bonuses/)
- **No per-view pay in India:** Instagram doesn't pay per view there and does not share Reels ad revenue with Indian creators. — [Influencermetric.in](https://influencermetric.in/blog/how-to-monetize-instagram-reels-india)
- **Creator Marketplace:** brand discovery reportedly needs about 1,000 followers, and India is reported as eligible. Meta's Creator Marketplace API limits rose in March 2026, which suggests the product is active. — [Kudozz](https://www.kudozz.in/blog/instagram-creator-monetization); [Changelog](https://developers.facebook.com/documentation/instagram-platform/changelog)
- **Paid partnership disclosure:** the "Paid partnership" label can be set at publish time via the API (Apr 22, 2026), which helps disclose brand deals in automated posts. — [Changelog](https://developers.facebook.com/documentation/instagram-platform/changelog)
- **[OLDER, Facebook, Jul 2025]:** unoriginal (reused) content loses Facebook monetization access; original remixes, commentary and voice-over remain eligible. — [Facebook Creators blog](https://creators.facebook.com/blog/combating-unoriginal-content); [Search Engine Journal](https://www.searchenginejournal.com/meta-follows-youtube-in-crackdown-on-unoriginal-content/551096/)

### Inferences
- **Eligibility:** I found no Meta rule excluding AI-generated or faceless accounts from Gifts or Subscriptions. Eligibility rests on follower counts, age, country and policy compliance (originality, recommendation eligibility, labeling). An unlabeled AI-person profile with limited reach would indirectly hurt earnings.
- **Planning:** for an India-based faceless account, plan revenue around affiliate links, brand deals and off-platform funnels, not platform payouts.

### Gaps
- The official Instagram Help Center pages for Gifts, Subscriptions and Bonuses (eligibility and country lists) could not be fetched. All thresholds are from secondary sources and should be re-verified in the Professional Dashboard.
- I found no official Meta source on AI-content eligibility for Instagram monetization specifically.

## 6. Music copyright on Instagram

### Takeaway
Instagram's licensed music library is for personal, non-commercial use. Business accounts are reported to be restricted to the royalty-free Meta Sound Collection. API-published Reels cannot tag licensed music: music tagging works only for original audio. The safest path for an automated faceless account is original or properly licensed royalty-free audio, or AI music it owns rights to, baked into the MP4. Since mid-2026, Meta's API flags whether a reel uses licensed music or original sound and withholds media URLs for copyrighted or flagged video.

### Cited Findings
- **Licensed library vs. Sound Collection:**
  - Business accounts reportedly lose the main licensed catalog and get the Meta Sound Collection.
  - Instagram Help reportedly says the Sound Collection has "over 14,000 songs and sounds which are entirely royalty free," usable in Reels and Stories and commercially (e.g., ads).
  - Licensed music may be unavailable in some regions.
  - Sources: secondary summaries of Instagram Help — [Instagram Help (iPad)](https://help.instagram.com/ipad-app/402084904469945); [Fox Music](https://www.foximusic.com/blog/instagram-reels-music-copyright-legal-guide/); [Soundstripe](https://www.soundstripe.com/blogs/instagram-music-library)
- **Sound Collection license scope:** tracks are reportedly cleared only for Facebook and Instagram, so the license doesn't travel to TikTok or YouTube when cross-posting. — [Fox Music](https://www.foximusic.com/blog/instagram-reels-music-copyright-legal-guide/)
- **API music limits:** "Music tagging is only available for original audio." `audio_name` sets the name of original audio once. — [IG User Media reference](https://developers.facebook.com/docs/instagram-platform/instagram-graph-api/reference/ig-user/media)
- **Instagram Audio API (Jun 1, 2026):** launched for Facebook Login apps, with audio search and a Reels-ads replacement-audio use case. The new `media_audio_type` field returns `MUSIC` or `ORIGINAL_SOUND`. — [Changelog](https://developers.facebook.com/documentation/instagram-platform/changelog)
- **Jul 30, 2026:** `media_url` is omitted for "copyrighted or flagged video." — [Changelog](https://developers.facebook.com/documentation/instagram-platform/changelog)
- **Business Suite and licensed audio:** Meta Business Suite reportedly can't add trending (licensed) audio when scheduling Reels. — [Planable](https://blog.planable.io/blog/schedule-instagram-reels/)

### Inferences
- **Audio choice:** embed royalty-free audio or audio you hold a license to, or AI-generated music from a service whose terms grant commercial rights, directly in the video. Copyrighted commercial tracks risk Rights Manager matches, which can mute audio or block the reel. The exact consequences could not be confirmed from an official page.
- **Trending sounds:** to use trending licensed sounds, a human must add them in-app (Creator account), which breaks full automation.

### Gaps
- I could not fetch the official Instagram Help pages on muted audio, blocked reels and business-account music restrictions.
- I found no Meta policy specific to AI-generated music.
- I did not verify the Instagram Audio API's scope (whether it allows attaching licensed tracks to organic Reels).

## 7. Cross-posting comparison: YouTube Shorts and TikTok AI and inauthentic-content policies

### Takeaway
YouTube is the strictest on monetizing mass-produced AI content. In July 2025 it renamed "repetitious content" to "inauthentic content," and on July 16, 2026 it spelled out three non-monetizable categories, including generic, template-based AI content. TikTok requires labeling of realistic AIGC, auto-labels via C2PA, and applies invisible watermarks. Meta penalizes unoriginality and missing disclosure rather than AI use itself.

### Cited Findings
- **YouTube, Jul 15, 2025 [OLDER, still current and expanded]:** the YPP "repetitious content" policy was renamed "inauthentic content" to cover mass-produced or repetitive videos. Rene Ritchie called it a "minor update." — [TechRepublic](https://techrepublic.com/article/news-youtube-ai-video-monetization-rules); [PPC Land](https://ppc.land/youtube-clarifies-inauthentic-content-policy-changes/)
- **YouTube, Jul 16, 2026 clarification (reported Jul 20):** three categories of inauthentic content cannot be monetized:
  1. "Generic, repetitive, or template-based" content made easily with AI, CGI or templates with little variation.
  2. Off-putting or distressing content designed to manipulate.
  3. AI representations of real people discussing finance, legal or health topics.
  - Channels with too much such content can't monetize. Trust and safety chief Matt Halprin: "AI can actually allow people to make a lot of videos... We've heard from our viewers that that's not something that they like."
  - Sources: [TechCrunch, Jul 20 2026](https://techcrunch.com/2026/07/20/youtube-clarifies-policies-around-ai-slop-and-upsetting-videos/); [Creator Insider video](https://www.youtube.com/watch?v=14Vm0CiyUVE); [Android Headlines](https://www.androidheadlines.com/2026/07/youtube-monetization-rules-ai-slop-inauthentic-content.html)
- **TikTok labeling:**
  - Creators must label realistic AIGC.
  - TikTok was the first video platform to adopt C2PA Content Credentials (May 2024) and auto-labels uploads that carry them.
  - It applies invisible watermarks to content made with its own tools and to C2PA-tagged uploads (March 2026 newsroom).
  - Users can control how much AIGC they see (Nov 2025).
  - Sources: [TikTok Newsroom, Nov 2025](https://newsroom.tiktok.com/more-ways-to-spot-shape-and-understand-ai-content?lang=en); [TikTok Newsroom, Mar 10 2026](https://newsroom.tiktok.com/tiktok-ssa-shares-more-ways-to-spot-shape-and-understand-ai-generated-content?lang=en-ZA); [Tubefilter, Jul 14 2026](https://www.tubefilter.com/2026/07/14/tiktok-ai-transparency-tools-content-labels/)
- **TikTok scale and ads:** sources conflict on labeled-content counts (1.3B vs. 3B+). A secondary source reports a Jul 21, 2026 ads rule requiring disclosure on all AI-generated ad content, which I did not verify. — [Cinerads](https://www.cinerads.com/blog/tiktok-ai-content-policy); [Commonthread](https://commonthreadco.com/blogs/coachs-corner/tiktok-ai-ad-disclosure-rules-ecommerce-2026)

### Inferences
- **Cross-posting the same AI Reel:**
  - Keep C2PA metadata intact. Labels propagate on Meta and TikTok, which is compliant and avoids non-disclosure penalties.
  - Ensure real variation between videos to avoid YouTube's "template-based" demonetization.
  - Avoid AI personas giving finance, health or legal advice.
  - Avoid platform-bound music licenses (e.g., Meta Sound Collection) in the master file.

### Gaps
- I did not fetch YouTube's official YPP policy page or TikTok's Community Guidelines on "unoriginal content," so TikTok's treatment of low-effort AI content for the Creator Rewards Program was not determined.
