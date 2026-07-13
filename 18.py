# Sum of Digits using python programming language 

# Get a number from the user
number = input("Enter a number: ")

# Initialize sum
total = 0

# Add each digit
for digit in number:
    total += int(digit)

# Display the result
print("Sum of digits =", total)
