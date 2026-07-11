# Prime Number Checker using python programming language 

# Get a number from the user
number = int(input("Enter a number: "))

# Check if the number is prime
if number > 1:
    for i in range(2, number):
        if number % i == 0:
            print(number, "is not a Prime Number.")
            break
    else:
        print(number, "is a Prime Number.")
else:
    print(number, "is not a Prime Number.")
