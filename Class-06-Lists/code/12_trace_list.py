# Trace a list: each method changes it in place. Follow the list after every line.
numbers = [10, 20, 30]

numbers.append(40)
numbers.insert(1, 15)
numbers.remove(30)

print(numbers)
