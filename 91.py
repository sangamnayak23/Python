# Factorial Calculator using python programming language 

number = int(input("Enter a number: "))

factorial = 1

# Calculate factorial
for i in range(1, number + 1):
    factorial *= i

print("Factorial:", factorial)
