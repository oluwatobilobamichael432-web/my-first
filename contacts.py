import json

def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

load_contacts()

contacts = load_contacts()
# ask user to add a contact
def add_contact():

    name = input("Enter your name\n")
    while name[0].islower():
            print("Name must begin with capital case")
            name = input("Enter name again\n")
    
    phone = input("Enter phone number\n")
    while not phone.isnumeric() or len(phone) != 11:
          print("Invalid phone number")
          phone = input("Enter a valid number\n")

    email = input("Enter email\n")
    while email.isupper():
          print("Wrong email pattern")
          email = input("Enter a valid email\n")

    contact = {"name": name, "phone": phone, "email": email }
    contacts.append(contact)

    return contact
    
print(add_contact())
print(contacts)

def view_contacts():
    
    if not contacts:
        print("No contact yet")
    else:
        for contact in contacts:
            print(f"Name: {contact['name']} | Phone: {contact['phone']} | Email: {contact['email']}")


view_contacts()

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

def save_contacts():
    with open("contacts.json", "w") as file:
        json.dump(contacts, file)

save_contacts()


while True:
    print("\n1. Add contact")
    print("2. View contacts")
    print("3. Search contact")
    print("4. Delete contact")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contacts()
    elif choice == "4":
        delete_contacts()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again")