# Assignment · Class 13

Practice for regular expressions, and for encapsulation, polymorphism and inheritance in practice: private attributes, one loop over many classes, chains of parents, `super()` inside an overriding method, `isinstance`, and the is-a or has-a choice. Do Part A on paper first. Write Parts B and C yourself before asking any AI assistant. For more coding problems with solutions, see [`PRACTICE.md`](PRACTICE.md).

Run your programs in [PyLens](https://scaler-pylens.vercel.app/) or with `python3 filename.py`.

## Part A · Predict the output (no running)

Write down what each snippet prints, or which error it raises. Then run it and compare.

**A1**
```python
class Box:
    def __init__(self):
        self.__items = []

    def add(self, x):
        self.__items.append(x)

    def count(self):
        return len(self.__items)

b = Box()
b.add(1)
b.add(2)
print(b.count())
print(b.__items)
```

**A2**
```python
class A:
    def hi(self):
        return "A"

class B(A):
    def hi(self):
        return "B" + super().hi()

class C(B):
    pass

print(C().hi())
```

**A3**
```python
class A:
    pass

class B(A):
    pass

b = B()
print(isinstance(b, A), isinstance(A(), B), type(b) == A)
```

**A4**
```python
class Parent:
    def __init__(self):
        self.x = 1

class Child(Parent):
    def __init__(self):
        self.y = 2
        super().__init__()

c = Child()
print(c.x, c.y)
```

**A5**
```python
class Dog:
    def speak(self):
        return "Woof"

class Duck:
    def speak(self):
        return "Quack"

class Stone:
    pass

for thing in [Dog(), Duck(), Stone()]:
    print(thing.speak())
```

**A6**
```python
class Wallet:
    def pay(self, amount):
        return f"paid {amount}"

class Capped(Wallet):
    def pay(self, amount):
        if amount > 100:
            return "refused"
        return super().pay(amount)

print(Capped().pay(50), Capped().pay(500))
```

**A7**
```python
class Account:
    def __init__(self, balance):
        self.__balance = balance

a = Account(100)
a.__balance = 999
print(a._Account__balance, a.__balance)
```

**A8**
```python
class Employee:
    def pay(self):
        return 100

class Manager(Employee):
    def bonus(self):
        return 10

print(Manager().pay() + Manager().bonus())
print(Employee().bonus())
```

**A9**
```python
import re
print(re.match(r"\d+", "abc123"))
print(re.search(r"\d+", "abc123").group())
```

**A10**
```python
import re
for w in ["bat", "bt", "boat"]:
    print(w, bool(re.fullmatch(r"b.t", w)))
```

**A11**
```python
import re
print(re.findall(r"\d+", "Rs.600 and Rs.1500"))
print(re.findall(r"Rs\.(\d)", "Rs.600 and Rs.1500"))
```

**A12**
```python
import re
m = re.search(r"(\w+)@(\w+)", "pay sumit@ybl now")
print(m.group(0), m.group(1), m.group(2))
```

## Part B · Write the program

**B1. A private marks list.** A `Student` whose marks are stored as `__marks`, with `add_mark(m)` that refuses marks outside 0 to 100 and prints `Refused m`, and `average()`. Add 80, 120 and 90; print the average. Show that `s.__marks` fails.

**B2. One loop, many shapes.** `Square`, `Circle` and `Triangle` classes, each with an `area()`, no shared parent. Print every area from one list with one loop, rounded to two decimals.

**B3. A chain of three.** `Vehicle` (name), `Car(Vehicle)` (adds seats), `ElectricCar(Car)` (adds range in km). Every `__init__` calls `super().__init__`. A `describe()` on Vehicle returns the name; Car and ElectricCar extend it with `super().describe()` so that an ElectricCar describes as `Nexon, 5 seats, 300 km`.

**B4. Count by kind.** Using B3, make a list of two cars and one electric car and print three numbers: how many are vehicles, how many are cars, how many are electric cars. Use `isinstance`.

**B5. Is-a or has-a.** For each pair, write one sentence and then the two class headers (with or without a parent): Teacher and Person; Classroom and Student; Dog and Animal; Order and OrderItem; UPI payment and Payment.

**B6. Fix the bugs.** This program should print `Rahul writes Python. Bonus 5000`. It has three mistakes. Find and fix each one, and write what went wrong.

```python
class Employee:
    def __init__(self, name):
        self.__name = name

    def describe(self):
        return f"{self.__name} is an employee."

class Developer(Employee):
    def __init__(self, name, language):
        self.language = language

    def describe(self):
        return f"{self.__name} writes {self.language}."

    def bonus():
        return 5000

d = Developer("Rahul", "Python")
print(d.describe(), "Bonus", d.bonus())
```

**B7. Find the hashtags.** Print every hashtag in `"Loved the #python class and #regex too, #AIML"` as a list, with `re.findall`.

**B8. Date reader.** From `"Paid on 04-11-2026 and 15-12-2026"`, print each date as `month 11, year 2026`, using groups.

## Part C · Project: grow PaisaPay v13

Start from [`code/paisapay_v13.py`](code/paisapay_v13.py).

1. **A StudentAccount.** A third class that inherits from Account, pays no fee on UPI only, and caps every payment at ₹2000 with the message `Student accounts are limited to ₹2000 per payment.` Override `fee_for` and `pay`; inside `pay`, check the cap and then call `super().pay(...)`.
2. **Three kinds at the start.** The menu asks `Account type (basic / premium / student)` and makes the right object. Everything else works unchanged.
3. **A transfer.** Add `transfer(self, other, amount)` to Account that moves money to another account through the existing methods, refusing when the balance is too low. Check that a StudentAccount's cap also applies to transfers, and say in one comment why that happens without any extra code.
4. **An IFSC check.** Add `is_valid_ifsc(code)` and a menu item that checks one: four capital letters, a zero, six capital letters or digits.
5. **A stricter SMS reader.** Make `read_bank_sms` also return the date from the message, as a fourth value.

Target output for one run (a student account, PIN 4321):

```text
Account type (basic / premium / student): student
Choose: 1
Pay to (UPI ID): sumit@ybl
Amount in rupees: 2500
Mode (upi / card / netbanking): upi
UPI PIN: 4321
Student accounts are limited to ₹2000 per payment.
Choose: 1
Pay to (UPI ID): sumit@ybl
Amount in rupees: 600
Mode (upi / card / netbanking): upi
UPI PIN: 4321
Paid ₹600 to Sumit via UPI
Fee ₹0 | Cashback ₹10 | Balance ₹410
```

## Part D · Think it through

Write two or three lines for each.

1. The double underscore can be bypassed with `_Account__balance`. If it is not a real lock, what does it buy the next programmer who reads the class?
2. The menu loop never checks whether the account is basic, premium or student, yet each pays a different fee. Name the idea and say where the decision actually happens.
3. `Director(Manager)` calls `super().__init__` once, yet three `__init__` methods run. Trace the calls.
4. Someone proposes `class Transaction(Account)` "because both are about money". Write the sentence that shows why it is wrong, and what Transaction would wrongly inherit.
5. `is_valid_upi_id` uses `fullmatch`. What wrong input would pass if it used `search`? Try it.

## With AI (after your own attempt)

Paste your finished Part C program into an AI assistant and ask:

> "List every method that StudentAccount inherits unchanged, every method it overrides, and for each override say whether it calls super(). Do not change the code."

Check each claim against your file. Then ask it to propose one more subclass and decide, before reading its code, which methods it would override and whether each one should call `super()`.
