import sqlite3
import uuid


def get_connection():

    return sqlite3.connect(
        "citizen.db",
        check_same_thread=False
    )


conn = get_connection()

conn.execute("""
CREATE TABLE IF NOT EXISTS sessions (
    session_id TEXT PRIMARY KEY,
    title TEXT
)
""")

conn.commit()


def create_session():

    session_id = str(
        uuid.uuid4()
    )

    count = conn.execute(
        """
        SELECT COUNT(*)
        FROM sessions
        """
    ).fetchone()[0]

    title = f"Chat {count + 1}"

    conn.execute(
        """
        INSERT INTO sessions
        (
            session_id,
            title
        )
        VALUES (?, ?)
        """,
        (
            session_id,
            title
        )
    )

    conn.commit()

    return session_id


def get_sessions():

    rows = conn.execute(
        """
        SELECT
            session_id,
            title
        FROM sessions
        ORDER BY rowid DESC
        """
    ).fetchall()

    return [
        {
            "session_id": row[0],
            "title": row[1]
        }
        for row in rows
    ]



def get_chat_history(session_id):

    conn = get_connection()

    rows = conn.execute(
        """
        SELECT
            role,
            message
        FROM memory
        WHERE session_id = ?
        ORDER BY id ASC
        """,
        (
            session_id,
        )
    ).fetchall()

    conn.close()

    return [
        {
            "role": row[0],
            "text": row[1]
        }
        for row in rows
    ]