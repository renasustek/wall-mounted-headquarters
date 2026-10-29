# Wall Mounted Headquarters

A wall-mounted dashboard for a Raspberry Pi and one monitor. It shows the clock, weather and personal goals (weight, LeetCode problems, jobs applied, habits) with red/amber/green pace indicators and projection lines. Goals are created and logged from a phone, and the wall screen updates live.

The screen switches between DAY, MORNING and BEDTIME modes and doubles as an alarm clock.

## Status

Pre-implementation. The full spec and build order are in [`v1-design-doc.txt`](v1-design-doc.txt).

## Stack

- Backend: Python 3.12, FastAPI, SQLite, Server-Sent Events
- Frontend: React, TypeScript, Vite
- Deployment: single Python process on a Raspberry Pi, Chromium in kiosk mode

## Setup

Setup instructions land with Task 0 of the roadmap.
