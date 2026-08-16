# Number Guessing Game using python programming language 

import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

# Get the user's guess
guess = int(input("Guess a number between 1 and 10: "))

# Check the guess
if guess == secret_number:
    print("Congratulations! You guessed correctly.")
else:
    print("Wrong guess!")
    print("The correct number was:", secret_number)
