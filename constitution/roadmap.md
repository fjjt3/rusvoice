# Roadmap

_Order and status of features. Provides a clear view of completed work, current focus, and upcoming ideas. Each entry links to its folder in `features/`._

## Done ✅

_Completed features, listed in order of implementation._

*(No features completed yet. Project initialization phase).*

## Next Up 🔜

_Immediate focus. Ideally only one feature "in progress" at a time._

1. **001 · environment-and-scaffolding** — Project folder structure, virtual environment setup, FastAPI/edge-tts dependencies, and test server execution.

## Backlog / Ideas 💡

_Uncommitted ideas that align with the constitution._

- **002 · core-tts-engine** — Encapsulated Python service for asynchronous in-memory audio generation using Russian neural voices.
- **003 · api-audio-streaming** — FastAPI endpoint to validate requests and stream MP3 audio.
- **004 · student-web-interface** — Interactive web UI featuring audio player controls, voice selection, and speed adjustments for students.
- **005 · text-chunking-processor** — Text processor to split long textbook passages into sequentially playable chunks.

> Every new feature is created under `features/NNN-feature-name/` containing `spec.md`, `plan.md`, and `tasks.md` before any code is written.