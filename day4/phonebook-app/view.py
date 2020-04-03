def contacts(contacts):
    for contact in contacts:
        print(
            f'{contact["first_name"]} {contact["last_name"]}: {contact["phone"]}'
        )