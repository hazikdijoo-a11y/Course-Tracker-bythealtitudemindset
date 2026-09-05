# Google Play listing — Course Tracker

## Identifiers

| Field | Value | Notes |
|---|---|---|
| App name | `Course Tracker` | 30 char limit; 14 used |
| Package name | `com.thealtitudemindset.coursetracker` | **Permanent.** Cannot ever be changed once published. |
| Category | **Productivity** | Health & Fitness also fits, but it triggers Play's extra Health apps declaration for no benefit here |
| Content rating | Everyone | |
| Website | https://tracker.thealtitudemindset.com/ | |
| Privacy policy | https://tracker.thealtitudemindset.com/privacy.html | |
| Contact email | hazikdijoo@gmail.com | shown publicly on the listing |

## Short description (80 char max)

```
Track habits on a spiral. One turn is a week, each aircraft a day.
```
65 characters.

## Full description (4000 char max)

```
Course Tracker draws your month as a single spiral. One turn of the spiral is one
week, and every aircraft on it is a day.

Because a day's position depends on its weekday, every Monday lines up as a spoke
running out from the centre. One glance tells you which day of the week you keep
dropping — the thing a row-and-column habit grid never shows you.

HOW A DAY IS SCORED

Tap a day to open its dial and tick off your habits. The day's colour is worked out
from the ticks, never set by hand:

• Solid green — you hit the target
• Hollow green — partly done, which reads as progress, not failure
• Red — a day that came and went with nothing ticked
• Grey — not yet: today, or still ahead
• Gold — a flight day

THE TARGET

80% of your habits, and you may always miss one. Below five habits a flat 80% would
quietly mean "all of them, every day" — 2 out of 3 is only 67% — so the grace of one
miss is what keeps the target honest at small habit counts. The app always tells you
the exact number you are aiming for.

BUILT FOR PEOPLE WITH IRREGULAR WEEKS

Mark a date as a flight day and it is excluded from your completion rate entirely,
while keeping whatever you did tick underneath it. A heavy roster month does not
punish your numbers.

Rates count against the days that have actually happened, not the whole month, so a
flawless first half reads as 100% rather than 50%. And adding a habit mid-month never
rewrites the days that came before it — each habit is only scored from the day you
added it.

YOUR DATA STAYS YOURS

No account. No server. No analytics. No ads. Everything lives on your device and
nothing is ever uploaded. Export your history to a file whenever you like and import
it on another device — that file is the only way it moves, and only you move it.

Works completely offline.

Up to 60 habits.

by The Altitude Mindset
```

## Screenshots required

Play needs **at least 2** phone screenshots (min 320px, max 3840px, 16:9 or 9:16).
Take these on the phone from the live app or the demo:

1. Month spiral, mid-month, with a mix of green / hollow / red / gold and today ringed
2. A day open — the habit dial with the radar and the percentage in the middle
3. The habits panel showing the daily target line
4. A flight-day month, showing gold spokes

The demo build is the easiest source, since it is already populated:
https://tracker.thealtitudemindset.com/demo.html

## Data safety form answers

| Question | Answer |
|---|---|
| Does your app collect or share any of the required user data types? | **No** |
| Is all of the user data collected by your app encrypted in transit? | N/A — no data collected |
| Do you provide a way for users to request that their data is deleted? | N/A — nothing is collected; users delete locally |
| Data types collected | **None** |
| Third-party SDKs | **None** |
| Ads | **No** |

This is unusually simple because it is true: the app makes no network requests after
load and has no analytics.

## Content rating questionnaire

Answer **No** to every question — no violence, sexuality, language, controlled
substances, gambling, user interaction, or location sharing. Result: **Everyone**.

---

## Screenshots (done)

`store/screenshots/` — four, Play-legal, taken from the demo build:

| File | Shows | Size | Ratio |
|---|---|---|---|
| `play-1-month-august.png` | Full month, every state, weekday spokes | 647x1096 | 1.694 |
| `play-2-day-93.png` | Day dial at 93%, target met | 720x1215 | 1.688 |
| `play-3-day-partial.png` | Day dial partly done, with the distance to target | 720x1215 | 1.688 |
| `play-4-month-september.png` | Current month, today ringed, radar sweeping | 647x1096 | 1.694 |

Upload `play-2-day-93.png` **first** — it is the one that explains the app in a
single glance, and the first screenshot is what shows in search results.

Two things that had to be fixed before these were usable, worth remembering if
they are ever reshot:
- Phone captures are ~1.98:1 and Play caps at 16:9. Cropping the browser chrome
  off the top happened to bring them inside the limit.
- Never shoot from the browser. The Chrome address bar in the frame makes the
  listing read as a website rather than an app.
