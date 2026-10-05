# input() pauses the program, shows a prompt, and waits for the user.
# Whatever the user types comes back as a value we can store.

name = input("What is your name? ")
print(name)

# The big surprise: input() ALWAYS returns a string (str),
# even when the user types digits.
age = input("What is your age? ")
print(age)
print(type(age))    # <class 'str'>
