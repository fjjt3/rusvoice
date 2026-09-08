# Tech Stack & Conventions

_How the project is built and the rules all code must follow._

## Technologies

- **Language:** Python 3.10+
- **Framework / Runtime:** FastAPI 0.100+ / Uvicorn
- **TTS Engine:** `edge-tts` (Microsoft Edge Neural Voices)
- **Database:** Not applicable (Stateless / No persistence)
- **Testing:** `pytest` / `pytest-asyncio` + `httpx` for API integration testing
- **Deployment:** Local development environment / Run via `uvicorn main:app --reload`

## Key Files & Modules

- `app/main.py` — FastAPI entry point, routes, and application server.
- `app/services/tts_engine.py` — Encapsulated service communicating with `edge-tts`.
- `app/templates/index.html` — Minimalist student web UI with embedded audio player.
- `features/` — Directories containing SDD specs, plans, and tasks for each feature.

## Commands

- `uvicorn app.main:app --reload` — Starts the local development server.
- `pytest` — Runs unit and endpoint test suites.
- `flake8 .` or `black --check .` — Enforces Python code style and formatting.

## Data Model / Domain

- `TTSRequest`:
  - `text` (str, required): Text snippet to synthesize (e.g., Russian textbook text). Max 5000 characters.
  - `voice` (str, optional): Neural voice identifier (`ru-RU-SvetlanaNeural`, `ru-RU-DmitryNeural`). Defaults to `ru-RU-SvetlanaNeural`.
  - `rate` (str, optional): Speed modifier in percentage format (e.g., `-20%`, `+0%`, `+20%`). Defaults to `+0%`.

## Conventions

- Standard Python **PEP 8** style guidelines (`snake_case` for variables/functions, `PascalCase` for classes).
- Explicit type hinting using `typing` and schema validation via **Pydantic**.
- Asynchronous endpoints (`async def`) to avoid blocking thread pools during audio generation I/O.
- Direct audio output using `StreamingResponse` with `audio/mpeg` MIME type.

## Visual Style

- Clean UI inspired by modern learning tools.
- Primary colors: Accessible blue (`#007bff`) over light backgrounds (`#f9f9f9`).
- System sans-serif typography (Arial / Inter) optimized for Cyrillic script readability.

## Hard Constraints

- **No writing audio files to disk:** Synthesized audio must be processed and streamed strictly in RAM (`io.BytesIO`).
- **No mandatory paid services:** The core application must function 100% free without credit cards or API keys.
- **No code without prior specification:** Every logic change must belong to an approved folder under `features/NNN-name/`.