# Student Attendance Tracker using python programming language 

students = {}

# Enter the number of students
n = int(input("Enter number of students: "))

# Record attendance
for i in range(n):
    name = input("Enter student name: ")
    status = input("Present or Absent (P/A): ")
    students[name] = status.upper()

# Display attendance
print("\n--- Attendance Report ---")

for name, status in students.items():
    if status == "P":
        print(name, "- Present")
    else:
        print(name, "- Absent")
