# Reverse a Number using python programming language 

# Get a number from the user
number = int(input("Enter a number: "))

# Reverse the number
reverse = 0
temp = number

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

# Display the result
print("Reversed number:", reverse)
