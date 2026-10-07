# Class 2 · Operators

In Class 1 we stored data. In this class we work with it: calculate, compare, combine conditions and update values. The class begins by finishing two Class 1 topics, `input()` and type casting.

**By the end of this class you can:**

- Take input from a user and convert it to the type you need.
- Calculate with arithmetic operators, including `//`, `%` and `**`.
- Compare values, and know that every comparison gives `True` or `False`.
- Tell `=` from `==`.
- Combine conditions with `and`, `or` and `not`.
- Update a variable with `+=`, `-=`, `*=`.
- Check membership with `in`, and know that `==` is not `is`.
- Read an expression with several operators using precedence.

## How to use this folder

| File | What it is |
|---|---|
| [`index.html`](https://prateekscaler.github.io/AIML-Jul26-Batch3-Python/Class-02-Operators/) | The interactive class page. [Open it here](https://prateekscaler.github.io/AIML-Jul26-Batch3-Python/Class-02-Operators/), no download needed. **Step by step** shows a little at a time (press → or Next). **Show everything** gives the whole class on one page. |
| [`code/`](code/) | Every example from the class as a runnable file, in order. |
| [`code/paisapay_v2.py`](code/paisapay_v2.py) | Today's version of our course project. |
| [`Python-Class-02-Operators.ipynb`](https://colab.research.google.com/github/prateekScaler/AIML-Jul26-Batch3-Python/blob/main/Class-02-Operators/Python-Class-02-Operators.ipynb) | The same examples as one notebook. [Open it in Google Colab](https://colab.research.google.com/github/prateekScaler/AIML-Jul26-Batch3-Python/blob/main/Class-02-Operators/Python-Class-02-Operators.ipynb) and run the cells, nothing to install. |
| [`ASSIGNMENT.md`](ASSIGNMENT.md) | Practice problems for this class. |
| [`INTERVIEW-READINESS.md`](INTERVIEW-READINESS.md) | Interview questions, gotchas and AI-era questions on today's topics. |

Run the code in [PyLens](https://scaler-pylens.vercel.app/), or on your own machine with `python3 filename.py`.

Official post-read for this class: <https://scaler-content.github.io/python-Foundations-2/>

---

## Part 1 · Finishing Class 1: input and type casting

The full notes for these topics are in the [Class 1 notes](../Class-01-Data-Types-Variables-Input-Output/README.md), sections 8 to 10. The short version:

```python
a = input("First amount: ")    # the user types 100
b = input("Second amount: ")   # the user types 50
print(a + b)                   # 10050
```

- **`input()` always returns a string**, even when the user types digits. `+` joins two strings, so the bill is wrong and nothing warns you.
- With `-` instead of `+`, Python refuses: `TypeError: unsupported operand type(s) for -: 'int' and 'str'`.
- **Type casting** converts between types. Convert as soon as the text arrives:

```python
a = int(input("First amount: "))
b = int(input("Second amount: "))
print(a + b)   # 150
```

- `int("25")` is `25`, `float("99.5")` is `99.5`, `str(100)` is `"100"`.
- `int()` treats text and numbers differently. On **text** it is strict: the text must be a whole number in digits, so `int("99.5")` is a `ValueError`. On a **number** it converts by cutting off the decimals, so `int(99.9)` is `99`, not 100. Text with a dot needs two steps: `int(float("99.5"))` is `99`.

**Why floats are not exact.** In decimal, 1/3 never ends; cut it to 0.33 and 0.33 + 0.33 + 0.33 is 0.99, not 1. A computer counts in binary, and in binary 0.1 never ends either, so it is stored cut short. The error is tiny, but it shows as soon as you add: `0.1 + 0.2` is `0.30000000000000004`. Each float is off by a tiny bit; across crores of transactions that is real money, which is why payment systems keep money as integer paise.

With these, [PaisaPay v1](../Class-01-Data-Types-Variables-Input-Output/code/paisapay_v1.py) is complete.

## Part 2 · Operators

An **operator** is a symbol or keyword that tells Python to perform an operation. Python has six families: arithmetic, comparison, logical, assignment, membership and identity.

### 1. Arithmetic operators

| Operator | Name | Example | Result |
|---|---|---|---|
| `+` | Addition | `10 + 3` | `13` |
| `-` | Subtraction | `10 - 3` | `7` |
| `*` | Multiplication | `10 * 3` | `30` |
| `/` | Division | `10 / 3` | `3.3333333333333335` |
| `//` | Floor division | `10 // 3` | `3` |
| `%` | Modulus (remainder) | `10 % 3` | `1` |
| `**` | Power | `2 ** 3` | `8` |

Three things to remember:

- **`/` always gives a float.** `15 / 5` is `3.0`, not `3`.
- **`//` and `%` are two halves of one division.** Share ₹10 among 3 friends: `10 // 3` is 3 each, `10 % 3` is 1 left over. A ₹450 bill among 4: `450 // 4` is 112, `450 % 4` is 2.
- **`%` tests "divides evenly".** `number % 2` is 0 for an even number. An ATM that gives only ₹100 notes needs `amount % 100` to be 0.

Predict, then run:

```python
print(15 + 5)    # 20
print(15 - 5)    # 10
print(15 * 5)    # 75
print(15 / 5)    # 3.0
print(15 // 4)   # 3
print(15 % 4)    # 3
print(2 ** 4)    # 16
```

> **Real world.** The Vancouver Stock Exchange started an index at 1000 in January 1982. After every trade, the software cut off the last decimals of the index instead of rounding. With about 3,000 updates a day, the index drifted down to 524.811 in 22 months. Recalculated correctly, it was 1098.892. Cutting always loses a little; thousands of times a day, it adds up. [Wikipedia](https://en.wikipedia.org/wiki/Vancouver_Stock_Exchange) · [Press reports](https://www5.in.tum.de/~huckle/Vancouv.pdf)

```python
price = 99.9
print(int(price))     # 99   cuts
print(round(price))   # 100  rounds
```

### 2. Comparison operators

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `>` | Greater than | `5 > 3` | `True` |
| `<` | Less than | `3 < 5` | `True` |
| `>=` | Greater than or equal to | `5 >= 5` | `True` |
| `<=` | Less than or equal to | `3 <= 2` | `False` |

**Every comparison produces a bool**, and the result can be stored:

```python
age = 20
is_adult = age >= 18
print(is_adult)   # True
```

Every IF node, filter and router in an n8n or Zapier workflow is one of these comparisons.

### 3. `=` vs `==`

| | Means |
|---|---|
| `age = 20` | Put 20 into `age` (assign) |
| `age == 20` | Is `age` equal to 20? (compare) |

A string is never equal to a number, and Python does not warn you:

```python
pin = "4321"
print(pin == 4321)   # False
```

Compare like with like, both sides the same type. A PIN is text, so compare it with text; convert to a number only when you really need one, and convert before you compare:

```python
print(pin == "4321")       # True
print(int(pin) == 4321)    # True
```

> **Real world.** In 2003 someone slipped a change into a copy of the Linux kernel code. It looked like a check, "is this user the admin?", but it used `=` instead of `==`, so it made the user the admin. It was noticed and removed before it reached the main code. One character changes a question into an order. [Princeton CITP](https://blog.citp.princeton.edu/2013/10/09/the-linux-backdoor-attempt-of-2003/) · [LWN](https://lwn.net/Articles/57135/)

### 4. Logical operators

| A | B | A and B | A or B |
|---|---|---|---|
| True | True | True | True |
| True | False | False | True |
| False | True | False | True |
| False | False | False | False |

- `and`: both must be True.
- `or`: at least one must be True.
- `not`: flips the value. `not True` is `False`.

Comparison operators **create** conditions. Logical operators **combine** them:

```python
age = 20
has_id = True

can_enter = age >= 18 and has_id
print(can_enter)   # True
```

The same condition can be written in other ways. All of these give the same answer for every age and ID; the second reads best because each check has a name:

```python
can_enter = has_id and age >= 18              # same checks, other order

is_adult = age >= 18                           # name each check first
can_enter = is_adult and has_id

can_enter = not (age < 18 or not has_id)      # "not blocked" says the same thing
```

### 5. Assignment shortcuts

| Shortcut | Same as |
|---|---|
| `x += 2` | `x = x + 2` |
| `x -= 2` | `x = x - 2` |
| `x *= 2` | `x = x * 2` |
| `x /= 2` | `x = x / 2` |
| `x //= 2` | `x = x // 2` |
| `x %= 2` | `x = x % 2` |

```python
score = 10
score += 5    # 15
score -= 2    # 13
score *= 2    # 26
```

Programmers call shortcuts like `+=` **syntactic sugar**: a sweeter way to write something the language can already do. It adds no new power; Python does exactly what the long form does. It helps the human: less typing, the variable name is written once (so `balance = balanec + 5` cannot happen), and it reads like what you mean, "add 5 to balance".

Watch the order of the two characters. `balance =+ 50` is plain assignment of `+50`, not "add 50".

### 6. Membership and identity

```python
upi_id = "rajani@paisapay"
print("@" in upi_id)        # True
print(" " not in upi_id)    # True
```

`==` asks "same value?". `is` asks "the very same object?":

```python
a = [100, 200]
b = [100, 200]
print(a == b)   # True
print(a is b)   # False
```

`is` says True only when two names point at one object:

```python
b = a            # not a copy: a second name for the same list
print(a is b)    # True
b += [300]
print(a)         # [100, 200, 300]
```

Compare values with `==`. Use `is` only to ask "same object?"; its everyday use is `x is None`, which comes in the functions class.

### 7. Operator precedence

When an expression has several operators, Python follows a fixed order, highest first:

| Order | Operators |
|---|---|
| 1 | Parentheses `( )` |
| 2 | Power `**` |
| 3 | `*` `/` `//` `%` |
| 4 | `+` `-` |
| 5 | Comparisons `==` `!=` `>` `<` `>=` `<=` |
| 6 | `not` |
| 7 | `and` |
| 8 | `or` |

```python
print(10 + 5 * 2)       # 20   multiplication first
print((10 + 5) * 2)     # 30   parentheses decide
print(2 + 3 ** 2)       # 11   power first
print(100 + 200 / 2)    # 200.0, not the average
print((100 + 200) / 2)  # 150.0
print(True or False and False)   # True
```

The last line, step by step: `and` goes before `or`, so Python groups it as `True or (False and False)`; `False and False` is `False`; `True or False` is `True`. Grouped the other way, `(True or False) and False`, it is `False`. Same words, opposite answer, which is why you write the parentheses when you mix `and` with `or`.

Is this BODMAS? Yes, for the maths part, and then Python keeps going:

| BODMAS at school | Python |
|---|---|
| Brackets | Parentheses `( )` |
| Orders (powers, roots) | Power `**` |
| Division, Multiplication | `* / // %`, same level, left to right |
| Addition, Subtraction | `+ -`, same level, left to right |
| Stops here | Then comparisons, then `not`, `and`, `or` |

Same level means left to right: `10 - 4 - 3` is 3, not 9. Maths uses the same convention; BODMAS only looks like "D before M, A before S", and `20 ÷ 2 × 5` is 50 in a maths class too. The one exception, in both maths and Python, is powers, which go right to left: `2 ** 3 ** 2` is 2 to the power 9, which is 512. Python also has operators school never had, `//` and `%`, and the whole True/False family after the maths.

Why `200.0` and not `200`? Mixing an int with a float gives a float: Python turns 100 into 100.0 first, because nothing is lost that way. The rules: int with int stays int (except `/`); any float in the mix makes the result a float; `/` always gives a float.

Parentheses say exactly what to calculate first, and they help the human reader too.

### 8. Both classes, one program

```python
score = int(input("Enter your score: "))

passed = score >= 40
excellent = score >= 90

print("Passed:", passed)
print("Excellent:", excellent)
```

`input()` gets the data, `int()` converts it, `>=` compares it, a bool variable stores the answer, and `print()` shows it.

### 9. Mini challenge: can they enter?

Rule: at least 18 **and** has an ID.

```python
age = int(input("Enter your age: "))
has_id = input("Do you have an ID? ")

can_enter = age >= 18 and has_id == "yes"

print("Can enter:", can_enter)
```

`input()` gives text, so the answer is compared with the text `"yes"`. Typing `Yes` gives `False`: text must match exactly.

## Using AI the right way in this class

1. **Check AI's arithmetic.** Ask an assistant "What is 23957 * 4873?" without letting it run code, then run `print(23957 * 4873)`. This is why agents call a code tool for maths.
2. **Read another version.** Ask: "Show me one other way to write can_enter = age >= 18 and has_id that gives the same result." Run it with a few values and confirm it matches yours.

## Project: PaisaPay v2

Version 2 adds today's operators to v1: a fee, cashback, a bill split, and two questions the program can ask about a payment.

```python
print("Welcome to PaisaPay")

name = input("Your name: ")
payee = input("Pay to: ")
amount = int(input("Amount in rupees: "))
people = int(input("Split between how many people? "))

balance = 1000
fee = 2
total = amount + fee
cashback = amount * 5 // 100
share = amount // people
left_over = amount % people

can_pay = balance >= total
is_big_payment = amount >= 500

balance -= total
balance += cashback

print("----- Receipt -----")
print("From:", name)
print("To:", payee)
print("Paid: ₹", amount, "+ fee ₹", fee)
print("Cashback: ₹", cashback)
print("Each person owes: ₹", share, "| left over: ₹", left_over)
print("Enough balance:", can_pay)
print("Big payment:", is_big_payment)
print("Balance left: ₹", balance)
```

```text
Welcome to PaisaPay
Your name: Rajani
Pay to: Zomato
Amount in rupees: 450
Split between how many people? 4
----- Receipt -----
From: Rajani
To: Zomato
Paid: ₹ 450 + fee ₹ 2
Cashback: ₹ 22
Each person owes: ₹ 112 | left over: ₹ 2
Enough balance: True
Big payment: False
Balance left: ₹ 570
```

Why `amount * 5 // 100` and not `/`? Division with `/` gives `22.5`, a float. Money stays in whole units, so we use `//`.

What v2 cannot do yet: pay ₹5000 and it prints `Enough balance: False`, then pays anyway. It can ask the question but cannot act on the answer. That needs decisions, in the next class.

## Recap

- `input()` always gives a `str`. Convert with `int()` or `float()`.
- **Arithmetic:** `+ - * / // % **`. `/` gives a float; `//` and `%` are a pair.
- **Comparison:** `== != > < >= <=`, always a bool.
- **`=` assigns, `==` compares.**
- **Logical:** `and`, `or`, `not` combine conditions.
- **Shortcuts:** `+=`, `-=`, `*=`.
- **Membership:** `in`, `not in`. And `==` is not `is`.
- **Precedence:** a fixed order; parentheses decide.

**Next class:** Control Statements. PaisaPay v3 learns to say no.
