import os

from dotenv import load_dotenv
from sarvamai import SarvamAI

load_dotenv()

client = SarvamAI(
    api_subscription_key=os.getenv("SARVAM_API_KEY")
)


def translate_text(
    text: str,
    source_lang: str = "auto",
    target_lang: str = "en-IN"
):

    response = client.text.translate(
        input=text,
        source_language_code=source_lang,
        target_language_code=target_lang,
        speaker_gender="Male"
    )

    return response.translated_text