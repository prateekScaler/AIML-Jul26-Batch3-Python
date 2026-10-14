# Three small practices: a greeting with a default, even or odd, a four-function calculator.
def greet(name="Student"):
    print("Hello", name)

def check_even(number):
    if number % 2 == 0:
        return "Even"
    return "Odd"

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

greet()
print(check_even(10))
print(add(10, 5), subtract(10, 5), multiply(10, 5), divide(10, 5))
