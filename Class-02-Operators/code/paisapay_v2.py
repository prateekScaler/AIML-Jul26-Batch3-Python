# PaisaPay v2: money maths and checks
# Built in Class 2. Adds operators to v1: a fee, cashback, a bill split,
# and two questions the program can now ask about a payment.

print("Welcome to PaisaPay")

name = input("Your name: ")
payee = input("Pay to: ")
amount = int(input("Amount in rupees: "))
people = int(input("Split between how many people? "))

balance = 1000
fee = 2                          # flat convenience fee, in rupees
total = amount + fee
cashback = amount * 5 // 100     # 5% cashback, in whole rupees
share = amount // people         # each person's share
left_over = amount % people      # rupees that do not divide evenly

can_pay = balance >= total
is_big_payment = amount >= 500

balance -= total
balance += cashback

print("----- Receipt -----")
print("From:", name)
print("To:", payee)
print("Paid: ₹", amount, "+ fee ₹", fee)
print("Cashback: ₹", cashback)
print("Each person owes: ₹", share, "| left over: ₹", left_over)
print("Enough balance:", can_pay)
print("Big payment:", is_big_payment)
print("Balance left: ₹", balance)

# What v2 cannot do yet:
#   - refuse a payment: it prints "Enough balance: False" and pays anyway
#   - act on any of its True/False answers (needs decisions, Class 3)
#   - take more than one payment (needs loops, Class 4)
