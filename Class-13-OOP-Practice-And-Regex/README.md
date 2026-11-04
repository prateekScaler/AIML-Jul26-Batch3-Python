# Class 13 · OOP in Practice, and Regular Expressions

Class 12 reached inheritance, `super()` and overriding. This class finishes object-oriented programming: encapsulation, polymorphism and six inheritance scenarios. Then a new tool, regular expressions: a small language for describing the shape of text, which PaisaPay uses to check a UPI ID and a PAN and to read a bank SMS.

**By the end of this class you can:**

- Keep data inside an object with a double underscore, say what name mangling does, and tell encapsulation from abstraction.
- Explain polymorphism and why it does not need a shared parent.
- Read a chain of classes and say where an attribute was set.
- Extend a parent's method with `super()` instead of retyping it.
- Use `isinstance` and know how it differs from `type`.
- Decide, from one sentence, whether two classes are is-a or has-a.
- Tell `re.search`, `re.match` and `re.fullmatch` apart.
- Read and write patterns with character classes and quantifiers.
- Pull every match out with `re.findall`, and pull pieces out with capturing groups.

## How to use this folder

| File | What it is |
|---|---|
| [`index.html`](index.html) | The interactive class page. [Open it here](https://prateekscaler.github.io/AIML-Jul26-Batch3-Python/Class-13-OOP-Practice-And-Regex/), no download needed. **Step by step** shows a little at a time (press → or Next). **Show everything** gives the whole class on one page. |
| [`code/`](code/) | Every example from the class as a runnable file, in order. |
| [`code/paisapay_v13.py`](code/paisapay_v13.py) | Our course project: classes finished, regex checks added. |
| [`Python-Class-13-OOP-Practice-And-Regex.ipynb`](Python-Class-13-OOP-Practice-And-Regex.ipynb) | The same examples as one notebook. [Open it in Google Colab](https://colab.research.google.com/github/prateekScaler/AIML-Jul26-Batch3-Python/blob/main/Class-13-OOP-Practice-And-Regex/Python-Class-13-OOP-Practice-And-Regex.ipynb) and run the cells, nothing to install. |
| [`PRACTICE.md`](PRACTICE.md) | Eighteen coding problems: twelve on encapsulation, polymorphism and inheritance, six on regex, with sample output, hints and solutions. |
| [`ASSIGNMENT.md`](ASSIGNMENT.md) | Predict the output, write programs, grow PaisaPay, think it through. |
| [`INTERVIEW-READINESS.md`](INTERVIEW-READINESS.md) | Interview questions, gotchas and AI-era questions on today's topics. |

Run the code in [PyLens](https://scaler-pylens.vercel.app/), or on your own machine with `python3 filename.py` (Python 3.10 or newer, because PaisaPay uses `match`).

Official post-reads for this class: https://scaler-content.github.io/python-Foundations-10/ (object-oriented programming) and https://scaler-content.github.io/python-Foundations-11/ (regular expressions)

---

## 1. Where Class 12 stopped

A method is a function inside a class, and `self` is the object it runs on. A class variable is one value on the class; a list there is shared by every object, so lists belong in `__init__`. `class Manager(Employee)` gives Manager everything Employee has, `super().__init__(...)` runs the parent's setup on the same object, and a child method with the parent's name overrides it. The three questions at the start of the class check exactly these.

## 2. Encapsulation and abstraction

```python
class OpenAccount:
    def __init__(self, balance):
        self.balance = balance

account = OpenAccount(100)
account.balance = -500             # nothing stops it
print(account.balance)             # -500
```

With the data open, the rule "no negative balance" lives nowhere: any line in the program can set `balance` to anything. The fix has two parts. First, two underscores on the name, and nothing else:

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

account = BankAccount(100)
print(account.__balance)           # AttributeError: no attribute '__balance'
```

Outside code can no longer read it by that name. Inside the class, `self.__balance` still works. That creates a new problem: nobody outside can read the balance or add money. So the second part adds methods, because methods live inside the class:

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
print(account._BankAccount__balance)  # 150: name mangling, the longer name still works
```

**Encapsulation** keeps the data inside the object and makes the methods the only door, so nobody can skip the rule in `deposit`. Two leading underscores say "internal". Python renames `__balance` to `_BankAccount__balance` inside the class (name mangling), which is why the direct read fails; `account._BankAccount__balance` still works. It is a speed bump and a strong "do not", not a lock. Writing `account.__balance = 1000000` from outside creates a new, unrelated attribute and changes nothing.

**Why the name?** To encapsulate means to put inside a capsule. Think of a medicine capsule:

| A capsule | A class |
|---|---|
| Keeps all the powder together in one piece | Keeps `__balance` and the methods that use it together in one class |
| Protects the powder: air and water stay out | Protects `__balance`: outside lines cannot reach it by name |
| One simple way to use it: swallow it, no measuring | One simple way to use it: call `deposit(50)`, no need to see inside |
| Can still be pulled open, if someone insists | `_BankAccount__balance` still works |

**Abstraction** is the other half: whoever calls `deposit(50)` does not need to know the rule inside or how the balance is stored. Encapsulation hides the data; abstraction hides the steps.

**PaisaPay, build 1.** The balance and the PIN become `__balance` and `__pin`, read through `get_balance()` and checked through `check_pin()`. The menu never sees the real PIN.

## 3. Inheritance recap, then polymorphism

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

**PaisaPay, build 2.** `PremiumAccount(Account)` overrides `fee_for` to return 0 and `cashback_for` to double the parent's answer. `pay` is written once in Account and calls `self.fee_for(mode)`; for a premium account that is the overridden one.

## 4. Six inheritance scenarios

```python
# Six inheritance scenarios: a chain of parents, extending a method, isinstance,
# a child's own method, a child that adds a check, and is-a versus has-a.
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

    def approve_leave(self, who):
        return f"{self.name} approved leave for {who}."


# 1. A chain: Director is a Manager, and a Manager is an Employee
class Director(Manager):
    def __init__(self, name, salary, team_size, region):
        super().__init__(name, salary, team_size)
        self.region = region

    # 2. Extend, do not replace: the parent's sentence, plus one more
    def describe(self):
        return super().describe() + f" Region: {self.region}."


d = Director("Sangeeta", 150000, 40, "South")
print(d.describe())
print(d.salary)                       # set by Employee.__init__, two levels up

# 3. isinstance: a Director is a Manager and an Employee; an Employee is not a Manager
e = Employee("Prajnika", 60000)
print(isinstance(d, Employee), isinstance(e, Manager))
print(type(d) == Manager, type(d).__name__)

# 4. A child's own method is not on the parent
print(d.approve_leave("Rahul"))
try:
    e.approve_leave("Rahul")
except AttributeError as err:
    print("AttributeError:", err)

# 5. A child adds a check, then hands over to the parent
class Wallet:
    def __init__(self, balance):
        self.balance = balance

    def pay(self, amount):
        self.balance -= amount
        print(f"Paid {amount}. Balance {self.balance}")


class StudentWallet(Wallet):
    def pay(self, amount):
        if amount > 2000:
            print("Student wallets are limited to 2000 per payment.")
            return
        super().pay(amount)


w = StudentWallet(5000)
w.pay(3000)
w.pay(1500)

# 6. is-a versus has-a: a Transaction is not a kind of Account, so no inheritance
class Transaction:
    def __init__(self, payee, amount):
        self.payee = payee
        self.amount = amount


class Account:
    def __init__(self, owner):
        self.owner = owner
        self.history = []          # has-a: an Account has Transactions

    def pay(self, payee, amount):
        self.history.append(Transaction(payee, amount))


a = Account("Vinay")
a.pay("Sumit", 600)
print(len(a.history), a.history[0].payee)
```

```text
Sangeeta manages a team of 40. Region: South.
150000
True False
False Director
Sangeeta approved leave for Rahul.
AttributeError: 'Employee' object has no attribute 'approve_leave'
Student wallets are limited to 2000 per payment.
Paid 1500. Balance 3500
1 Sumit
```

1. **A chain.** `Director(Manager)` and `Manager(Employee)`: each `super().__init__` hands the same object one level up, so `d.salary` was set by `Employee.__init__` two levels above. Reading an attribute looks in Director, then Manager, then Employee.
2. **Extend, do not replace.** `super().describe()` inside Director's `describe` reaches the next class up, Manager, and the child adds its own words. Override alone replaces; override plus `super()` extends.
3. **`isinstance` and `type`.** `isinstance(d, Employee)` is True because a Director is an Employee: it walks up the tree. `isinstance(e, Manager)` is False: the tree is never read downwards. `type(d) == Manager` is False because `type` names the exact class. Prefer `isinstance` whenever a child should count as its parent, which is almost always.
4. **One way.** Director reaches Manager's `approve_leave` by walking up. Employee has nothing above it, so `e.approve_leave(...)` is an `AttributeError`. Children get the parent's methods; parents never get the children's.
5. **A check, then hand over.** `StudentWallet.pay` refuses amounts above 2000, then calls `super().pay(amount)` for everything else. Nothing is copied. PaisaPay's `StudentAccount` in the assignment works the same way.
6. **Is-a or has-a.** Say the sentence. "A premium account is an account": inherit. "An account has transactions": a list inside. Inheriting for the wrong reason gives Transaction a `pay()` and a PIN it should never have. Full code: [`code/03_inheritance_scenarios.py`](code/03_inheritance_scenarios.py).

## 5. Mini project: every idea in one program

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

Manager adds `team_size`, Developer adds `language`, each with its own `describe()` and a `super().__init__`. A loop over a mixed list prints each description and salary: classes and objects, `__init__` and `self`, `super()`, overriding, polymorphism, and a private salary read through a method. Full code: [`code/04_employees.py`](code/04_employees.py).

## 6. Errors and debug clinic

| You see | It means | Fix |
|---|---|---|
| `TypeError: Cat.meow() takes 0 positional arguments but 1 was given` | a method without `self` | add `self` as the first parameter |
| `TypeError: Dog.__init__() missing 1 required positional argument: 'breed'` | `Dog()` called without what `__init__` needs | pass every argument after `self` |
| `AttributeError: 'Dog' object has no attribute 'age'` | never set, or set only on another object | set it in `__init__` |
| `AttributeError: 'Manager' object has no attribute 'name'` | the child's `__init__` never called the parent's | `super().__init__(...)` |
| `AttributeError: no attribute '__balance'` | reading a double-underscore attribute from outside | use the method |
| every object shares one list | a mutable class variable | create it in `__init__` |
| `balance = balance` inside `__init__` | a local variable that dies with the call | `self.balance = balance` |

## 7. Regular expressions

**What it solves.** Text with a pattern. Regex does three jobs: it checks a value (a valid PAN), pulls a piece out (the amount in a bank SMS), and finds matching lines (every ERROR in a log). It works in Python, JavaScript and Java, and in your editor's find box. It is free and fast, and it runs on your own machine.

**Which tool?** Use the simplest one that does the job.

| You want to know | Looking for | Use |
|---|---|---|
| Does the message contain "refund"? | exact text | `"refund" in message` |
| Does it contain a mobile number? | a shape | regex |
| Is the customer asking for money back, in any words? ("Mera paisa abhi tak wapas nahi aaya.") | a meaning | an LLM |

| | String method | Regex | LLM |
|---|---|---|---|
| Understands meaning | no | no | yes |
| Same input, same answer | always | always | not always |
| Speed | instant | fast, if the pattern is careful | seconds |
| Cost per call | free | free | usually paid |

They also work together: an LLM reads a messy letter and returns a PAN, and a regex checks that the answer has the shape of a PAN.

**Do you have to memorize it?** No. An AI assistant can write the pattern, and [regex101.com](https://regex101.com/) explains any pattern piece by piece. But the pattern can be wrong, so you must read it and test it on good and bad input. That is what this section teaches.

`in`, `find` and `split` test exact text. They cannot say "five digits, a dash, five digits". A regular expression, or regex, describes the shape of text. It is a small separate language: Python's `re` module reads the pattern. Write patterns as raw strings, `r"..."`, so a backslash reaches regex untouched.

### search, match, fullmatch

```python
import re

text = "concatenate"
print(re.search(r"cat", text))    # <re.Match object; span=(3, 6), match='cat'>
print(re.match(r"cat", text))     # None
```

`search` looks anywhere and gives a Match object, or None. `match` tests only the start of the string. `fullmatch` needs the whole string to fit, which makes it the right tool for checking one field, like a PIN or a PAN. A Match object counts as True and None as False, so `if re.search(...):` works.

### Metacharacters and classes

| Symbol | Means |
|---|---|
| `.` | any one character, except a newline |
| `^` `$` | start of the string, end of the string |
| `*` `+` `?` | zero or more, one or more, zero or one of the thing before |
| `{3}` `{2,4}` `{2,}` | exactly three, two to four, two or more |
| `[abc]` | a, b or c |
| `[a-z]` | a lowercase letter |
| `[A-Z]` | a capital letter |
| `[0-9]` | a digit |
| `[^0-9]` | anything but a digit; `^` inside brackets means not |
| `\d` | a digit, the same as `[0-9]` |
| `\w` | a letter, digit or underscore |
| `\s` | a space, tab or newline |
| `\D` `\W` `\S` | not a digit, not a word character, not whitespace |
| `\` | escape the next character: `\.` is a real dot |
| <code>&#124;</code> | or: <code>cat&#124;dog</code> matches either word |
| `( )` | a group: a piece to keep |

One at a time:

```python
# . is one blank to fill: c.t is like c_t
for word in ["cat", "cot", "ct", "coat"]:
    print(word, bool(re.search(r"c.t", word)))     # True, True, False, False

# ^ is the starting line, $ is the finish line
print(bool(re.search(r"^UPI", "Paid by UPI")))     # False
print(bool(re.search(r"UPI$", "Paid by UPI")))     # True

# \ takes away the special job: \. is a real dot
print(bool(re.search(r"bill.pdf", "bill-pdf")))    # True: the dot fills the blank
print(bool(re.search(r"bill\.pdf", "bill-pdf")))   # False: needs a real dot

# | means or
print(bool(re.search(r"UPI|card", "by card")))     # True

# [ ] picks one from the menu
print(bool(re.search(r"[cb]at", "rat")))           # False

# ranges
print(bool(re.search(r"[a-z]", "UPI")))            # False: capitals only
print(bool(re.search(r"[A-Z]", "UPI")))            # True
print(bool(re.search(r"[0-9]", "UPI")))            # False
print(bool(re.search(r"[^0-9]", "12a")))           # True: a is not a digit

# short forms
print(bool(re.search(r"\s", "UPI paid")))          # True
print(bool(re.search(r"\D", "123")))               # False: a capital flips the meaning
print(bool(re.search(r"[aeiou]", "sky")))          # False: no vowel
print(bool(re.search(r"\d", "Room 42")))           # True
print(bool(re.search(r"^\w+$", "hello world")))    # False: \w has no space
```

**Where each one helps in real work:**

| Symbol | Real use |
|---|---|
| `.` | Dates with any separator: `04.11.2026` fits 04-11-2026 and 04/11/2026 |
| `^` | Failures in a log: `^ERROR` keeps lines that start with ERROR |
| `$` | A disguised file: `pdf$` fits bill.pdf but not bill.pdf.exe |
| `\` | A bank SMS: `Rs\.600` needs a real dot |
| <code>&#124;</code> | Routing support messages: <code>refund&#124;chargeback</code> |
| `[ ]` | A mobile number: `^[6789]` checks the first digit |
| `[a-z]` | A password rule: needs a lowercase letter |
| `[A-Z]` | An IFSC such as HDFC0001234 starts with four capitals |
| `[0-9]` | Bad data: a digit in a name field, such as Rahul2 |
| `[^0-9]` | Clean money: `re.sub(r"[^0-9]", "", "₹1,25,000")` gives 125000 |
| `\d` | An OTP: `\d{6}` pulls 482913 from a message |
| `\w` | A username rule: `re.fullmatch(r"\w+", name)` |
| `\s` | Pasted text: `re.sub(r"\s+", " ", text)` leaves single spaces |
| `\S` | An ID in a sentence: `\S+@\S+` finds sumit@ybl |
| `+` | An amount of any length: `Rs\.\d+` |
| `*` | Optional spaces: `Rs *600` reads Rs600 and Rs 600 |
| `?` | Web links: `https?://` fits http and https |
| `{ }` | Exact lengths: a PIN code is `\d{6}`, a PAN is `[A-Z]{5}\d{4}[A-Z]` |

### Quantifiers

A quantifier counts the thing just before it.

```python
print(bool(re.search(r"go+d", "gd")))              # False: + needs at least one o
print(bool(re.search(r"go*d", "gd")))              # True: * allows zero
print(bool(re.search(r"colou?r", "color")))        # True: ? makes the u optional

for number in ["98765-43210", "9876-43210", "98765-432100", "9876543210"]:
    print(number, bool(re.fullmatch(r"\d{5}-\d{5}", number)))
# True, False, False, False
```

> **Real world, 2019.** On 2 July 2019 a new Cloudflare firewall rule held the piece `.*(?:.*=.*)`. On some inputs the engine retried every way to split the text between the `.*` parts. CPUs serving web traffic worldwide hit nearly 100%, and visitors saw 502 errors for 27 minutes. Prefer an exact class and count over `.*`, and test a pattern on bad input. [Cloudflare: Details of the outage on July 2, 2019](https://blog.cloudflare.com/details-of-the-cloudflare-outage-on-july-2-2019/)

### findall and groups

```python
text = "Reach us at 98765-43210 or 91234-56789, but not after 6 pm."
print(re.findall(r"\d{5}-\d{5}", text))     # ['98765-43210', '91234-56789']

text = "Name: Rex, Age: 3"
match = re.search(r"Name: (\w+), Age: (\d+)", text)
print(match.group(0))    # Name: Rex, Age: 3
print(match.group(1))    # Rex
print(match.group(2))    # 3

text = "Name: Rex, Age: 3; Name: Fido, Age: 5"
print(re.findall(r"Name: (\w+), Age: (\d+)", text))    # [('Rex', '3'), ('Fido', '5')]
```

`findall` returns every match as a list. Brackets make a group: the pattern describes the whole shape, and the groups say which pieces to keep. `group(0)` is the whole match. With groups in the pattern, `findall` returns one tuple per match, holding only the groups. Full code: [`code/05_regex_basics.py`](code/05_regex_basics.py) and [`code/06_regex_groups.py`](code/06_regex_groups.py).

### Mini project: read a server log

```python
logs = [
    "2026-11-04 21:05:02 ERROR Failed to connect to database",
    "2026-11-04 21:05:05 INFO Retry succeeded",
    "2026-11-04 21:06:40 WARNING Disk usage above 90%",
]
pattern = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.+)"
for line in logs:
    timestamp, level, message = re.match(pattern, line).groups()
    print(f"[{level}] {timestamp} - {message}")
```

Exact counts shape the timestamp, `\w+` takes the level as one word, and `.+` takes the rest of the line. `match` is enough because every line starts with its timestamp.

### Regex mistakes

| You see | It means | Fix |
|---|---|---|
| `AttributeError: 'NoneType' object has no attribute 'group'` | the pattern did not match, so `search` gave None | check `if m is not None:` first |
| `re.PatternError: missing ), unterminated subpattern at position 0` | the pattern itself is broken | close the bracket, or escape it: `\(` |
| `SyntaxWarning: "\d" is an invalid escape sequence` | the pattern has no `r` in front | write `r"\d"` |
| `report.pdf` also matches `reportXpdf` | an unescaped dot means any character | write `\.` |
| `findall` gives pieces, not whole matches | the pattern has groups | expect tuples, or remove the brackets |

## Project: PaisaPay v13

Version 13 finishes the classes from Class 12 and adds regex. A `Transaction` replaces the tuple; an `Account` holds the owner, a private balance, a private PIN and its own history, and does the paying; a `PremiumAccount` inherits everything and overrides the fee and cashback rules.

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

The full program is [`code/paisapay_v13.py`](code/paisapay_v13.py). A sample run on a premium account:

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

**New with regex.** The old UPI check only split on `@`. Now three patterns do the work:

```python
def is_valid_upi_id(upi_id):
    return re.fullmatch(r"[a-z0-9.]+@[a-z]+", upi_id) is not None

def is_valid_pan(pan):
    return re.fullmatch(r"[A-Z]{5}\d{4}[A-Z]", pan) is not None

def read_bank_sms(sms):
    m = re.search(r"Rs\.(\d+) debited from a/c XX(\d{4}) to (\w+)", sms)
    if m is None:
        return None
    amount, tail, payee = m.groups()
    return int(amount), tail, payee.title()
```

```text
Choose: 6
Paste the bank SMS: Rs.600 debited from a/c XX4321 to SUMIT on 04-11-26 via UPI
₹600 to Sumit from the account ending 4321
Choose: 7
PAN: ABCDE1234F
Valid PAN
```

What v13 cannot do yet: remember anything after the program ends. Files and modules come next.

## Recap

Before reading on, write your own three-point recap: what would you tell a friend who missed this class? Then compare.

- **Encapsulation** hides data behind methods; the double underscore renames, it does not lock. **Abstraction** hides steps behind a name.
- **Polymorphism**: one call, each object answers its own way. It needs the method, not a parent.
- **Scenarios**: a parent can have a parent; extend with `super()`; `isinstance` walks up, `type` names the exact class; children get methods, parents do not; check, then `super()`; is-a inherits, has-a is an attribute.
- **Regex**: a pattern describes a shape. `search` looks anywhere, `match` at the start, `fullmatch` at the whole string. Classes and quantifiers build the shape; `findall` gets every match; groups get the pieces.
- **PaisaPay v13**: a private balance and PIN, a PremiumAccount by inheritance, a UPI ID and a PAN checked by pattern, a bank SMS read with groups.

Next class: files and modules. PaisaPay remembers its data after exit.
