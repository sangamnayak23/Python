# Simple Contact Book using python programming language 

contacts = {}

# Add contacts
name = input("Enter name: ")
phone = input("Enter phone number: ")

contacts[name] = phone

# Display contact
print("\nContact Book:")
for name, phone in contacts.items():
    print(name, ":", phone)
