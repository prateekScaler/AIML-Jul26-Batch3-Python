# Chained calls run from the inside out: filter first, then map.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
print(result)             # [4, 16, 36, 64, 100]
