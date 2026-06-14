from langchain_core.tools import tool

from ai_agent.profile_memory import (
    get_profile
)


@tool
def recommendation_tool(
    query: str,
    session_id: str
) -> str:
    """
    Recommend government schemes
    based on user profile.
    """

    profile = get_profile(
        session_id
    )

    age = int(
        profile.get("age", 0)
    )

    income = int(
        profile.get("income", 0)
    )

    occupation = profile.get(
        "occupation",
        ""
    ).lower()

    land_owner = profile.get(
        "land_owner",
        "no"
    ).lower()

    recommendations = []

    if (
        occupation == "farmer"
        and land_owner == "yes"
    ):

        recommendations.append(
            "PM Kisan Samman Nidhi"
        )

        recommendations.append(
            "PM Fasal Bima Yojana"
        )

        recommendations.append(
            "Kisan Credit Card"
        )

    if income < 500000:

        recommendations.append(
            "Ayushman Bharat"
        )

    if income < 1800000:

        recommendations.append(
            "PM Awas Yojana"
        )

    if age > 0 and age <= 25:

        recommendations.append(
            "National Scholarship Portal Schemes"
        )

    if not recommendations:

        return """
I need more profile information
before recommending schemes.

Please provide:

• Age
• Occupation
• Annual Income
• Land Ownership
"""

    result = (
        "Based on your profile, "
        "you may be eligible for:\n\n"
    )

    for scheme in recommendations:

        result += f"• {scheme}\n"

    return result