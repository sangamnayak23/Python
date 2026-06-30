# Simple To-Do List using python programming language 

# Create an empty list to store tasks
tasks = []

print("📝 Simple To-Do List")

# Loop until the user chooses to exit
while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    # Add a new task
    if choice == "1":
        task = input("Enter the task: ")
        tasks.append(task)
        print("✅ Task added successfully!")

    # Display all tasks
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    # Remove a task
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            task_number = int(input("Enter task number to remove: "))

            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                print(f"🗑️ '{removed_task}' removed successfully!")
            else:
                print("Invalid task number.")

    # Exit the program
    elif choice == "4":
        print("👋 Thank you for using the To-Do List!")
        break

    # Handle invalid input
    else:
        print("Invalid choice. Please try again.")
