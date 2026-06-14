from ai_agent.state import AgentState

from backend.services.sarvam_chat import generate_response

from ai_agent.language import (
    get_requested_language
)


from ai_agent.profile_memory import (
    get_profile
)

def response_node(state: AgentState):

    # ==================================
    # TOOL ALREADY GENERATED FINAL ANSWER
    # ==================================


    profile = get_profile(
        state["session_id"]
    )

    if state.get("final_answer"):

        state["response"] = state["tool_result"]

        return state

    # ==================================
    # NORMAL LLM FLOW
    # ==================================

    memory = state.get(
        "memory",
        []
    )

    memory_text = "\n".join(
        [
            f"{role}: {message}"
            for role, message in memory[-20:]
        ]
    )

    requested_language = (
        get_requested_language(
            state["query"]
        )
    )

    last_assistant_response = ""

    for role, msg in reversed(memory):

        if role == "assistant":

            last_assistant_response = msg
            break

    prompt = f"""
    You are a multilingual AI Citizen Service Assistant.

    ==================================
    LANGUAGE RULES
    ==================================

    1. If the user explicitly requests:
       - in Tamil
       - in Hindi
       - in Bengali
       - in Assamese
       - in Telugu

       ALWAYS respond in that language.

    2. Otherwise detect language ONLY from
       CURRENT USER QUERY.

    3. Ignore language used in memory.

    4. Ignore language used in previous
       assistant responses.

    5. Reply ONLY in the chosen language.

    Requested Language:
    {requested_language}

    ==================================
    MEMORY RULES
    ==================================

    Use memory ONLY for facts.

    Example:

    User:
    My name is Rahul

    Later:
    What is my name?

    Assistant:
    Your name is Rahul.

    If user later says:

    My name is John

    then John becomes the latest name.

    ==================================
    REFERENCE RULES
    ==================================

    If the user says:

    - tell me above
    - explain above
    - translate above
    - tell me again
    - tell me in Tamil
    - tell me in Hindi
    - tell me in Bengali
    - tell me in Assamese
    - tell me in Telugu

    then use Latest Assistant Response.

    Latest Assistant Response:

    {last_assistant_response}


    ==================================
    PROFILE MEMORY
    ==================================

    {profile}

    ==================================
    PROFILE RULES
    ==================================

    If profile contains:

    name

    and user asks:

    - what is my name
    - tell my name
    - do you know my name

    then answer using profile memory.

    ==================================
    CURRENT USER QUERY
    ==================================

    {state['query']}

    ==================================
    KNOWLEDGE BASE
    ==================================

    {state.get('rag_context', '')}

    ==================================
    TOOL RESULT
    ==================================

    {state.get('tool_result', '')}

    ==================================
    RESPONSE PRIORITY
    ==================================

    1. Reference Requests

    2. Current User Query

    3. RAG Context

    4. Tool Result

    5. Memory

    ==================================
    IMPORTANT
    ==================================

    - Use RAG context for scheme information.
    - Do not invent scheme information.
    - Use memory only when needed.
    - If user asks to translate previous answer,
      use Latest Assistant Response.
    - Follow Requested Language if provided.
    - Otherwise answer in the language of the
      Current User Query.

    Provide a helpful response.
    """

    try:

        print("=" * 50)
        print("CURRENT QUERY:")
        print(state["query"])
        print("=" * 50)

        print("REQUESTED LANGUAGE:")
        print(requested_language)

        print("=" * 50)
        print("LAST ASSISTANT RESPONSE:")
        print(last_assistant_response)
        print("=" * 50)

        response = generate_response(
            prompt
        )

        state["response"] = response

    except Exception as e:

        state["response"] = (
            f"Sarvam Error: {str(e)}"
        )

    return state