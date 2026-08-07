# Divisible by 2 and 3 Checker using python programming language 

# Get a number from the user
number = int(input("Enter a number: "))

# Check divisibility
if number % 2 == 0 and number % 3 == 0:
    print(number, "is divisible by both 2 and 3.")
else:
    print(number, "is not divisible by both 2 and 3.")
