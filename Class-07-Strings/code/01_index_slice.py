# A string is a sequence of characters. Index and slice it exactly like a list.
amounts = [600, 300, 1500, 250]
print(amounts[0:3])      # a list slice, Class 6: start included, stop excluded

word = "Python"
print(len(word))

print(word[0])
print(word[3])
print(word[-1])
print(word[-2])

print(word[0:3])
print(word[:3])
print(word[2:])
print(word[::2])
print(word[::-1])
print(word[-4:])

card = "4111222233334444"
print(card[-4:], card[:4])
