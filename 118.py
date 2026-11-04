# Speed Calculator using python programming language 

distance = float(input("Enter distance in kilometers: "))
time = float(input("Enter time in hours: "))

if time > 0:
    speed = distance / time
    print("Speed:", speed, "km/h")
else:
    print("Time must be greater than zero.")
