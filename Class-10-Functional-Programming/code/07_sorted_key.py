# sorted has two switches: reverse says which way, key says what to compare.
amounts = [600, 250, 1500]
print(sorted(amounts, reverse=True))
print(amounts)

# sorted with a key: sort by one part of each record.
payments = [("Hitender", 600, "upi"),
            ("Saurabh", 250, "card"),
            ("Prajnika", 1500, "upi")]

by_amount = sorted(payments, key=lambda p: p[1])
print(by_amount)

biggest_first = sorted(payments, key=lambda p: p[1], reverse=True)
print(biggest_first[0])

print(max(payments, key=lambda p: p[1]))
