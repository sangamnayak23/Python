# Palindrome Checker using python programming language 

print("🔄 Welcome to the Palindrome Checker!")

# Get input from the user
text = input("Enter a word or phrase: ")

# Remove spaces and convert to lowercase
clean_text = text.replace(" ", "").lower()

# Check if the text is a palindrome
if clean_text == clean_text[::-1]:
    print("It is a palindrome!")
else:
    print("It is not a palindrome.")

print("Thank you for using the Palindrome Checker!")
