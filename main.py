import questionary
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from db.database import init_db
from services.task_service import (
    create_task,
    get_all_tasks,
    update_task_status,
    del_task,
    
)
from services.time_service import (
    add_time_entry,
    get_time_report,
)

console = Console()

def show_header():
    console.print(
        Panel.fit(
            "[bold cyan]Task & Time Tracker[/]\n"
            "[dim]CLI-приложение для учёта задач и времени[/]",
            border_style="cyan",
        )
    )

def main_menu():
    return questionary.select(
        "Выберите действие:",
        choices=[
            "➕ Создать задачу",
            "📋 Показать задачи",
            "🔄 Изменить статус задачи",
            "⏱ Добавить время к задаче",
            "📊 Показать отчёт",
            "Удалить задачу"
            "❌ Выход",
        ],
    ).unsafe_ask()


def show_tasks():
    tasks = get_all_tasks()

    if not tasks:
        console.print("[yellow]Задач пока нет[/]")
        return
    
    table = Table(title="Список задач")
    table.add_column("ID", justify="right")
    table.add_column("Название")
    table.add_column("Статус")
    table.add_column("Описание")
    table.add_column("Дедлайн")

    for task in tasks:
        color = {
            "new": "yellow",
            "in_progress": "cyan",
            "done": "green",
        }.get(task.status, "white")

        table.add_row(
            str(task.id),
            task.title,
            f"[{color}]{task.status}[/]",
            task.description,
            task.deadline,
        )

        console.print(table)

def create_task_ui():
    title = questionary.text("Название задачи:").ask()
    description = questionary.text("Описание:").ask()
    deadline = questionary.text(
        "Дедлайн (опционально):"
    ).ask()

    create_task(title, description, deadline or None)
    console.print("[green]Задача создана[/]")

def update_status_ui():
    task_id = questionary.text("ID задачи:").ask()
    status = questionary.select(
        "Новый статус:",
        choices=["new", "in_progress", "done"],
    ).ask()

    update_task_status(int(task_id), status)
    console.print("[green]Статус обновлён[/]")

def add_time_ui():
    task_id = questionary.text("ID задачи:").ask()
    minutes = questionary.text("Сколько минут потрачено:").ask()

    add_time_entry(int(task_id), int(minutes))
    console.print("[green]Время добавлено[/]")

def show_report():
    report = get_time_report()
    if not report:
        console.print("[yellow]Нет данных по времени[/]")
        return
    
    table = Table(title="Отчёт по времени")

    table.add_column("Задача")
    table.add_column("Минуты", justify="right")

    for title, minutes in report:
        table.add_row(title, str(minutes))

    console.print(table)


def delete_task_ui():
    task_id = questionary.text("ID задачи, которую вы хотите удалить?").ask()
    del_task(int(task_id))

def main():
    init_db()
    show_header()

    while True:
        choice = main_menu()

        if choice.startswith("➕"):
            create_task_ui()

        elif choice.startswith("📋"):
            show_tasks()

        elif choice.startswith("🔄"):
            update_status_ui()

        elif choice.startswith("⏱"):
            add_time_ui()

        elif choice.startswith("📊"):
            show_report()

        elif choice.startswith("❌"):
            console.print("[cyan]До свидания![/]")
            break

if __name__ == "__main__":
    main()