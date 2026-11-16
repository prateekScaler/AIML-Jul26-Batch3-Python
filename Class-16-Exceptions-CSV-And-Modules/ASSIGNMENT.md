# Assignment · Class 16

Practice for files and modules: the four modes, the `with` statement, reading line by line, `try` and `except`, CSV files, and importing your own modules and the standard library. A few questions bring back regex and inheritance from earlier classes. Do Part A on paper first. Write Parts B and C yourself before asking any AI assistant. For more coding problems with solutions, see [`PRACTICE.md`](PRACTICE.md).

Run your programs with `python3 filename.py` in one folder on your computer, so the files they create stay together. Every snippet below makes its own sample file first, so run each one in an empty folder.

## Part A · Predict the output (no running)

Write down what each snippet prints, or which error it raises. Then run it and compare.

**A1**
```python
with open("a.txt", "w") as f:
    f.write("one\n")
with open("a.txt", "w") as f:
    f.write("two\n")
with open("a.txt", "a") as f:
    f.write("three\n")
with open("a.txt", "r") as f:
    print(f.read())
```

**A2**
```python
with open("names.txt", "w") as f:
    f.write("Uma\nAkash\n")

with open("names.txt", "r") as f:
    for line in f:
        print(len(line), len(line.strip()))
```

**A3**
```python
with open("pay.txt", "w") as f:
    f.write("Paid 500")
    f.write("Paid 250")

with open("pay.txt", "r") as f:
    print(f.read())
```

**A4**
```python
import csv

with open("amounts.csv", "w", newline="") as f:
    f.write("name,amount\nVinay,500\nUma,250\n")

with open("amounts.csv", "r") as f:
    rows = list(csv.DictReader(f))

print(rows[0]["amount"] + rows[1]["amount"])
print(int(rows[0]["amount"]) + int(rows[1]["amount"]))
```

**A5**
```python
try:
    open("nothing_here.txt", "r")
except Exception:
    print("Something went wrong")
except FileNotFoundError:
    print("No such file")
```

**A6**
```python
with open("log.txt", "w") as f:
    f.write("start")

try:
    with open("log.txt", "x") as f:
        f.write("again")
except FileExistsError:
    print("refused")

with open("log.txt", "r") as f:
    print(f.read())
```

**A7**
```python
with open("log.txt", "w") as f:
    print(f.closed)
print(f.closed)
```

**A8**
```python
import math
from math import sqrt
import math as m

print(math.sqrt(16), sqrt(25), m.sqrt(36))
```

**A9**
```python
import math as m

print(m.sqrt(16))
print(math.sqrt(16))
```

**A10**
```python
class Payment:
    def fee(self):
        return 5

    def total(self, amount):
        return amount + self.fee()

class UpiPayment(Payment):
    def fee(self):
        return 0

print(Payment().total(100), UpiPayment().total(100))
```

**A11**
```python
class Deposit:
    rate = 4

class FixedDeposit(Deposit):
    rate = 7

print(Deposit.rate, FixedDeposit.rate, FixedDeposit().rate)
```

**A12**
```python
import re

amounts = re.findall(r"\d+", "Rs.600 to Akash, Rs.250 to Uma")
print(amounts)
print(sum(amounts))
```

## Part B · Write the program

**B1. A to-do keeper.** Ask the user for three tasks with `input()` and add each one to `tasks.txt` with `"a"`. Then print the whole file with a number before each task. Run it twice: the second run must show six tasks, not three.

**B2. Count a file.** Create `story.txt` with three or four lines of your choice. Print the number of lines, words and characters, the way the `wc` command does. Decide whether the `"\n"` at the end of each line counts as a character, and write your choice as a comment.

**B3. Keep the big payments.** `payments.txt` has one line per payment, such as `Swiggy,450`. Create it with five lines. Copy only the payments of ₹1000 or more into `big_payments.txt`. Read the source in one `with` block and write the result in a second one.

**B4. A marks report.** Create `marks.csv` with the header `name,maths,science,english` and four students: Sathvik, Parvatha, Raghunathan and Madhumaya. Read it with `csv.DictReader`. Print each student's average to one decimal place, then the topper's name.

**B5. Your own module.** Write `bill.py` with `add_gst(amount)` (18%, as a whole number) and `split(amount, people)` (each share rounded up with `math.ceil`). In `main.py`, import `bill` one way and `split` another way, and print the share for ₹1000 plus GST split among three friends.

