# filter: keep the items where the rule is True.
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))        # [2, 4, 6, 8]

amounts = [600, 250, 1500, 90]
big = list(filter(lambda a: a >= 500, amounts))
print(big)
