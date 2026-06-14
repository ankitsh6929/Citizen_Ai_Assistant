from ai_agent.state import AgentState

from ai_agent.agents.router_agent import (
    route
)


def tool_node(state: AgentState):

    result = route(
        state["intent"],
        state["query"],
        state["session_id"]
    )

    state["tool_result"] = result

    return state