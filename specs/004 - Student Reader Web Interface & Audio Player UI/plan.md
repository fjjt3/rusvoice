# 004 · Student Reader Web Interface & Audio Player UI — Plan

## Approach

Implement a single-page frontend using FastAPI's `HTMLResponse` or Jinja2 templates (`app/templates/index.html`). Use standard Vanilla JavaScript (`fetch` API and `URL.createObjectURL`) to communicate asynchronously with `POST /api/v1/tts` without full page reloads.

## Implementation

1. **HTML/CSS UI:** Create `app/templates/index.html` featuring a styled text area, voice/speed dropdowns, submit button, and hidden audio container.
2. **Frontend Logic:** Write inline JS to listen for form submit, construct the JSON payload, handle `Blob` audio responses, and bind them to the `<audio>` tag.
3. **FastAPI Route Integration:** Add a `GET /` endpoint in `app/main.py` serving `index.html`.
4. **Integration Test:** Create `tests/test_ui.py` to verify `GET /` returns status 200 and HTML content.

## Decisions

- **Vanilla JS + HTMLResponse:** Avoids external build steps, frontend bundlers, or heavy dependencies while maintaining instant responsiveness.
- **Audio Blob URL (`URL.createObjectURL`):** Allows immediate playback directly from memory buffers in the browser.

## Risks

- **CORS or asset loading errors:** Mitigated by embedding styling and scripting directly inside the single HTML template for local execution.