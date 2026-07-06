# Temperature Converter using python programming language 

print("Welcome to the Temperature Converter!")

# Display conversion options
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

# Get user's choice
choice = input("Enter your choice (1 or 2): ")

# Convert Celsius to Fahrenheit
if choice == "1":
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print("Temperature in Fahrenheit:", fahrenheit)

# Convert Fahrenheit to Celsius
elif choice == "2":
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print("Temperature in Celsius:", celsius)

# Handle invalid input
else:
    print("Invalid choice! Please select 1 or 2.")

print("Thank you for using the Temperature Converter!")
