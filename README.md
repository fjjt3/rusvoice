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

## Setup and Run on Windows

Open PowerShell in the project folder and run:

```powershell
cd "C:\Users\<your-user>\Desktop\workspace\IA\rusvoice"
py -3 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

Then open `http://localhost:8000` in your browser.

The application also provides:

- Health check: `GET /health`
- Interactive API docs: `http://localhost:8000/docs`

If the `py` command is not available but `python` is, replace `py -3` with
`python` in the virtual environment creation command. If PowerShell blocks
activation, the commands above still work because they call the virtual
environment's Python executable directly.

To activate the environment for later commands, run:

```powershell
.\.venv\Scripts\Activate.ps1
```

After activation, the shorter commands can be used:

```powershell
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

Stop the server with `Ctrl+C`.

## Setup and Run on macOS

Open Terminal in the project folder and run:

```bash
cd ~/Desktop/workspace/IA/rusvoice
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m uvicorn app.main:app --reload
```

Then open `http://localhost:8000` in your browser.

To activate the environment for later commands, run:

```bash
source .venv/bin/activate
```

After activation, the shorter commands can be used:

```bash
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

Stop the server with `Ctrl+C`.

## Test & Lint

```powershell
python -m pytest
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