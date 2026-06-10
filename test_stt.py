from backend.services.sarvam_stt import speech_to_text

text = speech_to_text("audio.wav")

print(type(text))
print(text)