# Simple Password Generator using python programming language 

import random
import string

# Create characters
characters = string.ascii_letters + string.digits

# Generate password
password = ""

for i in range(8):
    password += random.choice(characters)

print("Your password is:", password)
