# Practice problems · Class 16 · Exceptions, CSV and Modules

Eight problems, easy to hard, on `try`/`except`, CSV files and modules. Each uses only what Classes 1 to 16 covered. Every solution first creates the sample files it reads. Write each program yourself, run it against the sample, and only then open the hint or the solution. For four problems on reading and writing files, see [Class 15](../Class-15-File-Handling/PRACTICE.md).

---

## Warm-up

### 1. A reader that never crashes

Write `read_or_message(filename)`. It returns the whole file as a string, or `No file named <filename> yet.` when the file does not exist. Test it on `offers.txt`, which you create first, and on `coupons.txt`, which does not exist.

```text
10% cashback on Swiggy
No file named coupons.txt yet.
```

<details><summary>Hint</summary>

Put the `with open(...)` inside `try`. Catch `FileNotFoundError` by name, not every error.
</details>

<details><summary>Solution</summary>

```python
def read_or_message(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        return f"No file named {filename} yet."

with open("offers.txt", "w") as file:
    file.write("10% cashback on Swiggy")

print(read_or_message("offers.txt"))
print(read_or_message("coupons.txt"))
```
</details>

### 2. Your own module

Create two files in the same folder. `money.py` has two functions: `to_paise(rupees)` returns the amount in paise, and `add_gst(amount)` returns the amount plus 18% GST as a whole number (use `//`). `main.py` imports `money` three ways: `import money`, `from money import add_gst`, and `import money as m`. Running `python3 main.py` prints:

```text
25000
590
118000
```

The last line is ₹1000 plus GST, in paise.

<details><summary>Hint</summary>

Any `.py` file is a module. With `import money` you write `money.to_paise(...)`. With `from money import add_gst` you write `add_gst(...)` with no prefix. With `import money as m` you write `m.to_paise(...)`.
</details>

<details><summary>Solution</summary>

`money.py`:

```python
def to_paise(rupees):
    return rupees * 100

def add_gst(amount):
    return amount + amount * 18 // 100
```

`main.py`:

```python
import money
print(money.to_paise(250))

from money import add_gst
print(add_gst(500))

import money as m
print(m.to_paise(m.add_gst(1000)))
```
</details>


## Core

### 3. Spending per person

Create `payments.csv` with a header row `name,merchant,amount` and these five rows: Raghunathan, Swiggy, 450 · Parvatha, BigBasket, 1200 · Raghunathan, Zomato, 300 · Madhumaya, Uber, 250 · Parvatha, Swiggy, 180. Read it with `csv.DictReader` and print how much each person spent.

```text
Raghunathan: ₹750
Parvatha: ₹1380
Madhumaya: ₹250
```

<details><summary>Hint</summary>

A dictionary with `get(name, 0)`, as in Class 8. `row["amount"]` is the string `"450"`, so add `int(row["amount"])`. Without `int()`, `0 + "450"` raises a `TypeError`.
</details>

<details><summary>Solution</summary>

```python
import csv

with open("payments.csv", "w", newline="") as file:
    file.write("name,merchant,amount\n")
    file.write("Raghunathan,Swiggy,450\n")
    file.write("Parvatha,BigBasket,1200\n")
    file.write("Raghunathan,Zomato,300\n")
    file.write("Madhumaya,Uber,250\n")
    file.write("Parvatha,Swiggy,180\n")

totals = {}
with open("payments.csv", "r") as file:
    for row in csv.DictReader(file):
        name = row["name"]
        totals[name] = totals.get(name, 0) + int(row["amount"])

for name, total in totals.items():
    print(f"{name}: ₹{total}")
```
</details>

### 4. A results sheet

Hitender scored 72, Sathvik 35, Vinay 58 and Uma 40. The pass mark is 40. Write `results.csv` with `csv.writer`: a header row `name,marks,result`, then one row per student. Then read it back with `csv.reader` and print each row.

```text
['name', 'marks', 'result']
['Hitender', '72', 'pass']
['Sathvik', '35', 'fail']
['Vinay', '58', 'pass']
['Uma', '40', 'pass']
```

