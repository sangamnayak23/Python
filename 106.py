# Email Validator using python programming language 

email = input("Enter your email address: ")

# Check whether the email is valid
if "@" in email and "." in email and email.index("@") < email.rindex("."):
    print("Valid email address!")
else:
    print("Invalid email address!")
