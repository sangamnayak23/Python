# Marks Percentage Calculator using python programming language 

total_marks = float(input("Enter total marks: "))
obtained_marks = float(input("Enter obtained marks: "))

if total_marks > 0 and 0 <= obtained_marks <= total_marks:
    percentage = (obtained_marks / total_marks) * 100
    print("Percentage:", round(percentage, 2), "%")
else:
    print("Please enter valid marks.")