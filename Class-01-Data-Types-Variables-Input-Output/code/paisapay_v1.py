# PaisaPay v1: take one payment and print a receipt
# Built in Class 1 using print(), variables, input() and type casting.

print("Welcome to PaisaPay")

name = input("Your name: ")
payee = input("Pay to: ")
amount = int(input("Amount in rupees: "))

balance = 1000              # every new wallet starts with ₹1000
balance = balance - amount  # the money leaves the wallet

print("----- Receipt -----")
print("From:", name)
print("To:", payee)
print("Paid: ₹", amount)
print("Balance left: ₹", balance)

# What v1 cannot do yet:
#   - refuse a payment bigger than the balance (needs decisions, Class 3)
#   - accept an amount like 99.50 (int() rejects it)
#   - take more than one payment (needs loops, Class 4)
