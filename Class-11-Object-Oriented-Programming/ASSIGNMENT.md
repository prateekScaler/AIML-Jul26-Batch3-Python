# Assignment · Class 11

Practice for classes and objects: `__init__` and `self`, methods that change their object, class variables against instance variables, encapsulation, inheritance with `super()`, overriding and polymorphism. Do Part A on paper first. Write Parts B and C yourself before asking any AI assistant. For more coding problems with solutions, see [`PRACTICE.md`](PRACTICE.md).

Run your programs in [PyLens](https://scaler-pylens.vercel.app/) or with `python3 filename.py`.

## Part A · Predict the output (no running)

Write down what each snippet prints, or which error it raises. Then run it and compare.

**A1**
```python
class Dog:
    def __init__(self, name):
        self.name = name

d = Dog("Rex")
print(d.name, type(d).__name__)
```

**A2**
```python
class Dog:
    def __init__(self, name):
        self.name = name

d = Dog()
```

**A3**
```python
class Box:
    def __init__(self):
        self.items = []

a = Box()
b = Box()
a.items.append(1)
print(a.items, b.items)
```

**A4**
```python
class Box:
    items = []

a = Box()
b = Box()
a.items.append(1)
print(a.items, b.items)
```

**A5**
```python
class Account:
    def __init__(self, balance):
        self.__balance = balance

a = Account(100)
print(a.__balance)
```

**A6**
```python
class Parent:
    def hello(self):
        return "parent"

class Child(Parent):
    pass

print(Child().hello())
```

**A7**
```python
class Parent:
    def __init__(self):
        self.x = 1

class Child(Parent):
    def __init__(self):
        self.y = 2

print(Child().x)
```

**A8**
```python
class Parent:
    def __init__(self):
        self.x = 1

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.y = 2

c = Child()
print(c.x + c.y)
```

**A9**
```python
class Cat:
    def speak(self):
        return "Meow"

class Cow:
    def speak(self):
        return "Moo"

print([animal.speak() for animal in [Cat(), Cow()]])
```

**A10**
```python
class Timer:
    def tick(self):
        self.count += 1

t = Timer()
t.tick()
```

## Part B · Write the program

**B1. A Movie class.** Title, year and rating, with a `describe()` method that returns `Title (year): rating/10`. Make three movies and print the one with the highest rating using `max` with a key.

**B2. A Thermostat.** Starts at 20 degrees. `up()` and `down()` change it by one, never above 30 or below 16. `show()` prints the temperature. Press up twelve times and show.

**B3. A Queue class.** Wrap the Class 6 queue: `join(name)`, `serve()` (removes and returns the first person, or `None` if empty) and `length()`. Each queue must have its own list.

**B4. A private marks list.** A `Student` whose marks list is `__marks`, with `add_mark(m)` that refuses marks outside 0 to 100, and `average()`. Show the refused mark does not count.

**B5. Shapes with inheritance.** A `Shape` class with a name and a `describe()` that prints `name: area`, and `Square(Shape)` and `Circle(Shape)` that pass their name to `super().__init__` and each define `area()`. One loop describes a list of shapes.

**B6. Fix the bugs.** This program should print `Rajani has ₹1200`. It has three mistakes. Find and fix each one, and write what went wrong.

```python
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        balance = balance

    def add(amount):
        self.balance += amount

a = Account("Rajani", 1000)
a.add(200)
print(f"{a.owner} has ₹{a.balance}")
```

## Part C · Project: grow PaisaPay v11

Start from [`code/paisapay_v11.py`](code/paisapay_v11.py).

1. **Two accounts.** Make `rajani = Account("Rajani", 1000, "4321")` and `sumit = PremiumAccount("Sumit", 2500, "1111")`, and let the menu start by asking whose account to use. Everything else works unchanged, because each object carries its own data.
2. **A transfer.** Add a `transfer(self, other, amount)` method to Account that moves money from this account to another one: refuse it when the balance is too low, otherwise subtract here and add there through the existing methods.
3. **A StudentAccount.** A third class that inherits from Account, pays no fee on UPI only, and caps every payment at ₹2000 with the message `Student accounts are limited to ₹2000 per payment.` Override only what changes.

Target output for one run (Rajani's basic account, PIN 4321):

```text
Whose account (rajani / sumit): rajani
Choose: 1
Pay to (UPI ID): sumit@ybl
Amount in rupees: 600
Mode (upi / card / netbanking): upi
UPI PIN: 4321
Paid ₹600 to Sumit via UPI
Fee ₹0 | Cashback ₹10 | Balance ₹410
Choose: 6
Transfer to (rajani / sumit): sumit
Amount: 300
Transferred ₹300 to Sumit. Balance ₹110
```

## Part D · Think it through

Write two or three lines for each.

1. v10 passed `balance` into `pay` and got a new balance back. v11's `pay` returns nothing. Where did the balance go, and why is that better?
2. Why does `tricks = []` in the class body share one list, while `self.tricks = []` in `__init__` does not? Connect it to Class 6.
3. The double underscore can be bypassed with `_Account__balance`. If it is not a real lock, what is it for?
4. The menu loop never checks whether the account is basic or premium, yet premium pays no fee. Which idea from today makes that work?

## With AI (after your own attempt)

Paste your finished Part C program into an AI assistant and ask:

> "List every attribute of every class in this program. For each one, say whether it belongs to one object or to the class, and whether anything outside the class changes it directly. Do not change the code."

Check each claim. Then ask it to suggest one more subclass of Account and decide, before reading its code, which methods that subclass would have to override.
