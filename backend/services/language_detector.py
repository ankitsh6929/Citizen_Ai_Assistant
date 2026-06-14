def detect_language(text: str):

    text = text.strip()

    if any('\u0900' <= ch <= '\u097F' for ch in text):
        return "hi-IN"

    return "en-IN"