from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_index_returns_html():
    response = client.get("/")

    assert response.status_code == 200
    assert response.headers["content-type"] == "text/html; charset=utf-8"
    assert "RusVoice" in response.text
    assert 'id="player"' in response.text
    assert "/api/v1/tts" in response.text
