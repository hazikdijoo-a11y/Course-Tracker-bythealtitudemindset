# Getting Course Tracker onto Google Play

The app ships as a **Trusted Web Activity** (TWA) — a thin Android wrapper that runs
the existing PWA full-screen in Chrome's engine, with no browser UI. It is the
standard route for a PWA and does not fork the codebase: the Play app and the web app
stay the same thing.

---

## Blockers to know before you spend anything

**1. New personal developer accounts must run a closed test first.**
Google requires new personal accounts to run a closed test with **12 testers who stay
opted in for 14 continuous days** before you can even apply for production access.
Budget two to three weeks between creating the account and being publicly listed.
Verify the current rule in the Play Console when you sign up — this policy has moved
before.

**2. Digital Asset Links must live at the domain root.**
A TWA only opens without a browser bar if this file is reachable:

    https://tracker.thealtitudemindset.com/.well-known/assetlinks.json

That is the **root** of the github.io origin, not this project's folder. You would
need a second repo named exactly `hazikdijoo-a11y.github.io` containing
`.well-known/assetlinks.json`. Without it the app still runs, but shows a URL bar,
which looks unfinished.

**3. Consider a custom domain instead.**
`hazikdijoo-a11y.github.io` is shared with every other GitHub Pages project on your
account, and the listing will show that URL. Pointing a domain you own — e.g.
`tracker.thealtitudemindset.com` — at the same GitHub Pages site gives you a clean
origin, a professional listing, and a `.well-known` path you fully control. This is
the option I would take, and it changes nothing about the app itself.

**4. Minimum-functionality policy.**
Google rejects thin webview wrappers. A TWA of a genuine offline-capable PWA is
normally accepted, but the risk is not zero. The offline support, install behaviour
and lack of any browser chrome are what distinguish it — worth mentioning in the
review notes if it is ever queried.

---

## What only you can do

- [ ] Create a Google Play developer account and pay the **$25** one-time fee
- [ ] Complete identity verification (government ID; can take a few days)
- [ ] Accept the Developer Distribution Agreement
- [ ] Generate and **keep** the app signing key — whoever holds it controls all future
      updates. Use Play App Signing and store the upload key somewhere you will not
      lose it. Losing it means never being able to update the app again.
- [ ] Take the phone screenshots (see LISTING.md)
- [ ] Recruit 12 testers for the closed test
- [ ] Press Publish

## What is already prepared in this folder

- [x] `feature-graphic.png` — 1024×500, required
- [x] `icon-512.png` — 512×512, required
- [x] `LISTING.md` — app name, short and full description, data safety answers,
      content rating answers
- [x] `../privacy.html` — the privacy policy Play requires, ready to deploy with the site
- [x] `../twa-manifest.json` — Bubblewrap config, ready to build

## Building the Android package

Requires a JDK and the Android SDK (~1.5 GB), which Bubblewrap downloads on first run
into `~/.bubblewrap`. Neither is currently installed on this machine.

    npx @bubblewrap/cli init --manifest https://tracker.thealtitudemindset.com/manifest.json
    npx @bubblewrap/cli build

That produces `app-release-bundle.aab` — the file you upload to Play — and prints the
SHA-256 fingerprint of your signing key. That fingerprint goes into
`.well-known/assetlinks.json`; Bubblewrap will generate the file contents for you.

Order matters: build first to get the fingerprint, publish assetlinks.json second,
then upload the bundle.

---

## Build output (done)

`app-release-bundle.aab` and `app-release-signed.apk` are built in
`~/Downloads/twa-build/`, signed with the upload key at
`~/Downloads/twa-build/signing/`.

    package      com.thealtitudemindset.coursetracker
    versionCode  1
    versionName  1.0.0
    origin       tracker.thealtitudemindset.com
    upload key   SHA-256 5F:C7:E2:0E:95:3E:44:59:CC:0E:0B:96:49:6F:CC:D1:05:AB:7B:E6:DC:72:92:DA:5A:EB:3C:2D:17:DD:AD:C3

### One thing that must be done AFTER the first upload

`.well-known/assetlinks.json` currently lists the **upload key** fingerprint. That
is what makes the sideloaded APK verify, and it is correct for testing.

It is **not** what users will get. With Play App Signing, Google re-signs the app
with its own key, so the delivered app's fingerprint is different. After the first
upload go to:

    Play Console -> Test and release -> Setup -> App integrity -> App signing key certificate

Copy that SHA-256 and **add it to the array** — keep both, do not replace:

    "sha256_cert_fingerprints": [
      "5F:C7:...:C3",          <- upload key, keeps local testing working
      "<the one from Play>"    <- app signing key, what users actually run
    ]

If you skip this, the app still works but opens with a browser URL bar across the
top, which is the single most common way a TWA ships looking unfinished.
