import json
import questionary

from pathlib import Path
from rich.console import Console
from rich.table import Table

console = Console()

TASKS_FILE = Path("tasks.json")

def load_tasks():
    try:
        with TASKS_FILE.open() as file:
            tasks = json.load(file)
            if isinstance(tasks, list):
                return [{"text": task, "done": False}
                if isinstance(task, str)
                else task
                for task in tasks
                if isinstance(task, (str, dict))]
    except FileNotFoundError:
        pass
    except json.JSONDecodeError:
        print("\nFile is invalid! Let's a new file!")
    return []

def save_tasks(tasks):
    with TASKS_FILE.open('w') as file:
        json.dump(tasks, file)

def show_tasks(tasks):
    if not tasks:
        console.print("\nList of tasks is empty!")
        return
    table = Table(title="\nList of your tasks")
    table.add_column("№")
    table.add_column("Tasks")
    table.add_column("Status")
    for number, task in enumerate(tasks, start=1):
        status = "☑" if task["done"] else "☐"
        table.add_row(str(number), task["text"], status)
    console.print(table)

def add_task(tasks):
    task = questionary.text("\nFill your task: ").ask()
    task = task.strip()
    if not task:
        console.print("\n[yellow]You can't add a empty task![/yellow]")
        return
    tasks.append({"text": task, "done": False})
    save_tasks(tasks)
    print("[green]Added task:[/green] ", task)

def switch_status(tasks):
    if not tasks:
        console.print("\nList of tasks is empty!")
        return
    show_tasks(tasks)
    try:
        number = int(input("\nFill task number for switching status: "))
    except ValueError:
        console.print("\nFill the task with number!")
        return
    if number < 1 or number > len(tasks):
        print("\nYou don't have task with that number!")
        return
    task = tasks[number - 1]
    task["done"] = not task["done"]
    save_tasks(tasks)
    console.print(f"Switched status for task: {task['text']}")


def delete_task(tasks):
    show_tasks(tasks)
    try:
        number = int(input("\nFill task number for deletion: "))
    except ValueError:
        print("\nFill the task with number")
        return
    if number < 1 or number > len(tasks):
        print("\nYou don't have task with that number!")
        return
    removed_task = tasks.pop(number - 1)
    save_tasks(tasks)
    print(f"Removed task: {removed_task}")

def quit_app():
    print("\nBuy! See you next time!")