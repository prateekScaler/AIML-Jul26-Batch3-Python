# for walks through any sequence, one item at a time. Lists in detail: Class 6.
payees = ["Chai Point", "Zomato", "Jio"]

for payee in payees:
    print("Paid", payee)

# The loop variable is an ordinary variable. It keeps its last value.
amounts = [120, 450, 99]
for amount in amounts:
    print(amount)
print("After the loop, amount is", amount)
