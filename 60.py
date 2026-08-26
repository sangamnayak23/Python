# Palindrome Number Checker using python programming language 

# Get a number from the user
number = int(input("Enter a number: "))

# Convert the number to a string
text = str(number)

# Check if the number is the same when reversed
if text == text[::-1]:
    print(number, "is a Palindrome Number.")
else:
    print(number, "is not a Palindrome Number.")
