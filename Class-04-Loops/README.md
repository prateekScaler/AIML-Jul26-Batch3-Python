# Class 4 · Loops

PaisaPay v3 handled one payment and stopped. A chai stall takes fifty payments before 10 AM. In this class Python learns to repeat: write an instruction once and say how many times, or until when.

**By the end of this class you can:**

- Write a `for` loop over a `range` or a list, and say exactly which values the loop variable takes.
- Write a `while` loop, set its variable up before it, and make sure it can end.
- Use `break`, `continue` and `pass`, and say which block each one affects.
- Nest one loop inside another to print grids and patterns.
- Recognise the four loop patterns: accumulate, count, find, filter.

## How to use this folder

| File | What it is |
|---|---|
| [`index.html`](index.html) | The interactive class page. [Open it here](https://prateekscaler.github.io/AIML-Jul26-Batch3-Python/Class-04-Loops/), no download needed. **Step by step** shows a little at a time (press → or Next). **Show everything** gives the whole class on one page. |
| [`code/`](code/) | Every example from the class as a runnable file, in order. |
| [`code/paisapay_v4.py`](code/paisapay_v4.py) | Today's version of our course project. |
| [`Python-Class-04-Loops.ipynb`](Python-Class-04-Loops.ipynb) | The same examples as one notebook. [Open it in Google Colab](https://colab.research.google.com/github/prateekScaler/AIML-Jul26-Batch3-Python/blob/main/Class-04-Loops/Python-Class-04-Loops.ipynb) and run the cells, nothing to install. |
| [`PRACTICE.md`](PRACTICE.md) | Twelve coding problems on loops, easy to hard, with sample output, hints and solutions. |
| [`ASSIGNMENT.md`](ASSIGNMENT.md) | Predict the output, write programs, grow PaisaPay, think it through. |
| [`INTERVIEW-READINESS.md`](INTERVIEW-READINESS.md) | Interview questions, gotchas and AI-era questions on today's topics. |

Run the code in [PyLens](https://scaler-pylens.vercel.app/), or on your own machine with `python3 filename.py`.

Official post-read for this class: https://scaler-content.github.io/python-Foundations-4/

---

## 1. Why loops

Five customers, five `print` lines. One hundred customers? Write the instruction once, and tell Python how many times, or until when. That is a loop: do the action, ask "again?", repeat or move on.

Every app repeats. A bank statement is one line per transaction. An OTP timer counts 60, 59, 58. A PIN screen asks again until the PIN is right. And every agent you built in the GenAI modules is a loop: think, call a tool, observe the result, check whether the task is done, and if not, think again. An agent is a `while not done` loop around an LLM call.

## 2. The `for` loop and `range`

```python
for i in range(5):
    print("₹10 cashback sent")
```

`for` repeats what follows. `i` is the loop variable and changes on every pass. `range(5)` supplies the values. The indented block is what repeats, with the same indentation rule as `if`.

`range(5)` gives **0, 1, 2, 3, 4**. It starts at 0 and stops *before* 5. That one rule causes most loop bugs:

```python
for token in range(1, 6):      # 1 2 3 4 5    start included, stop excluded
for i in range(2, 11, 2):      # 2 4 6 8 10   the third number is the step
for sec in range(10, 0, -1):   # 10 down to 1 a negative step counts down
for sec in range(10, 0):       # nothing: step is +1, we are already past 0
```

To print EMI months 1 to 12, the range is `range(1, 13)`. `range(1, 12)` quietly skips the last EMI.

A `for` loop walks through any sequence, not only numbers:

```python
payees = ["Chai Point", "Zomato", "Jio"]
for payee in payees:
    print("Paid", payee)
```

After the loop, the loop variable still holds its last value. It is an ordinary variable.

## 3. The `while` loop

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

Check the condition, run the body, check again. The loop stops the moment the condition is False. Two lines are not optional: the variable must exist *before* the loop (`count = 1`), and something inside must move it towards False (`count += 1`).

Remove `count += 1` and the program prints 1 for ever: an **infinite loop**. No error, it just never ends.

> **Real world.** On 31 December 2008 thousands of Microsoft Zune 30 music players froze at once. The clock code had a `while` loop, and on day 366 of a leap year nothing inside it changed the day count. The loop ran until the day was over; the fix was to wait for 1 January. Simplified:
>
> ```python
> days = 366        # 31 December 2008, day 366 of a leap year
> leap = True
>
> while days > 365:
>     if leap:
>         if days > 366:      # 366 is not more than 366
>             days -= 366      # so this never runs
>     else:
>         days -= 365
> ```
>
> Every `while` needs a line that moves it towards False, on every path, every time. [Zune bug explained in detail](https://techcrunch.com/2008/12/31/zune-bug-explained-in-detail/) · [Zune 30](https://en.wikipedia.org/wiki/Zune_30#Freescale_Driver_Issue)

Changing the variable is not enough; the condition must actually become False. `while balance != 0` with `balance -= 300` from 1000 goes 700, 400, 100, −200 and never equals 0. Safer: `while balance >= 300`.

**`for` or `while`?** Use `for` when you know the sequence or the count: EMI months 1 to 12, every payee in a list, an OTP timer from 60 down to 1, the total of today's payments, a 10-row multiplication table. Use `while` when you know the stopping condition but not the count: ask for the PIN until it is correct, ask for an amount until it is more than 0, pay ₹300 at a time while the balance lasts, roll a die until it shows 6, keep the agent thinking until the task is done.

```python
pin = ""

while pin != "4321":
    pin = input("Enter UPI PIN: ")

print("Access granted!")
```

Delete `pin = ""` and the `while` line raises `NameError`: the condition is checked before anything else runs.

## 4. `break`, `continue`, `pass`

```python
for txn in range(1, 11):
    if txn == 6:
        break                 # leave the whole loop. Prints 1 to 5.
    print("Transaction", txn, "done")

for txn in range(1, 6):
    if txn == 3:
        continue              # skip the rest of this pass. Prints 1 2 4 5.
    print("Transaction", txn, "done")

for i in range(5):
    if i == 3:
        pass                  # do nothing. A placeholder where Python needs a line.
    else:
        print(i)
```

`break` ends the loop, not the program: the lines after the loop still run. In a `while` loop, `continue` jumps back to the condition and skips everything below it, including `count += 1`, so a `while` with `continue` can get stuck. In a `for` loop `range` moves on by itself.

> **Real world.** On 15 January 1990 AT&T's 114 long-distance switches crashed and restarted each other in a chain. The cause was a `break` inside an `if`, which left a bigger block than the programmer intended. For nine hours about half of all calls failed, over 50 million calls were blocked, and AT&T lost over $60 million. The same mistake, simplified:
>
> ```python
> calls = ["Delhi", "Mumbai", "Pune", "Chennai"]
>
> for call in calls:
>     if call == "Mumbai":
>         print("Mumbai line busy, skip it")
>         break                  # meant: skip this call. Does: leave the loop.
>     print("Connected", call)
>
> print("Switch idle")
> ```
>
> Pune and Chennai never get connected; the programmer wanted `continue`. Know exactly which block a `break` leaves; the indentation tells you. [The 1990 AT&T long distance network collapse](https://users.csc.calpoly.edu/~jdalbey/SWE/Papers/att_collapse)

## 5. Nested loops

```python
for branch in range(3):
    for counter in range(2):
        print(branch, counter)
```

For each pass of the outer loop, the inner loop runs completely: 3 × 2 = 6 lines. Nested loops draw grids. The outer loop is rows, the inner loop is columns. Every `print` ends with something, and the default is a new line, `end="\n"`. Writing `end=" "` ends with a space instead, so the next print continues on the same line; without it the inner loop would print nine stars on nine lines. The bare `print()` prints nothing and then its default new line, which finishes the row:

```python
for row in range(3):
    for column in range(3):
        print("*", end=" ")
    print()
```

The inner range may use the outer variable. `range(row)` for rows 1 to 3 prints a growing triangle.

## 6. Loop patterns

Four patterns cover most loops you will ever write. The skeleton is always loop, check, update, and the variable that collects the answer starts **above** the loop.

```python
total = 0                      # accumulate
for i in range(1, 6):
    total += i                 # 15

count = 0                      # count the matches
for amount in amounts:
    if amount >= 1000:
        count += 1

found = False                  # find, then stop looking
for amount in amounts:
    if amount == 5000:
        found = True
        break

for amount in amounts:         # filter
    if amount < 1000:
        continue
    print(amount)
```

Put `total = 0` inside the loop and it is wiped on every pass; only the last value survives. Add an `else: found = False` to the find pattern and the answer depends only on the last item.

## 7. Debug clinic

| Bug | What you see | Fix |
|---|---|---|
| `break` where `continue` belongs | The loop ends early. No error. | `continue` skips; `break` stops. |
| `while` that updates the wrong variable | Never ends. | Update the variable the condition reads. |
| `range(1, 12)` for 12 months | One line short. No error. | `range(1, 13)`. Stop is excluded. |
| `while pin != "4321"` with no `pin` before it | `NameError` | Set the variable before the loop. |

Loops rarely raise errors. They give the wrong answer quietly. Before fixing one, trace it: what does the condition read, and what changes it?

## Project: PaisaPay v4

Version 4 keeps running. The whole v3 decision now lives inside a menu loop, the PIN gets three attempts, and a mini statement counts payments, adds them up and remembers the biggest.

```python
# PaisaPay v4: the app keeps running
print("Welcome to PaisaPay")

balance = 1000
saved_pin = "4321"
count = 0
total_spent = 0
biggest = 0

choice = ""
while choice != "4":
    print()
    print("1. Pay   2. Balance   3. Mini statement   4. Exit")
    choice = input("Choose: ")

    if choice == "1":
        payee = input("Pay to: ")
        amount = int(input("Amount in rupees: "))

        pin_ok = False
        for attempt in range(3):
            pin = input("UPI PIN: ")
            if pin == saved_pin:
                pin_ok = True
                break
            print("Wrong PIN.", 2 - attempt, "attempts left")

        if not pin_ok:
            print("Three wrong PINs. Payment refused.")
        elif amount > balance:
            print("Insufficient balance. Payment refused.")
        else:
            balance -= amount
            print("Paid ₹", amount, "to", payee, "| Left ₹", balance)
            count += 1
            total_spent += amount
            if amount > biggest:
                biggest = amount

    elif choice == "2":
        print("Balance: ₹", balance)

    elif choice == "3":
        print("Count:", count, "| Spent ₹", total_spent)
        print("Biggest ₹", biggest)

    elif choice != "4":
        print("Unknown choice. Try again.")

print("Thank you for using PaisaPay")
```

A sample run:

```text
Welcome to PaisaPay

1. Pay   2. Balance   3. Mini statement   4. Exit
Choose: 1
Pay to: Chai Point
Amount in rupees: 300
UPI PIN: 1111
Wrong PIN. 2 attempts left
UPI PIN: 4321
Paid ₹ 300 to Chai Point | Left ₹ 700

1. Pay   2. Balance   3. Mini statement   4. Exit
Choose: 3
Count: 1 | Spent ₹ 300
Biggest ₹ 300

1. Pay   2. Balance   3. Mini statement   4. Exit
Choose: 4
Thank you for using PaisaPay
```

What v4 cannot do yet: fee, cashback and payment modes from v3 are out for now and return in v5 as functions; the statement knows totals, not every line, because a growing list is Class 6; and the same twenty lines repeat for every payment, which is exactly what functions fix in Class 5.

## Mini project and mini challenge

**Number analyzer.** Ask for a number, print 1 up to it and label each as even or odd. The stop value is `n + 1`, because `range` stops before its end. `range(1, n)` gives one number short, with no error.

**Guess the lucky number.** Keep asking until the user enters 7, with "Too low!" and "Too high!" hints. `while` is right because the number of guesses is unknown. `number = 0` before the loop gives the condition a safe starting value; set it to 7 and the loop body runs zero times.

Full code: [`code/10_number_analyzer.py`](code/10_number_analyzer.py), [`code/11_lucky_number.py`](code/11_lucky_number.py). Then do the twelve problems in [`PRACTICE.md`](PRACTICE.md).

## Recap

- **for** walks through a sequence. `range(start, stop, step)`, stop excluded.
- **while** repeats while a condition is True. Set the variable before, change it inside.
- **break / continue / pass**: leave the loop, skip one pass, do nothing.
- **Nested loops**: the inner loop runs fully for each outer pass.
- **Patterns**: accumulate, count, find, filter. Start the variable above the loop.
- **PaisaPay v4**: a menu loop, three PIN attempts, a mini statement.

Next class: functions. Name a block once, call it anywhere.
