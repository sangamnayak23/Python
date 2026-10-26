# Simple Discount Calculator using python programming language 

price = float(input("Enter the original price: "))
discount = float(input("Enter discount percentage: "))

discount_amount = price * discount / 100
final_price = price - discount_amount

print("Discount Amount:", discount_amount)
print("Final Price:", final_price)