**B6. Fix the bugs.** Create `amounts.txt` with three lines: `600`, `250`, `1500`. This program should print `Total: 2350`. It has three mistakes. Find and fix each one, and write what went wrong. Careful: run it as it is and it erases `amounts.txt`. Notice that too, and create the file again before you test your fix.

```python
total = 0
try:
    with open("amounts.txt", "w") as file:
        for line in file:
            total = total + line
except Exception:
    print("Something went wrong.")
except FileNotFoundError:
    print("amounts.txt is missing.")
print("Total:", total)
```

## Part C · Project: grow PaisaPay v16

Start from [`code/paisapay_v16.py`](code/paisapay_v16.py) and [`code/paisapay_checks.py`](code/paisapay_checks.py), in the same folder.

1. **Export a statement.** Add menu item `8 Export`. It writes `statement.txt`: one line per saved payment, then a total line. Print `Saved N payments to statement.txt`. Use `Rs.` rather than `₹` inside the file: on some Windows computers, `open()` cannot write the `₹` sign unless you name an encoding.
2. **A monthly total.** Add menu item `9 Month total`. It asks for a month such as `2026-10` and prints how much was spent in that month and in how many payments. Every date is saved as text like `2026-10-28`, so a string method from Class 7 can tell which month a payment belongs to.
3. **Survive a damaged row.** Today, one bad row in `paisapay_history.csv` stops PaisaPay with a `ValueError` before the menu appears. Change `load_history` so that it skips any row whose numbers cannot be read, counts the skipped rows, and prints `Skipped N damaged row in paisapay_history.csv.` Use `try` and `except ValueError` around each row, not around the whole file.
4. **A storage module.** Move `BALANCE_FILE`, `load_balance` and `save_balance` into a new module, `paisapay_store.py`, and import the two functions. Then write one comment: why is `load_history` harder to move into that module?

To test, delete `paisapay_balance.txt` if it exists, and create `paisapay_history.csv` with these lines. The fourth line is damaged on purpose.

```text
date,payee,amount,mode,fee,cashback
2026-10-28,Rajani,600,upi,0,10
2026-10-30,Sumit,2500,card,5,50
2026-10-31,Vinay,abc,upi,0,0
2026-11-02,Uma,250,upi,0,0
```

Target output for one run:

```text
Welcome to PaisaPay
Account type (basic / premium): basic
Skipped 1 damaged row in paisapay_history.csv.
Loaded 3 saved payments. Balance ₹1000

1 Pay  2 Balance  3 Statement  4 Exit  5 Add  6 Read SMS  7 Check PAN  8 Export  9 Month total
Choose: 9
Month (YYYY-MM): 2026-10
Spent ₹3100 in 2026-10 (2 payments)

1 Pay  2 Balance  3 Statement  4 Exit  5 Add  6 Read SMS  7 Check PAN  8 Export  9 Month total
Choose: 8
Saved 3 payments to statement.txt

1 Pay  2 Balance  3 Statement  4 Exit  5 Add  6 Read SMS  7 Check PAN  8 Export  9 Month total
Choose: 4
Thank you for using PaisaPay
```

And `statement.txt` afterwards:

```text
2026-10-28  Rs.600 to Rajani (UPI)
2026-10-30  Rs.2500 to Sumit (Card)
2026-11-02  Rs.250 to Uma (UPI)
Total: Rs.3350
```

## Part D · Think it through

Write two or three lines for each.

1. `save_balance` opens its file with `"w"`, but `save_payment` opens its file with `"a"`. What goes wrong if you swap the two modes? Describe each file after three payments.
2. `save_payment` writes the header row only when the file is new. What would `csv.DictReader` give back if the header were written before every payment?
3. Two copies of PaisaPay run at the same time. Both load a balance of ₹1000, and each pays ₹300. What does `paisapay_balance.txt` say at the end, and what should it say?
4. You save a file named `random.py` in your project folder, and a program in that folder calls `random.randint(1, 6)`. What happens, and why?
5. `load_balance` catches `FileNotFoundError` and `ValueError`, but not every error. Why is that better than one `except Exception`?

## With AI (after your own attempt)

Paste your finished Part C program into an AI assistant and ask:

> "List every place this program opens a file, the mode it uses, and what happens if that file is missing or damaged. Do not change the code."

Check each claim against your file by testing it: delete a file, damage a file, and run PaisaPay again. Then ask the assistant which mode each `open()` should use, and before reading its answer, write down your own choice for each one.
