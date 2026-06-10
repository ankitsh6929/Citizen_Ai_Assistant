from typing import TypedDict


class AgentState(TypedDict):

    query: str

    intent: str

    tool_result: str

    response: str

    memory: list

    rag_context: str