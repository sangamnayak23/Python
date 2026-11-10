# Shopping Budget Checker using python programming language 

budget = float(input("Enter your budget: "))
price = float(input("Enter the product price: "))

if price <= budget:
    print("You can buy this product.")
    print("Money left:", budget - price)
else:
    print("Your budget is not enough.")
    print("Extra money needed:", price - budget)