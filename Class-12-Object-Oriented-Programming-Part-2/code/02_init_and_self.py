# __init__ runs automatically when an object is made. self is that object.
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

rex = Dog("Rex", "Labrador")
fido = Dog("Fido", "Beagle")

print(rex.name, rex.breed)
print(fido.name, fido.breed)     # same code ran twice, self was a different dog each time

rex.age = 3                      # an attribute added after creation: works, but fragile
print(rex.age)
