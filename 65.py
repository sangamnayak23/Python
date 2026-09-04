# Even and Divisible by 5 Checker using python programming language 

# Get a number from the user
number = int(input("Enter a number: "))

# Check the conditions
if number % 2 == 0 and number % 5 == 0:
    print("The number is even and divisible by 5.")
else:
    print("The number does not satisfy both conditions.")
