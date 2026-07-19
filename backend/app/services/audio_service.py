from io import BytesIO
import tempfile
import os

from gtts import gTTS

# Global Whisper model cache
_model = None


def get_whisper_model():
    """
    Lazily loads the Whisper model only on first use.
    """
    global _model

    if _model is None:
        import whisper

        print("Loading Whisper model...")
        _model = whisper.load_model("base")
        print("✓ Whisper model loaded")

    return _model


def speech_to_text(audio_file):

    model = get_whisper_model()

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
        lang="en",
    )

    tts.write_to_fp(audio)

    audio.seek(0)

    return audio