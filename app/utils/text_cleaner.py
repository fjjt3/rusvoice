import re

_CONTROL_RE = re.compile(
    r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\x9f"
    r"\u00ad\u200b\u200e\u200f\u2028\u2029\u202a-\u202e\ufeff]+"
)

_LINE_BREAK_RE = re.compile(r"\r\n|\r|\n")

_HYPHEN_LINE_BREAK_RE = re.compile(r"-\s*\r\n|-\s*\r|-\s*\n\s*")

_WHITESPACE_RE = re.compile(r"\s+")


def clean_text(text: str, max_chars: int = 5000) -> str:
    cleaned = text
    cleaned = _CONTROL_RE.sub("", cleaned)
    cleaned = _HYPHEN_LINE_BREAK_RE.sub("", cleaned)
    cleaned = _LINE_BREAK_RE.sub(" ", cleaned)
    cleaned = _WHITESPACE_RE.sub(" ", cleaned)
    cleaned = cleaned.strip()

    if not text or not cleaned:
        raise ValueError("text must be a non-empty string after cleaning")

    if len(cleaned) > max_chars:
        raise ValueError(f"text exceeds maximum length of {max_chars} characters")

    return cleaned
