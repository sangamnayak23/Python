# Palindrome Checker using python programming language 

word = input("Enter a word: ")

# Reverse the word
reverse = word[::-1]

# Check palindrome
if word.lower() == reverse.lower():
    print("It is a Palindrome")
else:
    print("It is not a Palindrome")
