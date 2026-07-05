# Simple Quiz Game using python programming language 

# Dictionary containing questions and answers
quiz = {
    "What is the capital of India?": "delhi",
    "How many days are there in a week?": "7",
    "Which planet is known as the Red Planet?": "mars",
    "What is 5 + 3?": "8",
    "What is the largest ocean in the world?": "pacific"
}

score = 0

print("Welcome to the Quiz Game!")

# Ask each question
for question, answer in quiz.items():
    user_answer = input(question + " ").lower()

    # Check if the answer is correct
    if user_answer == answer:
        print("Correct!")
        score += 1
    else:
        print("Wrong! The correct answer is:", answer.title())

# Display the final score
print("\n Quiz Completed!")
print("Your Score:", score, "/", len(quiz))

print("Thank you for playing!")
