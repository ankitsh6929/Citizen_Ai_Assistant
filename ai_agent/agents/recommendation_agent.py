from ai_agent.tools.recommendation_tool import (
    recommendation_tool
)

def run(query,session_id):

    return recommendation_tool.invoke(
        {"query": query,
        "session_id": session_id
        }
    )