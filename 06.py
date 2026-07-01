# Random Password Generator using python programming language 

import random
import string

# Ask the user for the password length
length = int(input("Enter the password length: "))

# Combine letters, numbers, and symbols
characters = string.ascii_letters + string.digits + string.punctuation

# Generate a random password
password = ""
for i in range(length):
    password += random.choice(characters)

# Display the generated password
print("\n🔒 Your Random Password is:")
print(password)

print("\nThank you for using the Password Generator!")
