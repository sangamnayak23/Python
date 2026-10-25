# Currency Converter using python programming language 

# Get amount in Indian Rupees
rupees = float(input("Enter amount in INR: "))

# Example conversion rate (not live)
usd_rate = 83

# Convert INR to USD
dollars = rupees / usd_rate

# Display the result
print("Amount in USD:", round(dollars, 2))
