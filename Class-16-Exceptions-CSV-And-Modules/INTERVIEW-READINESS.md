# Interview Readiness · Class 16

Interviewers use files and modules to test whether you think about what can go wrong: a file that is missing, a mode that erases data, a number that comes back as a string, a file name that hides a real module. The questions below ask what Python does in each of those cases, and why.

How to use this page: answer each question out loud or on paper first, then open the answer. For "predict the output" questions, run the code in an empty folder after you commit to an answer.

- [A. Questions interviewers ask](#a-questions-interviewers-ask)
- [B. Gotchas: predict the output](#b-gotchas-predict-the-output)
- [C. Explore, with AI in the loop](#c-explore-with-ai-in-the-loop)

---

## A. Questions interviewers ask

**A1. Why do programs need files at all?**

<details><summary>Answer</summary>

Variables live in memory, and memory is cleared when the program ends. A file lives on disk, so the next run can read what the last run wrote. That is how PaisaPay v16 remembers the balance and the history. Real apps usually keep this data in a database, which is a program built to store and protect it.
</details>

**A2. What do the modes `"r"`, `"w"`, `"a"` and `"x"` do? Which one can lose data?**

<details><summary>Answer</summary>

`"r"` reads, and fails with `FileNotFoundError` if the file is missing. `"w"` writes, but first erases everything already in the file. `"a"` adds to the end and keeps what is there. `"x"` creates a new file and raises `FileExistsError` if one already exists. `"w"` is the one that loses data: opening a file with `"w"` erases it even if you write nothing.
</details>

**A3. Why use `with open(...)` instead of `open()` and `close()`?**

<details><summary>Answer</summary>

`with` closes the file when the block ends, even if an error happens inside the block. With plain `open()`, an error before `close()` leaves the file open. Writes can also wait in memory until the file is closed, so a file that is never closed can be missing its last lines.
</details>

**A4. What is the difference between `file.read()` and a `for` loop over the file?**

<details><summary>Answer</summary>

`read()` returns the whole file as one string, which is simple for small files. A `for` loop gives one line at a time, so even a file larger than memory can be handled. Each line keeps its `"\n"` at the end; use `strip()` before you compare or print it.
</details>

**A5. How does `try` with several `except` clauses decide which one runs?**

<details><summary>Answer</summary>

Python checks the `except` clauses from top to bottom and runs only the first one that matches the error. A general clause such as `except Exception` matches almost everything, so put the specific ones first. Catch errors by name: a bare catch-all hides real bugs, such as a typo in a variable name.
</details>

**A6. Why use the `csv` module when you could split each line on commas?**

<details><summary>Answer</summary>

A CSV value can contain a comma inside quotes: `"Sharma, Ravi",500`. `split(",")` cuts that into three pieces; `csv.reader` gives two. The module also handles quotes inside values and different line endings. Whichever way you read it, every value comes back as a string, so numbers need `int()`.
</details>

**A7. Why open a CSV file with `newline=""` when writing it?**

<details><summary>Answer</summary>

`csv.writer` ends every row with its own line ending. Without `newline=""`, Python can change those endings again when it writes them. On Windows that shows up as an empty row between every pair of rows. `newline=""` tells Python to leave the endings to the `csv` module.
</details>

**A8. What is a module? How is `import greetings` different from `from greetings import say_hello`?**

<details><summary>Answer</summary>

A module is any `.py` file. `import greetings` gives you the module, and you write `greetings.say_hello(...)`, so the reader always sees where the name came from. `from greetings import say_hello` copies one name into your file, so you write `say_hello(...)` with no prefix. `import greetings as g` is the first form with a shorter name.
</details>

**A9. Why do style guides say to avoid `from module import *`?**

<details><summary>Answer</summary>

It copies every public name from the module into your file, and you cannot see which ones. If two modules have a function with the same name, the later import silently replaces the earlier one. A reader also cannot tell where a name came from. See gotcha B7 below for a real case with `pow`.
</details>

**A10. What happens when you import a module? What is `if __name__ == "__main__":` for?**

<details><summary>Answer</summary>

Python runs the module's file from top to bottom, once per program. A second `import` of the same module reuses the first one. So any `print` or `input` at the top level of a module runs during the import. `__name__` is `"__main__"` only in the file you ran yourself, so code under `if __name__ == "__main__":` runs when you run the file, but not when another file imports it. That is where a module keeps its own tests and demos.
</details>

**A11. What is the standard library? How is it different from a package you install with `pip`?**

<details><summary>Answer</summary>

The standard library is the set of modules that comes with Python: `math`, `random`, `datetime`, `os`, `uuid`, `csv`, `re` and many more. Nothing to install. A package from `pip` is written by someone else and downloaded from the internet. Each one is code you now trust, so check the exact name and who publishes it before you install it.
</details>

**A12. A program fails with `AttributeError: module 'random' has no attribute 'randint'`. What is the likely cause?**

<details><summary>Answer</summary>

There is a file named `random.py` in the program's folder. Python looks in that folder before the standard library, so `import random` loads your file, which has no `randint`. Python 3.14 says so in the message: `(consider renaming '.../random.py' since it has the same name as the standard library module named 'random' ...)`. Rename the file. Never name your files `random.py`, `csv.py`, `math.py` or `re.py`.
</details>

---

## B. Gotchas: predict the output

Commit to an answer before you open each one. Run each one in an empty folder.

**B1.**

```python
with open("names.txt", "w") as f:
    f.write("Uma\nAkash\n")

with open("names.txt", "r") as f:
    for line in f:
        print(line)
```

<details><summary>Answer</summary>

```text
Uma

Akash

```

Each line keeps its own `"\n"`, and `print` adds another one. `print(line.strip())` gives one name per line.
</details>

**B2.**

```python
with open("pin.txt", "w") as f:
    f.write("4321")

with open("pin.txt", "r") as f:
    print(f.read())
    print(f.read() == "")
```

<details><summary>Answer</summary>

```text
4321
True
```

The file object remembers how far it has read. After the first `read()` it is at the end, so the second one returns an empty string. Read once into a variable and use the variable.
</details>

**B3.**

```python
with open("pay.txt", "w") as f:
    print(f.write("Paid Rs.600"))
```

<details><summary>Answer</summary>

`11`. `write()` returns the number of characters it wrote. It prints nothing by itself, and it does not add a newline.
</details>

**B4.**

```python
with open("notes.txt", "w") as f:
    f.write("Buy milk")

with open("notes.txt", "w") as f:
    pass

with open("notes.txt", "r") as f:
    print(len(f.read()))
```

<details><summary>Answer</summary>

`0`. `"w"` erases the file the moment it opens it, even if the block writes nothing.
</details>

**B5.**

```python
try:
    amount = int("12a")
    open("missing.txt", "r")
except FileNotFoundError:
    print("no file")
except ValueError:
    print("bad number")
print("done")
```

<details><summary>Answer</summary>

```text
bad number
done
```

`int("12a")` fails first, so Python jumps straight to the matching `except`. The `open` line never runs, so there is no `FileNotFoundError`.
</details>

**B6.**

```python
with open("new_log.txt", "a") as f:
    f.write("first\n")

with open("new_log.txt", "r") as f:
    print(f.read().strip())

try:
    open("other_log.txt", "r")
except FileNotFoundError as e:
    print(e)
```

<details><summary>Answer</summary>

```text
first
[Errno 2] No such file or directory: 'other_log.txt'
```

`"a"` creates the file if it does not exist. `"r"` never creates one.
</details>

**B7.**

```python
print(pow(2, 3))
from math import *
print(pow(2, 3))
```

<details><summary>Answer</summary>

```text
8
8.0
```

The built-in `pow` returns an int. `from math import *` silently replaced it with `math.pow`, which always returns a float. Nothing warned you.
</details>

**B8.**

```python
import csv

with open("amounts.csv", "w", newline="") as f:
    f.write("amount\n900\n1500\n250\n")

with open("amounts.csv", "r") as f:
    amounts = [row["amount"] for row in csv.DictReader(f)]

print(sorted(amounts))
print(max(amounts))
```

<details><summary>Answer</summary>

```text
['1500', '250', '900']
900
```

The values are strings, so they sort like words: by the first character, and `"1"` comes before `"2"`. `max` is `"900"` because `"9"` is the largest first character. Convert with `int()` before sorting or comparing.
</details>

**B9.**

```python
print(int(" 500\n"))
print(int("1,500"))
```

<details><summary>Answer</summary>

`500`, then `ValueError: invalid literal for int() with base 10: '1,500'`. `int()` ignores spaces and newlines around a number, but not a comma inside it. Amounts written by people, or by an LLM, often have commas.
</details>

**B10.**

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Intern(Employee):
    def __init__(self, name):
        super().__init__(name)

Intern("Karthikeyan")
```

<details><summary>Answer</summary>

`TypeError: Employee.__init__() missing 1 required positional argument: 'salary'`. `super().__init__` must pass every argument the parent asks for. Pass a value such as `super().__init__(name, 15000)`.
</details>

**B11.**

```python
class Account:
    def fee_for(self, mode):
        return 5 if mode == "card" else 0

    def total(self, amount, mode):
        return amount + self.fee_for(mode)

class PremiumAccount(Account):
    def fee_for(self, mode):
        return 0

print(Account().total(1000, "card"), PremiumAccount().total(1000, "card"))
```

<details><summary>Answer</summary>

`1005 1000`. `total` is written only on the parent, but `self` is the object that called it. For a premium account, `self.fee_for` finds the child's version first.
</details>

**B12.**

```python
import re

amounts = re.findall(r"\d+", "Rs.600 and Rs.250")
print(sum(amounts))
```

<details><summary>Answer</summary>

`TypeError: unsupported operand type(s) for +: 'int' and 'str'`. `findall` returns strings, just like a CSV reader. `sum(int(a) for a in amounts)` gives 850.
</details>

---

## C. Explore, with AI in the loop

These connect today's ideas to what you built in the GenAI modules.

**C1. A file tool for an agent.** Write `read_file(filename)` as a tool an agent could call. It must never crash. For a missing file, a file it is not allowed to read, and a file that is too large, it returns a short sentence the model can act on, such as `No file named report.txt. Ask the user for the right name.` Why is returning the error as text better for an agent than letting the program crash? Compare your messages with what an assistant writes for the same tool.

**C2. Reading an LLM's CSV safely.** Ask a model for "five expenses as CSV with columns merchant and amount". Save its reply to a file and read it with `csv.DictReader`. Look for what breaks: a header with extra spaces, an amount like `₹1,200`, a line of text before the table, a code fence around it. Write a reader that skips any row it cannot turn into a number with `try` and `except ValueError`, and counts what it skipped.

**C3. The package that does not exist.** Ask an assistant to solve a small file task "using a pip package". Before you install anything it names, search for that exact name on pypi.org and check who publishes it and how many people use it. Models sometimes invent package names that sound real, and attackers can register those names with harmful code inside. Then ask: "Can this be done with the standard library only?"

**C4. Catch the AI being wrong: `"w"` or `"a"`.** Ask an assistant for a function that "saves each new payment to payments.csv". Check its mode. If it used `"w"`, run it three times and look at the file. Then check whether it writes the header row every time. Ask it to explain each choice without fixing it, then fix it yourself.

**C5. Evaluation results in a file.** In the evaluation module, you compared runs of a prompt. Write `log_result(prompt_name, score)` that adds one row to `evals.csv` with `"a"`, writing the header only when the file is new, as PaisaPay v16 does. Then read the file back and print the average score per prompt. What should happen if two evaluation jobs write at the same time?

**C6. One module, many front doors.** PaisaPay's checks now live in `paisapay_checks.py`. The menu imports them, and an MCP server or an n8n Code node could run the same functions as tools. Why is one module better than copying `is_valid_upi_id` into each place? Ask an assistant to list what could go wrong if the copies drift apart, and check whether its answer names a real case from your own work.
