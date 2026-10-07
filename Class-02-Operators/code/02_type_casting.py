# Type casting = converting a value from one type to another.
# Convert the text as soon as it arrives, then the maths works.

a = int(input("First amount: "))
b = int(input("Second amount: "))

print(a + b)    # 150 when the user types 100 and 50

print(int("25"))       # 25
print(float("99.5"))   # 99.5
print(str(100))        # 100, but it is now text

# Worth trying one at a time:
#   int("99.5")   -> ValueError
#   int(99.9)     -> 99 (cuts the decimals, does not round)
#   "₹" + 500     -> TypeError;  "₹" + str(500) works
