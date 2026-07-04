# Dice Rolling Simulator using python programming language 

import random

print("🎲 Welcome to the Dice Rolling Simulator!")

# Keep rolling the dice until the user decides to stop
while True:
    input("\nPress Enter to roll the dice...")

    # Generate a random number between 1 and 6
    dice = random.randint(1, 6)

    # Display the result
    print("🎲 You rolled:", dice)

    # Ask the user if they want to roll again
    choice = input("Roll again? (yes/no): ").lower()

    if choice != "yes":
        print("👋 Thanks for playing!")
        break
