# ai_agent/memory_db.py

import sqlite3

conn = sqlite3.connect(
    "citizen.db",
    check_same_thread=False
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS memory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    role TEXT,
    message TEXT
)
""")

conn.commit()


def save_memory(role, message):

    cursor.execute(
        """
        INSERT INTO memory (
            role,
            message
        )
        VALUES (?, ?)
        """,
        (role, message)
    )

    conn.commit()


def get_memory():

    cursor.execute(
        """
        SELECT role, message
        FROM memory
        ORDER BY id DESC
        LIMIT 20
        """
    )

    rows = cursor.fetchall()

    return rows[::-1]