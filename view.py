contacts = [
    {"name": "John", "phone": "08012345678", "email": "john@mail.com"},
    {"name": "Amy", "phone": "08098765432", "email": "amy@mail.com"}
]

def view_contol():
    
    if not contacts:
        print("No contact yet")
    else:
        for contact in contacts:
            print(f"Name: {contact['name']} | Phone: {contact['phone']} | Email: {contact['email']}")


view_contol()