from __future__ import annotations

import sqlite3
from pathlib import Path
from typing import Any

DB_PATH = Path(__file__).resolve().parent.parent / "netpulse.db"


def get_connection() -> sqlite3.Connection:
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def init_db() -> None:
    with get_connection() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS diagnostics (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                summary TEXT NOT NULL,
                result TEXT NOT NULL
            )
            """
        )


def save_diagnostic(result: dict[str, Any]) -> None:
    init_db()
    with get_connection() as connection:
        connection.execute(
            "INSERT INTO diagnostics (summary, result) VALUES (?, ?)",
            (result.get("summary", "Network diagnosis"), str(result)),
        )


def get_recent_diagnostics(limit: int = 10) -> list[dict[str, Any]]:
    init_db()
    with get_connection() as connection:
        rows = connection.execute(
            "SELECT * FROM diagnostics ORDER BY id DESC LIMIT ?",
            (limit,),
        ).fetchall()
    return [dict(row) for row in rows]
