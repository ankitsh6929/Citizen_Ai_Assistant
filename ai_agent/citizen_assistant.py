from ai_agent.graph import graph
from ai_agent.rag_search import search_rag

from backend.services.sarvam_stt import speech_to_text
from backend.services.sarvam_translate import translate_text
from backend.services.sarvam_tts import text_to_speech
from backend.services.language_detector import detect_language

from ai_agent.profile_extractor import (
    extract_profile
)




from ai_agent.language import (
    get_requested_language
)

from ai_agent.memory_db import (
    save_memory,
    get_memory
)







def process_query(
    query: str,
    session_id: str
):

    extract_profile(query, session_id)

    memory = get_memory(
        session_id
    )

    # --------------------------------
    # TRANSLATE PREVIOUS RESPONSE
    # --------------------------------

    requested_language = (
        get_requested_language(query)
    )

    if requested_language:

        print("=" * 50)
        print("TRANSLATION REQUEST DETECTED")
        print(
            "TARGET LANGUAGE:",
            requested_language
        )
        print("=" * 50)

        last_assistant_response = ""

        for role, msg in reversed(memory):

            if role == "assistant":

                last_assistant_response = msg

                print(
                    "FOUND ASSISTANT RESPONSE:"
                )
                print(msg)

                break

        if last_assistant_response:

            translated_response = translate_text(
                last_assistant_response,
                target_lang=requested_language
            )

            save_memory(
                session_id,
                "user",
                query
            )

            save_memory(
                session_id,
                "assistant",
                translated_response
            )

            return translated_response

    # --------------------------------
    # NORMAL CHAT FLOW
    # --------------------------------

    save_memory(
        session_id,
        "user",
        query
    )

    memory = get_memory(
        session_id
    )

    rag_context = search_rag(
        query
    )

    result = graph.invoke(
        {
            "query": query,
            "session_id": session_id,
            "memory": memory,
            "rag_context": rag_context
        }
    )

    response = result["response"]

    save_memory(
        session_id,
        "assistant",
        response
    )

    return response






def process_voice(
    audio_path,
    language="hi-IN"
):

    # --------------------------------
    # STT
    # --------------------------------

    user_text = speech_to_text(
        audio_path
    )

    print("User Text:", user_text)

    detected_language = detect_language(
        user_text
    )

    print("=" * 50)
    print(
        "Detected LANGUAGE:",
        detected_language
    )
    print("=" * 50)

    # --------------------------------
    # TRANSLATION REQUEST DETECTION
    # --------------------------------

    memory = get_memory()

    requested_language = (
        get_requested_language(
            user_text
        )
    )

    if requested_language:

        last_assistant_response = ""

        for role, msg in reversed(memory):

            if role == "assistant":

                last_assistant_response = msg
                break

        if last_assistant_response:

            translated_response = translate_text(
                last_assistant_response,
                target_lang=requested_language
            )

            audio_file = text_to_speech(
                translated_response
            )

            save_memory(
                CURRENT_SESSION,
                "user",
                user_text
            )

            save_memory(
                CURRENT_SESSION,
                "assistant",
                translated_response
            )

            return {
                "user_text": user_text,
                "audio_file": audio_file,
                "response_text": translated_response
            }

    # --------------------------------
    # NORMAL VOICE FLOW
    # --------------------------------

    if detected_language != "en-IN":

        english_text = translate_text(
            user_text,
            target_lang="en-IN"
        )

    else:

        english_text = user_text

    print("English:", english_text)

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

    if detected_language != "en-IN":

        translated_response = translate_text(
            response_text[:900],
            target_lang=detected_language
        )

    else:

        translated_response = response_text

    audio_file = text_to_speech(
        translated_response
    )

    save_memory(
        CURRENT_SESSION,
        "user",
        user_text
    )

    save_memory(
        CURRENT_SESSION,
        "assistant",
        translated_response
    )

    print(
        "Audio Saved:",
        audio_file
    )

    return {
        "user_text": user_text,
        "audio_file": audio_file,
        "response_text": translated_response
    }