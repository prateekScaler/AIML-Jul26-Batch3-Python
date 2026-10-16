# A list comprehension builds a new list in one line: [expression for item in list if condition].
numbers = [1, 2, 3, 4, 5]

squares = []
for number in numbers:
    squares.append(number * number)
print(squares)

squares = [number * number for number in numbers]
print(squares)

numbers = [1, 2, 3, 4, 5, 6]
evens = [number for number in numbers if number % 2 == 0]
print(evens)

numbers = [2, 7, 4, 9, 1, 8]
names = ["asha", "rahul", "priya"]
print([number * 2 for number in numbers])
print([number for number in numbers if number > 5])
print([name.upper() for name in names])
