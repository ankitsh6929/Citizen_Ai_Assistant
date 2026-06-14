from ai_agent.agents.scheme_agent import run as scheme_agent

from ai_agent.agents.eligibility_agent import (
    run as eligibility_agent
)

from ai_agent.agents.recommendation_agent import (
    run as recommendation_agent
)

from ai_agent.agents.grievance_agent import (
    run as grievance_agent
)


def route(
    intent,
    query,
    session_id
):

    if intent == "scheme":

        return scheme_agent(
            query
        )

    elif intent == "eligibility":

        return eligibility_agent(
            query,
            session_id
        )

    elif intent == "recommendation":

        return recommendation_agent(
            query,
            session_id
        )

    elif intent == "grievance":

        return grievance_agent(
            query
        )

    return """
I can help with:

• Government Schemes
• Eligibility Checks
• Recommendations
• Grievances
"""