# Sum of Even Numbers using python programming language 

# Get numbers from the user
numbers = [10, 15, 20, 25, 30]

# Find the sum of even numbers
total = 0

for number in numbers:
    if number % 2 == 0:
        total += number

# Display the result
print("Numbers:", numbers)
print("Sum of even numbers:", total)
