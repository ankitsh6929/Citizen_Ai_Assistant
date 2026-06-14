from langchain_core.tools import tool
from datetime import datetime
import random


@tool
def grievance_tool(query: str) -> str:
    """
    Register grievance.
    """

    query = query.lower()

    scheme = None

    if "pm kisan" in query:
        scheme = "PM Kisan"

    elif "pm awas" in query:
        scheme = "PM Awas Yojana"

    elif "ayushman" in query:
        scheme = "Ayushman Bharat"

    if not scheme:

        return """
Please provide the scheme name.

Examples:

• PM Kisan
• PM Awas Yojana
• Ayushman Bharat

Also describe your issue.
"""

    grievance_id = (
        f"GRV-{datetime.now().year}-"
        f"{random.randint(1000,9999)}"
    )

    return f"""
Grievance Registered Successfully

Scheme:
{scheme}

Issue:
{query}

Reference ID:
{grievance_id}

Please save this reference ID for future tracking.
"""