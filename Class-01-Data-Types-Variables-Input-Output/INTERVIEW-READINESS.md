# Interview Readiness · Class 1

Data types, variables, input and output look basic. Interviewers use them to check whether you understand what Python is doing or only what it prints.

How to use this page: answer each question out loud or on paper first. Then open the answer. For the "predict the output" questions, run the code after you commit to an answer.

- [A. Questions interviewers ask](#a-questions-interviewers-ask)
- [B. Gotchas: predict the output](#b-gotchas-predict-the-output)
- [C. Explore, with AI in the loop](#c-explore-with-ai-in-the-loop)

---

## A. Questions interviewers ask

**A1. What is a variable in Python?**

<details><summary>Answer</summary>

A name that refers to a value. `age = 25` stores the value 25 and makes the name `age` refer to it. The name can later be pointed at a different value, even one of a different type.

A stronger answer adds: in Python a variable is a label attached to an object, not a fixed-size box that holds one kind of thing.
</details>

**A2. Is Python statically typed or dynamically typed? Is it strongly or weakly typed?**

<details><summary>Answer</summary>

**Dynamically typed:** you never declare a type, and the same name can refer to an `int` now and a `str` later.

```python
x = 5
x = "five"   # allowed
```

**Strongly typed:** Python does not silently convert between unrelated types.

```python
"5" + 5   # TypeError, not "55" and not 10
```

"Dynamic" is about *when* types are checked (while running). "Strong" is about *how strictly* they are enforced.
</details>

**A3. What does `input()` return? How do you read a number from the user?**

<details><summary>Answer</summary>

Always a `str`, whatever the user types. To get a number, cast it: `int(input("Age: "))` or `float(input("Price: "))`.
</details>

**A4. What is type casting? What is the difference between implicit and explicit conversion?**

<details><summary>Answer</summary>

Type casting is converting a value from one type to another.

- **Explicit:** you ask for it: `int("25")`, `float("99.5")`, `str(100)`.
- **Implicit:** Python does it for you in a few safe cases, for example `5 + 2.0` gives `7.0` (the int is widened to a float).

Python never implicitly converts between `str` and numbers.
</details>

**A5. What is the difference between `25`, `25.0` and `"25"`?**

<details><summary>Answer</summary>

`25` is an `int`, `25.0` is a `float`, `"25"` is a `str`. They print almost the same but behave differently: `25 + 1` is `26`, `25.0 + 1` is `26.0`, and `"25" + 1` is a `TypeError`.
</details>

**A6. What are the rules and conventions for naming variables?**

<details><summary>Answer</summary>

Rules (Python enforces these): letters, digits and underscores only; cannot start with a digit; no spaces; cannot be a keyword such as `class` or `if`; case-sensitive.

Conventions (people expect these): `snake_case` for variables, a name that says what the value means (`amount_paid`, not `a`), and do not reuse built-in names such as `print`, `input` or `type`.
</details>

**A7. Why should money not be stored as a `float`? What would you use?**

<details><summary>Answer</summary>

Floats are stored in binary and cannot represent many decimals exactly: `0.1 + 0.2` is `0.30000000000000004`. Small errors add up across many transactions.

Store money as an **`int` in the smallest unit** (paise, cents). Payment APIs do this: with Razorpay, ₹299 is sent as `29900`. Python also has a `Decimal` type for exact decimal arithmetic.
</details>

**A8. Is Python compiled or interpreted?**

<details><summary>Answer</summary>

Both, in two steps. Python first compiles your code to bytecode, then the Python virtual machine interprets that bytecode. In everyday terms it is called an interpreted language because you run the source directly and errors appear while it runs.

That is why a `SyntaxError` stops everything before the first line runs, while a `NameError` on line 10 only appears when line 10 is reached.
</details>

---

## B. Gotchas: predict the output

Commit to an answer before you open each one.

**B1.**

```python
a = input("First amount: ")    # user types 100
b = input("Second amount: ")   # user types 50
print(a + b)
```

<details><summary>Answer</summary>

`10050`. Both are strings and `+` joins strings. No error, just a wrong total.
</details>

**B2.**

```python
print("5" * 3)
```

<details><summary>Answer</summary>

`555`. A string times an int repeats the string. Not 15, and not an error.
</details>

**B3.**

```python
print(int(99.9))
print(int("99.9"))
```

<details><summary>Answer</summary>

The first line prints `99`: casting a float to an int cuts off the decimal part without rounding. The second line raises `ValueError: invalid literal for int() with base 10: '99.9'`, because the *text* "99.9" is not a whole number.
</details>

**B4.**

```python
name = print("What is your name?")
print(name)
```

<details><summary>Answer</summary>

```text
What is your name?
None
```

`print()` displays something but gives nothing back, so `name` holds `None`. The author meant `input()`.
</details>

**B5.**

```python
print = "hello"
print("hi")
```

<details><summary>Answer</summary>

`TypeError: 'str' object is not callable`. The first line replaced the built-in `print` function with a string. Python allowed it. Never reuse built-in names for variables.
</details>

**B6.**

```python
print(True + True)
```

<details><summary>Answer</summary>

`2`. In Python, `bool` is a kind of `int`: `True` behaves as 1 and `False` as 0.
</details>

**B7.**

```python
print(bool("False"))
```

<details><summary>Answer</summary>

`True`. Any non-empty string converts to `True`, including the text "False". This is the surprise that was parked in class.
</details>

**B8.**

```python
print(0.1 + 0.2 == 0.3)
```

<details><summary>Answer</summary>

`False`. `0.1 + 0.2` is `0.30000000000000004`. (`==` asks "are these equal?" and is covered in the next class.)
</details>

**B9.**

```python
pin = 0421
```

<details><summary>Answer</summary>

`SyntaxError: leading zeros in decimal integer literals are not permitted`. A PIN is text: `pin = "0421"`.
</details>

**B10.**

```python
x = int(" 42 ")
print(x)
```

<details><summary>Answer</summary>

`42`. `int()` ignores spaces around the digits. It does not accept `"4 2"`, `"42.0"` or `"1,000"`.
</details>

---

## C. Explore, with AI in the loop

These connect today's topics to what you built in the GenAI modules. There is not always one right answer. The goal is to investigate.

**C1. A tool call with the wrong type.** Your agent calls a tool `pay` with these arguments:

```json
{ "to": "Chai Point", "amount": "500" }
```

Inside the tool, the code runs `balance - amount` with `balance = 1000`. What happens? Where should this be prevented?

<details><summary>Things to find</summary>

`TypeError: unsupported operand type(s) for -: 'int' and 'str'`. The amount arrived as text.

Two places to prevent it: declare `"amount"` as `integer` in the tool's input schema so the model is told what to send, **and** cast and check inside the tool, because a schema is a request, not a guarantee.
</details>

**C2. JSON types and Python types.** Tool definitions and API responses use JSON. Make a table that maps each JSON type to a Python type. Why does `true` work in JSON but fail in Python?

<details><summary>Things to find</summary>

| JSON | Python |
|---|---|
| string | `str` |
| number | `int` or `float` |
| `true` / `false` | `True` / `False` |
| `null` | `None` |

JSON spells booleans in lowercase. In Python, lowercase `true` is read as a variable name and raises `NameError`.
</details>

**C3. The same bug in n8n.** In an n8n expression, a form field `amount` holds `"500"`. You write `{{ $json.amount + 10 }}`. What do you get, and why is it not an error?

<details><summary>Things to find</summary>

`"50010"`. n8n expressions run JavaScript, and JavaScript quietly joins a string and a number. Python refuses the same operation with a `TypeError`. Which behaviour would you rather have in a payments workflow?
</details>

**C4. When the model does not return a number.** You prompt an LLM: "How many items are in this order? Reply with the number." It replies `"3 items"` or `"Three"`. Your code runs `int(reply)`. What happens? List two ways to make this step reliable.

<details><summary>Things to find</summary>

`ValueError: invalid literal for int() with base 10: '3 items'`. A model's reply is always text and is not guaranteed to be clean.

Options to research: ask for structured output with a declared type, validate the reply before casting, and retry or fall back when the check fails. Casting is the exact point where many agent pipelines break.
</details>

**C5. AI as a tester, not an author.** Give an AI assistant your PaisaPay v1 code and ask:

> "List ten inputs a user could type that would crash this program or produce a wrong receipt. Do not fix the code."

Run each input yourself. For every crash, write down the error type. How many of the ten did the AI get right?

**C6. Catch the AI being wrong.** Ask an assistant, without running anything: "What does `int("99.5")` return in Python?" Then run it. If the answer was wrong, what does that tell you about checking small claims yourself?

**C7. Numbers that outgrow their type.** In 2014 YouTube moved its view counter from a 32-bit to a 64-bit integer as "Gangnam Style" approached 2,147,483,647 views, the largest value a 32-bit signed integer can hold. Find out: does a Python `int` have a maximum? Try `print(2 ** 100)`.

<details><summary>Things to find</summary>

A Python `int` has no fixed maximum; it grows as needed. Many other languages, databases and file formats do have fixed sizes. That matters the moment your Python value is stored somewhere else.
</details>

**C8. Why no leading zeros?** `pin = 0421` is a `SyntaxError` in Python. Ask an AI assistant why Python refuses a leading zero in an integer, and what a leading zero meant in older versions. Then test the answer: what does `print(0o421)` show?

<details><summary>Things to find</summary>

In Python 2, a leading zero meant the number was written in **octal** (base 8), so `0421` was 273, not 421. That surprised people, so Python 3 removed it. Octal now needs an explicit `0o` prefix: `0o421` is 273. A PIN, a phone number or a pincode with a leading zero is text, not a number.
</details>

**C9. Why can a name not start with a digit?** `2nd_payee = "Zomato"` is a `SyntaxError`. Ask an AI assistant why, and ask for one example where allowing it would be confusing. First run `print(1e3)` yourself.

<details><summary>Things to find</summary>

When Python reads a digit, it starts reading a number. `1e3` is already a valid number: it prints `1000.0`. If names could start with digits, Python could not tell whether `1e3` is a number or a variable. So the rule is simple: a name starts with a letter or an underscore.
</details>
