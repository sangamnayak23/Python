# Simple Tip Calculator using python programming language 

bill = float(input("Enter the bill amount: "))
tip_percent = float(input("Enter tip percentage: "))

tip = bill * tip_percent / 100
total = bill + tip

print("Tip Amount:", tip)
print("Total Bill:", total)
