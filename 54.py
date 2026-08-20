# Prime Number Checker using python programming language 

# Get a number from the user
number = int(input("Enter a number: "))

# Check whether the number is prime
if number < 2:
    print(number, "is not a Prime Number.")
else:
    prime = True

    for i in range(2, number):
        if number % i == 0:
            prime = False
            break

    if prime:
        print(number, "is a Prime Number.")
    else:
        print(number, "is not a Prime Number.")
