# Multiplication Table using python programming language 

# Get a number from the user
number = int(input("Enter a number: "))

# Print the multiplication table
print("\nMultiplication Table of", number)

for i in range(1, 11):
    print(number, "x", i, "=", number * i)
