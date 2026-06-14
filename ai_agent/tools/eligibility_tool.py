from langchain_core.tools import tool

from ai_agent.profile_memory import (
    get_profile
)


@tool
def eligibility_tool(query: str,
session_id: str
) -> str:
    """
    Check PM Kisan eligibility using stored profile.
    """

    profile = get_profile(session_id)

    print("=" * 50)
    print("PROFILE DATA")
    print(profile)
    print("=" * 50)

    age = profile.get("age")
    income = profile.get("income")
    occupation = profile.get("occupation")
    land_owner = profile.get("land_owner")

    missing = []

    if not age:
        missing.append("Age")

    if not income:
        missing.append("Annual Income")

    if not occupation:
        missing.append("Occupation")

    if not land_owner:
        missing.append("Land Ownership")
    print("AGE:", age)
    print("INCOME:", income)
    print("OCCUPATION:", occupation)
    print("LAND OWNER:", land_owner)
    
    if missing:

        return (
            "I need the following information:\n\n- "
            + "\n- ".join(missing)
        )

    if occupation.lower() != "farmer":

        return """
Not Eligible for PM Kisan.

Reason:
Applicant must be a farmer.
"""

    if land_owner.lower() != "yes":

        return """
Not Eligible for PM Kisan.

Reason:
Applicant must own cultivable land.
"""

    return f"""
Eligible for PM Kisan Scheme.

Citizen Profile:

✓ Age: {age}
✓ Income: {income}
✓ Occupation: {occupation}
✓ Land Owner: {land_owner}

Eligibility Result:

✓ Applicant is a farmer
✓ Applicant owns cultivable land

You appear eligible for PM Kisan Scheme.
"""