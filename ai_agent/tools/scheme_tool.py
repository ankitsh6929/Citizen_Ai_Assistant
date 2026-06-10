from langchain_core.tools import tool


@tool
def scheme_tool(query: str) -> str:
    """
    Search government schemes.
    """

    query = query.lower()

    if "pm kisan" in query:
        return """
PM Kisan Scheme:

• ₹6000 annual financial support
• For eligible farmers
• Paid in 3 installments
"""

    elif "pm awas" in query:
        return """
PM Awas Yojana:

• Housing assistance
• Support for economically weaker families
"""

    elif "ayushman" in query:
        return """
Ayushman Bharat:

• Health insurance coverage
• Cashless treatment
"""

    return "No matching government scheme found."