from unittest.mock import patch

from fastapi.testclient import TestClient

from app.main import app
from app.services.tts_engine import TTSError

client = TestClient(app)


def test_post_tts_returns_audio_stream():
    audio_bytes = b"\xff\xf3fake-mp3-data"
    with patch(
        "app.api.v1.endpoints.tts.generate_speech",
        return_value=audio_bytes,
    ) as mock_generate:
        response = client.post(
            "/api/v1/tts",
            json={"text": "Привет, мир!", "voice_key": "ru_female", "rate": "+0%"},
        )

    assert response.status_code == 200
    assert response.headers["content-type"] == "audio/mpeg"
    assert response.headers["content-disposition"] == "inline; filename=speech.mp3"
    assert response.content == audio_bytes
    mock_generate.assert_called_once_with("Привет, мир!", "ru_female", "+0%")


def test_post_tts_returns_400_on_empty_text():
    response = client.post("/api/v1/tts", json={"text": "   \n  "})

    assert response.status_code == 400
    assert "text" in response.json()["detail"]


def test_post_tts_returns_400_on_unknown_voice_key():
    with patch(
        "app.api.v1.endpoints.tts.generate_speech",
        side_effect=ValueError("unknown voice key: 'ru_unknown'"),
    ):
        response = client.post(
            "/api/v1/tts", json={"text": "Привет", "voice_key": "ru_unknown"}
        )

    assert response.status_code == 400
    assert "voice key" in response.json()["detail"]


def test_post_tts_returns_500_on_tts_error():
    with patch(
        "app.api.v1.endpoints.tts.generate_speech",
        side_effect=TTSError("network down"),
    ):
        response = client.post("/api/v1/tts", json={"text": "Привет"})

    assert response.status_code == 500
    assert "network down" in response.json()["detail"]
