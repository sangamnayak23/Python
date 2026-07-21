# Leap Year Checker using python programming language 

# Get year from the user
year = int(input("Enter a year: "))

# Check if it is a leap year
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a Leap Year.")
else:
    print(year, "is not a Leap Year.")
