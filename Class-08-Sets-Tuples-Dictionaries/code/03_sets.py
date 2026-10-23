# A set keeps one copy of each value. Curly brackets, no order.
numbers = {1, 2, 2, 3, 3, 3}
print(numbers)
print(len(numbers))

# The empty-set trap: {} is an empty dictionary.
empty = {}
print(type(empty))

empty_set = set()
print(type(empty_set))

# add, remove, discard
fruits = {"apple", "banana"}
fruits.add("cherry")
print(len(fruits), "cherry" in fruits)

fruits.discard("mango")      # not there: nothing happens
print(len(fruits))

# fruits.remove("mango")     # not there: KeyError: 'mango'
