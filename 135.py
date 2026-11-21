# Task Status Tracker using python programming language 

tasks = ["Study Python", "Complete Homework", "Read a Book"]

completed = input("Enter the task you completed: ")

if completed in tasks:
    tasks.remove(completed)
    print("Task marked as completed!")
else:
    print("Task not found!")

print("\nPending Tasks:")

for task in tasks:
    print("-", task)

print("Pending task count:", len(tasks))