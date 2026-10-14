# Parameters and arguments: the variable in the definition, the value at the call.
# With several parameters, arguments are matched by position.
def greet(name):
    print("Hello", name)

greet("Uma")
greet("Prince")
greet("Vinit")

def introduce(name, age):
    print("My name is", name)
    print("I am", age, "years old.")

introduce("Uma", 20)
