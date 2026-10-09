# Nested: the inner question is asked only when the outer answer is True.
pin_correct = True
balance = 1000
amount = 400

if pin_correct:
    if balance >= amount:
        print("Payment successful")
    else:
        print("Insufficient balance")
else:
    print("Wrong PIN")

# The same check with and: shorter, but one failure message for everything
if pin_correct and balance >= amount:
    print("Payment successful")

# An else belongs to the if at the SAME indentation.
# Delete the inner else above and, with balance 300, nothing prints at all.
