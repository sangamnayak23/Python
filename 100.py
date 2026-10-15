# Expense Tracker using python programming language 

expenses = []

# Enter the number of expenses
n = int(input("How many expenses? "))

# Get expense details
for i in range(n):
    amount = float(input("Enter expense amount: "))
    expenses.append(amount)

# Calculate total expenses
total = sum(expenses)

# Display the result
print("All Expenses:", expenses)
print("Total Expenses: ₹", total)
