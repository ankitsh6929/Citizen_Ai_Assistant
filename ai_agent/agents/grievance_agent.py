from ai_agent.tools.grievance_tool import (
    grievance_tool
)

def run(query):

    return grievance_tool.invoke(
        {"query": query}
    )