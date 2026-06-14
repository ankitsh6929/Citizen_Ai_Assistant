from ai_agent.tools.scheme_tool import (
    scheme_tool
)

def run(query):

    return scheme_tool.invoke(
        {"query": query}
    )