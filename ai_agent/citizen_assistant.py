from ai_agent.graph import graph
from ai_agent.rag_search import search_rag
from backend.services.sarvam_stt import speech_to_text
from backend.services.sarvam_translate import translate_text
from backend.services.sarvam_tts import text_to_speech


from ai_agent.memory_db import (
    save_memory,
    get_memory
)

def process_query(query: str):

    save_memory(
        "user",
        query
    )

    memory = get_memory()

    rag_context = search_rag(
        query
    )

    result = graph.invoke(
        {
            "query": query,
            "memory": memory,
            "rag_context": rag_context
        }
    )

    response = result["response"]

    save_memory(
        "assistant",
        response
    )

    return response

def process_voice(
    audio_path,
    language="hi-IN"
):

    # STT

    user_text = speech_to_text(audio_path)

    print("User Text:", user_text)

    # Translation

    english_text = translate_text(
        user_text,
        target_lang="en-IN"
    )

    print("English:", english_text)

    # Agent





    memory = get_memory()

    rag_context = search_rag(
        english_text
    )

    result = graph.invoke(
        {
            "query": english_text,
            "memory": memory,
            "rag_context": rag_context
        }
    )







    response_text = result["response"]

    print("Agent:", response_text)

    # Hindi Translation

    translated_response = translate_text(
    response_text[:900],
    target_lang=language
)

    print("Translated:", translated_response)

    audio_file = text_to_speech(
    translated_response
)

    print("Audio Saved:", audio_file)

    return {
    "audio_file": audio_file,
    "response_text": translated_response
}