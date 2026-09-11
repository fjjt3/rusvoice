import pytest

from app.utils.text_chunker import split_text_into_chunks


def test_short_text_returns_single_chunk():
    text = "Привет, мир! Это короткий текст."
    chunks = split_text_into_chunks(text)

    assert chunks == [text]


def test_empty_text_returns_empty_list():
    assert split_text_into_chunks("") == []


def test_whitespace_only_text_returns_empty_list():
    assert split_text_into_chunks("   \n\t ") == []


def test_splits_on_cyrillic_sentence_boundaries():
    text = "Привет! Как дела? Хорошо."
    chunks = split_text_into_chunks(text, max_chunk_size=10)

    assert chunks == ["Привет!", "Как дела?", "Хорошо."]


def test_splits_on_newlines():
    text = "Первая строка\nВторая строка\nТретья строка"
    chunks = split_text_into_chunks(text, max_chunk_size=15)

    assert chunks == ["Первая строка", "Вторая строка", "Третья строка"]


def test_long_text_splits_into_multiple_chunks():
    text = " ".join(f"Это предложение номер {i}." for i in range(1, 200))
    chunks = split_text_into_chunks(text, max_chunk_size=1000)

    assert len(chunks) > 1
    assert all(len(chunk) <= 1000 for chunk in chunks)


def test_chunks_reconstruct_original_words():
    text = " ".join(f"слово{i}" for i in range(1, 400))
    chunks = split_text_into_chunks(text, max_chunk_size=500)

    assert len(chunks) > 1
    assert all(len(chunk) <= 500 for chunk in chunks)
    assert " ".join(chunks) == text


def test_long_sentence_without_punctuation_uses_space_fallback():
    text = " ".join(["оченьдлинноеслово"] * 200)
    chunks = split_text_into_chunks(text, max_chunk_size=100)

    assert len(chunks) > 1
    assert all(len(chunk) <= 100 for chunk in chunks)
    assert " ".join(chunks) == text


def test_never_splits_mid_word():
    text = " ".join(f"слово{i}" for i in range(1, 300))
    chunks = split_text_into_chunks(text, max_chunk_size=200)

    for chunk in chunks:
        for token in chunk.split():
            assert token in text.split()


def test_does_not_leave_orphaned_punctuation():
    text = " ".join(f"Фраза номер {i}." for i in range(1, 100))
    chunks = split_text_into_chunks(text, max_chunk_size=120)

    for chunk in chunks:
        assert not chunk.startswith((".", "!", "?", ",", ";", ":"))
        assert chunk == chunk.strip()


def test_custom_max_chunk_size_respected():
    text = "А" * 50
    chunks = split_text_into_chunks(text, max_chunk_size=10)

    assert all(len(chunk) <= 10 for chunk in chunks)
    assert "".join(chunks) == text


def test_raises_value_error_on_non_positive_max_chunk_size():
    with pytest.raises(ValueError):
        split_text_into_chunks("Привет", max_chunk_size=0)
