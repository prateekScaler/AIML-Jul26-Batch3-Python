# reduce: combine everything into one value. It must be imported.
from functools import reduce

numbers = [1, 2, 3, 4]

total = reduce(lambda a, b: a + b, numbers)
print(total)              # 1+2 is 3, 3+3 is 6, 6+4 is 10

product = reduce(lambda a, b: a * b, numbers, 1)
print(product)            # 24, starting from 1
