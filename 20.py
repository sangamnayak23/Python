# Vowel Counter using python programming language 

# Get a string from the user
text = input("Enter a string: ").lower()

# Initialize vowel count
count = 0

# Count vowels
for char in text:
    if char in "aeiou":
        count += 1

# Display the result
print("Number of vowels:", count)
