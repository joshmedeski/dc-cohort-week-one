import data

def divider():
    print('- - - - - - - - - - - - - - - - - - - - - - - - -')

def show_menu():
    divider()
    print("Press '1' to add task")
    print("Press '2' to delete task")
    print("Press '3' to view all tasks")
    print("Press '4' to change priority of an existing task")
    print("Press 'q' to quit")

def show_tasks():
    print('All Tasks:')
    for index, task in enumerate(data.tasks):
        print(f'{index} - {task["description"]} - {task["priority"]}')

def select_task(action):
    show_tasks()
    return int(input(f"Choose the task by number to '{action}': "))