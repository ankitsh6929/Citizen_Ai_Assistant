from langdetect import detect


def detect_text_language(text):

    try:

        lang = detect(text)

        mapping = {
            "en": "English",
            "hi": "Hindi",
            "bn": "Bengali",
            "as": "Assamese",
            "ta": "Tamil",
            "te": "Telugu"
        }

        return mapping.get(
            lang,
            "English"
        )

    except:

        return "English"


def get_requested_language(query):

    query = query.lower()

    mappings = {
        "tamil": "ta-IN",
        "hindi": "hi-IN",
        "bengali": "bn-IN",
        "assamese": "as-IN",
        "telugu": "te-IN",
        "english": "en-IN"
    }

    translation_keywords = [
        "above",
        "previous",
        "translate",
        "repeat"
    ]

    if any(
        word in query
        for word in translation_keywords
    ):

        for lang, code in mappings.items():

            if lang in query:

                return code

    return None