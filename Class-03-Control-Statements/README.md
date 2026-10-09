# Class 3 · Control Statements

Until now every program ran top to bottom, every line, every time. In this class Python learns to decide: run this block only when a condition is true, otherwise do something else.

**By the end of this class you can:**

- Write `if`, `else` and `elif` blocks, and explain why indentation is part of the syntax.
- Explain why the order of conditions matters in an `elif` chain.
- Use `match` / `case` for one variable against exact values.
- Build conditions with `and`, `or` and `not`.
- Nest one decision inside another, and choose between nesting and `and`.
- Write a simple two-way choice as a ternary expression, and know when not to.

## How to use this folder

| File | What it is |
|---|---|
| [`index.html`](https://prateekscaler.github.io/AIML-Jul26-Batch3-Python/Class-03-Control-Statements/) | The interactive class page. [Open it here](https://prateekscaler.github.io/AIML-Jul26-Batch3-Python/Class-03-Control-Statements/), no download needed. **Step by step** shows a little at a time (press → or Next). **Show everything** gives the whole class on one page. |
| [`code/`](code/) | Every example from the class as a runnable file, in order. |
| [`code/paisapay_v3.py`](code/paisapay_v3.py) | Today's version of our course project. |
| [`Python-Class-03-Control-Statements.ipynb`](https://colab.research.google.com/github/prateekScaler/AIML-Jul26-Batch3-Python/blob/main/Class-03-Control-Statements/Python-Class-03-Control-Statements.ipynb) | The same examples as one notebook. [Open it in Google Colab](https://colab.research.google.com/github/prateekScaler/AIML-Jul26-Batch3-Python/blob/main/Class-03-Control-Statements/Python-Class-03-Control-Statements.ipynb) and run the cells, nothing to install. |
| [`ASSIGNMENT.md`](ASSIGNMENT.md) | Practice problems for this class. |
| [`INTERVIEW-READINESS.md`](INTERVIEW-READINESS.md) | Interview questions, gotchas and AI-era questions on today's topics. |

Run the code in [PyLens](https://scaler-pylens.vercel.app/), or on your own machine with `python3 filename.py`.

Official post-read for this class: <https://scaler-content.github.io/python-Foundations-3/>

---

## 1. Why programs need decisions

PaisaPay v2 could ask "is the balance enough?" and print `False`, then pay anyway:

```python
balance = 1000
amount = int(input("Amount in rupees: "))
can_pay = balance >= amount

balance -= amount                      # runs no matter what the answer was
print("Enough balance:", can_pay)      # Enough balance: False
print("Balance left: ₹", balance)      # Balance left: ₹ -4000
```

Line 3 asks the question. Line 5 deducts anyway. Every line ran, top to bottom, and nothing could stop it. A real app must choose: pay, or refuse. That choice is a **conditional statement**.

A condition is a question whose answer is `True` or `False`:

```python
balance = 500
amount = 200
print(balance >= amount)   # True
```

## 2. `if`

```python
balance = 1000
amount = 400

if balance >= amount:
    print("Payment successful")
```

| Part | Meaning |
|---|---|
| `if` | A decision is coming |
| `balance >= amount` | The condition, a True/False question |
| `:` | The code controlled by this `if` starts here |
| indented `print(...)` | Runs only when the condition is True |

When the condition is False, the indented block is skipped and nothing prints. A line that is **not** indented is outside the `if` and runs every time.

Two things that catch people:

- `if balance = amount:` is a `SyntaxError`. `=` assigns, `==` compares.
- `if balance >= amount:` followed by an unindented `print(...)` is an `IndentationError`. Indentation is part of Python's syntax, not styling. The convention is 4 spaces.

> **Real world.** In 2014 a line was accidentally duplicated in Apple's connection-security code. It was indented as if it belonged to an `if`, but in that language indentation means nothing, so the line ran every time and the security check below it was skipped on every iPhone and Mac. Simplified (this is C, not Python):
>
> ```c
> if (check_1_failed)
>     goto fail;
>     goto fail;          // pasted twice. Looks inside the if. Is not.
> if (check_2_failed)     // never reached
>     goto fail;
> ```
>
> Python makes indentation the truth: what you see is what runs. [The Apple goto fail vulnerability: lessons learned](https://dwheeler.com/essays/apple-goto-fail.html)

## 3. `else`

```python
balance = 300
amount = 800

if balance >= amount:
    print("Payment successful")
else:
    print("Insufficient balance")
```

`if` handles the condition being True. `else` handles everything else and has no condition of its own. Exactly one of the two blocks runs. Note that `500 >= 500` is True: paying your entire balance is allowed.

## 4. `elif` and the order of conditions

| Amount | Cashback |
|---|---|
| ₹5,000 or more | ₹100 |
| ₹2,000 or more | ₹50 |
| ₹500 or more | ₹10 |
| less than ₹500 | ₹0 |

```python
amount = int(input("Amount in rupees: "))

if amount >= 5000:
    cashback = 100
elif amount >= 2000:
    cashback = 50
elif amount >= 500:
    cashback = 10
else:
    cashback = 0

print("Cashback: ₹", cashback)
```

Python checks top to bottom and stops at the **first True** condition. For 2500: `2500 >= 5000` is False, `2500 >= 2000` is True, cashback is 50, and the remaining lines are never looked at. Tiers never add up, because only one block of a chain ever runs.

**Order matters.** This version gives ₹8,000 a cashback of ₹10, because `amount >= 500` is checked first and is already True:

```python
if amount >= 500:
    print("Cashback ₹10")
elif amount >= 5000:
    print("Cashback ₹100")
```

Put the most specific, highest condition first. The same mistake in a grading app sends a score of 95 to grade D, because `score >= 60` is checked first. The fix is the same: 90, then 80, then 70, then 60, then `else`.

```python
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
```

And two separate `if` statements are not a fix: they are two independent questions, and for ₹8,000 both would print.

## 5. `match` / `case`

For one variable checked against several exact values, `match` is cleaner than a chain of `elif mode == ...`:

```python
mode = input("Payment mode: ")

match mode:
    case "upi":
        print("Opening UPI app...")
    case "card":
        print("Enter card PIN")
    case "netbanking":
        print("Redirecting to your bank")
    case _:
        print("Unknown mode")
```

`match mode:` runs once. Each `case` is an exact, case-sensitive match checked top to bottom; `case _` is the wildcard and plays the role of `else`. Typing `UPI` gives "Unknown mode". Ranges such as `amount >= 5000` stay with `if` / `elif`. Needs Python 3.10 or newer.

## 6. Conditions with `and`, `or`, `not`

```python
if balance >= amount and pin_correct:   # both must be True
    print("Payment successful")

if has_upi_pin or has_fingerprint:      # at least one must be True
    print("Authorised")

if not is_frozen:                       # not flips the value
    print("Account active. Proceed.")
```

A trap that never errors:

```python
if mode == "upi" or "card":   # always True: "card" alone counts as True
```

Write it out: `mode == "upi" or mode == "card"`.

**What counts as True?** In a condition, zero (`0`, `0.0`), the empty string `""` and `None` count as False. Everything else counts as True, including `500`, `-1`, `"card"`, and the strings `"0"`, `"False"` and `" "`, because they are not empty. Check any value with `bool(value)`.

For the record, the full operator order, high to low: `**`, then `* / // %`, then `+ -`, then comparisons `== != < > <= >=`, then `not`, then `and`, then `or`. Brackets beat all of them. Maths first, then compare, then combine.

## 7. Nested conditions

```python
if pin_correct:
    if balance >= amount:
        print("Payment successful")
    else:
        print("Insufficient balance")
else:
    print("Wrong PIN")
```

The inner question is asked only when the outer answer is True. With a wrong PIN, the balance is never looked at.

| Use `and` when | Use nested when |
|---|---|
| Both checks are simple and independent | The second check depends on the first passing |
| One success message, one failure message | A different message at each level |
| Shorter, easier to read | More lines, but every failure is explained |

**An `else` belongs to the `if` at the same indentation.** Delete the inner `else` above and, with a correct PIN and a low balance, nothing prints at all: the remaining `else` belongs to the outer `if`.

## 8. The ternary operator

```python
status = "SUCCESS" if balance >= amount else "FAILED"
```

The shape is `value_if_true if condition else value_if_false`. Read it as a sentence. It is not new logic, only a compact `if` / `else` that produces a value. Keep it for simple two-way choices; three or more outcomes belong in `if` / `elif` / `else`. The clever one-liner `fee = 0 if amount < 1000 else 5 if amount < 10000 else 10` prints 5 for 1000, and takes a while to read, which is the point.

## 9. The pattern

Input → Condition → True or False → an action. Pass or fail, login, discount, OTP, traffic light: the same shape every time. The syntax is the small part; spotting the decision is the skill.

## 10. New errors today

| Error | Python is saying | Example |
|---|---|---|
| `IndentationError` | A block was expected, or the spacing does not line up | a `print` under `if` without the 4 spaces |
| `SyntaxError` | The shape is wrong; here an assignment where a question belongs | `if balance = amount:` |
| No error at all | The dangerous one: a wrong answer with no complaint | `mode == "upi" or "card"`, conditions in the wrong order |

## Project: PaisaPay v3

Version 3 adds decisions to v2: wrong PIN, unknown mode and insufficient balance are refused, cashback comes in tiers, and the payment mode is matched against exact values.

```python
print("Welcome to PaisaPay")

balance = 1000
saved_pin = "4321"

name = input("Your name: ")
payee = input("Pay to: ")
amount = int(input("Amount in rupees: "))
mode = input("Mode (upi / card / netbanking): ")
pin = input("UPI PIN: ")

fee = 2
total = amount + fee

if amount >= 5000:
    cashback = 100
elif amount >= 2000:
    cashback = 50
elif amount >= 500:
    cashback = 10
else:
    cashback = 0

match mode:
    case "upi":
        mode_text = "UPI"
    case "card":
        mode_text = "Card"
    case "netbanking":
        mode_text = "Net banking"
    case _:
        mode_text = "Unknown mode"

print("----- Receipt -----")
if pin != saved_pin:
    print("Wrong PIN. Payment refused.")
elif mode_text == "Unknown mode":
    print("Unknown payment mode. Payment refused.")
elif total > balance:
    print("Insufficient balance. Payment refused.")
else:
    balance = balance - total + cashback
    print("Paid: ₹", amount, "to", payee, "via", mode_text)
    print("Cashback: ₹", cashback)
    print("Balance left: ₹", balance)
```

```text
Welcome to PaisaPay
Your name: Sumit
Pay to: Chai Point
Amount in rupees: 600
Mode (upi / card / netbanking): upi
UPI PIN: 4321
----- Receipt -----
Paid: ₹ 600 to Chai Point via UPI
Cashback: ₹ 10
Balance left: ₹ 408
```

What v3 cannot do yet: it handles one payment, then stops, and a wrong PIN ends the program instead of offering another try. Both need loops, in the next class.

## Mini project and mini challenge

**Open a PaisaPay account.** Rule: at least 18 and KYC completed.

```python
age = int(input("Enter your age: "))
kyc_done = input("KYC completed? (yes/no): ")

if age >= 18 and kyc_done == "yes":
    print("Account opened. Welcome to PaisaPay!")
else:
    print("Sorry, you are not eligible.")
```

`and`, not `or`: with `or`, a 16-year-old with KYC would get in. Typing `Yes` with a capital Y gives "not eligible", because text comparison is exact.

**Diwali cashback.** ₹5,000 or more → 20%, ₹2,000 or more → 10%, otherwise 0%. The 5,000 check must come first; `>= 2000` first would swallow every big purchase.

```python
if amount >= 5000:
    cashback = 20
elif amount >= 2000:
    cashback = 10
else:
    cashback = 0
```

## Recap

- **if** runs a block only when a condition is True. **else** is everything else.
- **elif** gives many outcomes. Top to bottom, first True wins. Order matters.
- **match / case** is for one variable against exact values; `case _` is the else.
- **and / or / not** build bigger questions.
- **Nested if**: the inner question only when the outer is True. An else belongs to the if at its indentation.
- **Ternary**: `a if cond else b`, for simple two-way choices only.
- **Indentation is the syntax.** Inside vs outside the decision.

**Next class:** Loops. PaisaPay v4 keeps running: many payments, PIN retries, a mini statement.
