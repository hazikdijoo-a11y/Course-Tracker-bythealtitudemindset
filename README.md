# Course Tracker

*by The Altitude Mindset*

An installable, offline-first PWA habit tracker. A month is drawn as a single
Archimedean spiral: **one turn is one week**, so a month is roughly 4.3 turns,
and **each aircraft is a day**.

Because a day's angle is its position in the 7-day cycle, every occurrence of
the same weekday lines up as a spoke out from the centre — so you can see at a
glance which weekday you keep dropping. The weekday ring outside the spiral
names them.

No frameworks, no CDN, no build step. Plain HTML, CSS and JS in one file.

## How a day is scored

Tap an aircraft to open that day's checklist and tick off your habits. A day's
colour is **derived from the ticks**, never set by hand:

| Marker | Meaning |
|---|---|
| Solid green ✓ | Target met |
| Hollow green ◐ | Partly done — progress, not failure |
| Red ✕ | A day that has been and gone with nothing ticked |
| Grey outline | Not yet — today, or still ahead |
| Gold ✈ | Flight day |
| Dashed cream ring | Today |

### The target

80% of your habits, **with a guaranteed grace of one**:

```
required = max(1, min(ceil(total × 0.8), total − 1))
```

The grace matters below five habits, where a flat 80% quietly means "all of
them, every day" — 1/2, 2/3 and 3/4 all fall short of the bar. At five habits
and above this is arithmetically identical to plain ≥ 80%. A single habit is
unavoidably all-or-nothing. The habits panel always states your live target.

### Flight days

A property of the *date*, not of a habit: set it once and every habit on that
date reads gold. Flight days preserve whatever is ticked underneath and are
excluded from completion denominators, so a heavy flying month doesn't punish
your rate. Set one from the day strip below the spiral, from the day sheet, or
by tapping a day number on the spiral.

### Rates

A habit's monthly figure is counted against **days elapsed**, not the whole
month — a flawless first half of the month reads 100%, not 50%. Today counts,
so ticking today's habits moves the number straight away. Days ticked ahead of
time show on the spiral but never inflate the rate.

Each habit is scored only from its own `createdOn`, so **adding a habit
mid-month never rewrites days that came before it**.

Up to **60 habits**.

## Your data

`localStorage` on the device, under one versioned key. No account, no server,
nothing leaves the browser.

> **Install it, and export regularly.** This matters more than it sounds.
> iOS Safari clears the storage of a site you have not opened in 7 days — a
> long roster block could take your history with it. Adding the app to your
> Home Screen exempts it. The app asks for persistent storage where the browser
> supports it, shows when you last exported, and nags after three weeks.

**Export** writes a `.json` file; **Import** loads one back, replacing what is
on the device. That file is the only way history moves between a phone and a
laptop.

**Reset month** clears only the month you are looking at.

## Running it

Any static host. Locally:

    python3 -m http.server 8912

Then open <http://localhost:8912/>. It must be served over `http(s)` rather
than opened as a `file://` path — service workers only register on `https://`
or `localhost`, and without one there is no offline cache and no install
prompt.

## Keyboard

| Key | Does |
|---|---|
| Tab | The spiral is **one** stop, not 31 |
| ← → ↑ ↓ | Move between days |
| PageUp / PageDown | Jump a week |
| Home / End | First / last day of the month |
| Enter / Space | Open that day's checklist |
| ← → (outside the spiral) | Previous / next month |

Every marker carries an `aria-label` naming the date, the score and the verdict
("Today, 18 August, 3 of 3 habits, 100 percent, target met"). State is never
carried by colour alone — each one has a distinct glyph and outline weight.

The day numbers drawn on the spiral are a pointer-only shortcut for toggling a
flight day, deliberately `aria-hidden`; the day strip below is the accessible
equivalent.

## Files

| File | Purpose |
|---|---|
| `index.html` | The whole app — markup, inline CSS, inline JS |
| `manifest.json` | PWA manifest |
| `sw.js` | Service worker |
| `icon-192.png`, `icon-512.png` | App icons |

## Editing

Navigations are **network-first**, so a deployed change reaches installed users
on their next launch whether or not `CACHE` in `sw.js` was bumped. Icons and
the manifest stay cache-first — bump `CACHE` when you change those.

Brand colours live in `:root` in `index.html`: deep navy `#0B1B33`, champagne
gold `#E8C468`, cream `#F8F6F0`. Gold is only ever used on a dark ground —
on cream it measures 1.55:1.
