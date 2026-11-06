# Class 14 · Revision: OOP and Regex in Practice

A revision class before file handling. It goes back over object-oriented programming (why a class, objects, class variables and instance variables, encapsulation, `self`), practises choosing between a string method, a regex and an LLM for a real task, and works through inheritance scenarios that people often get wrong.

**By the end of this class you can:**

- Say why a class helps, and tell a class from an object.
- Tell a class variable from an instance variable, and predict what changes when you assign to each.
- Explain encapsulation with `self.__balance` and the methods that guard it.
- Say which object `self` is, and so which method runs when a parent's method calls one the child overrides.
- Choose a string method, a regex or an LLM for a task, and say when an LLM's answer needs a regex check.

## How to use this folder

| File | What it is |
|---|---|
| [`index.html`](index.html) | The interactive class page. [Open it here](https://prateekscaler.github.io/AIML-Jul26-Batch3-Python/Class-14-Revision-OOP-And-Regex/), no download needed. **Step by step** shows a little at a time (press → or Next). **Show everything** gives the whole class on one page. |
| [`code/`](code/) | The examples from the class as runnable files. |
| [`Python-Class-14-Revision-OOP-And-Regex.ipynb`](Python-Class-14-Revision-OOP-And-Regex.ipynb) | The same examples as one notebook. [Open it in Google Colab](https://colab.research.google.com/github/prateekScaler/AIML-Jul26-Batch3-Python/blob/main/Class-14-Revision-OOP-And-Regex/Python-Class-14-Revision-OOP-And-Regex.ipynb) and run the cells, nothing to install. |

For more practice on these topics, use the problems from the last three classes: [Class 11](../Class-11-Object-Oriented-Programming/PRACTICE.md), [Class 12](../Class-12-Object-Oriented-Programming-Part-2/PRACTICE.md) and [Class 13](../Class-13-OOP-Practice-And-Regex/PRACTICE.md).

Run the code in [PyLens](https://scaler-pylens.vercel.app/), or on your own machine with `python3 filename.py`.

---

## 1. Object-oriented programming

- **Why a class:** one blueprint. The methods are written once; each object keeps its own data. Fix a method once and every object gets the fix.
- **Class and object:** `a = Account("Rajani", 1000)` builds one object, also called an instance, of the class Account.
- **Class variable and instance variable:** written in the class body (`bank = "PaisaPay"`), one value is shared by every object. Written on `self` (`self.balance = balance`), each object has its own. Changing `Account.bank` changes what every object sees; `a.bank = "OtherPay"` makes a new instance variable on `a` only.
- **Encapsulation:** `self.__balance` keeps the data inside; `deposit()` and `pay()` are the door, so their rules cannot be skipped. Outside the class, `acc.__balance` is an `AttributeError`.
- **Methods and self:** `deposit` is written once in the class. `rajani.deposit(500)` runs it with `self` = rajani, so only Rajani's balance changes.

```python
class Account:
    bank = "PaisaPay"                 # class variable: shared by every object

    def __init__(self, owner, balance):
        self.owner = owner            # instance variables: each object's own
        self.__balance = balance      # private: change it only through methods

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

rajani = Account("Rajani", 1000)
sumit = Account("Sumit", 2500)
Account.bank = "PaisaPay Plus"
print(rajani.bank, sumit.bank)        # PaisaPay Plus PaisaPay Plus
rajani.bank = "OtherPay"
print(rajani.bank, sumit.bank)        # OtherPay PaisaPay Plus
rajani.deposit(500)
print(rajani.get_balance(), sumit.get_balance())   # 1500 2500
print(rajani.__balance)               # AttributeError: 'Account' object has no attribute '__balance'
```

Full example: [`code/03_oop_recap.py`](code/03_oop_recap.py).

## 2. Which tool: a string method, a regex, or an LLM?

For each job, pick the simplest tool that works. Exact text needs a string method, a shape needs a regex, and a meaning needs an LLM. When an LLM's answer must be right, check it with a regex.

| The job | Use |
|---|---|
| Does a file name end in `.csv`? | a string method |
| Pull the six-digit OTP out of each of 10,000 SMS messages, fast and free. | a regex |
| A customer writes "paise kat gaye par recharge nahi hua". Is it a failed-recharge complaint? | an LLM |
| A scanned letter, typed messily, has the customer's PAN somewhere in it. You must store a correct PAN. | an LLM, then a regex to check its answer |
| Is this a valid IFSC code: four capitals, a 0, then six letters or digits? | a regex |
| Sort 500 customer reviews into happy, angry and confused. | an LLM |
| A line from a file reads `Sumit,600,UPI`. You need the three parts. | a string method |

Regex at work, in code: [`code/01_regex_at_work.py`](code/01_regex_at_work.py).

## 3. Inheritance scenarios

```python
# 1. A parent method calls a method the child overrides: the child's version runs
class Account:
    def fee_for(self, mode):
        return 5 if mode == "card" else 0

    def total(self, amount, mode):
        return amount + self.fee_for(mode)    # self is whatever object called total

class PremiumAccount(Account):
    def fee_for(self, mode):
        return 0

print(Account().total(1000, "card"))          # 1005
print(PremiumAccount().total(1000, "card"))   # 1000
```

`total` is written once, in Account. `self` is the object that made the call, so the search for `fee_for` starts at that object's own class. PaisaPay's `pay()` works this way for a PremiumAccount.

```python
# 2. A child class variable hides the parent's
class Deposit:
    rate = 4

class FixedDeposit(Deposit):
    rate = 7

print(Deposit.rate, FixedDeposit.rate, FixedDeposit().rate)   # 4 7 7
```

```python
# 3. super() works in any method, not only __init__
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def describe(self):
        return f"{self.name} earns {self.salary}"

class Manager(Employee):
    def describe(self):
        return super().describe() + " and leads a team"

print(Manager("Chitransh", 90000).describe())   # Chitransh earns 90000 and leads a team

# 4. super().__init__ needs every argument the parent asks for
class Intern(Employee):
    def __init__(self, name):
        super().__init__(name)

Intern("Karthikeyan")
# TypeError: Employee.__init__() missing 1 required positional argument: 'salary'
```

## Recap

- **A class** is one blueprint: methods written once, data kept in each object.
- **Class variable:** in the class body, shared. **Instance variable:** on `self`, each object's own. Assigning on one object makes its own copy.
- **Encapsulation:** `self.__balance` stays inside; the methods are the door.
- **self** is the object before the dot, so a parent's method runs the child's override.
- **Which tool:** exact text, a string method; a shape, a regex; a meaning, an LLM, checked by a regex when it must be right.

Next class: file handling and modules. PaisaPay will remember its data after it closes.
