# RusVoice

Russian language learner TTS app. FastAPI backend + `edge-tts` neural voices, with in-memory MP3 streaming — no audio files written to disk, no database, no paid APIs.

## Features

- Real-time TTS synthesis of textbook excerpts into native-sounding Russian speech
- Adjustable playback speed and voice selection
- Simple web UI with embedded audio player
- Stateless, in-memory audio streaming

## Requirements

- Python 3.10+
- FastAPI 0.100+
- `edge-tts` (requires internet connection)

## Setup

```
pip install -r requirements.txt
```

## Run

```
uvicorn app.main:app --reload
```

- Health check: `GET /health`
- Interactive API docs: `http://localhost:8000/docs`

## Test & Lint

```
pytest
flake8 .
black --check .
```

## Conventions

- All endpoints are `async def`
- Audio responses use `StreamingResponse` with `audio/mpeg`
- Text input capped at 5000 chars
- Default voice: `ru-RU-SvetlanaNeural`, rate `+0%`
- Spec-driven development: feature work lives in `features/NNN-name/` with `spec.md`, `plan.md`, `tasks.md`

## Docs

- `mission.md` — purpose and principles
- `roadmap.md` — feature order and status
- `tech-stack.md` — technologies and hard constraints