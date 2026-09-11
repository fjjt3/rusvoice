from pydantic import BaseModel


class TTSRequest(BaseModel):
    text: str
    voice_key: str = "ru_female"
    rate: str = "+0%"
