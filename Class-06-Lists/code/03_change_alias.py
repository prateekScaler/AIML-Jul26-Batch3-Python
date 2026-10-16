# Lists are mutable: a box can be replaced. And two names can point at one list.
fruits = ["Apple", "Banana", "Mango"]
fruits[1] = "Orange"
print(fruits)

original = [10, 20, 30]
alias = original          # the same list, a second name
alias[0] = 99
print(original)           # [99, 20, 30]

copy = original.copy()    # a real second list
copy[0] = 10
print(original, copy)
