# Coachella 2026 — Stream Schedule

A single-file web app for browsing the Coachella 2026 YouTube livestream schedule. No build step, no external dependencies — fonts are bundled locally.

## Features

- **Weekend toggle** — switch between Weekend 1 (Apr 10–12) and Weekend 2 (Apr 17–19); defaults to the current/upcoming weekend
- **Day tabs** — switch between Friday, Saturday, and Sunday within each weekend
- **All stages** — Coachella Stage, Outdoor Theatre, Sahara, Mojave, Gobi, Sonora, Yuma, Quasar, Do LaB, each color-coded
- **YouTube stream links** — stage names link directly to their live YouTube streams (W2 note: Yuma is streaming, Sonora is not)
- **Now Playing bar** — auto-detects which sets are currently live based on your local clock
- **Timezone selector** — converts all set times to your timezone; preference saved to `localStorage`
- **Artist search** — filters across all days in the current weekend in real time
- **Favorites** — heart any set to save it; favorites persist across sessions via `localStorage`
- **My Schedule tab** — shows all favorited sets sorted chronologically with conflict warnings for overlapping sets



## Stack

Plain HTML/CSS/JS. Fonts (`Bebas Neue`, `DM Mono`) are downloaded and served from the `fonts/` directory — no network requests required.
