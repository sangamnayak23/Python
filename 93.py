# Sum of Numbers using python programming language 

numbers = input("Enter numbers separated by spaces: ")

# Convert input into a list of integers
numbers = [int(x) for x in numbers.split()]

# Calculate the sum
total = sum(numbers)

print("Sum:", total)
