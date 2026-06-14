import sqlite3

conn = sqlite3.connect(
    "citizen.db",
    check_same_thread=False
)

conn.execute("""
CREATE TABLE IF NOT EXISTS profile (
    session_id TEXT,
    key TEXT,
    value TEXT,
    PRIMARY KEY (session_id, key)
)
""")

conn.commit()


def save_profile(
    session_id,
    key,
    value
):

    conn.execute(
        """
        INSERT OR REPLACE INTO profile
        (
            session_id,
            key,
            value
        )
        VALUES (?, ?, ?)
        """,
        (
            session_id,
            key,
            str(value)
        )
    )

    conn.commit()

    print("=" * 50)
    print("PROFILE SAVED")
    print(session_id)
    print(f"{key} = {value}")
    print("=" * 50)


def get_profile(
    session_id
):

    rows = conn.execute(
        """
        SELECT
        key,
        value
        FROM profile
        WHERE session_id = ?
        """,
        (
            session_id,
        )
    ).fetchall()

    profile = {
        key: value
        for key, value in rows
    }

    print("=" * 50)
    print("CURRENT PROFILE")
    print(profile)
    print("=" * 50)

    return profile


def clear_profile(
    session_id
):

    conn.execute(
        """
        DELETE FROM profile
        WHERE session_id = ?
        """,
        (
            session_id,
        )
    )

    conn.commit()

    print("=" * 50)
    print("PROFILE CLEARED")
    print(session_id)
    print("=" * 50)