contacts = [
    {"name": "John", "phone": "08012345678", "email": "john@mail.com"},
    {"name": "Amy", "phone": "08098765432", "email": "amy@mail.com"}
]

def delete_contacts():
    find = input("Enter the name to be deleted\n")
    found = False
    to_delete = None

    for contact in contacts:
        if contact["name"] == find:
            found = True
            to_delete = contact

    if found:
        contacts.remove(to_delete)
        print("Contact successfuly deleted")
    else:
        print("Contact not found")

delete_contacts()