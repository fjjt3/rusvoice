# 001 · Core Text-To-Speech Engine Module — Tasks

- [x] Create `app/services/tts_engine.py` with voice constants and custom `TTSError` exception.
- [x] Implement async function `generate_speech(text: str, voice: str = "ru-RU-SvetlanaNeural", rate: str = "+0%") -> bytes`.
- [x] Validate input text (raise `ValueError` or `TTSError` if empty or whitespace).
- [x] Create `tests/test_tts_engine.py` to test audio generation asynchronously with pytest.
- [x] Validate implementation against acceptance criteria in `spec.md`.
- [x] Update feature status in `spec.md` to `implemented ✅`.
- [x] Move feature to "Done" in `../../constitution/roadmap.md`.