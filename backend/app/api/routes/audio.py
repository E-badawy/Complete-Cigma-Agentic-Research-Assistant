from fastapi import APIRouter, UploadFile, File
from fastapi.responses import StreamingResponse

router = APIRouter(
    prefix="/audio",
    tags=["Audio"]
)


@router.post("/transcribe")
async def transcribe_audio(
    file: UploadFile = File(...)
):
    from app.services.audio_service import speech_to_text

    text = speech_to_text(file.file)

    return {
        "transcript": text
    }


@router.post("/tts")
def generate_audio(
    text: str
):
    from app.services.audio_service import text_to_speech

    audio = text_to_speech(text)

    return StreamingResponse(
        audio,
        media_type="audio/mpeg",
        headers={
            "Content-Disposition":
            'attachment; filename="speech.mp3"'
        }
    )