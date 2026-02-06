from datetime import datetime
from db.database import get_connection

def add_time_entry(task_id: int, minutes: int):
    now = datetime.now().isoformat()

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
    """
    INSERT INTO time_entries (task_id, start_time, end_time, duration_minutes)
    VALUES (?, ?, ?, ?)
    """,
    (task_id, now, now, minutes)
        )

def get_time_report():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
    """
    SELECT t.title, SUM(te.duration_minutes)
    FROM tasks t
    JOIN time_entries te ON t.id = te.task_id
    GROUP BY t.id
    """
        )
        return cursor.fetchall()