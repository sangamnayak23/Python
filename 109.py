# Leap Year Checker using python programming language 

year = int(input("Enter a year: "))

# Check whether the year is a leap year
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("It is a Leap Year")
else:
    print("It is not a Leap Year")
