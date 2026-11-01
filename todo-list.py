import questionary

from actions import show_tasks, add_task, delete_task, quit_app, load_tasks, switch_status

def todo_app():
    tasks = load_tasks()

    while True:
        action = questionary.select(
            "What would you like to do?",
            choices=["Show tasks", "Add task", "Switch status", "Delete task", "Quit"],
        ).ask()

        if action == "Show tasks":
            show_tasks(tasks)
        elif action == "Add task":
            add_task(tasks)
        elif action == "Switch status":
            switch_status(tasks)
        elif action == "Delete task":
            delete_task(tasks)
        elif action == "Quit":
            quit_app()
            break
        elif action is None:
            break

todo_app()