# map: the same change to every item.
numbers = [1, 2, 3, 4]

squared = map(lambda x: x ** 2, numbers)
print(squared)            # a map object, not a list: nothing is squared yet
print(list(squared))      # [1, 4, 9, 16]: list() asks for the values

amounts = [600, 250, 1500]
in_paise = list(map(lambda a: a * 100, amounts))
print(in_paise)
