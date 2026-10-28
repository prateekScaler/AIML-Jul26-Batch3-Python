# The same three tasks, both ways.
from functools import reduce

numbers = [1, 2, 3, 4]

squared_loop = []
for n in numbers:
    squared_loop.append(n ** 2)
squared_func = list(map(lambda n: n ** 2, numbers))
print(squared_loop == squared_func, squared_func)

evens_loop = []
for n in numbers:
    if n % 2 == 0:
        evens_loop.append(n)
evens_func = list(filter(lambda n: n % 2 == 0, numbers))
print(evens_loop == evens_func, evens_func)

total_loop = 0
for n in numbers:
    total_loop += n
total_func = reduce(lambda a, b: a + b, numbers)
print(total_loop == total_func, total_func)
