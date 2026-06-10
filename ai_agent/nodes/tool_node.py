from ai_agent.state import AgentState

from ai_agent.tools.scheme_tool import scheme_tool
from ai_agent.tools.eligibility_tool import eligibility_tool
from ai_agent.tools.grievance_tool import grievance_tool


def tool_node(state: AgentState):

    query = state["query"]

    if state["intent"] == "scheme":

        result = scheme_tool.invoke(
            {"query": query}
        )

    elif state["intent"] == "eligibility":

        result = eligibility_tool.invoke(
            {"query": query}
        )

    elif state["intent"] == "grievance":

        result = grievance_tool.invoke(
            {"query": query}
        )

    else:

        result = """
I can help with:

• Government Schemes
• Eligibility Checks
• Grievance Registration
"""

    state["tool_result"] = result

    return state