# Slicing: [start:stop] with stop excluded, like range. A third number is the step.
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[-2:])
print(numbers[:])

numbers = [1, 2, 3, 4, 5, 6]
print(numbers[0:6:2])
print(numbers[1:5:2])
print(numbers[::-1])
