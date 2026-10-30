import json

try:
    with open("tasks.json") as file:
        tasks = json.load(file)
except (FileNotFoundError, json.decoder.JSONDecodeError):
    tasks = []

def show_tasks(tasks):
    if not tasks:
        print("\nList of tasks is empty")
        return

    for number, task in enumerate(tasks, start=1):
        print(number, task)

while True:

    print("\n1 - show tasks")
    print("2 - add task")
    print("3 - delete task")
    print("q - quit")

    action = input("\nFill action or input q to quit: ")

    if action == "1":
        show_tasks(tasks)
    elif action == "2":
        task = input("\nFill your task: ")
        tasks.append(task)
        print("Added task: ", task)
    elif action == "3":
        try:
            number = int(input("\nFill task number: "))
            tasks.pop(number - 1)
        except ValueError:
            print("\nFill the task with number")
    elif action == "q":
        break
    else:
        print("\nStop it!")




