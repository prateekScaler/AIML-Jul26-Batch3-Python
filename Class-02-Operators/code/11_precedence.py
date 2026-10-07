# Operator precedence: the order Python follows.
# ()  then **  then * / // %  then + -  then comparisons  then not, and, or

print(10 + 5 * 2)       # 20  multiplication first
print((10 + 5) * 2)     # 30  parentheses decide
print(2 + 3 ** 2)       # 11  power first

# A real bug: the average of two amounts
print(100 + 200 / 2)    # 200.0  wrong
print((100 + 200) / 2)  # 150.0  right

print(True or False and False)   # True: and goes before or
