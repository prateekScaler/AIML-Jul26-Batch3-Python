# The ternary operator: a compact if / else that gives a value.
balance = 1000
amount = 400

if balance >= amount:
    status = "SUCCESS"
else:
    status = "FAILED"
print(status)

status = "SUCCESS" if balance >= amount else "FAILED"   # value_if_true if condition else value_if_false
print(status)

# Readable only for a simple two-way choice. Three or more outcomes: use if / elif / else.
amount = 1000
fee = 0 if amount < 1000 else 5 if amount < 10000 else 10   # hard to read; prints 5
print(fee)
