# 001 · Core Text-To-Speech Engine Module

**Status:** implemented ✅

## What it does

Implements an isolated, asynchronous service in Python that converts text strings into MP3 audio streams using Edge-TTS (`edge-tts`). It supports selecting specific Russian neural voices (`ru-RU-SvetlanaNeural`, `ru-RU-DmitryNeural`) and adjusting speech rates (e.g., `-20%`, `+0%`, `+20%`).

## Why

Encapsulating the core speech synthesis logic into a standalone service ensures clean separation of concerns, decouples edge-tts implementation from FastAPI route handlers, and prevents saving temporary audio files to disk by handling raw audio bytes strictly in memory (`io.BytesIO`).

## Acceptance criteria

- [x] Core TTS service class/function generates valid MP3 byte streams asynchronously using `edge-tts`.
- [x] Supports Russian female (`ru-RU-SvetlanaNeural`) and male (`ru-RU-DmitryNeural`) neural voice options.
- [x] Supports speed modification parameters (`rate` string like `-20%` or `+0%`).
- [x] Returns audio strictly as in-memory bytes (`BytesIO` / `bytes`) without writing any files to disk.
- [x] Throws appropriate custom exceptions when text is empty or edge-tts generation fails.
- [x] Unit test suite passes with mock/real Edge-TTS execution asserting non-empty audio byte output.

## Out of scope

- FastAPI endpoints or HTTP streaming responses (deferred to `002-backend-api-gateway`).
- UI controls and player front-end (deferred to `003-student-web-interface`).
- Text chunking for passages longer than 5000 characters (deferred to `004-text-chunking-processor`).