import json
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
                return tasks
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
    for number, task in enumerate(tasks, start=1):
        table.add_row(str(number), task)
    console.print(table)

def add_task(tasks):
    task = input("\nFill your task: ").strip()
    if not task:
        print("\nYou can't add a empty task!")
        return
    tasks.append(task)
    save_tasks(tasks)
    print("Added task: ", task)

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