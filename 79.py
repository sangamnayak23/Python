# Number Guessing Game using python programming language 

import random

number = random.randint(1, 10)

guess = int(input("Guess a number between 1 and 10: "))

if guess == number:
    print("Correct! You won 🎉")
else:
    print("Wrong guess!")
    print("The number was:", number)
