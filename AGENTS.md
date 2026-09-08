# AGENTS.md

## Project

Russian language learner TTS app. FastAPI + `edge-tts`. No database. No audio files on disk — everything streams from RAM via `io.BytesIO`.

## Workflow (SDD)

No code without a feature spec. Every feature lives in `features/NNN-name/` with `spec.md`, `plan.md`, `tasks.md`. The roadmap (`roadmap.md`) is the source of truth for what's approved and in progress.

## Commands

```
uvicorn app.main:app --reload   # dev server
pytest                           # tests
flake8 .                        # lint
black --check .                 # format check
```

## Hard Constraints

- No audio files written to disk — streaming only
- No paid APIs or keys required
- Python 3.10+, FastAPI 0.100+, `edge-tts`
- All endpoints must be `async def`
- Audio responses: `StreamingResponse` with `audio/mpeg`
- Text input capped at 5000 chars
- Default voice: `ru-RU-SvetlanaNeural`, rate `+0%`

## Style

PEP 8 (`snake_case` functions, `PascalCase` classes). Pydantic for validation. Type hints everywhere.
