# BMI Calculator using python programming language 

# Get user details
weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

# Calculate BMI
bmi = weight / (height * height)

# Display the result
print("Your BMI is:", round(bmi, 2))

if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 25:
    print("Category: Normal weight")
elif bmi < 30:
    print("Category: Overweight")
else:
    print("Category: Obesity")
