# Class 5 · Functions

PaisaPay v4 asks for the PIN, three attempts, before a payment: ten lines. A real app asks the same way before a refund, before adding a card and before changing the PIN. Copy the ten lines four times, fix a bug in one copy, and the other three keep the bug. In this class Python learns to name a block of code: write it once, call it by name, change it in one place.

**By the end of this class you can:**

- Define a function with `def`, call it, and say exactly when its body runs.
- Tell a parameter from an argument, and match arguments by position or by name.
- Use `return` to hand a value back, and explain why a function without `return` gives `None`.
- Say where a variable lives: local inside a function, global outside.
- Give a parameter a default, and write a one-line `lambda`.

## How to use this folder

| File | What it is |
|---|---|
| [`index.html`](index.html) | The interactive class page. [Open it here](https://prateekscaler.github.io/AIML-Jul26-Batch3-Python/Class-05-Functions/), no download needed. **Step by step** shows a little at a time (press → or Next). **Show everything** gives the whole class on one page. |
| [`code/`](code/) | Every example from the class as a runnable file, in order. |
| [`code/paisapay_v5.py`](code/paisapay_v5.py) | Today's version of our course project. |
| [`Python-Class-05-Functions.ipynb`](Python-Class-05-Functions.ipynb) | The same examples as one notebook. [Open it in Google Colab](https://colab.research.google.com/github/prateekScaler/AIML-Jul26-Batch3-Python/blob/main/Class-05-Functions/Python-Class-05-Functions.ipynb) and run the cells, nothing to install. |
| [`PRACTICE.md`](PRACTICE.md) | Twelve coding problems on functions, easy to hard, with sample output, hints and solutions. |
| [`ASSIGNMENT.md`](ASSIGNMENT.md) | Predict the output, write programs, grow PaisaPay, think it through. |
| [`INTERVIEW-READINESS.md`](INTERVIEW-READINESS.md) | Interview questions, gotchas and AI-era questions on today's topics. |

Run the code in [PyLens](https://scaler-pylens.vercel.app/), or on your own machine with `python3 filename.py` (Python 3.10 or newer, because PaisaPay uses `match`).

Official post-read for this class: https://scaler-content.github.io/python-Foundations-5/

---

## 0. Carried over from Class 4

Class 4 ran out of time at the debug clinic, so this class opens with three steps from it: the loop debug clinic (`break` where `continue` belongs, a `while` that updates the wrong variable, an off-by-one `range`), a loop inside a loop (the inner loop runs fully for each outer pass, 3 × 2 = 6 lines), and nested loops that draw grids, with what `end=" "` does: every `print` ends with a new line by default, `end=" "` ends with a space instead, and a bare `print()` finishes the row. The full notes for these are in [Class 4, sections 5 and 7](../Class-04-Loops/README.md#5-nested-loops).

## 1. Why functions

The ten-line PIN block from v4 is needed before a payment, a refund, a new card and a PIN change. Pasting it four times works until the day you fix a bug in one copy and forget the other three. A function fixes that: write the block once, give it a name, use the name everywhere, change it in one place.

Every tool an agent calls is a function. The tool schema you wrote in n8n or for an MCP server is a function signature: a name, its parameters, and what comes back. And every big program is a set of small named blocks. Nobody reads 500 lines top to bottom; they read `pay()`, `add_money()`, `show_balance()`, `is_valid_pin()` and understand the app from the names.

> **Real world.** On 22 March 2016 a developer removed his packages from npm, the JavaScript library store. One of them, `left-pad`, was an eleven-line function that pads text with spaces. Thousands of projects, including Babel and React, used it, and their builds broke within minutes. Write a function once and everyone reuses it: that is the power, and the risk. [The npm left-pad incident](https://en.wikipedia.org/wiki/Npm_left-pad_incident)

## 2. Define, then call

```python
def welcome():
    print("Welcome to PaisaPay")

welcome()
welcome()
welcome()
```

`def` starts a definition, `welcome` is the name, `()` holds the parameters, and the indented body is what runs. The definition alone runs nothing; it is a blueprint. Every call, `welcome()`, runs the body start to finish.

## 3. Parameters and arguments

```python
def greet(name):
    print("Hello", name)

greet("Uma")
greet("Prince")
```

`name` is the **parameter**, the variable in the definition. `"Uma"` is the **argument**, the value given at the call. With several parameters the arguments are matched by position: `introduce("Uma", 20)` puts `"Uma"` in `name` and `20` in `age`. Swap them and Python does not complain; it just prints nonsense.

A function can hold anything you already know: variables, operators, conditions, loops. It does not replace them; it packages them.

## 4. `return`: hand the result back

```python
def add(a, b):
    print(a + b)

result = add(10, 20)
print(result)
```

This prints `30` and then `None`. The `print` inside shows 30 to the human; the function hands nothing back, and Python's word for nothing is `None`. With `return a + b` instead, `result` holds 30 and can be stored, printed or used inside a bigger calculation: `square(5) + 10`.

`return` also ends the function at once. Any line after it never runs. The rule: `print` is for the human watching the screen, `return` is for the rest of the program.

## 5. Scope: local and global

A variable created inside a function is **local**: born when the function runs, gone when it ends. Use it outside and you get `NameError`. To get a value out, `return` it. A variable created outside every function is **global**, and a function can read it. Assigning to that name inside a function makes a new local instead, which is why `balance = balance + 100` inside a function raises `UnboundLocalError`. The clean habit: pass values in as arguments, hand them out with `return`.

## 6. Default and keyword arguments

```python
def greet(name="Student"):
    print("Hello", name)

greet()            # Hello Student
greet("Prince")    # Hello Prince

def power(number, exponent=2):
    return number ** exponent

print(power(5), power(5, 3))     # 25 125
```

A default fills the gap when no argument is given; an argument replaces it. Arguments can also be matched by name: `introduce(age=20, name="Vinit")` is correct in any order. Positional arguments must come before keyword ones. Python fills parameters left to right, and once one argument is named it cannot tell where a plain value after it should go, so `greet(message="Hi", "Vinit")` is a `SyntaxError` before anything runs. Plain values first, named ones after: `greet("Vinit", message="Hi")` or `greet(name="Vinit", message="Hi")`.

## 7. Validation helpers

```python
def is_valid_amount(amount):
    return amount > 0 and amount <= 100000

def is_valid_pin(pin):
    return pin == saved_pin
```

Small functions that answer yes or no. The name starts with `is_`, the result is a bool, and it reads like a question inside an `if`. Check inputs at the door, once, in one place. Here is why:

```python
memory = ["hello", "PIN=4321", "KEY=secret99"]

def heartbeat(count):
    sent = 0
    for word in memory:
        if sent == count:
            break
        print(word)
        sent += 1

heartbeat(1)     # hello
heartbeat(3)     # hello, PIN=4321, KEY=secret99
```

A client sends "hello" and asks for one word back. An attacker sends "hello" and asks for three, and the function sends back the PIN and the key from memory, because it believed `count`. One line at the door fixes it: `if count != 1: return`.

> **Real world.** OpenSSL, the code behind the padlock on most websites, had a "heartbeat" function: send some text and its length, get the same text back. It never checked that the length matched the text, so a 1-byte message that claimed to be 64,000 bytes got 64,000 bytes of server memory in reply: passwords, keys. Disclosed in April 2014 as Heartbleed, it affected about 17% of the internet's secure servers, around half a million. A function must not trust its arguments; validate at the boundary. [Heartbleed](https://en.wikipedia.org/wiki/Heartbleed)

## 8. Short forms so far, then `lambda`

Python often has a long way and a short way with the same meaning. Class 2 gave `balance -= 300` for `balance = balance - 300`. Class 3 gave the ternary, `status = "OK" if balance >= 500 else "LOW"`, for a four-line `if` / `else`. A short form never changes what happens; it changes how much you type and read. Today adds one more.


```python
square = lambda x: x * x
add = lambda a, b: a + b
```

`square` above is one expression, so is there a shorter way to write something this small, the way the ternary shortened a two-way `if` in Class 3? Yes. A `lambda` is a small function with no name of its own: parameters, a colon, one expression whose value is returned. Use it for short, throw-away operations; anything longer than a line deserves a `def`. Class 9 uses lambdas a lot.

## 9. Small functions, one job each

```python
def calculate_average(score1, score2, score3):
    return (score1 + score2 + score3) / 3

def check_result(average):
    if average >= 40:
        return "Pass"
    return "Fail"
```

One function computes, another decides, the main program connects them. Each can be tested alone. Good programs are small functions with clear names, not one long block.

## 10. Debug clinic

| Bug | What you see | Fix |
|---|---|---|
| `message = greet` without parentheses | No error, nothing prints, `message` holds the function itself | `greet()` |
| `print(result)` after `calculate()` returned it | `NameError` | `result = calculate()` |
| `balance = show_balance(balance)` | The balance becomes `None` | Store only what a function returns |
| `greet()` when `greet(name)` has no default | `TypeError: missing 1 required positional argument` | Pass the argument or add a default |

Before fixing: was it called? Did it return? Did someone catch the return?

## Project: PaisaPay v5

Version 5 keeps the v4 menu loop and turns every job into a function. Fee, cashback and payment modes from v3 are back, each as a helper. Money stays a whole number of rupees.

```python
# PaisaPay v5: named blocks
print("Welcome to PaisaPay")

saved_pin = "4321"

def is_valid_amount(amount):
    return amount > 0 and amount <= 100000

def is_valid_pin(pin):
    return pin == saved_pin

def fee_for(mode):
    if mode == "card":
        return 5
    elif mode == "netbanking":
        return 2
    return 0

def cashback_for(amount):
    if amount >= 5000:
        return 100
    elif amount >= 2000:
        return 50
    elif amount >= 500:
        return 10
    return 0

def mode_name(mode):
    match mode:
        case "upi":
            return "UPI"
        case "card":
            return "Card"
        case "netbanking":
            return "Net banking"
        case _:
            return "Unknown mode"

def show_balance(balance):
    print("Balance: ₹", balance)

def add_money(balance, amount):
    if not is_valid_amount(amount):
        print("Invalid amount. Nothing added.")
        return balance
    print("Added ₹", amount)
    return balance + amount

def ask_pin():
    for attempt in range(3):
        pin = input("UPI PIN: ")
        if is_valid_pin(pin):
            return True
        print("Wrong PIN.", 2 - attempt, "attempts left")
    return False

def pay(balance, payee, amount, mode="upi"):
    if not is_valid_amount(amount):
        print("Invalid amount. Payment refused.")
        return balance
    if mode_name(mode) == "Unknown mode":
        print("Unknown payment mode. Payment refused.")
        return balance
    fee = fee_for(mode)
    if amount + fee > balance:
        print("Insufficient balance. Payment refused.")
        return balance
    cashback = cashback_for(amount)
    print("Paid ₹", amount, "to", payee, "via", mode_name(mode))
    print("Fee ₹", fee, "| Cashback ₹", cashback)
    return balance - amount - fee + cashback

balance = 1000
choice = ""
while choice != "4":
    print()
    print("1. Pay   2. Balance   3. Add money   4. Exit")
    choice = input("Choose: ")

    if choice == "1":
        payee = input("Pay to: ")
        amount = int(input("Amount in rupees: "))
        mode = input("Mode (upi / card / netbanking): ")
        if ask_pin():
            balance = pay(balance, payee, amount, mode)
        else:
            print("Three wrong PINs. Payment refused.")

    elif choice == "2":
        show_balance(balance)

    elif choice == "3":
        amount = int(input("Amount to add: "))
        balance = add_money(balance, amount)

    elif choice != "4":
        print("Unknown choice. Try again.")

print("Thank you for using PaisaPay")
```

A sample run:

```text
Welcome to PaisaPay

1. Pay   2. Balance   3. Add money   4. Exit
Choose: 1
Pay to: Chai Point
Amount in rupees: 600
Mode (upi / card / netbanking): upi
UPI PIN: 4321
Paid ₹ 600 to Chai Point via UPI
Fee ₹ 0 | Cashback ₹ 10

1. Pay   2. Balance   3. Add money   4. Exit
Choose: 3
Amount to add: 500
Added ₹ 500

1. Pay   2. Balance   3. Add money   4. Exit
Choose: 2
Balance: ₹ 910

1. Pay   2. Balance   3. Add money   4. Exit
Choose: 4
Thank you for using PaisaPay
```

Two habits in this program are worth copying. Every function that changes the balance returns the new balance, and the caller stores it: `balance = pay(...)`. Every function that refuses a payment still returns the balance, unchanged, so the caller never ends up with `None`.

What v5 cannot do yet: the mini statement is out, because totals need a list that grows (Class 6); typed input is not cleaned and amounts are whole rupees, not paise (strings and formatting, Class 7); and a UPI ID or PAN cannot be checked properly yet (regex, Class 11).

## Mini practices and mini challenge

Three to write now: `greet(name)` with a default of `"Student"`, `check_even(number)` that returns `"Even"` or `"Odd"`, and a four-function calculator. Then the bill calculator: `calculate_bill(price, quantity, tax=5)` returns the subtotal plus tax in whole rupees, so `calculate_bill(100, 2)` is 210 and `calculate_bill(100, 2, tax=10)` is 220.

Full code: [`code/09_practice.py`](code/09_practice.py), [`code/11_bill.py`](code/11_bill.py). Then do the twelve problems in [`PRACTICE.md`](PRACTICE.md).

## Recap

Before reading on, write your own three-point recap: what would you tell a friend who missed this class? Then compare.

- **def** names a block once. Nothing runs until you call it.
- **Parameters and arguments**: the variable in the definition, the value at the call. Matched by position, or by name.
- **return** hands a value back and ends the function. `print` only shows it. No return means `None`.
- **Scope**: locals live and die inside. Globals are readable everywhere. Pass in, return out.
- **Defaults and keywords**: `mode="upi"` fills the gap; `pay(..., mode="card")` names it.
- **lambda**: a one-expression function for small jobs.
- **PaisaPay v5**: nine functions: checks, fee, cashback, mode, show, add, PIN, pay.

Next class: lists. A box that grows, so PaisaPay can remember every payment.
