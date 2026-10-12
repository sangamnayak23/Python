# Duplicate Remover using python programming language 

numbers = input("Enter numbers separated by spaces: ")

# Convert input into a list
numbers = [int(x) for x in numbers.split()]

# Remove duplicate numbers
unique_numbers = list(set(numbers))

# Sort the numbers
unique_numbers.sort()

print("Numbers without duplicates:", unique_numbers)
