# 005 · Text Chunking Processor — Plan

## Approach

Create a dedicated text chunking module (`app/utils/text_chunker.py`) that uses regular expressions and sentence boundary rules to break down long textbook passages into an ordered array of strings, ensuring each chunk is within safe character limits.

## Implementation

1. **Chunking Algorithm:** Implement `split_text_into_chunks(text: str, max_chunk_size: int = 1000) -> list[str]` in `app/utils/text_chunker.py`.
2. **Boundary Logic:** Use regex splitting on sentence-ending punctuation (`[.!?\n]+`) while keeping track of current chunk length to append sentences iteratively until reaching `max_chunk_size`.
3. **Integration Optional Utility:** Expose chunking logic for future backend streaming or frontend paragraph-by-paragraph rendering.
4. **Unit Tests:** Implement `tests/test_text_chunker.py` testing long multi-sentence texts, short texts (returning single chunk), and edge cases with Cyrillic punctuation.

## Decisions

- **Sentence-level splitting over word-level:** Splitting at full stops or punctuation maintains natural speech rhythm and intonation when synthesized by Edge-TTS.

## Risks

- **Passages with missing punctuation:** Mitigated by adding a fallback word-level splitter if a single sentence exceeds `max_chunk_size`.