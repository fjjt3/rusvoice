# 001 · Core Text-To-Speech Engine Module — Plan

## Approach

Create a dedicated service module (`app/services/tts_engine.py`) using `edge-tts.Communicate`. The service will stream chunks into an in-memory `io.BytesIO` buffer asynchronously and return raw MP3 bytes.

## Implementation

1. **Voice Configuration:** Define voice mappings and default options (`ru-RU-SvetlanaNeural` default) in `app/services/tts_engine.py`.
2. **Synthesis Service:** Implement an async function `generate_speech(text: str, voice: str, rate: str) -> bytes` that streams audio chunks into a `BytesIO` buffer.
3. **Validation & Exception Handling:** Add input checks for non-empty text and wrap `edge-tts` calls in custom `TTSError` handling.
4. **Unit Tests:** Implement `tests/test_tts_engine.py` using `pytest` and `pytest-asyncio` to test synthesis output and invalid inputs.

## Decisions

- **In-memory buffering (`io.BytesIO`):** Avoids disk I/O overhead, temporary file cleanup, and stays compliant with hard constraints in `constitution/tech-stack.md`.
- **Async generation:** Uses native async stream iterations to remain non-blocking for FastAPI integration.

## Risks

- **Network interruption during Edge-TTS call:** Mitigated by wrapping `Communicate.stream()` in a try/except block that raises a domain-specific exception.