# Mini challenge: three lists from one. sorted() for a copy, comprehensions for the rest.
temperatures = [28, 31, 29, 35, 30, 27, 33]

in_order = sorted(temperatures)
hot = [t for t in temperatures if t > 30]
fahrenheit = [t * 9 / 5 + 32 for t in temperatures]

print(in_order)
print(hot)
print(fahrenheit)
