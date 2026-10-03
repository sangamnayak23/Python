# Prime Number Checker using python programming language 

number = int(input("Enter a number: "))

# Check if the number is prime
if number < 2:
    print("Not a prime number")
else:
    prime = True

    for i in range(2, number):
        if number % i == 0:
            prime = False
            break

    if prime:
        print("It is a Prime Number")
    else:
        print("It is not a Prime Number")
