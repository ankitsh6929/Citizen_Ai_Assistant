from ai_agent.memory import (
    save_user_data,
    get_user_data
)

save_user_data(
    "name",
    "Ankit"
)

print(
    get_user_data("name")
)