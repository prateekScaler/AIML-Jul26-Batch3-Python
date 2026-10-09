# if: run the indented block only when the condition is True.
balance = 1000
amount = 400

if balance >= amount:
    print("Payment successful")

# When the condition is False, the block is skipped and nothing prints.
balance = 300
if balance >= amount:
    print("Payment successful")
print("Thank you for using PaisaPay")   # not indented: outside the if, runs every time

# Two errors to try, one at a time:
#   if balance = amount:      -> SyntaxError  (= assigns, == compares)
#   if balance >= amount:
#   print("x")                -> IndentationError (the block must be indented)
