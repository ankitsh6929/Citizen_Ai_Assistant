from langchain_core.tools import tool


@tool
def grievance_tool(query: str) -> str:
    """
    Register grievance.
    """

    return """
Your grievance has been recorded.

Reference ID:
GRV-2026-001
"""