# Practice problems · Class 11 · Object-Oriented Programming

Twelve problems, easy to hard. Each uses only what Classes 1 to 11 covered. Write every program yourself in [PyLens](https://scaler-pylens.vercel.app/) or with `python3`, run it against the sample, and only then open the hint or the solution.

How to work: decide what each object must remember (that goes in `__init__` through `self.`) and what it must be able to do (those are methods, each starting with `self`). When two classes share most of their code, one inherits from the other.

- [Warm-up](#warm-up) · problems 1 to 4
- [Core](#core) · problems 5 to 9
- [Challenge](#challenge) · problems 10 to 12

---

## Warm-up

### 1. A Student class

Write a `Student` class with a name and a city, and a `greet()` method that prints a sentence. Make two students and greet both.

```text
Hi, I am Hitender from Pune.
Hi, I am Saurabh from Nagpur.
```

<details><summary>Solution</summary>

```python
class Student:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def greet(self):
        print(f"Hi, I am {self.name} from {self.city}.")

Student("Hitender", "Pune").greet()
Student("Saurabh", "Nagpur").greet()
```
</details>

### 2. A counter that remembers

Write a `Counter` class with `tick()` and `reset()` methods and a `count` attribute. Tick three times, print, reset, print.

```text
3
0
```

<details><summary>Solution</summary>

```python
class Counter:
    def __init__(self):
        self.count = 0

    def tick(self):
        self.count += 1

    def reset(self):
        self.count = 0

c = Counter()
c.tick()
c.tick()
c.tick()
print(c.count)
c.reset()
print(c.count)
```
</details>

### 3. A rectangle with methods

Write a `Rectangle` class with width and height, and methods `area()` and `perimeter()`. Print both for a 4 by 3 rectangle.

```text
12 14
```

<details><summary>Solution</summary>

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

r = Rectangle(4, 3)
print(r.area(), r.perimeter())
```
</details>

### 4. Two objects, two lists

Write a `Playlist` class where every playlist starts with its own empty `songs` list and has an `add(song)` method. Add one song to the first playlist only, then print both lists.

```text
['Tum Hi Ho'] []
```

<details><summary>Hint</summary>

The list must be created inside `__init__` with `self.songs = []`. A list written in the class body would be shared.
</details>

<details><summary>Solution</summary>

```python
class Playlist:
    def __init__(self):
        self.songs = []

    def add(self, song):
        self.songs.append(song)

mine = Playlist()
yours = Playlist()
mine.add("Tum Hi Ho")
print(mine.songs, yours.songs)
```
</details>

---

## Core

### 5. A wallet with rules

Write a `Wallet` class with a balance, `add(amount)` that refuses amounts of zero or less, and `spend(amount)` that refuses an amount above the balance. Each method prints what happened. Start with ₹500.

```text
Added ₹200. Balance ₹700
Invalid amount.
Not enough balance.
Spent ₹300. Balance ₹400
```

<details><summary>Solution</summary>

```python
class Wallet:
    def __init__(self, balance):
        self.balance = balance

    def add(self, amount):
        if amount <= 0:
            print("Invalid amount.")
            return
        self.balance += amount
        print(f"Added ₹{amount}. Balance ₹{self.balance}")

    def spend(self, amount):
        if amount > self.balance:
            print("Not enough balance.")
            return
        self.balance -= amount
        print(f"Spent ₹{amount}. Balance ₹{self.balance}")

w = Wallet(500)
w.add(200)
w.add(-50)
w.spend(1000)
w.spend(300)
```
</details>

### 6. A private PIN

Write a `Card` class that stores the PIN with a double underscore, and a `check(pin)` method that returns True or False. Show that `check` works and that reading the PIN directly fails.

```text
True False
AttributeError
```

<details><summary>Hint</summary>

Store it as `self.__pin`. Reading `card.__pin` from outside raises `AttributeError`; catch nothing, just know it fails, or wrap the read in a function and print the error type by hand.
</details>

<details><summary>Solution</summary>

```python
class Card:
    def __init__(self, pin):
        self.__pin = pin

    def check(self, pin):
        return pin == self.__pin

card = Card("4321")
print(card.check("4321"), card.check("0000"))
try:
    print(card.__pin)
except AttributeError:
    print("AttributeError")
```

(`try` and `except` arrive in Class 13; here they only let the program keep going after the error.)
</details>

### 7. Count the objects

Add a class variable `count` to a `Student` class and increase it inside `__init__`, so the class knows how many students have been created. Print it after making three.

```text
3
```

<details><summary>Hint</summary>

`Student.count += 1` inside `__init__` changes the class variable, not an instance one.
</details>

<details><summary>Solution</summary>

```python
class Student:
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1

Student("Akshay")
Student("Amit")
Student("Aanand")
print(Student.count)
```
</details>

### 8. Inherit a describe()

Write a `Vehicle` class with a name and a `describe()` method, and a `Bike(Vehicle)` class that adds a `gears` attribute through `super().__init__` and overrides `describe()`. Print both descriptions.

```text
Nano is a vehicle.
Splendor is a bike with 4 gears.
```

<details><summary>Solution</summary>

```python
class Vehicle:
    def __init__(self, name):
        self.name = name

    def describe(self):
        return f"{self.name} is a vehicle."

class Bike(Vehicle):
    def __init__(self, name, gears):
        super().__init__(name)
        self.gears = gears

    def describe(self):
        return f"{self.name} is a bike with {self.gears} gears."

print(Vehicle("Nano").describe())
print(Bike("Splendor", 4).describe())
```
</details>

### 9. One loop, many shapes

Write `Square` and `Circle` classes, each with an `area()` method (use 3.14 for pi). Put one of each in a list and print every area with one loop, rounded to two decimals.

```text
16
28.26
```

<details><summary>Solution</summary>

```python
class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

for shape in [Square(4), Circle(3)]:
    print(round(shape.area(), 2))
```
</details>

---

## Challenge

### 10. A Transaction with a receipt

Write a `Transaction` class with payee, amount and mode, and a `receipt()` method that returns the Class 7 receipt line with the mode in capitals. Make a list of three transactions, print each receipt, and the total with `sum` over a `map`.

```text
Paid ₹600 to Praveen via UPI
Paid ₹250 to Vamsi via CARD
Paid ₹1500 to Sathvik via UPI
Total ₹2350
```

<details><summary>Solution</summary>

```python
class Transaction:
    def __init__(self, payee, amount, mode):
        self.payee = payee
        self.amount = amount
        self.mode = mode

    def receipt(self):
        return f"Paid ₹{self.amount} to {self.payee} via {self.mode.upper()}"

history = [Transaction("Praveen", 600, "upi"), Transaction("Vamsi", 250, "card"), Transaction("Sathvik", 1500, "upi")]
for t in history:
    print(t.receipt())
print("Total ₹" + str(sum(map(lambda t: t.amount, history))))
```
</details>

### 11. A library of books

Write a `Book` class (title, author, copies) with `issue()` and `give_back()` methods that change the copies and print a message or `Not available`. Write a `Library` class that holds a list of books, with `add(book)` and `search(word)` that prints the titles containing the word. Build the Class 9 library this way.

```text
Issued Python Basics. 2 left.
Not available
Python Basics
Data Science 101
```

<details><summary>Hint</summary>

The library's list goes in its `__init__`. `search` loops over `self.books` and tests `word.lower() in book.title.lower()`.
</details>

<details><summary>Solution</summary>

```python
class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

    def issue(self):
        if self.copies == 0:
            print("Not available")
            return
        self.copies -= 1
        print(f"Issued {self.title}. {self.copies} left.")

    def give_back(self):
        self.copies += 1

class Library:
    def __init__(self):
        self.books = []

    def add(self, book):
        self.books.append(book)

    def search(self, word):
        for book in self.books:
            if word.lower() in book.title.lower():
                print(book.title)

lib = Library()
lib.add(Book("Python Basics", "R. Rao", 3))
lib.add(Book("Data Science 101", "S. Iyer", 0))
lib.books[0].issue()
lib.books[1].issue()
lib.search("python")
lib.search("data")
```
</details>

### 12. Predict, then run

Without running, write down what each line prints or which error it raises. Then run and compare.

```python
class A:
    tag = "a"
    def __init__(self, n):
        self.n = n
    def show(self):
        return f"{self.tag}{self.n}"

class B(A):
    tag = "b"

x = A(1)
y = B(2)
print(x.show(), y.show())
print(isinstance(y, A), isinstance(x, B))
y.tag = "z"
print(y.show(), A.tag, B.tag)
print(A(1) == A(1))
z = x
z.n = 9
print(x.n)
print(A.show(x))
A.show()
```

<details><summary>Answer</summary>

```text
a1 b2
True False
z2 a b
False
9
a9
TypeError: A.show() missing 1 required positional argument: 'self'
```

`y.show()` finds `tag` on B first. `isinstance(y, A)` is True because a B is an A; an A is not a B. `y.tag = "z"` makes an instance attribute on y only; the class values are untouched. Two separate objects are never `==` unless the class says how to compare them (Class 11 does not). `z = x` is two names for one object, so `x.n` changed. `A.show(x)` is what `x.show()` means. The last line passes nothing as `self`.
</details>

---

Finished all twelve? Give the `Wallet` in problem 5 a `PremiumWallet` child that adds 1% cashback on every spend, without copying `spend`: call `super().spend(amount)` and then add the cashback.
