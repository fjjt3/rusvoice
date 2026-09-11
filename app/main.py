from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from app.api.v1.endpoints.tts import router as tts_router

app = FastAPI(title="RusVoice", version="0.1.0")

app.include_router(tts_router, prefix="/api/v1")

_INDEX_TEMPLATE = Path(__file__).parent / "templates" / "index.html"


@app.get("/", response_class=HTMLResponse)
async def index():
    return _INDEX_TEMPLATE.read_text(encoding="utf-8")


@app.get("/health")
async def health():
    return {"status": "ok"}
