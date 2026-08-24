# Count Even and Odd Numbers using python programming language 

# Create a list of numbers
numbers = [10, 15, 22, 31, 40, 55]

# Initialize counters
even_count = 0
odd_count = 0

# Count even and odd numbers
for number in numbers:
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

# Display the result
print("Numbers:", numbers)
print("Even numbers:", even_count)
print("Odd numbers:", odd_count)
