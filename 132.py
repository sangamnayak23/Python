# Shopping Item Counter using python programming language 

items = []

count = int(input("How many items do you want to add? "))

for i in range(count):
    item = input("Enter item name: ")
    items.append(item)

print("\nYour Shopping List:")
for item in items:
    print("-", item)

print("Total items:", len(items))