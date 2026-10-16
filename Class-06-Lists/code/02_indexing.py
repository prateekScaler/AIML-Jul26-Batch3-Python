# Indexing: the first box is 0, the last box is -1. Past the end: IndexError.
fruits = ["Apple", "Banana", "Mango", "Orange"]

print(fruits[0])
print(fruits[2])
print(fruits[-1])
print(fruits[-2])

payees = ["Chai Point", "Zomato", "Jio", "Uber"]
print(payees[1], payees[-1])

# print(fruits[5])      # IndexError: list index out of range
