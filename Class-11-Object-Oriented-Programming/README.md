# Class 11 · Object-Oriented Programming

PaisaPay has one account: a balance, a PIN and a history passed into every function. Make it fifty accounts and the shape breaks. Today the data and the rules that work on it move into one thing, a class, and we make as many accounts as we need from it.

The class opens by finishing Class 10: `reduce` with its premise, chaining, `sorted` with a key, and a function that returns a function. Sections 0 and 1 are that material.

**By the end of this class you can:**

- Combine a list into one value with `reduce`, and say why it lives in `functools`.
- Write a function that returns a function, and use it as a rule factory.
- Explain the difference between a class and an object, write a class with `__init__` and methods, and say what `self` is.
- Tell a class variable from an instance variable, and avoid the shared-list trap.
- Keep data inside an object with a double underscore and change it only through methods.
- Use inheritance with `super()`, override a method, and explain polymorphism.

## How to use this folder

| File | What it is |
|---|---|
| [`index.html`](index.html) | The interactive class page. [Open it here](https://prateekscaler.github.io/AIML-Jul26-Batch3-Python/Class-11-Object-Oriented-Programming/), no download needed. **Step by step** shows a little at a time (press → or Next). **Show everything** gives the whole class on one page. |
| [`code/`](code/) | Every example from the class as a runnable file, in order. |
| [`code/paisapay_v11.py`](code/paisapay_v11.py) | Today's version of our course project. |
| [`Python-Class-11-Object-Oriented-Programming.ipynb`](Python-Class-11-Object-Oriented-Programming.ipynb) | The same examples as one notebook. [Open it in Google Colab](https://colab.research.google.com/github/prateekScaler/AIML-Jul26-Batch3-Python/blob/main/Class-11-Object-Oriented-Programming/Python-Class-11-Object-Oriented-Programming.ipynb) and run the cells, nothing to install. |
| [`PRACTICE.md`](PRACTICE.md) | Twelve coding problems on classes, objects, inheritance and encapsulation, easy to hard, with sample output, hints and solutions. |
| [`ASSIGNMENT.md`](ASSIGNMENT.md) | Predict the output, write programs, grow PaisaPay, think it through. |
| [`INTERVIEW-READINESS.md`](INTERVIEW-READINESS.md) | Interview questions, gotchas and AI-era questions on today's topics. |

Run the code in [PyLens](https://scaler-pylens.vercel.app/), or on your own machine with `python3 filename.py` (Python 3.10 or newer, because PaisaPay uses `match`).

Official post-read for this class: https://scaler-content.github.io/python-Foundations-10/

---

## 0. Finishing Class 10: reduce, chaining, sorted with a key

```python
from functools import reduce

numbers = [1, 2, 3, 4]
total = reduce(lambda a, b: a + b, numbers)       # 1+2 is 3, 3+3 is 6, 6+4 is 10
product = reduce(lambda a, b: a * b, numbers, 1)  # 24, starting from 1
```

`map` changes every item and `filter` keeps some; both give back a collection. `reduce` is different: it combines everything into one value. It combines the first two items, then that result with the next, and so on; in the lambda, `a` is the running answer and `b` is the next item. A third argument is the starting value: what the running answer holds before the first item. Pick one that changes nothing, 0 for adding and 1 for multiplying, and an empty list gives that start back instead of `TypeError: reduce() of empty iterable with no initial value`.

**The import matters.** `map` and `filter` are built in; `reduce` lives in the `functools` module, and without `from functools import reduce` you get `NameError: name 'reduce' is not defined`. Think of Python as a kitchen. About 70 built-in functions sit on the counter, ready before your first line runs: `print`, `len`, `sum`, `sorted`, `map`, `filter`. Everything else is in drawers, the modules: `math` has `sqrt`, `random` has `randint`, `functools` has `reduce`. A drawer stays closed until you `import` it. The counter holds what nearly every program needs; what only some programs need goes in a drawer, so a small script starts fast and your own names clash with nothing. Even the counter is a module, `builtins`, which Python opens for you: `import builtins; print(builtins.len is len)` prints `True`. Python 2 kept `reduce` on the counter; few programs used it, so Python 3 moved it to a drawer.

> **Real world, 2005.** In Python 2, `reduce` was a built-in next to `map` and `filter`. Guido van Rossum, Python's creator, wrote that almost every `reduce` he saw made him stop and work out what it did, where a plain loop or `sum` read better. Python 3 moved it into `functools`. For a total, `sum(amounts)` beats a reduce. [Guido van Rossum, "The fate of reduce() in Python 3000"](https://www.artima.com/weblogs/viewpost.jsp?thread=98196) · [Python docs: functools.reduce](https://docs.python.org/3/library/functools.html#functools.reduce)

> **Real world, 2004.** To index the whole web, Google needed thousands of machines on one job. Jeffrey Dean and Sanjay Ghemawat split every job into two steps, map each page to (word, count) pairs and reduce all the pairs for a word into one total, and named the system MapReduce after the two functional tools. [Google Research: MapReduce](https://research.google/pubs/mapreduce-simplified-data-processing-on-large-clusters/)

### Chaining: read from the inside out

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
print(result)    # [4, 16, 36, 64, 100]
```

The innermost call runs first: `filter` keeps the even numbers, `map` squares what filter hands it, `list` collects. If one line is hard to read, two are allowed: `evens = filter(...)` then `squares = map(..., evens)`.

### sorted with a key

```python
payments = [("Hitender", 600, "upi"),
            ("Saurabh", 250, "card"),
            ("Prajnika", 1500, "upi")]

print(sorted(payments, key=lambda p: p[1]))
# [('Saurabh', 250, 'card'), ('Hitender', 600, 'upi'), ('Prajnika', 1500, 'upi')]
# both print ('Prajnika', 1500, 'upi')
print(sorted(payments, key=lambda p: p[1], reverse=True)[0])
print(max(payments, key=lambda p: p[1]))
```

`sorted` has two switches: `reverse=True` says which way, `sorted(amounts, reverse=True)` gives biggest first and leaves `amounts` alone; `key` says what to compare. Without a key, tuples sort by their first item, the names. The key is a function that hands `sorted` one value per record to compare; the records themselves come back, in that order. `max` and `min` take the same key. When two keys tie, the original order is kept. `sort()` with a key changes the list in place and gives None; `sorted` makes a new list, exactly as in Class 6. Full code: [`code/00_chain_and_sorted.py`](code/00_chain_and_sorted.py). [Python docs: Sorting HOWTO, key functions](https://docs.python.org/3/howto/sorting.html#key-functions)

## 1. Finishing Class 10: a function that returns a function

```python
def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)
print(double(5), triple(5))     # 10 15

def at_least(minimum):
    return lambda amount: amount >= minimum

is_big = at_least(500)
print(is_big(600), is_big(90))                        # True False
print(list(filter(at_least(1000), [600, 250, 1500]))) # [1500]
```

`make_multiplier(2)` does not return a number. It returns a new function that remembers `n` was 2; `double` and `triple` are separate functions with their own remembered `n`. Last class a function took a function; this is the other direction, a function that returns one. Both are higher-order. `at_least` is a rule factory: change the minimum in one place, or hand a fresh rule straight to `filter`. Full code: [`code/01_returns_function.py`](code/01_returns_function.py).

---

## 2. Why classes

PaisaPay v10 keeps `balance`, `saved_pin` and `history` as three variables, and `pay` takes the balance in and gives it back. Fifty accounts means fifty sets of three variables, the right balance and the right history passed to every call, and no way to say "all accounts". What we want is one thing that holds an account's data and the rules that work on it, and a way to make as many as we need. That is a class.

A **class** is a blueprint: what every account has and can do, with no money in it. An **object**, also called an instance, is one real account with its own numbers. One blueprint, as many houses as you like.

You have been using objects since Class 6. `5` is an int object, `"abc"` a str object, a list a list object, and `type()` names the class. Every method you have called, `.upper()`, `.append()`, `.get()`, was a class at work. Today you write the class yourself. [Python docs: objects, values and types](https://docs.python.org/3/reference/datamodel.html#objects-values-and-types)

## 3. A class, objects, `__init__` and `self`

```python
class Dog:
    pass

rex = Dog()
fido = Dog()
print(rex)            # <__main__.Dog object at 0x...>
print(rex == fido)    # False: two separate objects from one blueprint
```

`class` starts a new type of thing, `Dog` is its name (capitalised by convention), the colon starts the body, and `pass` means nothing here yet. Every `Dog()` builds a new, independent object.

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

rex = Dog("Rex", "Labrador")
fido = Dog("Fido", "Beagle")
print(rex.name, fido.name)    # Rex Fido
```

`__init__` runs by itself when you write `Dog("Rex", "Labrador")`; you never call it. The two underscores on each side (say "dunder init") mark a name that Python itself calls at a set moment, so it cannot clash with your own method names; later you will meet `__str__`, called when you print an object, and `__len__`, called by `len()`. You never invent your own dunder names. `self` is the object this code is running on: the same `__init__` ran twice, and `self` was rex the first time and fido the second. It is not a keyword, only the name everyone gives the first parameter of a method. Values stored through `self.` are **instance attributes** and belong to that one object.

When you call `rex.bark()`, Python passes rex as `self`: `rex.bark()` is `Dog.bark(rex)` in disguise. You write `self` when defining a method, never when calling it. A method written without `self` fails with `TypeError: meow() takes 0 positional arguments but 1 was given`, the one being the object.

## 4. Methods

```python
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
rex.bark()                 # Rex says Woof!
print(rex.describe())      # Rex is 3 years old.
rex.have_birthday()
print(rex.describe())      # Rex is 4 years old.
```

A method is a function inside the class, and it takes `self` first. `bark` reads `self.name`, the name of the dog it was called on. `have_birthday` changes `self.age`: a method can change its own object, and the object keeps its state between calls. This is how an account remembers its balance.

**PaisaPay v11, build 1.** The `(name, amount, mode)` tuple becomes a `Transaction` object with named parts, `t.amount` instead of `t[1]`, and its own `describe()`.

## 5. Class variables and the shared-list trap

```python
class Dog:
    species = "Canis familiaris"      # class variable: one value for every dog

    def __init__(self, name):
        self.name = name              # instance variable: this dog only
```

Some data is true for every object; write it in the class body, outside `__init__`. Safe here, because a string cannot change. The trouble starts with a list:

```python
class Dog:
    tricks = []

    def __init__(self, name):
        self.name = name

rex = Dog("Rex")
fido = Dog("Fido")
rex.tricks.append("sit")
print(rex.tricks, fido.tricks)     # ['sit'] ['sit']
```

There is only one `tricks` list. It belongs to the class, every dog looks at it, and `append` changed it in place: Class 6's two-names-one-list, one level up. The fix is a fresh list per object, made inside `__init__`:

```python
class Dog:
    def __init__(self, name):
        self.name = name
        self.tricks = []
```

Now `rex.tricks` is `['sit']` and `fido.tricks` is `[]`. The rule: a class variable for what is the same for every object; `self.x` in `__init__` for what belongs to one object, and always for a list or a dictionary. Assigning `a.bank = "OtherPay"` to one object is safe: it makes a new instance attribute on that object and hides the class one; the others still see the class value. Mutating a shared list is the trap.

> **Industry practice.** Python's own tutorial uses this exact Dog-and-tricks example, labelled "mistaken use of a class variable", and names the cause: shared data has surprising effects with mutable objects such as lists and dictionaries. [Python tutorial: class and instance variables](https://docs.python.org/3/tutorial/classes.html#class-and-instance-variables)

**PaisaPay v11, build 2.** An `Account` class holds `owner`, `balance`, `pin` and `history`, with `self.history = []` in `__init__`, so every account has its own. `pay` no longer takes a balance and gives one back: it changes its own.

## 6. Encapsulation and abstraction

```python
class OpenAccount:
    def __init__(self, balance):
        self.balance = balance

account = OpenAccount(100)
account.balance = -500             # nothing stops it
print(account.balance)             # -500
```

With the data open, the rule "no negative balance" lives nowhere: any line in the program can set `balance` to anything. The fix puts the data inside and makes the methods the only door.

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

account = BankAccount(100)
account.deposit(50)
account.deposit(-500)              # refused by the rule inside
print(account.get_balance())       # 150
print(account.__balance)           # AttributeError: no attribute '__balance'
```

**Encapsulation** keeps the data inside the object and makes the methods the only door, so nobody can skip the rule in `deposit`. Two leading underscores say "internal". Python renames `__balance` to `_BankAccount__balance` inside the class (name mangling), which is why the direct read fails; `account._BankAccount__balance` still works. It is a speed bump and a strong "do not", not a lock. Writing `account.__balance = 1000000` from outside creates a new, unrelated attribute and changes nothing.

**Abstraction** is the other half: whoever calls `deposit(50)` does not need to know the rule inside or how the balance is stored. Encapsulation hides the data; abstraction hides the steps.

**PaisaPay v11, build 3.** The balance and the PIN become `__balance` and `__pin`, read through `get_balance()` and checked through `check_pin()`. The menu never sees the real PIN.

## 7. Inheritance, super(), overriding, polymorphism

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def describe(self):
        return f"{self.name} is an employee."

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def describe(self):
        return f"{self.name} manages a team of {self.team_size}."

class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def describe(self):
        return f"{self.name} writes code in {self.language}."

for person in [Manager("Chitransh", 90000, 5), Developer("Rahul", 75000, "Python"), Employee("Prajnika", 60000)]:
    print(person.describe())
```

```text
Chitransh manages a team of 5.
Rahul writes code in Python.
Prajnika is an employee.
```

`class Manager(Employee)` means Manager **inherits** from Employee: everything Employee can do, Manager can do, with no new code. Employee is the parent (base class), Manager the child (subclass). `super().__init__(name, salary)` runs the parent's `__init__` on this same object, then the child adds what is new; forget that line and `mgr.name` is an `AttributeError`. A child can **override** a method: Python looks in the object's own class first, then the parent. **Polymorphism** means one call, many forms: the loop calls `describe()` the same way and each object answers its own way. It does not even need a shared parent; Python only needs the method to exist on the object.

> **Industry practice.** `bool` is a child class of `int`: the docs say booleans are a subtype of integers. So `True + True` is 2 and `sum([True, False, True])` counts the Trues. A child class is its parent plus something. [Python docs: numeric types](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)

**PaisaPay v11, build 4.** `PremiumAccount(Account)` overrides `fee_for` to return 0 and `cashback_for` to double the parent's answer. `pay` is written once in Account and calls `self.fee_for(mode)`; for a premium account that is the overridden one.

## 8. Mini project: every idea in one program

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def describe(self):
        return f"{self.name} is an employee."
```

Manager adds `team_size`, Developer adds `language`, each with its own `describe()` and a `super().__init__`. A loop over a mixed list prints each description and salary: classes and objects, `__init__` and `self`, `super()`, overriding, polymorphism, and a private salary read through a method. Full code: [`code/08_employees.py`](code/08_employees.py).

## 9. Errors and debug clinic

| You see | It means | Fix |
|---|---|---|
| `TypeError: Cat.meow() takes 0 positional arguments but 1 was given` | a method without `self` | add `self` as the first parameter |
| `TypeError: Dog.__init__() missing 1 required positional argument: 'breed'` | `Dog()` called without what `__init__` needs | pass every argument after `self` |
| `AttributeError: 'Dog' object has no attribute 'age'` | never set, or set only on another object | set it in `__init__` |
| `AttributeError: 'Manager' object has no attribute 'name'` | the child's `__init__` never called the parent's | `super().__init__(...)` |
| `AttributeError: no attribute '__balance'` | reading a double-underscore attribute from outside | use the method |
| every object shares one list | a mutable class variable | create it in `__init__` |
| `balance = balance` inside `__init__` | a local variable that dies with the call | `self.balance = balance` |

## Project: PaisaPay v11

Version 11 is v10 plus classes. A `Transaction` replaces the tuple; an `Account` holds the owner, a private balance, a private PIN and its own history, and does the paying; a `PremiumAccount` inherits everything and overrides the fee and cashback rules. The menu makes one account of the chosen kind and calls its methods.

```python
class Account:
    def __init__(self, owner, balance, pin):
        self.owner = owner
        self.__balance = balance
        self.__pin = pin
        self.history = []

    def get_balance(self):
        return self.__balance

    def check_pin(self, pin):
        return pin == self.__pin

    def fee_for(self, mode):
        if mode == "card":
            return 5
        elif mode == "netbanking":
            return 2
        return 0

    def pay(self, upi_id, amount, mode="upi"):
        fee = self.fee_for(mode)
        if amount + fee > self.__balance:
            print("Insufficient balance. Payment refused.")
            return
        cashback = self.cashback_for(amount)
        self.__balance = self.__balance - amount - fee + cashback
        payee = name_for(upi_id)
        self.history.append(Transaction(payee, amount, mode, fee, cashback))
        print(f"Paid ₹{amount} to {payee} via {mode_name(mode)}")
        print(f"Fee ₹{fee} | Cashback ₹{cashback} | Balance ₹{self.__balance}")


class PremiumAccount(Account):
    def fee_for(self, mode):
        return 0

    def cashback_for(self, amount):
        return super().cashback_for(amount) * 2
```

The full program is [`code/paisapay_v11.py`](code/paisapay_v11.py). A sample run on a premium account:

```text
Account type (basic / premium): premium

1 Pay  2 Balance  3 Statement  4 Exit  5 Add
Choose: 1
Pay to (UPI ID): sumit@ybl
Amount in rupees: 600
Mode (upi / card / netbanking): card
UPI PIN: 4321
Paid ₹600 to Sumit via Card
Fee ₹0 | Cashback ₹20 | Balance ₹420
```

What v11 cannot do yet: check a UPI ID or a card number properly, which is regex in Class 12; and remember anything after the program ends, which is files in Class 13.

## Recap

Before reading on, write your own three-point recap: what would you tell a friend who missed this class? Then compare.

- **Class**: the blueprint. **Object**: one thing built from it, with its own data.
- **`__init__`** runs when an object is made. **`self`** is the object a method runs on; write it when defining, never when calling.
- **Class variable**: one value for all. A list there is one list for all: make lists in `__init__`.
- **Encapsulation** hides data behind methods; **abstraction** hides steps behind a name.
- **Inheritance** reuses a parent's code, **`super()`** runs the parent's setup, **overriding** replaces a method, **polymorphism** lets one call do many things.
- **PaisaPay v11**: Transaction and Account objects, a private balance and PIN, a PremiumAccount by inheritance.

Next class: classes continue from `self` and methods, through to PaisaPay v11. Regular expressions after that.
