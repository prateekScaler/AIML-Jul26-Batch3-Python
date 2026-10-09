# Mini challenge: Diwali cashback.
# 5,000 or more -> 20%   2,000 or more -> 10%   otherwise -> 0%
amount = int(input("Enter purchase amount: "))

if amount >= 5000:
    cashback = 20
elif amount >= 2000:
    cashback = 10
else:
    cashback = 0

print("Cashback:", cashback, "%")
print("You get back ₹", amount * cashback // 100)
