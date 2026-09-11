import io

from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse

from app.schemas.tts import TTSRequest
from app.services.tts_engine import TTSError, generate_speech
from app.utils.text_cleaner import clean_text

router = APIRouter(tags=["tts"])


@router.post("/tts")
async def synthesize_speech(request: TTSRequest) -> StreamingResponse:
    try:
        cleaned_text = clean_text(request.text)
        audio_bytes = await generate_speech(
            cleaned_text, request.voice_key, request.rate
        )
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except TTSError as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc

    return StreamingResponse(
        io.BytesIO(audio_bytes),
        media_type="audio/mpeg",
        headers={"Content-Disposition": "inline; filename=speech.mp3"},
    )
