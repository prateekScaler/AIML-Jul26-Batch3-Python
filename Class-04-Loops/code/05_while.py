# while: repeat while the condition is True.
# Set the variable before the loop. Change it inside, or the loop never ends.
count = 1

while count <= 5:
    print(count)
    count += 1

# The condition decides how many times, not a number.
balance = 1000

while balance >= 300:
    balance -= 300
    print("Paid ₹300. Left:", balance)
