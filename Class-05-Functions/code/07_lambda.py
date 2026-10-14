# lambda: a one-expression function with no name of its own.
# Use it for small, throw-away operations; def for anything longer.
def square(x):
    return x * x

square = lambda x: x * x
print(square(5))

add = lambda a, b: a + b
print(add(10, 20))

double = lambda x: x * 2
print(double(3) + double(4))
