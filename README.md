# Wall Mounted Headquarters

A monitor on the wall that tells you whether you're on track. It shows the clock, weather and your personal goals (weight, LeetCode problems, jobs applied, gym streak) with red/amber/green pace indicators and projection lines, like a manager who never forgets. You create goals and log progress from your phone. The wall updates within seconds.

Runs on a Raspberry Pi. One Python process, no Node on the device.

> **Status:** pre-implementation. The full spec and build order live in [`v1-design-doc.txt`](v1-design-doc.txt). Nothing below is built yet.

## What the wall shows

| Mode | When | Content |
|---|---|---|
| **Day** | Default | Clock, date, weather, one tile per goal with status and chart |
| **Morning** | Alarm time, for 5 minutes (configurable) | Today's weather, week-so-far progress, what to do today to stay on target |
| **Bedtime** | Configurable bedtime | Dimmed screen: clock, alarm time, hours of sleep, tomorrow's forecast |

The screen also rings as an alarm clock.

## Goals

Three goal types, created from the phone in under 30 seconds. No code change adds a new goal.

- **Number:** enter a value. Weight 90 kg → 80 kg.
- **Counter:** tap to add. 20 LeetCode problems by 12 Nov.
- **Streak:** daily yes/no habit. Gym, with consecutive days shown.

The app turns a total over a deadline into per-week and per-day rates, compares your actual pace against the required pace, and projects where you'll land at the deadline.

| Status | Actual ÷ expected progress |
|---|---|
| Green | ≥ 0.95 |
| Amber | ≥ 0.75 |
| Red | < 0.75 |

## Stack

- **Backend:** Python 3.12, FastAPI, SQLite, Server-Sent Events for live updates
- **Frontend:** React, TypeScript, Vite, built to static files and served by FastAPI
- **Weather:** Open-Meteo (free, no API key)
- **Remote access:** Tailscale
- **Tests:** pytest, Vitest, React Testing Library, Playwright

## Architecture

Layers depend inward only: `domain ← services ← api`. Domain code is pure: no I/O, no clock, no randomness. Time and weather are injected, so tests never touch the real clock or network.

```
app/
  domain/      pace maths, streaks, modes (pure)
  services/    goals, settings, weather
  storage/     SQLite repositories
  adapters/    Open-Meteo client
  api/         FastAPI routes, SSE, static files
frontend/      phone UI at /, wall UI at /display
deploy/        systemd units, kiosk script, backups
```

## Roadmap

Built test-first, in this order. Details per task are in the design doc.

- [ ] 0. Project scaffold and tooling
- [ ] 1. Result type and domain types
- [ ] 2. Pace maths: expected, actual, status
- [ ] 3. Required rate and projection
- [ ] 4. Streaks and today's plan
- [ ] 5. Screen mode and alarm schedule
- [ ] 6. SQLite storage
- [ ] 7. Goal service with validation
- [ ] 8. REST API
- [ ] 9. Weather adapter and cache
- [ ] 10. Live updates (SSE)
- [ ] 11. Phone UI
- [ ] 12. Wall display: day mode with charts
- [ ] 13. Morning and bedtime modes
- [ ] 14. Alarm sound
- [ ] 15. Raspberry Pi deployment
- [ ] 16. End-to-end check

## Security

One shared token from an env var, stored in a cookie after the first `?token=` visit. Meant for the home network and Tailscale only. Never expose it to the public internet.

## Running it

Setup, env vars, test commands and Pi deployment steps arrive with Tasks 0, 15 and 16.
