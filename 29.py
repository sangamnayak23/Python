# Armstrong Number Checker using python programming language 

# Get a number from the user
num = int(input("Enter a number: "))

# Calculate the sum of cubes of digits
temp = num
total = 0

while temp > 0:
    digit = temp % 10
    total += digit ** 3
    temp //= 10

# Check if it is an Armstrong number
if total == num:
    print(num, "is an Armstrong Number.")
else:
    print(num, "is not an Armstrong Number.")
