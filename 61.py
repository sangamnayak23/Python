# Vowel Counter using python programming language 

# Get a string from the user
text = input("Enter a string: ")

# Initialize vowel count
count = 0

# Check each character
for char in text.lower():
    if char in "aeiou":
        count += 1

# Display the result
print("Number of vowels:", count)
