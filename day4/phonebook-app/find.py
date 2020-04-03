def contacts_by_first_name(contacts, first_name_query):
    # Create empty list to put items into when found
    results = []
    # Find all contacts with matching first name
    # Put found items in the `results` list
    for contact in contacts:
        if contact['first_name'] == first_name_query:
            results.append(contact)
    # return the results
    return results