# 004 · Student Reader Web Interface & Audio Player UI — Tasks

- [x] Create `app/templates/index.html` with responsive layout and Cyrillic font support.
- [x] Implement UI controls: textarea, voice dropdown, speed dropdown (`-20%`, `+0%`, `+20%`), and `<audio>` player.
- [x] Add JavaScript to handle `fetch('/api/v1/tts')`, Blob creation, and audio player source binding.
- [x] Serve `index.html` on `GET /` route in `app/main.py`.
- [x] Create `tests/test_ui.py` to assert `GET /` returns HTTP 200 and `text/html`.
- [x] Validate implementation against acceptance criteria in `spec.md`.
- [x] Update feature status in `spec.md` to `implemented ✅`.
- [x] Move feature to "Done" in `../../constitution/roadmap.md`.