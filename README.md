# Course Tracker

*by The Altitude Mindset*

An installable, offline-first PWA habit tracker. The month is drawn as a single
Archimedean spiral: each habit is one full 360° turn, and each day on a turn is
an aircraft-shaped marker you tap to log the day.

Because a marker's angle depends only on the date, the same day is radially
aligned across every turn — so a flight day reads as a clean spoke from the
centre outward.

## Using it

- **Tap an aircraft** to cycle it: not logged → completed → missed → not logged.
- **Tap a day number** (or a date in the strip below the spiral) to mark it a
  flight day. Flight days turn every habit blue on that date, preserve the
  values underneath, and are excluded from completion-rate denominators.
- **‹ ›** in the centre, or the arrow keys, move between months.
- Up to **5 habits**, one per turn.

## Storage

`localStorage` on the device, under a single versioned key — no account, no
server, nothing leaves the browser. Use **Export** / **Import** to move history
between a phone and a laptop.

## Running it

Any static host works. Locally:

    python3 -m http.server 8912

Then open <http://localhost:8912/>. It must be served over `http(s)` rather
than opened as a `file://` path — service workers only register on `https://`
or `localhost`, and without one there is no offline cache and no install
prompt.

## Files

| File | Purpose |
|---|---|
| `index.html` | The whole app — markup, inline CSS, inline JS |
| `manifest.json` | PWA manifest |
| `sw.js` | Cache-first service worker |
| `icon-192.png`, `icon-512.png` | App icons |

No frameworks, no CDN, no build step.

## Editing

After changing any file, bump `CACHE` in `sw.js` (`course-tracker-v1` →
`-v2`). The worker serves cached files first, so installed copies will
otherwise keep showing the old version.
