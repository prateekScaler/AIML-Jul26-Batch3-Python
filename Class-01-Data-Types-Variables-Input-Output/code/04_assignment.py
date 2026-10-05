# = means "assign", not "is equal to".
# Python works out the RIGHT side first, then stores the result under the name.

age = 20
print(age)        # 20

age = age + 1     # right side: 20 + 1 = 21, then store 21 under age
print(age)        # 21

# A wallet balance changes the same way:
balance = 1000
balance = balance - 200
balance = balance - 300
print(balance)    # 500

# Assignment copies the value. It does not link two names together.
price = 499
total = price
price = 599
print(total)      # still 499
