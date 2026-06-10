import os
import base64
from dotenv import load_dotenv
from sarvamai import SarvamAI

load_dotenv()

client = SarvamAI(
    api_subscription_key=os.getenv("SARVAM_API_KEY")
)


def text_to_speech(text):

    response = client.text_to_speech.convert(
        model="bulbul:v3",
        text=text,
        target_language_code="hi-IN",
        speaker="shubh"
    )

    # Get Base64 audio
    audio_base64 = response.audios[0]

    # Decode
    audio_bytes = base64.b64decode(audio_base64)

    # Save WAV
    with open("response.wav", "wb") as f:
        f.write(audio_bytes)

    return "response.wav"