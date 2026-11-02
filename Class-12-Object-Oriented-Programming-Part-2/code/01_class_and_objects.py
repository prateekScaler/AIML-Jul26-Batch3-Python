# A class is a blueprint. An object is one thing built from it.
class Dog:
    pass

rex = Dog()
fido = Dog()

print(rex)                 # <__main__.Dog object at 0x...>: the address varies
print(rex == fido)         # False: two separate objects from one blueprint
print(type(rex).__name__)
