# Quiz Score Calculator using python programming language 

score = 0

answer1 = input("What is the capital of India? ")
if answer1.lower() == "new delhi":
    score += 1

answer2 = input("How many days are in a week? ")
if answer2 == "7":
    score += 1

answer3 = input("Which language are we learning? ")
if answer3.lower() == "python":
    score += 1

print("\nYour Score:", score, "/ 3")
print("Percentage:", (score / 3) * 100, "%")