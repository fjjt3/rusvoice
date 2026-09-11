# 002 · Text Preprocessing and Phonetic Parser — Tasks

- [x] Create `app/utils/text_cleaner.py`.
- [x] Implement `clean_text(text: str, max_chars: int = 5000) -> str` with regex-based normalization.
- [x] Add explicit preservation for Cyrillic Unicode ranges, punctuation, numbers, and stress marks (`\u0301`).
- [x] Implement hyphenation repair for line breaks (`word- \n next` -> `wordnext`).
- [x] Create `tests/test_text_cleaner.py` with test cases for raw textbook text, extra spaces, line breaks, and limits.
- [x] Validate implementation against acceptance criteria in `spec.md`.
- [x] Update feature status in `spec.md` to `implemented ✅`.
- [x] Move feature to "Done" in `../../constitution/roadmap.md`.