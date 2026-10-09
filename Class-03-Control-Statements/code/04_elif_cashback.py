# elif: more than two outcomes. Top to bottom, the first True wins.
amount = int(input("Amount in rupees: "))

if amount >= 5000:
    cashback = 100
elif amount >= 2000:
    cashback = 50
elif amount >= 500:
    cashback = 10
else:
    cashback = 0

print("Cashback: ₹", cashback)
# Try 2500 (50), 5000 (100), 499 (0)
