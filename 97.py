# List Sorter using python programming language 

numbers = input("Enter numbers separated by spaces: ")

# Convert input into a list of integers
numbers = [int(x) for x in numbers.split()]

# Sort numbers in ascending order
numbers.sort()

# Display the sorted list
print("Sorted numbers:", numbers)
