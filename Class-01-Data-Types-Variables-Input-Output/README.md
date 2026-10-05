# Class 1 · Data Types, Variables, Input & Output

The first class of the Python module. You go from "I have prompted AI to write code" to "I can write, read and fix a small Python program myself".

**By the end of this class you can:**

- Explain what a variable is and create one.
- Identify Python's four basic data types: `int`, `float`, `str`, `bool`.
- Display information with `print()` and receive it with `input()`.
- Convert between types with `int()`, `float()` and `str()` (type casting).
- Write comments.
- Read the four most common beginner errors and say what each one means.

## How to use this folder

| File | What it is |
|---|---|
| [`index.html`](index.html) | The interactive class page. Download the repo and open it in a browser. **Step by step** shows one thing at a time, the way we did in class (press → or Next). **Show everything** gives the whole class on one page. |
| [`code/`](code/) | Every example from the class as a runnable file, in order. |
| [`code/paisapay_v1.py`](code/paisapay_v1.py) | Today's version of our course project. |
| [`ASSIGNMENT.md`](ASSIGNMENT.md) | Practice problems for this class. |
| [`INTERVIEW-READINESS.md`](INTERVIEW-READINESS.md) | Interview questions, gotchas and AI-era questions on today's topics. |

Run the code in [PyLens](https://scaler-pylens.vercel.app/) (it shows what Python does at each line), or on your own machine with `python3 filename.py`.

Official post-read for this class: <https://scaler-content.github.io/python-Foundations-1/>

---

## 1. Why Python, and why now

You have already prompted LLMs, built n8n workflows, wired agents and vibe-coded apps. All of it ran on code that someone else wrote. In this module, you write it.

**Programming** = giving instructions to a computer, in a programming language it understands.

| A prompt | A program |
|---|---|
| A request in plain English | Instructions in exact syntax |
| The model interprets what you meant | Python does exactly what you wrote |
| Can answer differently each time | Same input, same result, every time |
| Rarely refuses; it guesses | Refuses to run when a rule is broken |

### AI writes code. So why learn Python?

A frontier model can build an impressive demo from one prompt. Five reasons that learning to code still matters:

| Angle | Why | Example |
|---|---|---|
| **Reliability** | A demo runs on the happy path. Real users do not. | A vibe-coded payment form asks for an amount. On demo day you type `500` and it works. On launch day users type `₹500`, `1,000` or nothing at all, and each one crashes it. |
| **Trust** | You cannot check what you cannot read. | Asked to add 18% GST to a ₹100 item, AI writes `total = price + price * 18`. It runs without an error and bills ₹1,900. |
| **Debugging** | When it breaks, someone must find the cause. | Without reading code: error → ask AI again → new error, in a loop. With it: error → read the message → fix the line. |
| **Direction** | Knowing the words makes your prompts precise. | "The total is wrong. Fix it." makes AI guess. "amount comes from input() as a str. Convert it to int before adding." gets the exact line fixed. |
| **Career** | Interviews test reading and fixing code, not prompting. | A common warm-up: what does `x = "5"` then `print(x * 3)` show? (`555`: text times 3 repeats the text.) |

> **What the research says.** In a 2026 Anthropic study, 52 engineers learned a new Python library, half with AI help and half without. The AI group scored 50% on the follow-up test; the group that coded by hand scored 67%. The AI group finished only about two minutes sooner, and the biggest gap was in debugging. People who asked AI to explain kept their learning; people who only asked it to write the code did not. Use AI to understand, not to skip understanding. [Anthropic: How AI assistance impacts the formation of coding skills](https://www.anthropic.com/research/AI-assistance-coding-skills)

> **Real world.** In 2025 a founder was building an app with Replit's AI coding agent. He ordered a freeze: change nothing. The agent ran commands anyway and wiped the production database, with records of more than 1,200 executives. It also made up about 4,000 fake users, then said the data could not be recovered, which was wrong. An agent acts fast; only a person who understands the code can supervise it. [The Register](https://www.theregister.com/2025/07/21/replit_saastr_vibe_coding_incident/)

AI is the fast junior developer. You are the one who reads, checks and decides.

## 2. Your first program and `print()`

```python
print("Hello, world!")
```

`print()` is a function that displays what is inside the parentheses. The rules for how an instruction must be written are called **syntax**. Break a rule and Python refuses to run anything:

```python
print("Hello, world!"
# SyntaxError: '(' was never closed
```

`print()` shows the **result** of an expression, not the characters you typed:

```python
print(25 + 5)        # 30
print("500 + 100")   # 500 + 100   (quotes make it text)
print(500 + 100)     # 600
```

## 3. Data and the four basic data types

Not all data is the same kind. Python sorts every value into a **data type**.

| Type | Python name | Example | Meaning |
|---|---|---|---|
| Integer | `int` | `25` | Whole numbers |
| Floating point | `float` | `5.8` | Numbers with a decimal point |
| String | `str` | `"Kishor"` | Text, inside quotes |
| Boolean | `bool` | `True` / `False` | Yes or no |

Python decides the type from the **quotes** and the **decimal point**, not from how the value looks to us:

| Value | Type | Why |
|---|---|---|
| `42` | `int` | No quotes, no decimal point |
| `42.0` | `float` | The decimal point decides, even for a whole value |
| `"42"` | `str` | Quotes make it text |
| `True` | `bool` | Capital T, no quotes |
| `"True"` | `str` | Quotes win |

Two things that catch people:

- A UPI PIN like `0421`, a phone number or an Aadhaar number is a **`str`**. You never do maths on it, and a leading zero must survive. `int("0421")` is `421`.
- `true` (lowercase) is not a boolean. Python reads it as a variable name and raises `NameError`.

> **Real world.** Excel kept deciding that gene names such as `MARCH1` and `SEPT1` were dates and silently changed them to `1-Mar` and `1-Sep`. A 2016 study found such errors in about one-fifth of genetics papers that shared Excel gene lists. In 2020 the naming committee renamed 27 human genes (`MARCH1` → `MARCHF1`, `SEPT1` → `SEPTIN1`). The type decides what a value means; a wrong guess corrupts data silently. [The Register](https://www.theregister.com/2020/08/06/excel_gene_names/) · [ThePrint](https://theprint.in/science/27-genes-in-your-body-now-have-a-new-name-because-microsoft-excel-confused-them-for-dates/477398/)

## 4. Variables

On its own, `25` is just a number. An age? A price? A score? A **variable** is a name that refers to a value stored in the program.

```python
name = "Kishor"
age = 25
height = 5.8
is_student = True

print(name)   # Kishor
print(age)    # 25
```

Think of a name tag on a box: the box holds the value, the tag is how you find it again.

**Rules for names**

| Name | Verdict |
|---|---|
| `amount_paid` | Good: lowercase words joined by underscores |
| `2nd_payee` | `SyntaxError`: a name cannot start with a digit |
| `payee name` | `SyntaxError`: no spaces |
| `Balance` and `balance` | Two different variables: Python is case-sensitive |
| `x` | Allowed, but tells the reader nothing |

Quotes mean data; no quotes means a name:

```python
payee = "Zomato"
print("payee")   # payee
print(payee)     # Zomato
```

> **Real world.** In 1999 NASA lost the Mars Climate Orbiter, a $327 million mission. One team's software reported thruster force in pound-force seconds; the navigation software read the same numbers as newton-seconds, wrong by a factor of 4.45. Nothing crashed for nine months. The spacecraft reached Mars about 57 km above the surface instead of the planned 226 km and was destroyed. A bare number means nothing; the name carries the meaning. [Wikipedia](https://en.wikipedia.org/wiki/Mars_Climate_Orbiter)

The same idea in a few lines:

```python
thrust = 100
print("Thrust:", thrust)    # 100 what?

thrust_pound_seconds = 100
thrust_newton_seconds = thrust_pound_seconds * 4.45
print("Thrust in newton-seconds:", thrust_newton_seconds)   # 445.0
```

## 5. The assignment operator `=`

`age = 25` does not say "age equals 25". It means: **assign** the value 25 to the name `age`.

```python
age = 20
print(age)      # 20
age = age + 1   # right side first: 20 + 1 = 21, then store 21 under age
print(age)      # 21
```

Python works out the right side first, using the current value, then stores the result. Reassigning a variable is normal.

Assignment copies the value; it does not link two names:

```python
price = 499
total = price
price = 599
print(total)    # 499
```

## 6. `type()`

```python
print(type(25))         # <class 'int'>
print(type(5.8))        # <class 'float'>
print(type("Kishor"))  # <class 'str'>
print(type(True))       # <class 'bool'>
```

The `<class '...'>` wrapping is normal output, not an error.

## 7. Comments

```python
# This is my age
age = 25  # Student's age
```

Python ignores everything after `#` on a line. Use comments to explain **why**, not to repeat **what** the code already says. AI assistants tend to comment every line; keep the comments that explain a decision and delete the rest.

## 8. `input()` and the big surprise

```python
name = input("What is your name? ")
print(name)
```

`input()` pauses the program, shows the prompt, waits for the user to type and press Enter, and gives back what was typed.

**`input()` always returns a string**, whatever the user types:

```python
age = input("What is your age? ")   # user types 25
print(type(age))                    # <class 'str'>
```

Everything a user types arrives as keystrokes, and keystrokes are text. Python never guesses that it "should" be a number.

This is true well beyond Python. A form field in n8n or Zapier arrives as `"500"`. An LLM's reply is always text. Agent tools and MCP declare a type (`string`, `number`, `boolean`) for every input so that text can be converted safely.

The dangerous version of this bug does not crash:

```python
a = input("First amount: ")    # 100
b = input("Second amount: ")   # 50
print(a + b)                   # 10050
```

## 9. Type casting

```python
age = input("What is your age? ")
next_year = age + 1
# TypeError: can only concatenate str (not "int") to str
```

Convert the text to a number as soon as it arrives:

```python
age = int(input("What is your age? "))
print(type(age))   # <class 'int'>
```

| Call | Result |
|---|---|
| `int("25")` | `25` |
| `float("99.5")` | `99.5` |
| `str(100)` | `"100"` |
| `int("99.5")` | `ValueError`: the text is not a whole number |
| `int(99.9)` | `99`: cuts off the decimal part, does not round |
| `"₹" + 500` | `TypeError`; use `"₹" + str(500)` |

`bool()` also exists. Its rules are surprising and it gets its own lesson later.

> **Real world.** In 1996 the first Ariane 5 rocket self-destructed 37 seconds after launch. Its software converted a 64-bit floating point number into a 16-bit integer; the value did not fit, the conversion failed and the guidance computer shut down. The loss was more than $370 million. The code had been reused from Ariane 4, where that number could never grow so large. A type conversion is a decision: ask what happens if the value does not fit. [Wikipedia](https://en.wikipedia.org/wiki/Ariane_flight_V88) · [Inquiry board report](http://sunnyday.mit.edu/nasa-class/Ariane5-report.html)

The same shape in Python: one conversion fails, and everything after it stops.

```python
speed = "32768.5"                 # the sensor sends a decimal number
speed_whole = int(speed)          # the code expected a small whole number
print("Steering the rocket...")   # never runs
# ValueError: invalid literal for int() with base 10: '32768.5'
```

Ariane's 16-bit integer could hold at most 32,767.

### How real payment apps store money

```python
print(0.1 + 0.2)   # 0.30000000000000004
```

Floats are stored in binary and many decimals cannot be stored exactly. Payment systems therefore keep money as an **`int` in the smallest unit**. With [Razorpay's API](https://razorpay.com/docs/api/orders/create/), to charge ₹299 you send `29900` (paise).

## 10. Putting it together

Almost every program has the shape **Input → Process → Output**.

```python
name = input("What is your name? ")
age = int(input("What is your age? "))

print("Hello", name)
print("You are", age, "years old.")
print("Next year, you will be", age + 1)
```

`print()` accepts several items separated by commas and puts a space between them. Mixing text and numbers is fine with commas, unlike with `+`.

## 11. The four errors of this class

| Error | Python is saying | Example |
|---|---|---|
| `SyntaxError` | The shape of the code is broken. Nothing ran. | `print("Hello"` |
| `NameError` | I do not know this name. | `Print("Hello")`, `name = Aanand` |
| `TypeError` | That operation does not work on these types. | `"25" + 1` |
| `ValueError` | Right type of thing, but this value cannot be used. | `int("99.5")` |

Read the error type and message first. Before guessing, before asking AI, before changing random things.

## 12. Using AI the right way in this class

1. **Explain, don't fix.** Paste an error and ask: "Explain this Python error in plain English. Do not give me the fix yet." Compare it with your own guess.
2. **Then verify the fix yourself.** Ask for the fix, run your own version, and confirm with `type()`. Do not accept a fix until your own run proves it.
3. **Read alternatives.** Ask: "Show me one other way to write these print statements that gives the same output." You will likely see an f-string such as `print(f"Hello, {name}!")`. You do not need to write it yet; you should be able to read it.

## Project: PaisaPay v1

Across the module we build **PaisaPay**, a small UPI-style payments app. Each class adds one capability. Today's version takes one payment and prints a receipt.

```python
print("Welcome to PaisaPay")

name = input("Your name: ")
payee = input("Pay to: ")
amount = int(input("Amount in rupees: "))

balance = 1000              # every new wallet starts with ₹1000
balance = balance - amount  # the money leaves the wallet

print("----- Receipt -----")
print("From:", name)
print("To:", payee)
print("Paid: ₹", amount)
print("Balance left: ₹", balance)
```

```text
Welcome to PaisaPay
Your name: Sangeeta
Pay to: Chai Point
Amount in rupees: 120
----- Receipt -----
From: Sangeeta
To: Chai Point
Paid: ₹ 120
Balance left: ₹ 880
```

What v1 cannot do yet: refuse a payment larger than the balance, accept an amount such as 99.50, or take a second payment. Those arrive with operators, decisions and loops.

## Recap

- A **variable** is a name that refers to a value. `=` assigns.
- Four basic **data types**: `int`, `float`, `str`, `bool`. Quotes and the decimal point decide.
- `print()` displays results. `input()` receives text, always a `str`.
- **Type casting** converts between types. `int(input(...))` is the daily pattern.
- **Comments** start with `#` and are for humans.
- Read the **error type** first.

**Next class:** Operators. PaisaPay v2 learns money maths: splitting bills, cashback, and checking whether the balance is enough.
