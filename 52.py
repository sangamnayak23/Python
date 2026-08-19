# Factorial Calculator using python programming language 

# Get a number from the user
number = int(input("Enter a number: "))

# Calculate factorial
factorial = 1

for i in range(1, number + 1):
    factorial = factorial * i

# Display the result
print("Factorial of", number, "is:", factorial)