<details><summary>Hint</summary>

Build a list of rows, then `writer.writerows(rows)`. Open with `newline=""` when writing a CSV. Look at the output: you wrote the number 72, but it comes back as the string `'72'`.
</details>

<details><summary>Solution</summary>

```python
import csv

marks = [("Hitender", 72), ("Sathvik", 35), ("Vinay", 58), ("Uma", 40)]
rows = [["name", "marks", "result"]]
for name, score in marks:
    result = "pass" if score >= 40 else "fail"
    rows.append([name, score, result])

with open("results.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(rows)

with open("results.csv", "r") as file:
    for row in csv.reader(file):
        print(row)
```
</details>

### 5. Three ways to fail

Write `average_from(filename)`. It reads one whole number per line and returns their average. It must never crash. Return `No such file.` when the file is missing, `A line is not a number.` when a line is not a number, and `The file is empty.` when there are no lines. Test it on four files: `good.txt` (100, 200, 300), `bad.txt` (100, abc), `empty.txt` (nothing) and `missing.txt` (not created).

```text
200.0
A line is not a number.
The file is empty.
No such file.
```

<details><summary>Hint</summary>

One `try`, three `except` clauses: `FileNotFoundError`, `ValueError` (from `int("abc")`) and `ZeroDivisionError` (from dividing by a length of 0). `int()` ignores the `"\n"` at the end of a line, so `int("100\n")` is 100.
</details>

<details><summary>Solution</summary>

```python
def average_from(filename):
    try:
        with open(filename, "r") as file:
            numbers = [int(line) for line in file]
        return sum(numbers) / len(numbers)
    except FileNotFoundError:
        return "No such file."
    except ValueError:
        return "A line is not a number."
    except ZeroDivisionError:
        return "The file is empty."

with open("good.txt", "w") as file:
    file.write("100\n200\n300\n")
with open("bad.txt", "w") as file:
    file.write("100\nabc\n")
with open("empty.txt", "w") as file:
    file.write("")

for name in ["good.txt", "bad.txt", "empty.txt", "missing.txt"]:
    print(average_from(name))
```
</details>

### 6. Keep only the valid PANs

`pans.txt` has one PAN per line, typed by hand: `abcde1234f`, `PQRST9876Z`, `ABC1234` and `  lmnop4321k  `. Clean each one (strip, then uppercase), keep the valid ones in `valid_pans.txt`, and print the counts and the new file. A PAN is five capital letters, four digits and one capital letter.

```text
3 valid, 1 refused
ABCDE1234F
PQRST9876Z
LMNOP4321K
```

<details><summary>Hint</summary>

Read all the lines first and collect the good ones in a list. Then write the list in a second `with` block. Use `re.fullmatch` from Class 13, so `ABC1234` with extra text around it cannot pass.
</details>

<details><summary>Solution</summary>

```python
import re

with open("pans.txt", "w") as file:
    file.write("abcde1234f\nPQRST9876Z\nABC1234\n  lmnop4321k  \n")

good = []
refused = 0
with open("pans.txt", "r") as file:
    for line in file:
        pan = line.strip().upper()
        if re.fullmatch(r"[A-Z]{5}\d{4}[A-Z]", pan):
            good.append(pan)
        else:
            refused += 1

with open("valid_pans.txt", "w") as file:
    for pan in good:
        file.write(pan + "\n")

print(f"{len(good)} valid, {refused} refused")
with open("valid_pans.txt", "r") as file:
    for line in file:
        print(line.strip())
```
</details>


## Challenge

### 7. A UPI log report

Create `upi_log.csv` with the header `txn_id,payee,amount,status` and these rows: T1, Swiggy, 450, SUCCESS · T2, Zomato, 300, FAILED · T3, BigBasket, 1200, SUCCESS · T4, Uber, 250, FAILED · T5, Swiggy, 180, SUCCESS. Write `analyze(filename)`. It counts all transactions, lists the failed IDs, adds up the money moved by successful ones, and writes the three lines to `report.txt`. If the file is missing, it prints an error and stops. Call it on `upi_log.csv` and on `old_log.csv` (which does not exist), then print `report.txt`.

