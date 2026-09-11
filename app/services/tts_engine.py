import io

import edge_tts

VOICES = {
    "ru_female": "ru-RU-SvetlanaNeural",
    "ru_male": "ru-RU-DmitryNeural",
}

DEFAULT_VOICE = "ru_female"
DEFAULT_RATE = "+0%"


class TTSError(Exception):
    """Raised when speech synthesis fails."""


async def generate_speech(
    text: str, voice_key: str = DEFAULT_VOICE, rate: str = DEFAULT_RATE
) -> bytes:
    if not text or not text.strip():
        raise ValueError("text must be a non-empty string")

    try:
        voice = VOICES[voice_key]
    except KeyError:
        raise ValueError(f"unknown voice key: {voice_key!r}") from None

    try:
        communicate = edge_tts.Communicate(text, voice, rate=rate)
        buffer = io.BytesIO()
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                buffer.write(chunk["data"])
        return buffer.getvalue()
    except Exception as exc:
        raise TTSError(f"speech generation failed: {exc}") from exc
