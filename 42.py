# Simple Interest Calculator using python programming language 

# Get values from the user
principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time in years: "))

# Calculate simple interest
interest = (principal * rate * time) / 100

# Display the result
print("Simple Interest:", interest)
