# Water Intake Tracker using python programming language 

goal = 2000
total = 0

glasses = int(input("Enter water consumed in ml: "))
total += glasses

print("Water consumed:", total, "ml")
print("Remaining to reach 2000 ml:", max(0, goal - total), "ml")

if total >= goal:
    print("Daily water goal reached!")
else:
    print("Keep tracking your water intake!")