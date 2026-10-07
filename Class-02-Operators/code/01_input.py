# input() pauses the program, shows a prompt, and waits for the user.
# It ALWAYS returns a string (str), even when the user types digits.

name = input("What is your name? ")
print(name)

# The big surprise: two friends paid for dinner. Add the amounts.
# Type 100 and 50: this prints 10050, not 150. + joins two strings.
a = input("First amount: ")
b = input("Second amount: ")
print(a + b)
print(type(a))    # <class 'str'>

# With - instead of +, Python refuses outright:
#   balance = 1000
#   amount = input("Amount to pay: ")
#   print(balance - amount)
#   TypeError: unsupported operand type(s) for -: 'int' and 'str'
