contacts = []

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

