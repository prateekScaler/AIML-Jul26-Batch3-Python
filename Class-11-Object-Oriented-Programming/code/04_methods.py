# A method is a function inside a class. It takes self first.
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")

    def describe(self):
        return f"{self.name} is {self.age} years old."

    def have_birthday(self):
        self.age += 1

rex = Dog("Rex", 3)
rex.bark()
print(rex.describe())
rex.have_birthday()
print(rex.describe())          # a method changed the object's own data
