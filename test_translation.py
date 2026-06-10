from backend.services.sarvam_translate import translate_text

result = translate_text(
    "नमस्ते",
    target_lang="en-IN"
)

print(result)