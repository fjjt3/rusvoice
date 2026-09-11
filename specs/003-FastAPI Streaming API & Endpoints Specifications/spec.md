# 003 · FastAPI Streaming API & Endpoints Specifications

**Status:** implemented ✅

## What it does

Exposes RESTful HTTP endpoints via FastAPI to handle text synthesis requests, process incoming parameters, integrate preprocessing and speech engines, and stream the generated MP3 audio back to the client in real time.

## Why

Providing a structured API layer connects the frontend client with the underlying core TTS engine and text cleaning utilities, allowing clients to receive audio streams with minimal latency without saving temporary files to disk.

## Acceptance criteria

- [x] Endpoint `POST /api/v1/tts` accepts request payload (`text`, `voice_key`, `rate`).
- [x] Endpoint integrates `clean_text` (from SPEC-002) before passing text to `generate_speech` (from SPEC-001).
- [x] Returns a `StreamingResponse` with MIME type `audio/mpeg` and header `Content-Disposition: inline; filename=speech.mp3`.
- [x] Handles invalid inputs (e.g., empty text, invalid voice keys) by returning standard HTTP 400 JSON error responses.
- [x] Handles internal TTS service failures by returning HTTP 500 JSON error responses.
- [x] Integration tests verify response status codes, content-type headers, and streaming byte output.

## Out of scope

- HTML frontend rendering or static asset serving (deferred to `004-student-web-interface`).
- User authentication, rate limiting, or API key validation.
- Long-text automatic chunking pipeline (deferred to `005-text-chunking-processor`).