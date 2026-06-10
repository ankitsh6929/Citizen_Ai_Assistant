memory = []

def save_memory(role, message):
    memory.append(
        {
            "role": role,
            "message": message
        }
    )

def get_memory():
    return memory