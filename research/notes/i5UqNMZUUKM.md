# In-app Subscriptions & Paywalls with RevenueCat in React Native
- URL: https://www.youtube.com/watch?v=i5UqNMZUUKM | Channel: notJust.dev | Views: 43328 | Length: 8873s (2h28m)
- Sources used: https://videohighlight.com/v/i5UqNMZUUKM (full description, learning objectives and timecodes); https://www.revenuecat.com/blog/engineering/expo-in-app-purchase-tutorial/ (RevenueCat's written Expo + react-native-purchases tutorial covering the same setup steps); search snippets from classcentral.com and recapio.com listings
- Confidence: low (description and timecodes plus the vendor's written tutorial for the same stack; no transcript of the stream itself)

## Core claims (3-7 bullets, what the video argues)
- RevenueCat abstracts cross-platform in-app purchase logic so a React Native/Expo app can sell subscriptions without native StoreKit/Billing code (video is sponsored by RevenueCat).
- Paywalls can be designed once and managed remotely: "Managing Paywall Content and Subscription Offers Remotely" is a listed learning goal, i.e. change offers without an app release.
- A proper subscription flow needs: product configuration on App Store Connect and Google Play, RevenueCat entitlements/offerings, purchase, restore, subscription-status checks, and sandbox testing.
- Best practices for subscription UX and reading RevenueCat metrics are covered at a high level ("Best Practices for Subscription User Experience", "Analyzing Subscription Data and RevenueCat Metrics").

## Specific tactics (concrete, actionable; include numbers, prices, timings, exact UI choices)
- Timeline of the build: 08:40 create Expo project; 13:00 install libraries and create a Development Build (Expo managed workflow needs a dev client, not Expo Go, for native purchase modules); 22:20 set up RevenueCat; 29:56 configure subscription products (App Store Connect incl. p8 key, per classcentral listing); 51:50 configure RevenueCat in React Native; 01:11:35 build the RevenueCat Paywall (recapio snippet mentions full-screen modal and footer paywall layouts from react-native-purchases-ui); 01:56:00 Google Play setup.
- From RevenueCat's written tutorial for the same stack: install expo-dev-client and react-native-purchases; configure products and offerings in the RevenueCat dashboard; build with `eas build --profile development --platform android|ios`; for Android upload the APK to an internal track with a matching version number so products load; run `expo start --dev-client`; use RevenueCat debug logs (Console.app / LogCat) to see which products fail to load.
- Asset bundle for the project: assets.notjust.dev/paywall.

## Named examples (apps/companies cited and what they did)
- RevenueCat (sponsor; SDKs react-native-purchases and react-native-purchases-ui, hosted paywalls), Expo / EAS, Apple App Store Connect, Google Play Console, notJust.dev's React Native Mastery course (upsell).

## Numbers & evidence (any stats, revenue, conversion rates, retention figures; mark self-reported vs third-party)
- None found; the video is an implementation tutorial rather than a conversion-data talk.

## Contradictions or caveats (where this disagrees with common advice or other videos)
- Sponsored content: tool choice is RevenueCat by design; alternatives (Superwall, Adapty, native StoreKit 2) are not compared.
- Emphasizes remotely configurable paywalls, which is the technical prerequisite for the high experiment velocity that paywall-strategy videos (e.g. Tim Gabe) argue separates top apps.

## Memorable framings (quotable one-liners or named frameworks, verbatim if available)
- RevenueCat's model vocabulary: Products -> Entitlements -> Offerings (per classcentral listing of the related tutorial).
- "All you have to do is write some React, tell Expo to build your apps, and let RevenueCat do all of the tricky cross-platform in-app purchase logic." (RevenueCat tutorial, not the video)
