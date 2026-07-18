# Count Even and Odd Numbers using python programming language 

# Create a list of numbers
numbers = [10, 15, 22, 33, 40, 51]

even = 0
odd = 0

# Count even and odd numbers
for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

# Display the result
print("Even numbers:", even)
print("Odd numbers:", odd)
