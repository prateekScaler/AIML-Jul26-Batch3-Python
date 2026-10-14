# Scope: a variable created inside a function is local and dies with it.
# A function can read a global variable. Prefer passing values in and returning them out.
name = "Uma"

def greet():
    print("Hello", name)          # reads the global

greet()

def make_message():
    message = "Hello"             # local
    return message                # the way to get it out

print(make_message())

def calculate():
    result = 10 + 20
    return result

calculate()
# print(result)                   # NameError: result was local
