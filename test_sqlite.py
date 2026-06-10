from ai_agent.memory_db import (
    save_memory,
    get_memory
)

save_memory(
    "user",
    "My name is Ankit"
)

print(
    get_memory()
)