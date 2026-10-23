student = {"name": "Rajani", "age": 22, "course": "AIML"}

# A loop over a dictionary gives the keys.
for key in student:
    print(key)

# items() gives key and value together.
for key, value in student.items():
    print(key, "->", value)

# values() gives only the values.
for value in student.values():
    print(value)

# A tuple keeps its order. A set makes no promise about order.
coords = (10, 20, 30)
for value in coords:
    print(value)

fruits = {"apple", "banana", "cherry"}
for fruit in fruits:
    print(fruit)
