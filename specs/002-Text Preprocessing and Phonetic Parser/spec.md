# 002 · Text Preprocessing and Phonetic Parser

**Status:** implemented ✅

## What it does

Cleans, normalizes, and prepares input text before sending it to the TTS engine. It strips unsupported control characters, normalizes whitespace, cleans up formatting artifacts from copied textbook PDFs, and ensures proper sentence boundary detection for Cyrillic text.

## Why

Raw text copied from digital textbooks or PDFs often contains line breaks, special hyphenation marks, and irregular spacing. Preprocessing normalizes this text to avoid artificial pauses or mispronunciations in the synthesized audio.

## Acceptance criteria

- [x] Text cleaner function strips invalid non-printable characters while preserving standard Cyrillic text, punctuation, and numbers.
- [x] Removes line breaks (`\n`, `\r`) within sentences and normalizes multi-space strings to single spaces.
- [x] Fixes hyphenated words split across lines (e.g., `раз- \nговор` -> `разговор`).
- [x] Preserves valid stress marks (*udarenie*) or special symbols used in Russian study material if supported.
- [x] Handles empty strings and string lengths exceeding safety limits (raises `ValueError` if text is empty or > 5000 chars).
- [x] Comprehensive unit test suite covers text normalization cases and edge conditions.

## Out of scope

- Direct Edge-TTS audio stream generation (handled in `001-core-tts-engine`).
- Text chunking across multi-page chapters (deferred to `005-text-chunking-processor`).
- Full automatic phonetic stress placement (*udarenie*) dictionary integration.