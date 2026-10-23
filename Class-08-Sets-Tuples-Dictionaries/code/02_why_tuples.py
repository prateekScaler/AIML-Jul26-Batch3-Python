# A function that returns two values returns a tuple.
def min_and_max(numbers):
    return min(numbers), max(numbers)

result = min_and_max([600, 1500, 250])
print(result)
print(type(result))

smallest, biggest = min_and_max([600, 1500, 250])
print(smallest, biggest)

# A payment as a fixed record: name, amount, mode. A receipt should not change.
payment = ("Rajani", 600, "upi")
name, amount, mode = payment
print(f"Paid ₹{amount} to {name} via {mode}")
