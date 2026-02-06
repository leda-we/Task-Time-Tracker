from datetime import datetime
from db.database import get_connection
from model.task import Task

def create_task(title: str, description: str, deadline: str | None):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
    """
    INSERT INTO tasks (title, description, status, created_at, deadline)
    VALUES (?, ?, ?, ?, ?)
    """,
    (
        title,
        description,
        "new",
        datetime.now().isoformat(),
        deadline,
    )
        )

def get_all_tasks() -> list[Task]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tasks")
        rows = cursor.fetchall()

    return [
        Task(
            id=row[0],
            title=row[1],
            description=row[2],
            status=row[3],
            created_at=row[4],
            deadline=row[5],
        )
        for row in rows
    ]

def update_task_status(task_id: int, status: str):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE tasks SET status = ? WHERE id = ?",
            (status, task_id)
        )

def del_task(task_id: int):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM employess WHERE id = ?")