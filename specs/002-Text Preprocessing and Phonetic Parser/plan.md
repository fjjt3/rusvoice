# 002 · Text Preprocessing and Phonetic Parser — Plan

## Approach

Implement a dedicated utility module (`app/utils/text_cleaner.py`) with pure, stateless functions using regular expressions (`re`) for string sanitation and normalization optimized for Russian text.

## Implementation

1. **Text Sanitation:** Create `clean_text(raw_text: str) -> str` using regex patterns to remove unwanted control characters and unify space characters.
2. **Line-Break & Hyphen Repair:** Replace line breaks with spaces and join hyphenated line-endings specifically used in printed textbook layouts.
3. **Length Validation:** Validate normalized text length (raise `ValueError` if empty or over 5000 characters).
4. **Unit Tests:** Implement `tests/test_text_cleaner.py` with test fixtures representing typical messy textbook copy-pastes.

## Decisions

- **Pure function pattern:** Keeps text cleaning entirely stateless, fast, and easy to unit test without external dependencies.
- **Max length cap (5000 chars):** Prevents timeout or memory issues during downstream Edge-TTS processing.

## Risks

- **Accidental removal of Russian stress accents:** Regex must explicitly preserve combining acute accent characters (`\u0301`) often found in Russian textbooks.