from fastapi import APIRouter, UploadFile, File
from ai_agent.citizen_assistant import process_voice
from fastapi import Form
router = APIRouter()

@router.post("/voice")
async def voice_chat(
    audio: UploadFile = File(...),
    language: str = Form("hi-IN")
):

    with open(
        "audio.wav",
        "wb"
    ) as buffer:

        buffer.write(
            await audio.read()
        )

    result = process_voice(
        "audio.wav",
        language
    )

    return result