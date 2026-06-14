import re

from ai_agent.profile_memory import (
    save_profile,
    get_profile
)


def extract_profile(
    query,
    session_id
):

    q = query.lower()

    # -------------------------
    # AGE
    # -------------------------

    age_patterns = [

        r'age\s*(?:is)?\s*(\d+)',

        r'i am\s*(\d+)',

        r'i am\s*(\d+)\s*years',

        r'(\d+)\s*years old'
    ]

    for pattern in age_patterns:

        match = re.search(
            pattern,
            q
        )

        if match:

            save_profile(
                session_id,
                "age",
                match.group(1)
            )

            break

    # -------------------------
    # INCOME
    # -------------------------

    income_patterns = [

        r'annual income\s*(?:is|=)?\s*([\d,]+)',

        r'my income\s*(?:is|=)?\s*([\d,]+)',

        r'income\s*(?:is|=)?\s*([\d,]+)',

        r'i earn\s*([\d,]+)'
    ]

    for pattern in income_patterns:

        match = re.search(
            pattern,
            q
        )

        if match:

            income = (
                match.group(1)
                .replace(",", "")
            )

            save_profile(
                session_id,
                "income",
                income
            )

            break

    # -------------------------
    # NAME
    # -------------------------

    name_patterns = [

        r'my name is\s+([a-z]+)'
    ]

    for pattern in name_patterns:

        match = re.search(
            pattern,
            q
        )

        if match:

            save_profile(
                session_id,
                "name",
                match.group(1).title()
            )

            break

    # -------------------------
    # OCCUPATION
    # -------------------------

    if (
        "farmer" in q
        or "agriculture" in q
        or "agricultural worker" in q
    ):

        save_profile(
            session_id,
            "occupation",
            "farmer"
        )

    # -------------------------
    # LAND OWNERSHIP
    # -------------------------

    land_keywords = [

        "own land",
        "owns land",
        "have land",
        "agricultural land",
        "cultivable land",
        "farmland"
    ]

    if any(
        keyword in q
        for keyword in land_keywords
    ):

        save_profile(
            session_id,
            "land_owner",
            "yes"
        )

    print("=" * 50)
    print("PROFILE EXTRACTION COMPLETE")
    print(
        get_profile(session_id)
    )
    print("=" * 50)