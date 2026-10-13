# Character Frequency Counter using python programming language 

text = input("Enter a word: ")

# Count each character
frequency = {}

for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

# Display character frequencies
for char, count in frequency.items():
    print(char, ":", count)
