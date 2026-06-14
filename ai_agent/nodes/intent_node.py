from ai_agent.state import AgentState


def intent_node(state: AgentState):

    query = state["query"].lower()

    # -------------------------
    # RECOMMENDATION
    # -------------------------

    if any(
        phrase in query
        for phrase in [
            "recommend",
            "recommended",
            "suggest scheme",
            "which scheme",
            "which schemes",
            "best scheme",
            "government schemes for me",
            "recommend schemes",
            "suggest schemes"
        ]
    ):

        state["intent"] = "recommendation"

    # -------------------------
    # ELIGIBILITY
    # -------------------------

    elif any(
        word in query
        for word in [
            "eligible",
            "eligibility",
            "age",
            "income",
            "occupation",
            "farmer",
            "land",
            "state"
        ]
    ):

        state["intent"] = "eligibility"

    # -------------------------
    # GRIEVANCE
    # -------------------------

    elif any(
        word in query
        for word in [
            "grievance",
            "complaint",
            "issue",
            "problem",
            "not received"
        ]
    ):

        state["intent"] = "grievance"

    # -------------------------
    # SCHEME
    # -------------------------

    elif any(
        word in query
        for word in [
            "scheme",
            "pm kisan",
            "pm awas",
            "ayushman",
            "fasal bima",
            "kisan credit card"
        ]
    ):

        state["intent"] = "scheme"

    # -------------------------
    # GENERAL
    # -------------------------

    else:

        state["intent"] = "general"

    print("=" * 50)
    print("INTENT:", state["intent"])
    print("QUERY :", state["query"])
    print("=" * 50)

    return state