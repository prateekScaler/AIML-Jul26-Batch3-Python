# Debug clinic: three snippets, three errors.
# Remove the # from ONE snippet at a time, predict the error type, then run.

# Snippet 1
# name = Aanand
# NameError: name 'Aanand' is not defined
# Why: no quotes, so Python looks for a variable called Aanand.

# Snippet 2
# age = input("Age: ")
# print(age + 1)
# TypeError: can only concatenate str (not "int") to str
# Why: input() returns text. Fix: age = int(input("Age: "))

# Snippet 3
# Print("Hello")
# NameError: name 'Print' is not defined
# Why: Python is case-sensitive. Only lowercase print is the built-in function.

print("Uncomment one snippet at a time and read the error type first.")
