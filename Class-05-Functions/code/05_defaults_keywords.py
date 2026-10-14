# Default arguments fill a gap. Keyword arguments match by name, not position.
def greet(name="Student"):
    print("Hello", name)

greet()
greet("Prince")

def power(number, exponent=2):
    return number ** exponent

print(power(5), power(5, 3))

def introduce(name, age):
    print(name, age)

introduce(age=20, name="Vinit")   # by name: order does not matter

def greet_with(name, message="Welcome"):
    print(message, name)

greet_with("Vinit")
greet_with("Vinit", "Good morning")
greet_with(name="Vinit", message="Good evening")
