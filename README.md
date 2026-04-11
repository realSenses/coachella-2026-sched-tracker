# Coachella 2026 — Stream Schedule

A single-file web app for browsing the Coachella 2026 YouTube livestream schedule. No build step, no external dependencies — fonts are bundled locally.

> **Weekend 2 support coming soon.**

## Features

- **Day tabs** — switch between Friday (Apr 10), Saturday (Apr 11), and Sunday (Apr 12)
- **All 9 stages** — Coachella Stage, Outdoor Theatre, Sahara, Mojave, Gobi, Sonora, Yuma, Quasar, Do LaB, each color-coded
- **YouTube stream links** — stage names link directly to their live YouTube streams
- **Now Playing bar** — auto-detects which sets are currently live based on your local clock
- **Timezone selector** — converts all set times to your timezone; preference saved to `localStorage`
- **Artist search** — filters across all days in real time
- **Favorites** — heart any set to save it; favorites persist across sessions via `localStorage`
- **My Schedule tab** — shows all favorited sets sorted chronologically with conflict warnings for overlapping sets

## Usage

Double-click `coachella2026.html`, or run a local server to avoid browser CORS restrictions on fonts (Chrome in particular blocks local font loading over `file://`):

```
python3 -m http.server 8000
```

Then open `http://localhost:8000/coachella2026.html`.

## Stack

Plain HTML/CSS/JS. Fonts (`Bebas Neue`, `DM Mono`) are downloaded and served from the `fonts/` directory — no network requests required.
