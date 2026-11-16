# Daily Step Counter using python programming language 

goal = 10000

steps = int(input("Enter your steps today: "))

print("Steps walked:", steps)
print("Steps remaining:", max(0, goal - steps))

if steps >= goal:
    print("Congratulations! Goal completed.")
else:
    print("Keep walking to reach your goal!")