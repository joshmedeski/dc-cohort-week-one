# The file to run the app
import data
import find
import view

print('Welcome to the Phone Book App')

is_running = True

while is_running:
    print('Press 1 to search by first name')
    print('Press 2 for all contacts')
    print('Press "q" to quit')
    menu_choice = input('Choose a menu item: ')
    if menu_choice == '1':
        first_name_query = input("Search by first name:")
        first_name_results = find.contacts_by_first_name(
            data.contacts, first_name_query)
        view.contacts(first_name_results)
    elif menu_choice == '2':
        view.contacts(data.contacts)
    elif menu_choice == 'q':
        is_running = False
    else:
        print("Oops, please try again")

print('Exit Application')
