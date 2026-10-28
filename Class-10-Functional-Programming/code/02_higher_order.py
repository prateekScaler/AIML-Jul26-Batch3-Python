# A function can take another function as an argument.
def apply_twice(func, value):
    return func(func(value))

def add_three(x):
    return x + 3

print(apply_twice(add_three, 10))    # add_three(10) is 13, add_three(13) is 16

# We pass add_three, not add_three(). The function itself, not its answer.
