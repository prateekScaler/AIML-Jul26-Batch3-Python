# A lambda is a small function written in one line. Same answer as def.
def square(x):
    return x * x

square_lambda = lambda x: x * x

print(square(5))
print(square_lambda(5))
