from actions import show_tasks, add_task, delete_task, quit_app, load_tasks

def todo_app():
    tasks = load_tasks()

    while True:
        print("\n-=- What would you like to do? -=-")
        print("\n1 - show tasks")
        print("2 - add task")
        print("3 - delete task")
        print("q - quit")

        action = input("\nFill action or input q to quit: ")

        if action == "1":
            show_tasks(tasks)
        elif action == "2":
            add_task(tasks)
        elif action == "3":
            delete_task(tasks)
        elif action == "q":
            quit_app()
            break
        else:
            print("\nStop it!")

todo_app()


