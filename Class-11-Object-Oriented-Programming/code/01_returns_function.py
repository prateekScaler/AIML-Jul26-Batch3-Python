# A function can also return a function (the other direction of higher-order).
def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))
print(triple(5))

# A rule factory: build the rule once, use it many times.
def at_least(minimum):
    return lambda amount: amount >= minimum

is_big = at_least(500)
print(is_big(600), is_big(90))
print(list(filter(at_least(1000), [600, 250, 1500])))
