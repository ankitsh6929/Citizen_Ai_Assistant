from langchain_core.tools import tool


@tool
def eligibility_tool(query: str) -> str:
    """
    Check eligibility.
    """

    return """
Eligibility Check:

Please provide:

1. Age
2. State
3. Occupation
4. Annual Income

Then I can determine eligibility.
"""