from io import BytesIO
import tempfile
import os

import whisper
from gtts import gTTS

# Load Whisper once
model = whisper.load_model("base")


def speech_to_text(audio_file):

    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp:

        temp.write(audio_file.read())
        temp_path = temp.name

    result = model.transcribe(temp_path)

    os.remove(temp_path)

    return result["text"]


def text_to_speech(text: str):

    audio = BytesIO()

    tts = gTTS(
        text=text,
        lang="en"
    )

    tts.write_to_fp(audio)

    audio.seek(0)

    return audio