import pytest

from app.utils.text_cleaner import clean_text


def test_collapses_whitespace():
    assert clean_text("Привет    мир!") == "Привет мир!"


def test_joins_hyphenated_line_break():
    assert clean_text("раз-\nговор") == "разговор"


def test_joins_hyphenated_line_break_with_spaces():
    assert clean_text("раз- \nговор") == "разговор"


def test_replaces_line_break_with_space():
    assert clean_text("Привет\nмир") == "Привет мир"


def test_normalizes_crlf():
    assert clean_text("Привет\r\nмир") == "Привет мир"


def test_removes_control_characters():
    assert clean_text("\x00Привет\x07мир\x1f") == "Приветмир"


def test_preserves_combining_accent():
    assert clean_text("Еде\u0301т гра\u0301ч") == "Еде\u0301т гра\u0301ч"


def test_preserves_cyrillic_punctuation_and_numbers():
    source = "Урок 1: «Привет, мир!» — работаем."
    assert clean_text(source) == source


def test_strips_surrounding_whitespace():
    assert clean_text("  Привет мир  ") == "Привет мир"


def test_raises_value_error_on_empty_text():
    with pytest.raises(ValueError):
        clean_text("")


def test_raises_value_error_on_whitespace_only_text():
    with pytest.raises(ValueError):
        clean_text("   \n\t ")


def test_raises_value_error_when_over_max_chars():
    with pytest.raises(ValueError):
        clean_text("а" * 5001)


def test_accepts_text_at_max_chars():
    assert len(clean_text("а" * 5000)) == 5000


def test_raises_value_error_with_custom_max_chars():
    with pytest.raises(ValueError):
        clean_text("Приветмир", max_chars=5)