```text
Error: old_log.csv not found.
Transactions: 5
Failed: 2 (T2, T4)
Money moved: Rs.1830
```

<details><summary>Hint</summary>

This is the log analyzer from class. Read the rows into a list inside `try`, so the file is closed before you work on them. `", ".join(failed)` joins the failed IDs. Write `Rs.` rather than `₹` inside the file: on some Windows computers, `open()` cannot write the `₹` sign unless you name an encoding.
</details>

<details><summary>Solution</summary>

```python
import csv

with open("upi_log.csv", "w", newline="") as file:
    file.write("txn_id,payee,amount,status\n")
    file.write("T1,Swiggy,450,SUCCESS\n")
    file.write("T2,Zomato,300,FAILED\n")
    file.write("T3,BigBasket,1200,SUCCESS\n")
    file.write("T4,Uber,250,FAILED\n")
    file.write("T5,Swiggy,180,SUCCESS\n")

def analyze(filename):
    try:
        with open(filename, "r") as file:
            rows = list(csv.DictReader(file))
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return

    failed = [r["txn_id"] for r in rows if r["status"] == "FAILED"]
    moved = sum(int(r["amount"]) for r in rows if r["status"] == "SUCCESS")

    with open("report.txt", "w") as file:
        file.write(f"Transactions: {len(rows)}\n")
        file.write(f"Failed: {len(failed)} ({', '.join(failed)})\n")
        file.write(f"Money moved: Rs.{moved}\n")

analyze("upi_log.csv")
analyze("old_log.csv")

with open("report.txt", "r") as file:
    for line in file:
        print(line.strip())
```
</details>

### 8. Sangeeta's wallet remembers

Split a small wallet into two files, as PaisaPay v16 does. `wallet_store.py` has `load_balance(default)` and `save_balance(balance)`, which keep the balance in `wallet.txt`. `load_balance` returns the default when the file is missing, and prints a message and returns the default when the file holds something that is not a number. `main.py` imports them, shows the balance, asks for an amount, refuses it if it is too big, and otherwise pays and saves.

Run `main.py` three times. Before the third run, open `wallet.txt` in an editor, replace the number with `abc` and save it.

```text
$ python3 main.py
Balance ₹1000
Amount to pay: 300
Paid ₹300. Balance ₹700

$ python3 main.py
Balance ₹700
Amount to pay: 900
Not enough balance. Balance ₹700

$ python3 main.py
wallet.txt is damaged. Starting from ₹1000.
Balance ₹1000
Amount to pay: 200
Paid ₹200. Balance ₹800
```

<details><summary>Hint</summary>

Save with `"w"`: the new balance replaces the old one. A file holds text, so write `str(balance)` and read back with `int(...)`. Two `except` clauses: `FileNotFoundError` for the first run, `ValueError` for `int("abc")`.
</details>

<details><summary>Solution</summary>

`wallet_store.py`:

```python
BALANCE_FILE = "wallet.txt"

def load_balance(default):
    try:
        with open(BALANCE_FILE, "r") as file:
            return int(file.read().strip())
    except FileNotFoundError:
        return default
    except ValueError:
        print(f"{BALANCE_FILE} is damaged. Starting from ₹{default}.")
        return default

def save_balance(balance):
    with open(BALANCE_FILE, "w") as file:
        file.write(str(balance))
```

`main.py`:

```python
from wallet_store import load_balance, save_balance

balance = load_balance(1000)
print(f"Balance ₹{balance}")
amount = int(input("Amount to pay: ").strip())
if amount > balance:
    print(f"Not enough balance. Balance ₹{balance}")
else:
    balance -= amount
    save_balance(balance)
    print(f"Paid ₹{amount}. Balance ₹{balance}")
```
</details>

