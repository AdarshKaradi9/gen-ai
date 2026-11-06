# Technical feasibility: Screen-Time Companion (solo founder)

## Key takeaways for the build

- **iOS is buildable by one person, but the Screen Time API is the main source of risk.** The blocking pieces (pick apps, shield them on a schedule, custom shield text) are well understood and wrapped for React Native by `react-native-device-activity` (v0.6.1, last published 19 Feb 2026, verified on npm). Expect weeks of overnight testing on real devices. The iOS Simulator cannot run the monitor extension (developer report, Sept 2026).
- **File the Family Controls (Distribution) entitlement requests on day one.** You need four of them, one per bundle ID: the app, the ActivityMonitor extension, the ShieldConfiguration extension and the ShieldAction extension. Developers report waits from one day to about two months (anecdotal forum reports, 2026). Without approval you cannot ship to TestFlight.
- **Your app cannot read per-app usage numbers.** App picks come back as opaque tokens. The DeviceActivityReport extension can draw usage charts, but Apple sandboxes it on purpose: it cannot write data out or make network calls (Apple DTS on the forums). For character health and the "hours reclaimed" counter, meter usage with threshold events (for example "15 more minutes used"), which the monitor extension can record. Show exact daily totals only inside a report view. The onboarding "years of your life" number has to come from a figure the user types in, which is what Opal and Brainrot do.
- **The shield cannot open your app.** Apple DTS has confirmed there is no supported API for this. The working pattern: the shield extension posts a local notification, the user taps it, and the "unlock" screen runs inside your app. That is useful for the product, because every sanctioned unlock passes through your code and can trigger the "Sam unlocked TikTok at 1:14am" message to friends.
- **The accountability wedge now has native support on iOS.** Since iOS 26.4, a Screen Time passcode lock covers third-party apps that use individual authorization. With the lock on, the user cannot revoke the permission or delete the app (one sec's blog, March 2026, vendor claim). Onboarding can ask a friend to set that passcode. For bypasses outside the app (permission revoked, app deleted, device without the lock), use a server heartbeat: if the device goes quiet, tell the friends.
- **Android is a second, separate project.** There is no blocking API comparable to Apple's. Either use an AccessibilityService (fastest detection, which ScreenZen and one sec use) under stricter Google Play review since 28 Jan 2026, or poll UsageStatsManager and draw an overlay from a foreground service (`specialUse` type). Launch iOS-only.
- **Recommended stack:** Expo with a custom dev client, `react-native-device-activity`, hand-written Swift for the shield and report extensions, Supabase or Firebase for friends, heartbeat and push, and RevenueCat for the paywall. Rough estimate: 8 to 12 weeks for an iOS MVP built by one experienced React Native developer (my estimate, not sourced).

## 1. iOS: what Apple's Screen Time frameworks do

"The Screen Time API" is four frameworks and, in practice, three app extensions. **FamilyControls** handles authorization through `AuthorizationCenter`, which takes `.individual` for a self-control app or `.child` for parental control. It also provides the `FamilyActivityPicker`. **ManagedSettings** applies shields to the chosen apps, categories and web domains. **DeviceActivity** handles schedules and usage-threshold events. Their callbacks (`intervalDidStart`, `intervalDidEnd`, `eventDidReachThreshold`) go to a DeviceActivityMonitor extension, not to the app. **ManagedSettingsUI** styles the shield through a ShieldConfiguration extension and handles its buttons through a ShieldAction extension. These extensions are the core of the product, because the app is usually suspended or killed when a block needs to start. The app and its extensions share only an App Group container (dev.to, "The iOS Screen Time API in 2026").

**Authorization.** Apple's documentation says individual authorization needs approval from the device owner through a biometric prompt. Child authorization needs a parent in the same Family Sharing group, and an app authorized for a child cannot be deleted. An app with individual authorization could always be deleted, and revoking it in Settings removed its blocks (Apple forums thread 708000). That changed in iOS 26.4: per one sec's founder, whose company "worked closely with Apple" on it, "Lock Screen Time Settings" with a passcode now applies to one sec, and with it locked the user cannot turn off the permission or uninstall the app (vendor blog, March 2026). I could not find Apple's own release note confirming that this applies to every individually authorized app. Test it on a device before building onboarding around it.

**Entitlement.** Development builds work with the development capability. Distribution needs Family Controls (Distribution), requested through Apple's form per bundle ID; the library README warns that until all four are approved "you can't even build an Expo Dev Client." 2026 forum threads report main apps approved in a day while extensions sat in "Submitted" for weeks, a form change removing the bundle ID field, and profiles lagging approvals (forums 824969, 824665, 821163, 815031; anecdotal).

**What you can know about usage.** The picker returns only opaque `ApplicationToken`, `ActivityCategoryToken` and `WebDomainToken` values; your app can count them but never name them. The shield extension is the exception and receives the app's `localizedDisplayName` (dev.to). `DeviceActivityReport` renders usage in a sandboxed SwiftUI extension; Apple DTS says the sandbox is intentional, and App Group writes, Core Data writes and HTTP calls from it fail silently (forums 818174, 736351). So: a character drawn inside the report view can reflect real usage but that value cannot reach widgets, the server or friends; for anything shared, register threshold events (say every 5 or 15 minutes of use) that the monitor extension records, giving coarse minutes; and the onboarding "years of your life" figure must come from the user typing in their Screen Time average.

**Custom shield screens.** A `ShieldConfiguration` (Apple docs, verified) takes only a background blur style and colour, an icon, a title, a subtitle, a primary button label and colour, a secondary button label, and, in the newest SDK, submenu items for the secondary button. It cannot show a custom SwiftUI view or an animation. A character "wilting" on the shield therefore has to be a set of pre-rendered static icons, one per health state, read from the App Group. The ShieldAction delegate can respond only with `.none`, `.close` or `.defer`. It cannot open the parent app (Apple DTS, forum 719905). The `NSExtensionContext.open` workaround failed on iOS 26 in device testing (dev.to), and one sec's developer has asked Apple for an `openParentApp` response (forum 820790). For now, both one sec and the dev.to author post a local notification when the shield appears, and tapping it opens the app.

**Detecting a bypass.** Sanctioned unlocks (notification tap, "5 more minutes" in-app) and schedule edits run through your code, so they are fully visible and can push to friends. Revoking access in Settings gives no live signal: `authorizationStatus` does not emit and does not update until the app restarts (forum 820796; library README). Deleting the app gives none either. Cover both with a heartbeat: a daily repeating schedule whose `intervalDidStart` calls your server, plus app-open pings, so the server can tell friends "Sam's blocker has been quiet for 24h." This is my inference and needs testing, since whether monitors keep firing after revocation is undocumented. The stronger fix is the iOS 26.4 passcode lock with a friend holding the code.

**Known breakages (2025-2026).** Forum and developer reports, all anecdotal: on iOS 26.2 and 26.3, `eventDidReachThreshold` fires with zero usage, often when a locked phone is picked up (forums 812472, 809410; reportedly fixed in a 26.5 beta, still reported after). On 26.3.1, `intervalDidStart` and `intervalDidEnd` sometimes never fire (forums 819224, 820956). Later sub-minute thresholds get dropped; `stopMonitoring` triggers `intervalDidEnd`, which can briefly re-shield everything; a non-repeating schedule starting "now" silently moves to tomorrow; intervals under 15 minutes are rejected; and the picker "is prone to crashes" (library README). Each has a known guard (wall-clock and burst filters, not-before timestamps, backdated starts, re-arming monitors; dev.to). Budget for them. The dossier's Unstar analysis puts "permissions reset after iOS updates" at 16% of competitor complaints, so every rival pays this cost too.

**How competitors implement it.** one sec uses Shortcuts automations ("when Instagram is opened") for its pause screen, Screen Time shields for hard blocks, and a "Shortcuts App Lock" against disabling automations (one sec tutorials and blog). I found no technical write-up from Opal; its features map directly onto ManagedSettings and DeviceActivity.

## 2. React Native / Expo or Swift?

React Native with Expo is viable for the app; the extensions must be Swift you edit. `react-native-device-activity` (MIT, Kingstinct) gives an Expo config plugin, the picker as components, schedules and threshold events, `updateShield`, shield actions, web filtering, and an "actions" system that lets the monitor extension block, unblock, notify or call a URL from rules written to the App Group in advance. It needs a custom dev client (no Expo Go), allows at most 20 simultaneous monitors, and does not cover DeviceActivityReport, which you write in SwiftUI. Reported gotchas (dev.to, Expo SDK 57): set `copyToTargetFolder: false` or `expo prebuild` overwrites your custom extensions; avoid underscores in event names; declare each extension under EAS `appExtensions`; build with the iOS 26 SDK (ITMS-90725). Going fully native is possible but slower for the character, social and paywall UI, and loses code sharing with Android.

## 3. Android

Android has no sanctioned blocking API. Two approaches:
- **Usage access plus overlay.** A foreground service (type `specialUse`) polls UsageStatsManager about once a second and draws a `TYPE_APPLICATION_OVERLAY` lock screen, with a boot receiver and watchdog against OEM battery killers. The blocked app is visible for up to one poll and keeps running underneath (dev.to, HonorFit).
- **AccessibilityService.** ScreenZen asks for usage access, overlay, accessibility and battery exemption (third-party reviews). one sec defaults to accessibility because it "runs more stable... much faster response", keeping usage access as fallback (one sec help centre).

Policy: a blocker cannot declare `isAccessibilityTool`, so it needs an in-app prominent disclosure with affirmative consent and the Play Console declaration. The update effective 28 Jan 2026 bans using the API to "autonomously initiate, plan, and execute actions" (Google Play help; MyAppMonitor). Showing a block screen is not that, but review is case by case. Android 17's Advanced Protection Mode revokes accessibility from non-accessibility apps while on (The Hacker News, March 2026). Recommendation: default to usage access plus overlay, offer accessibility as optional "faster blocking".

## 4. App Store review risks

- **2.5.1 (unapproved API use):** rejections for using `blockedApplications` to hide apps (forum 776058) and automated flags when a binary's entitlements did not match, as recently as August 2026 (forums 822078, 838802; anecdotal). Use shields, not hiding, and check all four targets.
- **3.1.2 (subscriptions):** at least one Screen Time app rejected under 3.1.2(c) for its paywall (forum report). Honest billing should mean strict disclosure anyway.
- **Data use:** one consultant notes approvals are held to "parental or institutional control, never covert monitoring." Share with friends only what the user opts into.
- **Precedent:** Apple pulled MDM-based screen-time apps in 2018-2019 (TechCrunch). Family Controls avoids that path.

## 5. Recommended stack and hardest parts

**Stack:** Expo SDK 5x with EAS Build and a custom dev client; `react-native-device-activity` with `copyToTargetFolder: false`; custom Swift for the ShieldConfiguration extension (health-state icons and the notification on display), the ShieldAction extension and the DeviceActivityMonitor extension (threshold metering, re-shield, heartbeat); a SwiftUI DeviceActivityReport extension for the in-app daily chart; WidgetKit (through an Expo targets plugin) reading App Group state; Supabase or Firebase for accounts, friend groups, the heartbeat and push fan-out; RevenueCat for the trial reminder and paywall. Android follows later, as a Kotlin module sharing the React Native UI.

**Hardest parts, ranked (my estimates):**
1. Reliable shields and metering across iOS 26.x, guarding against phantom and dropped events. Two to four weeks, mostly testing overnight on devices.
2. The entitlement and provisioning process. Little engineering, but up to two months of calendar risk.
3. Bypass detection: the notification-based unlock flow, the heartbeat, and onboarding for the friend-held iOS 26.4 passcode. About two weeks.
4. Character health from coarse threshold data, kept consistent between the app, widget and shield. About one to two weeks.
5. Android blocking on OEM devices that kill background services. Four to six weeks, deferred until after launch.

## Sources
- https://dev.to/twillywill/the-ios-screen-time-api-in-2026-what-apples-docs-dont-tell-you-151e
- https://github.com/kingstinct/react-native-device-activity
- https://registry.npmjs.org/react-native-device-activity
- https://developer.apple.com/documentation/familycontrols
- https://developer.apple.com/documentation/managedsettingsui/shieldconfiguration
- https://developer.apple.com/forums/thread/708000
- https://developer.apple.com/forums/thread/719905
- https://developer.apple.com/forums/thread/783532
- https://developer.apple.com/forums/thread/820790
- https://developer.apple.com/forums/thread/820796
- https://developer.apple.com/forums/thread/818174
- https://developer.apple.com/forums/thread/736351
- https://developer.apple.com/forums/thread/812472
- https://developer.apple.com/forums/thread/819224
- https://developer.apple.com/forums/thread/820956
- https://developer.apple.com/forums/thread/824969
- https://developer.apple.com/forums/thread/824665
- https://developer.apple.com/forums/thread/821163
- https://developer.apple.com/forums/thread/815031
- https://developer.apple.com/forums/thread/776058
- https://developer.apple.com/forums/thread/822078
- https://developer.apple.com/forums/thread/838802
- https://one-sec.app/blog/lock-screen-time-permission/
- https://tutorials.one-sec.app/en/articles/10336706
- https://tutorials.one-sec.app/en/articles/3148866
- https://support.google.com/googleplay/android-developer/answer/10964491
- https://myappmonitor.com/blog/google-play-accessibility-services-policy-update
- https://thehackernews.com/2026/03/android-17-blocks-non-accessibility.html
- https://nibble-app.com/blog/screenzen
- https://habitdoom.com/blog/is-screenzen-safe
- https://drobinin.com/consulting/screen-time-family-controls/building-with-screen-time-and-family-controls/
- https://techcrunch.com/2018/12/05/apple-puts-third-party-screen-time-apps-on-notice/
