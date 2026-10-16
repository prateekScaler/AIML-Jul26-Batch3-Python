# remove takes a value and gives back nothing. pop takes a position and gives back the item.
fruits = ["Apple", "Banana", "Mango"]

fruits.remove("Banana")
print(fruits)

taken = fruits.pop(0)
print(taken)
print(fruits)

fruits.pop()
print(fruits)

queue = ["Hitender", "Parvatha", "Akash"]
served = queue.pop(0)
print(served, queue)

# fruits.remove("Mango")   # ValueError: list.remove(x): x not in list
