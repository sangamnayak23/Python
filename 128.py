# Parking Fee Calculator using python programming language 

hours = int(input("Enter parking hours: "))
rate = 20

if hours > 0:
    fee = hours * rate
    print("Total Parking Fee: ₹", fee)
else:
    print("Please enter valid parking hours.")