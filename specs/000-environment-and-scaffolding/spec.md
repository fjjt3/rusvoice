# 000 · Environment and Scaffolding

**Status:** in progress

## What it does

Establishes the foundational project structure, Python virtual environment, dependencies, and basic application entry point. It provides a functional baseline server to verify that the core tech stack (FastAPI and Edge-TTS) is properly installed and runnable.

## Why

Setting up the dev environment and scaffolding first ensures a predictable workspace, eliminates dependency conflicts early, and aligns with SDD principles before writing feature-specific business logic.

## Acceptance criteria

- [ ] Project directory structure is created following the repository architecture guidelines.
- [ ] Virtual environment (`.venv`) is configured and running Python 3.10+.
- [ ] Dependencies (`fastapi`, `uvicorn`, `edge-tts`, `pydantic`, `pytest`) are defined in a `requirements.txt` file and installable without errors.
- [ ] A minimal FastAPI health check endpoint (`GET /health`) runs successfully on Uvicorn.
- [ ] `.gitignore` is present and prevents tracking `.venv`, `__pycache__`, and temporary system files.

## Out of scope

- Audio generation or Edge-TTS integration logic (deferred to `001-core-tts-engine`).
- Custom UI templates or frontend assets (deferred to `004-student-web-interface`).
- Advanced API validation or production deployment scripts.