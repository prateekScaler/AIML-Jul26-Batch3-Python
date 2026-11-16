# Class 16 · Exceptions, CSV and Modules

Class 15 gave programs a memory: files. This class makes file programs safe and useful. You catch errors with `try` and `except` instead of crashing, read and write CSV files, and split code into modules you can import. PaisaPay v16 remembers its balance and every payment between runs.

**By the end of this class you can:**

- Catch a named error, such as `FileNotFoundError`, with `try`/`except`.
- Read and write CSV files with `csv.reader`, `csv.DictReader` and `csv.writer`.
- Write your own module, import it four ways, and use the standard library.

## How to use this folder

| File | What it is |
|---|---|
| [`index.html`](index.html) | The interactive class page. [Open it here](https://prateekscaler.github.io/AIML-Jul26-Batch3-Python/Class-16-Exceptions-CSV-And-Modules/), no download needed. **Step by step** shows a little at a time (press → or Next). **Show everything** gives the whole class on one page. |
| [`code/`](code/) | Every example from the class as a runnable file, in order. Each file first creates the sample files it reads, so it runs anywhere. |
| [`code/paisapay_v16.py`](code/paisapay_v16.py) | Our course project, now with saved data. Keep [`code/paisapay_checks.py`](code/paisapay_checks.py), the module it imports, in the same folder. |
| [`code/greetings.py`](code/greetings.py) | The small module that `03_import_modules.py` imports. |
| [`Python-Class-16-Exceptions-CSV-And-Modules.ipynb`](Python-Class-16-Exceptions-CSV-And-Modules.ipynb) | The same examples as one notebook. [Open it in Google Colab](https://colab.research.google.com/github/prateekScaler/AIML-Jul26-Batch3-Python/blob/main/Class-16-Exceptions-CSV-And-Modules/Python-Class-16-Exceptions-CSV-And-Modules.ipynb) and run the cells in order, nothing to install. |
| [`PRACTICE.md`](PRACTICE.md) | Eight coding problems on `try`/`except`, CSV files and modules, with sample output, hints and solutions. |
| [`ASSIGNMENT.md`](ASSIGNMENT.md) | Predict the output, write programs, grow PaisaPay, think it through. |
| [`INTERVIEW-READINESS.md`](INTERVIEW-READINESS.md) | Interview questions, gotchas and AI-era questions on today's topics. |

Run the code on your own machine with `python3 filename.py` (Python 3.10 or newer, because PaisaPay uses `match`), in Google Colab, or in [PyLens](https://scaler-pylens.vercel.app/). Files are made in the folder the program runs in.

New to running Python on your own computer or to the terminal? See the two guides in the [Class 15 notes](../Class-15-File-Handling/README.md).

Official post-read for this class: https://scaler-content.github.io/python-Foundations-12/

---

## 1. Where Class 15 stopped

Class 15 covered files: memory and storage, the working folder, `open()` and `.read()`, the four modes, `with`, and reading line by line ([notes](../Class-15-File-Handling/README.md)). This class starts with what to do when a file is missing.

## 2. `try` and `except`

You have met errors before. Each one has a name, and Python calls them **exceptions**:

| This line | You met it in | The error |
|---|---|---|
| `int("abc")` | input, Class 1 | `ValueError` |
| `1200 / 0` | operators, Class 2 | `ZeroDivisionError` |
| `"500" + 100` | types, Class 2 | `TypeError` |
| `marks[5]` | lists, Class 6 | `IndexError` |
| `contacts["vamsi@oksbi"]` | dictionaries, Class 8 | `KeyError` |
| `open("missing.txt")` | files, last class | `FileNotFoundError` |

So far an exception stopped the program. `try` and `except` give the program a plan B. Class 2's bill split, with nobody to split with:

```python
bill = 1200
people = 0

try:
    share = bill / people
    print("Each pays", share)
except ZeroDivisionError:
    print("Nobody to split with.")          # prints this; no crash
```

Read it aloud: "try to split the bill, **except** if it is a division by zero, then print a message." The line after the failing one, `print("Each pays", share)`, never runs: the error skips it. An `except` catches only the error it names: `"500" + 100` is a `TypeError`, and `except ValueError:` does not catch it.

Two things can go wrong in the bill split, so each gets its own `except`:

```python
def split(bill, people_text):
    try:
        people = int(people_text)
        return bill / people
    except ValueError:
        return "Please type a number."
    except ZeroDivisionError:
        return "Nobody to split with."

print(split(1200, "4"))
print(split(1200, "four"))
print(split(1200, "0"))
```

```text
300.0
Please type a number.
Nobody to split with.
```

The same plan works for files, where things you do not control can break:


Files live outside your program, so things you do not control can break: a missing file (`FileNotFoundError`), no permission (`PermissionError`), a folder instead of a file (`IsADirectoryError`), bad data (`ValueError`).

```python
try:
    file = open("missing.txt")
    print("A")                  # skipped: the error happened on the line above
except FileNotFoundError:
    print("B")
print("C")                      # prints B, then C
```

Read it aloud: "try to open the file, **except** if it is not found, then print a message." Python calls an error that happens while the program runs an **exception**, something outside the normal path; `except FileNotFoundError:` names the one to catch, and its indented lines are plan B. (Java and JavaScript call this `catch`.) When the code in `try` works, `except` is skipped. When an error happens, Python jumps straight to a matching `except`, then carries on after it. An `except` only catches the error it names: `except ValueError` does not catch a `FileNotFoundError`, and the program still crashes. With several `except` lines, the first match wins, so put specific errors first.

Not only files fail. Text that is not a number breaks `int()`:

```python
try:
    amount = int("abc")
    print("Amount:", amount)
except ValueError:
    print("Please type a number.")      # this prints
```

Python picks the `except` by the kind of error, not by position: a `ValueError` passes over `except FileNotFoundError:` and runs `except ValueError:`.

> **Real world, 1996.** About 37 seconds after the first Ariane 5 launched, a 64-bit number was converted to a 16-bit integer, and it did not fit. Only four of seven such conversions were protected. This one was not, the guidance computer stopped, and the rocket broke up: a loss of more than US$370 million. Before you write `try`, ask what can fail and what should happen then. [ESA: Inquiry Board report](https://www.esa.int/Newsroom/Press_Releases/Ariane_501_-_Presentation_of_Inquiry_Board_report) · [Wikipedia: Ariane flight V88](https://en.wikipedia.org/wiki/Ariane_flight_V88)

## 3. CSV files

A CSV file is a table written as text: one row per line, commas between the columns. The passbook as `payments.csv`:

```text
payee,amount
Sumit,600
Vamsi,250
```

Splitting on commas yourself breaks when a value has a comma: `'"Sumit Kumar, Jr",600'.split(",")` gives 3 parts. A CSV puts such a value in quotes, and the `csv` module reads it as 2 parts. Reading the line `"Sumit Kumar, Jr",600` with `csv.reader` gives `['Sumit Kumar, Jr', '600']`: the comma stays in the name, and the quotes are gone.

```python
import csv

with open("payments.csv", "r") as file:
    for row in csv.reader(file):
        print(row)               # ['payee', 'amount'], ['Sumit', '600'], ['Vamsi', '250']

total = 0
with open("payments.csv", "r") as file:
    for row in csv.DictReader(file):
        print(row["payee"], row["amount"])
        total += int(row["amount"])
print("Total:", total)           # Total: 850

rows = [["payee", "amount"], ["Sumit", 600], ["Vamsi", 250]]
with open("payments.csv", "w", newline="") as file:
    csv.writer(file).writerows(rows)
```

`csv.reader` gives one list per row, header included: `int(row[1])` on the header row is `ValueError: invalid literal for int() with base 10: 'amount'`. `csv.DictReader` uses the header as keys, so you write `row["amount"]`. Every value is a string: `row["amount"] + 1` is a `TypeError`, and `int(row["amount"]) + 1` works. The keys are exactly the header's text: `row["Amount"]` is `KeyError: 'Amount'`. Opening a CSV with `"w"` erases it, header included; use `"a"` to add a row. `\n` is the line feed (move to the next line) and `\r` is the carriage return (go back to the start of the line; the name comes from typewriters). Windows ends every line with both, `\r\n`; Mac and Linux use only `\n`. When a program writes text, Python changes every `\n` into the line ending of that computer: no change on Mac and Linux, `\r\n` on Windows. `newline=""` matters on Windows: csv already ends every row with `\r\n`, and without `newline=""` Windows adds its own `\r`, so each row ends `\r\r\n` and a spreadsheet shows an empty row after every row. Read back, those come as empty lists (`[]`), and `int(row[1])` then fails with IndexError. On a Mac or Linux the bug hides, so always add it.

> **Real world, 2016 and 2020.** Opened in Excel, the gene name MARCH1 became the date 1-Mar. A 2016 study found that about one-fifth of genomics papers with Excel gene lists had such errors, and in 2020 scientists renamed 27 genes, for example MARCH1 to MARCHF1. A CSV is plain text; the program that opens it decides what each value means. [Genome Biology, 2016](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-016-1044-7) · [Engadget, 2020](https://www.engadget.com/scientists-rename-genes-due-to-excel-151748790.html)

## 4. Modules

Any `.py` file is a module. It becomes one when another file imports it by name.

```python
# greetings.py
def say_hello(name):
    return f"Hello, {name}!"

def say_goodbye(name):
    return f"Goodbye, {name}!"
```

```python
import greetings                       # greetings.py is in the same folder
print(greetings.say_hello("Parveen"))  # Hello, Parveen!
```

| You write | Then you call | Use it when |
|---|---|---|
| `import greetings` | `greetings.say_hello(...)` | you want it clear where a name came from |
| `from greetings import say_hello` | `say_hello(...)` | you need one or two names |
| `import greetings as g` | `g.say_hello(...)` | the module name is long |
| `from greetings import *` | `say_hello(...)` | avoid it: names can clash without a warning |

```python
def say_hello(name):
    return "Hi " + name

from greetings import *
print(say_hello("Prasad"))    # Hello, Prasad! The import replaced your function.
```

**The standard library** comes with Python, so there is nothing to install. Knowing that a module exists matters more than learning all of it.

```python
import math, random, datetime, os
print(math.sqrt(49))           # 7.0, every time
print(random.randint(1, 6))    # 1 to 6, changes
print(datetime.date.today())   # today's date
print(os.getcwd())             # get current working directory: where open() looks
```

Importing runs the module's file once; a second `import` reuses it. `from greetings import say_hello` brings in `say_hello` only, so `greetings.say_hello(...)` is then a `NameError`. A module in another folder gives `ModuleNotFoundError`. To import from a folder, name it: `from helpers import greetings`, `from helpers.greetings import say_hello`, or `import helpers.greetings`. The dot means "inside".

Python looks for a module in your program's folder first. A file of your own named `random.py` hides the real `random` module. Never name a file after a module you use.

> **Real world, 2017.** `pip install` downloads packages from PyPI that are not built in. In 2017 Slovakia's security team found ten PyPI packages with look-alike names, such as `urlib3` for `urllib3`, that ran hidden code on install. PyPI removed them. Type the exact name, and check that a package an AI suggests really exists. [BleepingComputer](https://www.bleepingcomputer.com/news/security/ten-malicious-libraries-found-on-pypi-python-package-index/) · [python-dev announcement](https://mail.python.org/pipermail/python-dev/2017-September/149569.html)

## 5. Mini project: a log file analyzer

Read website visits from a CSV, handle a missing file, count the errors (status code 400 or above), and write a summary file. Full program: [`code/05_log_analyzer.py`](code/05_log_analyzer.py).

```text
visits.csv: page,status_code / /home,200 / /login,200 / /admin,403 / /checkout,500

Total requests: 4
Errors: 2
```

403 and 500 are both 400 or more, so there are two errors. The header is not a visit. `int(r["status_code"])` converts the string the CSV gave. The program uses every idea from today: `try`, `with`, `DictReader`, `int()` and `"w"`.

## Project: PaisaPay v16

PaisaPay now remembers. Version 13 forgot every payment at Exit.

- **The balance** lives in `paisapay_balance.txt`. `load_balance` reads it at start, with two excepts: no file on the first run, and a damaged file. `save_balance` writes it with `"w"` after every change, not only at Exit, so a crash loses nothing.
- **Every payment** is appended to `paisapay_history.csv` with `"a"`. The header goes in only when the file is new (`os.path.exists`). Each payment gets its date from `datetime.date.today()`. At start, `load_history` reads the rows back with `DictReader` and turns the numbers back into ints.
- **The checks** (UPI ID, PAN, bank SMS, payment mode) moved into their own module, [`paisapay_checks.py`](code/paisapay_checks.py), and the app imports them.

```text
Run 1: pay Sumit ₹600 by UPI, then Exit.
Run 2:
Welcome to PaisaPay
Account type (basic / premium): basic
Loaded 1 saved payments. Balance ₹410
```

`paisapay_history.csv` after run 1:

```text
date,payee,amount,mode,fee,cashback
2026-11-16,Sumit,600,upi,0,10
```

What v16 cannot do yet: stay correct when two copies run at the same time, and stop anyone from opening `paisapay_balance.txt` and typing a new number. Real payment apps keep this data in a database on a server, for both reasons.

## Errors and debug clinic

| You see | It means | Fix |
|---|---|---|
| `FileNotFoundError: [Errno 2] No such file or directory: 'missing.txt'` | the file is not there, or the name or folder is wrong | check the name; catch it with try/except |
| `ValueError: invalid literal for int() with base 10: 'abc'` | text that is not a number went into int() | catch ValueError, or clean the text first |
| `TypeError: can only concatenate str (not "int") to str` | a value read from a CSV is text | int() it first |
| `KeyError: 'Amount'` | no column with exactly that name | match the header's spelling and capitals |
| `IndexError: list index out of range` | an empty row, often from a missing newline="" | write with newline=""; skip empty rows |
| `ModuleNotFoundError: No module named 'greeting'` | a typo, or the file is in another folder | check the name and the folder |
| `NameError: name 'greetings' is not defined` | you imported a function, not the module | call say_hello(...) directly |
| `AttributeError: module 'random' has no attribute 'randint'` | your own random.py hides the real one | rename your file |

**The except that hid a bug.** `passbook.txt` exists, yet this prints "No passbook yet.":

```python
try:
    with open("passbook.txt") as file:
        text = fille.read()
    print(len(text))
except:
    print("No passbook yet.")
```

Line 3 has a typo, `fille`, which raises a NameError. A bare `except:` catches every error, so it hid the typo and printed the wrong message. Name the error instead, `except FileNotFoundError:`, and Python shows the real problem: `NameError: name 'fille' is not defined. Did you mean: 'file'?`

## AI moments

1. **Which errors to catch.** Ask an assistant: "I am reading a text file in Python. Besides FileNotFoundError and PermissionError, what other exceptions can realistically happen here? Should I catch all of them, or let some crash the program?" Then test one yourself: pass a folder name, and see that your two excepts do not catch `IsADirectoryError`. Catch an error only when you have a real answer for it.
2. **Find the right module.** Ask: "I need a unique ID for each row of a CSV file I write in Python. Is there a standard library module for that, and how do I use it?" It will likely point to `uuid`. Check the official Python docs to confirm it is built in, not a package you would install.

## Recap

- **`try`/`except`:** try the risky part; `except` runs only if its named error happens, then the program goes on.
- **Name the error.** With several `except` lines, the one that matches the kind of error runs. A bare `except:` hides bugs.
- **CSV:** a table as text. `csv.reader` gives lists; `csv.DictReader` gives dictionaries keyed by the header.
- **Every CSV value is a string.** Convert with `int()`. Write with `newline=""`.
- **Modules:** any `.py` file can be imported. The standard library is already installed. Never name a file after a module.
- **PaisaPay v16** remembers its balance and every payment between runs.
