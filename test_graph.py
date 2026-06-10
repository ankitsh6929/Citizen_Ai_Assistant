from ai_agent.graph import graph

result = graph.invoke(
    {
        "query": "Tell me about PM Kisan Scheme"
    }
)

print("\n")
print(result["response"])
print("\n")