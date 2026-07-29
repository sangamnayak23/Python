# Vowel or Consonant Checker using python programming language 

# Get a character from the user
ch = input("Enter a character: ").lower()

# Check if it is a vowel or consonant
if ch in "aeiou":
    print(ch, "is a Vowel.")
else:
    print(ch, "is a Consonant.")
