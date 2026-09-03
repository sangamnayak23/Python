# Count Words in a Sentence using python programming language 

# Get a sentence from the user
sentence = input("Enter a sentence: ")

# Count the words
words = sentence.split()
count = len(words)

# Display the result
print("Number of words:", count)
