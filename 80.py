# Simple To-Do List using python programming language 

tasks = []

# Add tasks
for i in range(3):
    task = input("Enter a task: ")
    tasks.append(task)

# Display tasks
print("\nYour To-Do List:")

for i, task in enumerate(tasks, 1):
    print(i, ".", task)
