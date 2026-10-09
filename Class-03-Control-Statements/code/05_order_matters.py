# The order of conditions matters: the first True wins.
amount = 8000

# Bug: the broad condition comes first, so ₹8000 gets ₹10
if amount >= 500:
    print("Cashback ₹10")
elif amount >= 5000:
    print("Cashback ₹100")

# Fixed: most specific first
if amount >= 5000:
    print("Cashback ₹100")
elif amount >= 500:
    print("Cashback ₹10")

# Not a fix: two separate ifs are two independent questions, both print
if amount >= 5000:
    print("Cashback ₹100")
if amount >= 500:
    print("Cashback ₹10")
