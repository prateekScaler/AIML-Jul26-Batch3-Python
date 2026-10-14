# Trace a call: arguments in, body runs, value returned, value used.
def calculate(x, y):
    total = x + y
    return total * 2

result = calculate(5, 3)
print(result)
