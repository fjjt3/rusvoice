# 004 · Student Reader Web Interface & Audio Player UI

**Status:** implemented ✅

## What it does

Provides a clean, browser-based web interface for language students. It includes a text area for inputting textbook excerpts, selectors for voice gender and playback speed (slow/normal/fast), and an embedded HTML5 audio player that streams the generated Russian speech instantly.

## Why

Students need an intuitive, friction-free UI to quickly paste text from their textbooks, adjust playback speed for listening comprehension, and listen to native audio without touching code or API clients.

## Acceptance criteria

- [x] Serving `GET /` renders a clean, responsive HTML page with modern CSS styling.
- [x] Text input area accepts Cyrillic text and includes placeholder text in Russian/English.
- [x] Controls allow selecting Russian voices (`Svetlana` / `Dmitry`) and playback speed (`-20%` Slow, `+0%` Normal, `+20%` Fast).
- [x] Submitting text sends an asynchronous `fetch` request to `POST /api/v1/tts`.
- [x] HTML5 `<audio>` player receives the dynamic blob URL stream and enables instant playback.
- [x] Error messages (e.g., empty text, network error) are gracefully displayed to the user.

## Out of scope

- Complex state management frameworks (React/Vue) — vanilla HTML/JS/CSS keeps it lightweight.
- Automatic paragraph chunking UI controls (deferred to `005-text-chunking-processor`).