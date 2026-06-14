from typing import TypedDict


class AgentState(TypedDict):

    query: str

    session_id: str

    intent: str

    tool_result: str

    response: str

    memory: list

    rag_context: str

    final_answer: bool