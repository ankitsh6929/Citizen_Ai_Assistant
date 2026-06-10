from ai_agent.state import AgentState


def intent_node(state: AgentState):

    query = state["query"].lower()

    if "scheme" in query:
        state["intent"] = "scheme"

    elif "eligible" in query:
        state["intent"] = "eligibility"

    elif "grievance" in query:
        state["intent"] = "grievance"

    elif "complaint" in query:
        state["intent"] = "grievance"

    elif "pm kisan" in query:
        state["intent"] = "scheme"

    elif "pm awas" in query:
        state["intent"] = "scheme"

    elif "ayushman" in query:
        state["intent"] = "scheme"

    else:
        state["intent"] = "general"

    return state