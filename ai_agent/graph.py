from langgraph.graph import StateGraph
from langgraph.graph import END

from ai_agent.state import AgentState

from ai_agent.nodes.intent_node import intent_node
from ai_agent.nodes.tool_node import tool_node
from ai_agent.nodes.response_node import response_node


builder = StateGraph(AgentState)

builder.add_node(
    "intent",
    intent_node
)

builder.add_node(
    "tool",
    tool_node
)

builder.add_node(
    "response",
    response_node
)


builder.set_entry_point(
    "intent"
)


def route_intent(state):

    return state["intent"]


builder.add_conditional_edges(
    "intent",
    route_intent,
    {
        "scheme": "tool",
        "eligibility": "tool",
        "recommendation": "tool",
        "grievance": "tool",
        "general": "response"
    }
)


builder.add_edge(
    "tool",
    "response"
)

builder.add_edge(
    "response",
    END
)

graph = builder.compile()