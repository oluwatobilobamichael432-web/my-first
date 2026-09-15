import sqlite3

conn = sqlite3.connect("contacts.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        phone TEXT,
        email TEXT
    )
''')

conn.commit()




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
    cursor.execute(
        "INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)",
        (name, phone, email)
    )

    conn.commit()
    print("Contact added successfuly\n")
add_contact()




def view_contacts():

    cursor.execute("SELECT * FROM contacts")
    rows = cursor.fetchall()
    
    if not rows:
        print("No contact yet")
    else:
        for row in rows:
            print(f"Name: {row[1]} | Phone: {row[2]} | Email: {row[3]}")

view_contacts()




def search_contacts():

    find = input("Enter a name to search for\n")
    cursor.execute("SELECT * FROM contacts WHERE name = ?", (find,))
    rows = cursor.fetchall()

    if not rows:
        print("Contact not found")
    else:
        for row in rows:
            print(f"Name: {row[1]} | Phone: {row[2]} | Email: {row[3]}")

search_contacts()

def delete_contacts():
    find = input("Enter the name to be deleted\n")

    cursor.execute("DELETE FROM contacts WHERE name = ?", (find,))
    conn.commit()
    print("Contact deleted (if it existed)")
delete_contacts()


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