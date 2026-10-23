# A tuple is a fixed collection: round brackets, and it cannot change.
point = (3, 4)
print(point)
print(point[0])

# The comma makes the tuple, not the brackets.
point = 3, 4
print(point)
print(type(point))

# The single-element trap: (5) is just 5. (5,) is a tuple.
x = (5)
y = (5,)
print(type(x))
print(type(y))

# Index, slice, unpack: the same as a list.
coords = (10, 20, 30, 40)
print(coords[0])
print(coords[1:3])
print(coords[-1])

x, y = (3, 4)
print(x)
print(y)

# Only two methods: count and index. Nothing to add, remove or sort.
coords = (10, 20, 10, 30, 10)
print(coords.count(10))
print(coords.index(30))

# Trying to change a tuple. Remove the # to see the error.
# coords[0] = 99      # TypeError: 'tuple' object does not support item assignment
