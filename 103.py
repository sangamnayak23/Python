# Simple Quiz Game using python programming language 

score = 0

# Store questions, options, and correct answers
questions = [
    ("What is the capital of India?",
     "A. Mumbai  B. Delhi  C. Chennai", "B"),

    ("Which language are we learning?",
     "A. Python  B. Java  C. HTML", "A"),

    ("How many days are in a week?",
     "A. 5  B. 6  C. 7", "C")
]

# Ask each question
for question, options, answer in questions:
    print("\n" + question)
    print(options)

    choice = input("Enter your answer (A/B/C): ").upper()

    if choice == answer:
        print("Correct answer!")
        score += 1
    else:
        print("Wrong answer!")

# Display final score
print("\nYour score:", score, "/", len(questions))
