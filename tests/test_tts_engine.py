from unittest.mock import MagicMock, patch

import pytest

from app.services.tts_engine import TTSError, VOICES, generate_speech


def _make_stream(*chunks: bytes):
    async def _stream():
        for data in chunks:
            yield {"type": "audio", "data": data}
        yield {"type": "SessionEnd", "data": b""}

    return _stream


@pytest.mark.asyncio
async def test_generate_speech_returns_audio_bytes():
    fake_communicate = MagicMock()
    fake_communicate.stream.side_effect = _make_stream(b"chunk1", b"chunk2", b"chunk3")

    with patch(
        "app.services.tts_engine.edge_tts.Communicate", return_value=fake_communicate
    ):
        result = await generate_speech("Привет, мир!")

    assert isinstance(result, bytes)
    assert result == b"chunk1chunk2chunk3"
    fake_communicate.stream.assert_called_once()


@pytest.mark.asyncio
async def test_generate_speech_uses_requested_voice_and_rate():
    fake_communicate = MagicMock()
    fake_communicate.stream.side_effect = _make_stream(b"chunk1")

    with patch("app.services.tts_engine.edge_tts.Communicate") as mock_communicate:
        mock_communicate.return_value = fake_communicate
        await generate_speech("Привет", voice_key="ru_male", rate="-20%")

    mock_communicate.assert_called_once_with("Привет", VOICES["ru_male"], rate="-20%")


@pytest.mark.asyncio
async def test_generate_speech_raises_value_error_on_empty_text():
    with pytest.raises(ValueError):
        await generate_speech("")


@pytest.mark.asyncio
async def test_generate_speech_raises_value_error_on_whitespace_text():
    with pytest.raises(ValueError):
        await generate_speech("   \n\t ")


@pytest.mark.asyncio
async def test_generate_speech_raises_value_error_on_unknown_voice():
    with pytest.raises(ValueError):
        await generate_speech("Привет", voice_key="ru_unknown")


@pytest.mark.asyncio
async def test_generate_speech_raises_tts_error_on_stream_failure():
    with patch(
        "app.services.tts_engine.edge_tts.Communicate",
        side_effect=RuntimeError("network down"),
    ):
        with pytest.raises(TTSError):
            await generate_speech("Привет")
