# Rock, Paper, Scissors Game using python programming language 

import random

# List of possible choices
choices = ["rock", "paper", "scissors"]

print("🎮 Welcome to Rock, Paper, Scissors!")

# Get the user's choice
user_choice = input("Enter rock, paper, or scissors: ").lower()

# Generate the computer's choice
computer_choice = random.choice(choices)

print("You chose:", user_choice)
print("Computer chose:", computer_choice)

# Check if the user entered a valid choice
if user_choice not in choices:
    print("❌ Invalid choice! Please enter rock, paper, or scissors.")
# Check for a tie
elif user_choice == computer_choice:
    print("🤝 It's a tie!")
# Check if the user wins
elif (
    (user_choice == "rock" and computer_choice == "scissors") or
    (user_choice == "paper" and computer_choice == "rock") or
    (user_choice == "scissors" and computer_choice == "paper")
):
    print("🎉 Congratulations! You win!")
# Otherwise, the computer wins
else:
   
