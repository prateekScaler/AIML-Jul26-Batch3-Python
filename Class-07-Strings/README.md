# Class 7 · Strings

PaisaPay v6 refused a payment because the user typed ` UPI` instead of `upi`. The user did nothing wrong. In this class Python learns to read, clean, cut and build text: strings.

**By the end of this class you can:**

- Index and slice a string the way you index and slice a list.
- Clean text with `strip`, `lower`, `upper` and `title`, and search it with `find`, `in`, `startswith` and `endswith`.
- Cut a string into a list with `split` and glue a list back with `join`.
- Build text with values inside it using f-strings, including `:.2f`.
- Explain why a string cannot be changed in place, and why every string method must have its result stored.

## How to use this folder

| File | What it is |
|---|---|
| [`index.html`](index.html) | The interactive class page. [Open it here](https://prateekscaler.github.io/AIML-Jul26-Batch3-Python/Class-07-Strings/), no download needed. **Step by step** shows a little at a time (press → or Next). **Show everything** gives the whole class on one page. |
| [`code/`](code/) | Every example from the class as a runnable file, in order. |
| [`code/paisapay_v7.py`](code/paisapay_v7.py) | Today's version of our course project. |
| [`Python-Class-07-Strings.ipynb`](Python-Class-07-Strings.ipynb) | The same examples as one notebook. [Open it in Google Colab](https://colab.research.google.com/github/prateekScaler/AIML-Jul26-Batch3-Python/blob/main/Class-07-Strings/Python-Class-07-Strings.ipynb) and run the cells, nothing to install. |
| [`PRACTICE.md`](PRACTICE.md) | Twelve coding problems on strings, easy to hard, with sample output, hints and solutions. |
| [`ASSIGNMENT.md`](ASSIGNMENT.md) | Predict the output, write programs, grow PaisaPay, think it through. |
| [`INTERVIEW-READINESS.md`](INTERVIEW-READINESS.md) | Interview questions, gotchas and AI-era questions on today's topics. |

Run the code in [PyLens](https://scaler-pylens.vercel.app/), or on your own machine with `python3 filename.py` (Python 3.10 or newer, because PaisaPay uses `match`).

Official post-read for this class: https://scaler-content.github.io/python-Foundations-7/

---

## 0. Revision: four short forms

Four short forms from earlier classes went past too quickly, so the class opens with them. Each has a long way that is always correct and a short way that means the same thing.

| Short form | Long way | Short way | Earns its place when |
|---|---|---|---|
| Ternary (Class 3) | `if balance >= 500:` / `status = "OK"` / `else:` / `status = "LOW"` | `status = "OK" if balance >= 500 else "LOW"` | one of two values, inside a print or a call; never for three outcomes |
| For over a list (Class 4) | a counter, `while i < len(items)`, `items[i]`, `i += 1` | `for item in items:` | every item in turn; use the index loop only when you need the position |
| List comprehension (Class 6) | start empty, loop, `append` | `[item * 2 for item in items if item >= 500]` | make, from, keep: transform or filter a list in one step |
| Lambda (Class 5) | `def f(x):` / `return x * 5 // 100` | `lambda x: x * 5 // 100` | a one-line rule handed to another function, as `sorted` and `filter` take in Class 9 |

Where the names come from: a ternary is Latin for "made of three", because it takes a value, a question and another value, Python's only three-part operator. `for` is the English word, read as "for each amount in amounts". `lambda` is the Greek letter the logician Alonzo Church used in the 1930s for functions without names. The name "comprehension" comes from mathematics, where a set can be written by its rule instead of by listing its members: the set of all x × 2 for x in amounts. Python borrowed the idea and the name; think "comprehensive", the whole list stated in one rule, not "comprehension" as in understanding. It is syntactic sugar in the strict sense: a shorter way to write something the language could already do, since every comprehension can be written as the loop, and Python builds the same list either way.

Three things to remember. A ternary must have its `else`, because it has to produce a value either way. The loop variable is a copy of the box, so `amount = amount * 2` inside a `for` does not change the list; build a new list with a comprehension instead. A comprehension never changes its source list. And if a short form needs a second read, write the long form: correct beats clever.

## 1. Why strings

Everything arrives as text. `input()` gives text even when the user typed a number. A file, a web page and a bank SMS are text. An LLM's answer is text, and your code has to find the number, the name or the JSON inside it. Parsing is string work.

## 2. A string is a sequence

```python
word = "Python"
print(len(word))     # 6
print(word[0])       # P
print(word[-1])      # n
print(word[0:3])     # Pyt     start included, stop excluded
print(word[2:])      # thon
print(word[::2])     # Pto     every second character
print(word[::-1])    # nohtyP  reversed
print(word[-4:])     # thon    the last four
```

Slicing works exactly as it did on lists in Class 6: `amounts[0:3]` gives boxes 0, 1 and 2, and so does `word[0:3]`. Single or double quotes both make a string; double quotes help when the text has an apostrophe. Every character has an index, 0 from the front and -1 from the back, and slicing follows the same exclusive-stop rule as `range` and lists. `len` counts every character, spaces included, and `len("")` is 0: the empty string is a string, not nothing. `input()` always gives a string, so `"4321" == 4321` is False.

## 3. String methods

| Method | What it does | Example |
|---|---|---|
| `lower()`, `upper()` | change the case | `"Card".lower()` → `"card"` |
| `title()` | a capital at the start of every word, where a word is any run of letters: it restarts at a space, hyphen, apostrophe or digit | `"rashi sharma".title()` → `"Rashi Sharma"`, `"it's".title()` → `"It'S"` |
| `strip()` | remove spaces at both ends only | `"  Rashi  ".strip()` → `"Rashi"` |
| `replace(old, new)` | replace every match | `"banana".replace("a", "o")` → `"bonono"` |
| `find(piece)` | the index where it starts, or -1 | `"I love Python".find("Python")` → `7` |
| `startswith`, `endswith` | True or False | `"report.pdf".endswith(".pdf")` → `True` |
| `split()`, `split(",")` | cut into a list | `"Python is easy".split()` → `['Python', 'is', 'easy']` |
| `", ".join(list)` | glue a list into a string | `", ".join(["A", "B"])` → `"A, B"` |

`in` works on strings as it does on lists: `"@" in upi_id`. Two habits matter in every real program. Lower-case and strip user input before you compare it, so "YES", "Yes" and " yes" are the same answer. And compare `find` with a number, never with True or False: not found is -1, which is not False.

`split` and `join` are the bridge between strings and lists: `"rashi@okaxis".split("@")` gives `['rashi', 'okaxis']`, and `"@".join(...)` puts it back.

## 4. f-strings

```python
name = "Rashi"
age = 20
print("My name is " + name + " and I am " + str(age) + " years old.")   # works, clumsy
print(f"My name is {name} and I am {age} years old.")                    # same, clean
print(f"Total: {price * quantity}")                                      # an expression
print(f"Price: {price:.2f}")                                             # two decimals
```

Say "eff-string"; the name is short for formatted string. The `f` before the quote tells Python to fill the braces. Any type goes in, no `str()` needed, and an expression inside the braces is worked out first. Forget the `f` and the braces are printed as they are, `Hello {name}`, with no error: the most common f-string bug.

## 5. Escape characters

A backslash makes the next character special: `\n` is a new line, `\t` a tab, `\"` and `\'` a quote inside the string, `\\` one backslash. `'It's a nice day'` is a `SyntaxError` because the string ends after `It`; write `"It's a nice day"` with the other quote, or `'It\'s a nice day'`.

## 6. Strings cannot change

`word[0] = "J"` raises `TypeError: 'str' object does not support item assignment`. A string is immutable. To "change" it, build a new one: `word = "J" + word[1:]`.

That has a consequence that is the trap of the class:

```python
text = "hello"
text.upper()        # builds "HELLO" and throws it away
print(text)         # hello
text = text.upper() # caught
```

Class 6: `sort()` changes the list in place and gives back `None`. Today: `upper()` cannot change the string and gives back a new one. Opposite mechanisms, the same bug: the real result is the return value, so store it. Because each method returns a usable string, they chain: `input("Name: ").strip().title()`. [Python tutorial: strings are immutable](https://docs.python.org/3/tutorial/introduction.html#text)

| | List | String |
|---|---|---|
| Ordered, indexed from 0, sliceable, loopable | yes | yes |
| `x[0] = ...` | allowed, mutable | TypeError, immutable |
| Methods | change the list, return None | cannot change it, return a new string |

## 7. Walking through a string

```python
word = "education"
count = 0
for character in word:
    if character in "aeiou":
        count += 1
print("Vowels:", count)    # 5
```

## 8. A word is not nothing

> **Real world.** A man in California chose the car number plate NULL. In many computer systems the word NULL means "nothing here", so every fine with a missing plate number was sent to him, $12,049 at one point, and the renewal website treated his plate as empty and refused him. The text NULL is four letters; an empty value is a different thing. In Python, `"None"` is a string of four letters, `""` is a string with nothing in it, and `None` is not a string at all. [Wired: how a NULL licence plate landed one hacker in ticket hell](https://www.wired.com/story/null-license-plate-landed-one-hacker-ticket-hell/)

## 9. Debug clinic

| Bug | What you see | Fix |
|---|---|---|
| `'It's late'` | `SyntaxError: unterminated string literal` | Use the other quote, or `\'` |
| `word[0] = "J"` | `TypeError` | Build a new string: `"J" + word[1:]` |
| `text.upper()` on its own line | nothing changes, no error | `text = text.upper()` |
| `if text.find("x"):` | True even when not found | compare with -1: `if text.find("x") != -1:` |
| `"Hello {name}"` | prints the braces | add the `f` |

## Project: PaisaPay v7

Version 7 is v6 plus strings. Every answer goes through `clean`, which strips and lower-cases it, so ` UPI` works. A UPI ID is checked with `split("@")`: exactly one `@` with something on both sides, and the part before `@` becomes the payee's name on the receipt. A card number is masked with a slice so only the last four digits ever show. Every message is an f-string.

```python
def clean(text):
    return text.strip().lower()

def is_valid_upi_id(upi_id):
    parts = upi_id.split("@")
    return len(parts) == 2 and len(parts[0]) > 0 and len(parts[1]) > 0

def mask(card):
    return "**** **** **** " + card[-4:]

def print_receipt(name, amount, mode, fee, cashback, balance):
    print(f"Paid ₹{amount} to {name} via {mode_name(mode)}")
    print(f"Fee ₹{fee} | Cashback ₹{cashback} | Balance ₹{balance}")
```

The full program is [`code/paisapay_v7.py`](code/paisapay_v7.py). A sample run:

```text
1 Pay  2 Balance  3 Statement  4 Exit  5 Add  6 Card
Choose: 1
Pay to (UPI ID): rashi@okaxis
Amount in rupees: 600
Mode (upi / card / netbanking):  UPI
UPI PIN: 4321
Paid ₹600 to Rashi via UPI
Fee ₹0 | Cashback ₹10 | Balance ₹410

1 Pay  2 Balance  3 Statement  4 Exit  5 Add  6 Card
Choose: 6
Card number: 4111 2222 3333 4444
Card linked: **** **** **** 4444
```

What v7 cannot do yet: keep the name, amount and mode of one payment together, which needs records in Class 8; survive a non-number typed as an amount, which `int()` still crashes on until errors in Class 12; and check a UPI ID or card number properly, which is regex in Class 11.

## Mini practices and mini challenge

A name formatter that strips, title-cases and greets; a sentence analyzer that prints the length, first and last characters, the upper-case version, a replacement and the list of words; and a username validator with `len`, `in` and `lower`. Full code: [`code/12_practice.py`](code/12_practice.py), [`code/13_username.py`](code/13_username.py). Then do the twelve problems in [`PRACTICE.md`](PRACTICE.md).

## Recap

Before reading on, write your own three-point recap: what would you tell a friend who missed this class? Then compare.

- **A string** is a sequence of characters. Index and slice it like a list.
- **Methods**: lower, upper, title, strip, replace, find, startswith, endswith, split. All give back something new.
- **join**: `", ".join(list)` glues a list into a string.
- **f-strings**: `f"Hello {name}"`, expressions and `:.2f` inside the braces.
- **Escapes**: `\n`, `\t`, `\"`.
- **Immutable**: `word[0] = "J"` is refused. Build a new string, and catch what methods return.
- **PaisaPay v7**: clean input, a UPI ID check, a masked card, f-string receipts.

Next class: sets, tuples and dictionaries. A payment as one record, unique payees, lookups by name.
