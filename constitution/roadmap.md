# Roadmap

_Order and status of features. Provides a clear view of completed work, current focus, and upcoming ideas. Each entry links to its folder in `features/`._

## Done ✅

_Completed features, listed in order of implementation._

1. **000 · environment-and-scaffolding** — Project folder structure, virtual environment setup, FastAPI/edge-tts dependencies, and test server execution.
2. **001 · core-text-to-speech-engine-module** — Isolated async service for in-memory MP3 synthesis using Russian neural voices.
3. **002 · text-preprocessing-and-phonetic-parser** — Regex-based text cleaner fixing PDF artifacts and normalizing Cyrillic text for synthesis.
4. **003 · fastapi-streaming-api-and-endpoints** — `POST /api/v1/tts` streaming MP3 endpoint wired to text cleaner and TTS engine.
5. **004 · student-reader-web-interface-and-audio-player** — Responsive student UI with textarea, voice/speed controls, and blob-fed HTML5 audio player.
6. **005 · text-chunking-processor** — Sentence-boundary text splitter producing ordered chunks under a configurable character limit.

## Next Up 🔜

_Ideal focus. Ideally only one feature "in progress" at a time._

*(No features in progress. All planned features complete.)*

## Backlog / Ideas 💡

_Uncommitted ideas that align with the constitution._

> Every new feature is created under `features/NNN-feature-name/` containing `spec.md`, `plan.md`, and `tasks.md` before any code is written.