# Simple Contact Book using python programming language 

# Create an empty dictionary to store contacts
contacts = {}

print("📒 Welcome to the Contact Book!")

while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    # Add a new contact
    if choice == "1":
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print("✅ Contact added successfully!")

    # View all contacts
    elif choice == "2":
        if contacts:
            print("\nSaved Contacts:")
            for name, phone in contacts.items():
                print(f"{name}: {phone}")
        else:
            print("No contacts found.")

    # Search for a contact
    elif choice == "3":
        name = input("Enter contact name to search: ")
        if name in contacts:
           
