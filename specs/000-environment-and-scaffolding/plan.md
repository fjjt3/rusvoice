# 000 · Environment and Scaffolding — Plan

## Approach

Set up a clean, minimal FastAPI project structure. Keep dependencies strictly pinned to avoid breaking changes, and build a bare-bones health endpoint to validate the runtime before implementing TTS features.

## Implementation

1. **File structure setup:** Create `app/`, `tests/`, and root setup files (`requirements.txt`, `.gitignore`, `.env.example`).
2. **Environment & Dependencies:** Define `requirements.txt` with `fastapi`, `uvicorn[standard]`, `edge-tts`, `pydantic`, `pytest`, `pytest-asyncio`, and `httpx`.
3. **App Bootstrap:** Implement `app/main.py` containing the FastAPI initialization and a basic `GET /health` route returning `{"status": "ok"}`.
4. **Smoke test setup:** Create `tests/test_health.py` to test the health route using `httpx` and `pytest`.

## Decisions

- **Single `requirements.txt` instead of Poetry/Pipenv:** Keeps setup ultra-lightweight and simple for standalone local usage.
- **Uvicorn standard installation:** Ensures native WebSockets and performance extensions are available out of the box.

## Risks

- **Edge-TTS Python version incompatibility:** Mitigated by specifying Python 3.10+ in the environment requirements.