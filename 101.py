# Shopping Bill Generator using python programming language 

items = []

# Enter the number of items
n = int(input("Enter number of items: "))

# Get item details
for i in range(n):
    name = input("Enter item name: ")
    price = float(input("Enter item price: "))
    items.append((name, price))

# Display the bill
print("\n----- Shopping Bill -----")

total = 0

for name, price in items:
    print(name, ":", price)
    total += price

print("-------------------------")
print("Total Amount: ₹", total)
