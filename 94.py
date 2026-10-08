# Largest Number Finder using python programming language 

numbers = input("Enter numbers separated by spaces: ")

# Convert input into a list of integers
numbers = [int(x) for x in numbers.split()]

# Find the largest number
largest = max(numbers)

print("Largest number:", largest)
