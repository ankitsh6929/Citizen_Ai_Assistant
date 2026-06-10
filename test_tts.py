from backend.services.sarvam_tts import text_to_speech

result = text_to_speech(
    "नमस्ते, मैं आपका नागरिक सहायक हूँ।"
)

print(result)