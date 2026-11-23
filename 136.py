# Library Book Tracker using python programming language 

books = ["Python", "Java", "C++"]

book_name = input("Enter the book name: ")

if book_name in books:
    print("Book is available!")
else:
    print("Book is not available.")

print("\nAvailable Books:")
for book in books:
    print("-", book)