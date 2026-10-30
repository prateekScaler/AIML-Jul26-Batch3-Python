# Carried over from Class 10: chained calls run from the inside out,
# and sorted takes a key that says which part of each record to compare.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
print(result)             # [4, 16, 36, 64, 100]

amounts = [600, 250, 1500]
print(sorted(amounts, reverse=True))   # biggest first
print(amounts)                         # untouched

payments = [("Hitender", 600, "upi"),
            ("Saurabh", 250, "card"),
            ("Prajnika", 1500, "upi")]

by_amount = sorted(payments, key=lambda p: p[1])
print(by_amount)

biggest_first = sorted(payments, key=lambda p: p[1], reverse=True)
print(biggest_first[0])

print(max(payments, key=lambda p: p[1]))
