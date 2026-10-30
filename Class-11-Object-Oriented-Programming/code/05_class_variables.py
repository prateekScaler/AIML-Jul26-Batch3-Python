# A class variable is shared by every object. An instance variable belongs to one.
class Dog:
    species = "Canis familiaris"      # class variable: the same for every dog

    def __init__(self, name):
        self.name = name              # instance variable: this dog only

rex = Dog("Rex")
fido = Dog("Fido")
print(rex.species, fido.species)

# The trap: a mutable class variable is one list, shared by all.
class Dog:
    tricks = []

    def __init__(self, name):
        self.name = name

rex = Dog("Rex")
fido = Dog("Fido")
rex.tricks.append("sit")
print(rex.tricks, fido.tricks)    # ['sit'] ['sit']: fido never learned anything

# The fix: give each dog its own list, inside __init__.
class Dog:
    def __init__(self, name):
        self.name = name
        self.tricks = []

rex = Dog("Rex")
fido = Dog("Fido")
rex.tricks.append("sit")
print(rex.tricks, fido.tricks)    # ['sit'] []
