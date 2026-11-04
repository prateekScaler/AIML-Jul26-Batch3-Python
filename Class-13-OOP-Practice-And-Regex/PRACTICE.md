# Practice problems · Class 13 · OOP in Practice, and Regular Expressions

Eighteen problems, easy to hard: twelve on object-oriented programming, six on regex. Each uses only what Classes 1 to 13 covered. Write every program yourself in [PyLens](https://scaler-pylens.vercel.app/) or with `python3`, run it against the sample, and only then open the hint or the solution.

How to work: for every class, say the sentence first. "A square is a shape" means inherit. "A library has books" means a list inside. When a child changes a rule, decide whether it adds a check (then call `super()`) or replaces the rule (then rewrite the method).

- [Warm-up](#warm-up) · problems 1 to 4
- [Core](#core) · problems 5 to 9
- [Challenge](#challenge) · problems 10 to 12
- [Regex](#regex) · problems 13 to 18

---

## Warm-up

### 1. A private counter

Write a `Counter` class whose count is stored as `__count`, with `tick()` and `value()` methods. Tick three times and print the value. Then show that reading `c.__count` from outside fails.

```text
3
AttributeError
```

<details><summary>Hint</summary>

The real name is `_Counter__count`. The plain name does not exist, so the read raises `AttributeError`.
</details>

<details><summary>Solution</summary>

```python
class Counter:
    def __init__(self):
        self.__count = 0

    def tick(self):
        self.__count += 1

    def value(self):
        return self.__count

c = Counter()
c.tick()
c.tick()
c.tick()
print(c.value())
try:
    print(c.__count)
except AttributeError:
    print("AttributeError")
```
</details>

### 2. A shape family

Write a `Shape` class with a name and a `describe()` method that returns `name with area N`, calling `self.area()`. Write `Square(Shape)` with a side and its own `area()`. Describe a square of side 3.

```text
square with area 9
```

<details><summary>Hint</summary>

`describe` lives on the parent and calls `self.area()`. For a square, `self` is the square, so the square's `area` runs.
</details>

<details><summary>Solution</summary>

```python
class Shape:
    def __init__(self, name):
        self.name = name

    def describe(self):
        return f"{self.name} with area {self.area()}"

class Square(Shape):
    def __init__(self, side):
        super().__init__("square")
        self.side = side

    def area(self):
        return self.side * self.side

print(Square(3).describe())
```
</details>

### 3. Extend, do not replace

A `Vehicle` has a name and a `describe()` that returns `name is a vehicle.` Write `Bike(Vehicle)` whose `describe()` returns the parent's sentence followed by ` It has 2 wheels.` Do not retype the parent's sentence.

```text
Splendor is a vehicle. It has 2 wheels.
```

<details><summary>Solution</summary>

```python
class Vehicle:
    def __init__(self, name):
        self.name = name

    def describe(self):
        return f"{self.name} is a vehicle."

class Bike(Vehicle):
    def describe(self):
        return super().describe() + " It has 2 wheels."

print(Bike("Splendor").describe())
```
</details>

### 4. Count with isinstance

Using the `Shape` and `Square` classes from problem 2, add `Circle(Shape)` with a radius (use 3.14). Make a list of two squares and one circle. Print how many items are a `Shape` and how many are a `Circle`.

```text
3 1
```

<details><summary>Hint</summary>

`isinstance(s, Shape)` is True for a Square too, because a Square is a Shape. `sum` over True and False counts the Trues: bool is an int.
</details>

<details><summary>Solution</summary>

```python
class Shape:
    def __init__(self, name):
        self.name = name

class Square(Shape):
    def __init__(self, side):
        super().__init__("square")
        self.side = side

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("circle")
        self.radius = radius

shapes = [Square(2), Circle(1), Square(5)]
print(sum(isinstance(s, Shape) for s in shapes), sum(isinstance(s, Circle) for s in shapes))
```
</details>

---

## Core

### 5. A capped wallet

Write a `Wallet` with a balance and `pay(amount)` that subtracts and prints `Paid N. Balance M`. Write `StudentWallet(Wallet)` that refuses any payment above 2000 with `Limit is 2000 per payment.` and otherwise pays like a normal wallet, without copying the paying code.

```text
Limit is 2000 per payment.
Paid 1200. Balance 3800
```

<details><summary>Hint</summary>

Check first, then `super().pay(amount)`.
</details>

<details><summary>Solution</summary>

```python
class Wallet:
    def __init__(self, balance):
        self.balance = balance

    def pay(self, amount):
        self.balance -= amount
        print(f"Paid {amount}. Balance {self.balance}")

class StudentWallet(Wallet):
    def pay(self, amount):
        if amount > 2000:
            print("Limit is 2000 per payment.")
            return
        super().pay(amount)

w = StudentWallet(5000)
w.pay(2500)
w.pay(1200)
```
</details>

### 6. One loop, three channels

Write `Email`, `SMS` and `Push` classes, each with a `send(message)` method that returns `Email: message`, `SMS: message` or `Push: message`. They share no parent. Send one message through all three with one loop.

```text
Email: Your OTP is 4821
SMS: Your OTP is 4821
Push: Your OTP is 4821
```

<details><summary>Hint</summary>

Polymorphism needs the method, not a parent.
</details>

<details><summary>Solution</summary>

```python
class Email:
    def send(self, message):
        return f"Email: {message}"

class SMS:
    def send(self, message):
        return f"SMS: {message}"

class Push:
    def send(self, message):
        return f"Push: {message}"

for channel in [Email(), SMS(), Push()]:
    print(channel.send("Your OTP is 4821"))
```
</details>

### 7. A chain of three

Write `Person` (name), `Student(Person)` (adds a course) and `Topper(Student)` (adds a rank). Each `__init__` calls `super().__init__`. Make a Topper and print all three attributes on one line.

```text
Sangeeta AIML 1
```

<details><summary>Solution</summary>

```python
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

class Topper(Student):
    def __init__(self, name, course, rank):
        super().__init__(name, course)
        self.rank = rank

t = Topper("Sangeeta", "AIML", 1)
print(t.name, t.course, t.rank)
```
</details>

### 8. A card that locks

Write a `Card` class with a private PIN and a private count of wrong attempts. `check(pin)` returns `True` for the right PIN, and after three wrong attempts returns `Locked` for every call, right or wrong.

```text
False False False
Locked
```

<details><summary>Hint</summary>

Two private attributes. The lock check comes first, before the PIN comparison.
</details>

<details><summary>Solution</summary>

```python
class Card:
    def __init__(self, pin):
        self.__pin = pin
        self.__wrong = 0

    def check(self, pin):
        if self.__wrong >= 3:
            return "Locked"
        if pin == self.__pin:
            return True
        self.__wrong += 1
        return False

card = Card("4321")
print(card.check("0000"), card.check("1111"), card.check("2222"))
print(card.check("4321"))
```
</details>

### 9. Has-a, not is-a

Write a `Book` (title, copies) and a `Library` that holds a list of books, with `add(book)` and `issue(title)` that lowers the copies and prints `Issued title` or `Not available`. Book must not inherit from Library.

```text
Issued Python Basics
Not available
```

<details><summary>Hint</summary>

A library has books: a list in `__init__`. A book is not a kind of library.
</details>

<details><summary>Solution</summary>

```python
class Book:
    def __init__(self, title, copies):
        self.title = title
        self.copies = copies

class Library:
    def __init__(self):
        self.books = []

    def add(self, book):
        self.books.append(book)

    def issue(self, title):
        for book in self.books:
            if book.title == title:
                if book.copies == 0:
                    print("Not available")
                    return
                book.copies -= 1
                print(f"Issued {title}")
                return
        print("Not available")

lib = Library()
lib.add(Book("Python Basics", 1))
lib.issue("Python Basics")
lib.issue("Python Basics")
```
</details>

---

## Challenge

### 10. Two kinds of account

Write `Account` with a balance and `withdraw(amount)` that refuses when the balance is too low (`Insufficient balance.`) and otherwise subtracts and prints `Withdrew N. Balance M`. Write `CurrentAccount(Account)` that allows going down to -5000 (an overdraft) and `SavingsAccount(Account)` that refuses any withdrawal above 20000 (`Daily limit is 20000.`). One loop withdraws 25000 from one of each kind, starting at 10000.

```text
Insufficient balance.
Insufficient balance.
Daily limit is 20000.
```

<details><summary>Hint</summary>

SavingsAccount adds a check and hands over with `super()`. CurrentAccount changes the rule itself, so it rewrites `withdraw`.
</details>

<details><summary>Solution</summary>

```python
class Account:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
            return
        self.balance -= amount
        print(f"Withdrew {amount}. Balance {self.balance}")

class CurrentAccount(Account):
    def withdraw(self, amount):
        if amount > self.balance + 5000:
            print("Insufficient balance.")
            return
        self.balance -= amount
        print(f"Withdrew {amount}. Balance {self.balance}")

class SavingsAccount(Account):
    def withdraw(self, amount):
        if amount > 20000:
            print("Daily limit is 20000.")
            return
        super().withdraw(amount)

for acc in [Account(10000), CurrentAccount(10000), SavingsAccount(10000)]:
    acc.withdraw(25000)
```
</details>

### 11. Payroll with a bonus

Write `Employee` (name, salary) with `pay()` returning the salary, and `Manager(Employee)` whose `pay()` returns the parent's pay plus a bonus of 10000. Print the total payroll of a mixed list with `sum` and `map`.

```text
235000
```

<details><summary>Solution</summary>

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def pay(self):
        return self.salary

class Manager(Employee):
    def pay(self):
        return super().pay() + 10000

staff = [Employee("Rahul", 75000), Manager("Chitransh", 90000), Employee("Prajnika", 60000)]
print(sum(map(lambda e: e.pay(), staff)))
```
</details>

### 12. Predict, then run

Without running, write down what each print shows. Then run and compare.

```text
BA
True False
True False
1 5
```

<details><summary>Answer</summary>

```python
class A:
    def __init__(self):
        self.__x = 1

    def who(self):
        return "A"

class B(A):
    def who(self):
        return "B" + super().who()

b = B()
print(b.who())
print(isinstance(b, A), type(b) == A)
print(hasattr(b, "_A__x"), hasattr(b, "__x"))
b.__x = 5
print(b._A__x, b.__x)
```

`BA`: the child runs and calls the parent through `super()`. A B is an A, but its exact type is B. The private attribute is stored as `_A__x`, so a plain `__x` does not exist until the outside assignment creates a new, unrelated attribute named `__x`; the real one is still 1.
</details>

---

## Regex

For regex, predict the output first. A pattern punishes guessing faster than anything else in this course.

### 13. Which messages have a number?

For each message, print the message and `True` or `False` for whether it contains a digit.

```text
Pay Kishor 500 True
Thank you False
Room 42 True
```

<details><summary>Solution</summary>

```python
import re

for message in ["Pay Kishor 500", "Thank you", "Room 42"]:
    print(message, bool(re.search(r"\d", message)))
```
</details>

### 14. A valid PIN

A UPI PIN here is exactly four digits. Check each string with `re.fullmatch`.

```text
4321 True
432 False
43210 False
43a1 False
```

<details><summary>Hint</summary>

`search` would find four digits inside `43210`. `fullmatch` needs the whole string to fit.
</details>

<details><summary>Solution</summary>

```python
import re

for pin in ["4321", "432", "43210", "43a1"]:
    print(pin, bool(re.fullmatch(r"\d{4}", pin)))
```
</details>

### 15. Total from a statement

Pull every rupee amount out of this text and print the total. Use a group so that you get the digits only.

```text
['600', '250', '1500']
2350
```

<details><summary>Hint</summary>

`.` must be escaped as `\.`. `findall` gives strings, so convert them before adding.
</details>

<details><summary>Solution</summary>

```python
import re

text = "Paid Rs.600 to Madhumaya, Rs.250 to Prince, Rs.1500 to Shubhodip"
amounts = re.findall(r"Rs\.(\d+)", text)
print(amounts)
print(sum(map(int, amounts)))
```
</details>

### 16. An Indian mobile number

A mobile number here has ten digits and starts with 6, 7, 8 or 9. Check each string.

```text
9876543210 True
5876543210 False
98765 False
98765432101 False
```

<details><summary>Hint</summary>

One character from a set, then exactly nine digits.
</details>

<details><summary>Solution</summary>

```python
import re

for number in ["9876543210", "5876543210", "98765", "98765432101"]:
    print(number, bool(re.fullmatch(r"[6-9]\d{9}", number)))
```
</details>

### 17. An IFSC code

An IFSC code has four capital letters, a zero, then six capital letters or digits. Check each string.

```text
HDFC0001234 True
SBIN0ABC123 True
HDFC1001234 False
hdfc0001234 False
```

<details><summary>Solution</summary>

```python
import re

for code in ["HDFC0001234", "SBIN0ABC123", "HDFC1001234", "hdfc0001234"]:
    print(code, bool(re.fullmatch(r"[A-Z]{4}0[A-Z0-9]{6}", code)))
```
</details>

### 18. Spending per payee

Read these bank messages with one pattern and print how much went to each payee, using a dictionary from Class 8.

```text
{'RAVI': 750, 'AAKASH': 250}
```

<details><summary>Hint</summary>

The last message has no amount, so `search` gives None. Check before you use the match.
</details>

<details><summary>Solution</summary>

```python
import re

messages = [
    "Rs.600 debited from a/c XX4321 to RAVI on 04-11-26",
    "Rs.250 debited from a/c XX4321 to AAKASH on 04-11-26",
    "Rs.150 debited from a/c XX4321 to RAVI on 05-11-26",
    "Your balance is low",
]
totals = {}
for sms in messages:
    m = re.search(r"Rs\.(\d+) debited from a/c XX\d{4} to (\w+)", sms)
    if m is not None:
        amount, payee = m.groups()
        totals[payee] = totals.get(payee, 0) + int(amount)
print(totals)
```
</details>

---

Finished them all? Give problem 10 a `StudentAccount` that pays no fee and caps every withdrawal at 2000, and write the one-line sentence that says why it inherits from `Account` rather than holding one.
