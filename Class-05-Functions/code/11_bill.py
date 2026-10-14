# Mini challenge: a bill with a default tax rate in whole percent.
# Money stays a whole number of rupees.
def calculate_bill(price, quantity, tax=5):
    subtotal = price * quantity
    return subtotal + subtotal * tax // 100

print(calculate_bill(100, 2))
print(calculate_bill(100, 2, tax=10))
