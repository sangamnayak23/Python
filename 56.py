# Sum of Digits using python programming language 

# Get a number from the user
number = int(input("Enter a number: "))

# Find the sum of digits
total = 0
temp = abs(number)

while temp > 0:
    digit = temp % 10
    total += digit
    temp //= 10

# Display the result
print("Sum of digits:", total)
