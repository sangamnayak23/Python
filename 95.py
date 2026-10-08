# Vowel Counter using python programming language 

text = input("Enter a word or sentence: ")

vowels = "aeiou"
count = 0

# Count the vowels
for letter in text.lower():
    if letter in vowels:
        count += 1

print("Number of vowels:", count)
