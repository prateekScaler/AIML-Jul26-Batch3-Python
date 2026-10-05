# Type casting = converting a value from one type to another.

# The problem: input() gives text, and text + number is not allowed.
#   age = input("What is your age? ")
#   next_year = age + 1
#   TypeError: can only concatenate str (not "int") to str

# The fix: convert the text to an int as soon as it arrives.
age = int(input("What is your age? "))
print(type(age))       # <class 'int'>
print(age + 1)         # real arithmetic now works

# The casting functions
print(int("25"))       # 25     text  -> whole number
print(float("99.5"))   # 99.5   text  -> decimal number
print(str(100))        # 100    number -> text (it prints the same, but it is a str)

# Things worth trying one at a time:
#   int("99.5")   -> ValueError: invalid literal for int() with base 10: '99.5'
#   int(99.9)     -> 99  (cuts off the decimal part, does not round)
#   "₹" + 500     -> TypeError;  "₹" + str(500) works
