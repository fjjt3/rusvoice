# 003 · FastAPI Streaming API & Endpoints Specifications — Plan

## Approach

Define a structured Pydantic schema for request validation and implement a dedicated router (`app/api/v1/endpoints/tts.py`) mounted on the main FastAPI application. Stream the raw `io.BytesIO` audio buffer directly to the client via `StreamingResponse`.

## Implementation

1. **Request Schema:** Create `app/schemas/tts.py` containing `TTSRequest` (with fields `text`, `voice_key`, `rate` and validation rules).
2. **API Endpoint:** Implement `POST /api/v1/tts` in `app/api/v1/endpoints/tts.py` that validates inputs, cleans the text, invokes `generate_speech`, and returns `StreamingResponse`.
3. **Router Integration:** Register the router in `app/main.py` under the `/api/v1` prefix.
4. **Integration Tests:** Create `tests/test_tts_api.py` using `httpx.AsyncClient` or `TestClient` to test successful audio streaming and HTTP error responses.

## Decisions

- **JSON Body over Form Data:** Standardizes API payloads and allows clean Pydantic schema validation.
- **In-memory StreamingResponse:** Maintains compliance with the hard constraint of zero disk I/O.

## Risks

- **Uncaught engine exceptions:** Mitigated by wrapping service calls in `try/except` blocks to catch `ValueError` and `TTSError`, mapping them to `HTTPException(400)` and `HTTPException(500)` respectively.