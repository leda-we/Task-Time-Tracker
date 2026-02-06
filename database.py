import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "database.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_db():
    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute(
    """CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    status TEXT NOT NULL,
    created_at TEXT NOT NULL,
    deadline TEXT
    )
    """
        )

        cursor.execute(
    """CREATE TABLE IF NOT EXISTS time_entries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_id INTEGER NOT NULL,
    start_time TEXT,
    end_time TEXT,
    duration_minutes INTEGER,
    FOREIGN KEY (task_id) REFERENCES tasks(id)
    )
    """
        )