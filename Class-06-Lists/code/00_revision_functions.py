# Revision from Class 5: scope, and the order of parameters.
# A function can read a global, but assigning inside makes a new local.
x = 10

def show():
    x = 5          # a new local x
    print(x)

show()             # 5
print(x)           # 10: the outside x never changed

# A function cannot change an outside number. It hands back a new one.
balance = 1000

def add_bonus(balance):
    return balance + 100

balance = add_bonus(balance)
print(balance)     # 1100

# Definition: required parameters first, defaults last.
# Call: positional arguments first, keyword arguments last.
def pay(amount, mode="upi", note=""):
    print(amount, mode, note)

pay(500)
pay(500, "card")
pay(500, note="rent")
# pay(mode="card", 500)         # SyntaxError: positional argument follows keyword argument
# def pay(mode="upi", amount)   # SyntaxError: parameter without a default follows parameter with a default
