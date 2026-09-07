contacts = [
    {"name": "John", "phone": "08012345678", "email": "john@mail.com"},
    {"name": "Amy", "phone": "08098765432", "email": "amy@mail.com"}
]


def search_contacts():

    find = input("Enter a name to search for\n")
    found = False

    for contact in contacts:
        if contact["name"] == find:
            found = True
            print(f"Name: {contact['name']} | Phone: {contact['phone']} | Email: {contact['email']}")

    if not found:
        print("Contact not found")

search_contacts()