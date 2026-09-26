# Student Grade Calculator using python programming language 

marks = float(input("Enter your marks: "))

# Check grade
if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 40:
    grade = "D"
else:
    grade = "F"

print("Your Grade is:", grade)
