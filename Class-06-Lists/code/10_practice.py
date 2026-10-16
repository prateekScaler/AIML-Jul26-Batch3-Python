# Two practices: a shopping list and a number list.
shopping = ["Milk", "Bread", "Eggs"]
shopping.append("Apples")
shopping.insert(1, "Rice")
shopping.remove("Bread")
print(shopping)
for item in shopping:
    print(item)

numbers = [12, 5, 8, 20, 3, 15]
numbers.sort()
print(numbers[0], numbers[-1])
print(numbers[:3])
print([x for x in numbers if x > 10])
