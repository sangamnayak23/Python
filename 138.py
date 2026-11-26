# Daily Habit Tracker using python programming language 

habits = ["Exercise", "Reading", "Coding"]

print("Today's Habits:")
for habit in habits:
    print("-", habit)

completed = input("\nEnter the habit you completed: ")

if completed in habits:
    habits.remove(completed)
    print("Habit marked as completed!")
else:
    print("Habit not found!")

print("\nRemaining Habits:")
for habit in habits:
    print("-", habit)

print("Habits remaining:", len(habits))