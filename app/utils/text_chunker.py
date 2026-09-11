import re

_SENTENCE_RE = re.compile(r"[^.!?\n]+[.!?]*")


def _split_long_segment(segment: str, max_chunk_size: int) -> list[str]:
    chunks: list[str] = []
    current = ""
    for word in segment.split():
        if len(word) > max_chunk_size:
            if current:
                chunks.append(current)
                current = ""
            for start in range(0, len(word), max_chunk_size):
                chunks.append(word[start : start + max_chunk_size])
            continue

        candidate = f"{current} {word}".strip() if current else word
        if len(candidate) <= max_chunk_size:
            current = candidate
        else:
            if current:
                chunks.append(current)
            current = word

    if current:
        chunks.append(current)
    return chunks


def split_text_into_chunks(text: str, max_chunk_size: int = 1000) -> list[str]:
    if max_chunk_size <= 0:
        raise ValueError("max_chunk_size must be a positive integer")

    if not text or not text.strip():
        return []

    sentences = [match.group().strip() for match in _SENTENCE_RE.finditer(text)]
    sentences = [sentence for sentence in sentences if sentence]

    chunks: list[str] = []
    current = ""

    for sentence in sentences:
        if len(sentence) > max_chunk_size:
            if current:
                chunks.append(current)
                current = ""
            chunks.extend(_split_long_segment(sentence, max_chunk_size))
            continue

        candidate = f"{current} {sentence}".strip() if current else sentence
        if len(candidate) <= max_chunk_size:
            current = candidate
        else:
            if current:
                chunks.append(current)
            current = sentence

    if current:
        chunks.append(current)

    return chunks
