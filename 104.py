# Rock, Paper, Scissors using python programming language 

import random

# Store the choices
choices = ["rock", "paper", "scissors"]

# Get the player's choice
player = input("Choose rock, paper, or scissors: ").lower()

# Computer selects a random choice
computer = random.choice(choices)

print("Computer chose:", computer)

# Check the winner
if player not in choices:
    print("Invalid choice!")
elif player == computer:
    print("It's a tie!")
elif (
    (player == "rock" and computer == "scissors") or
    (player == "paper" and computer == "rock") or
    (player == "scissors" and computer == "paper")
):
    print("You win!")
else:
    print("Computer wins!")
