from ai_agent.state import AgentState

from backend.services.sarvam_chat import generate_response


def response_node(state: AgentState):

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

    prompt = f"""
    You are an AI Citizen Service Assistant.

    Previous Conversation Memory:
    {memory_text}

    Current User Query:
    {state['query']}

    Relevant Knowledge Base Context:
    {state.get('rag_context', '')}

    Tool Result:
    {state.get('tool_result', '')}

    Use previous conversation memory when relevant.

    Example:
    If the user previously said:
    "My name is Ankit"

    and later asks:
    "What is my name?"

    then answer:
    "Your name is Ankit."

    Provide a helpful response.
    """

    try:

        response = generate_response(
            prompt
        )

        state["response"] = response

    except Exception as e:

        state["response"] = (
            f"Sarvam Error: {str(e)}"
        )

    return state