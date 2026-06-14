from ai_agent.tools.eligibility_tool import (
    eligibility_tool
)

def run(
    query,
    session_id
):

    return eligibility_tool.invoke(
        {
            "query": query,
            "session_id": session_id
        }
    )