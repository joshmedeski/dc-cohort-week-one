import data
import view

is_running = True

while is_running:
    view.show_menu()
    user_input = input('Choose an option: ')
    view.divider()

    if user_input == '1':
        print('Add Task')
        new_task_description = input("What is the description? ")
        new_task_priority = input("What is the priority (low, med, high)? ")
        data.tasks.append({
            "description": new_task_description,
            "priority": new_task_priority
        })
        print("Task was added successfully")
    elif user_input == '2':
        index_of_task_to_delete = view.select_task('remove')
        data.tasks.pop(index_of_task_to_delete)
        print('Task removed successfully')
    elif user_input == '3':
        if data.tasks:
            view.show_tasks()
        else:
            print('No tasks found')
    elif user_input == '4':
        print()
    elif user_input == 'q':
        is_running = False
