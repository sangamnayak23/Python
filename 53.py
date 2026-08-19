# Fibonacci Series using python programming language 

# Get the number of terms
n = int(input("Enter the number of terms: "))

# Initialize the first two terms
a = 0
b = 1

# Generate Fibonacci series
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
