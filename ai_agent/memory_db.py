import sqlite3


def get_connection():

    return sqlite3.connect(
        "citizen.db",
        check_same_thread=False
    )


conn = get_connection()

conn.execute("""
CREATE TABLE IF NOT EXISTS memory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id TEXT,
    role TEXT,
    message TEXT
)
""")

conn.commit()
conn.close()


def save_memory(
    session_id,
    role,
    message
):

    conn = get_connection()

    conn.execute(
        """
        INSERT INTO memory
        (
            session_id,
            role,
            message
        )
        VALUES (?, ?, ?)
        """,
        (
            session_id,
            role,
            message
        )
    )

    conn.commit()
    conn.close()


def get_memory(
    session_id
):

    conn = get_connection()

    rows = conn.execute(
        """
        SELECT
        role,
        message
        FROM memory
        WHERE session_id = ?
        ORDER BY id DESC
        LIMIT 20
        """,
        (
            session_id,
        )
    ).fetchall()

    conn.close()

    return rows[::-1]