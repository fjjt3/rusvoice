# 003 · FastAPI Streaming API & Endpoints Specifications — Tasks

- [x] Create Pydantic request model `app/schemas/tts.py` (`TTSRequest`).
- [x] Create endpoint file `app/api/v1/endpoints/tts.py` with `POST /api/v1/tts`.
- [x] Wire `clean_text` and `generate_speech` inside the endpoint handler.
- [x] Return `StreamingResponse(io.BytesIO(audio_bytes), media_type="audio/mpeg")`.
- [x] Mount the API router in `app/main.py`.
- [x] Create `tests/test_tts_api.py` covering status 200 (audio/mpeg stream), 400 (validation error), and 500 (engine error).
- [x] Validate implementation against acceptance criteria in `spec.md`.
- [x] Update feature status in `spec.md` to `implemented ✅`.
- [x] Move feature to "Done" in `../../constitution/roadmap.md`.