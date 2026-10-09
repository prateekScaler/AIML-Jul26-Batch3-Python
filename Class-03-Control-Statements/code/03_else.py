# else: everything else. Exactly one of the two blocks runs.
balance = 300
amount = 800

if balance >= amount:
    print("Payment successful")
else:
    print("Insufficient balance")

# Equal counts as enough: 500 >= 500 is True
balance = 500
amount = 500
if balance >= amount:
    print("Payment successful")
else:
    print("Insufficient balance")
