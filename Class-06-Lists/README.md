# Class 6 · Lists

PaisaPay v5 forgot every payment the moment it was made. In this class Python learns to keep many values under one name, in order: a list. The class opens with two short revisions from Class 5 that caused confusion: where a variable lives, and which parameters go first.

**By the end of this class you can:**

- Explain local and global scope, and say why a function cannot change an outside number.
- Put required parameters before defaults, and positional arguments before keywords.
- Make a list, find a box by its index from the front or the back, and take a slice.
- Add and remove with `append`, `insert`, `remove` and `pop`, and sort with `sort` and `sorted`.
- Walk through a list with a loop, and build a new list with a comprehension.

## How to use this folder

| File | What it is |
|---|---|
| [`index.html`](index.html) | The interactive class page. [Open it here](https://prateekscaler.github.io/AIML-Jul26-Batch3-Python/Class-06-Lists/), no download needed. **Step by step** shows a little at a time (press → or Next). **Show everything** gives the whole class on one page. |
| [`code/`](code/) | Every example from the class as a runnable file, in order. |
| [`code/paisapay_v6.py`](code/paisapay_v6.py) | Today's version of our course project. |
| [`Python-Class-06-Lists.ipynb`](Python-Class-06-Lists.ipynb) | The same examples as one notebook. [Open it in Google Colab](https://colab.research.google.com/github/prateekScaler/AIML-Jul26-Batch3-Python/blob/main/Class-06-Lists/Python-Class-06-Lists.ipynb) and run the cells, nothing to install. |
| [`PRACTICE.md`](PRACTICE.md) | Twelve coding problems on lists, easy to hard, with sample output, hints and solutions. |
| [`ASSIGNMENT.md`](ASSIGNMENT.md) | Predict the output, write programs, grow PaisaPay, think it through. |
| [`INTERVIEW-READINESS.md`](INTERVIEW-READINESS.md) | Interview questions, gotchas and AI-era questions on today's topics. |

Run the code in [PyLens](https://scaler-pylens.vercel.app/), or on your own machine with `python3 filename.py` (Python 3.10 or newer, because PaisaPay uses `match`).

Official post-read for this class: https://scaler-content.github.io/python-Foundations-6/

---

## 0. Revision from Class 5

**Where does a variable live?** A variable created inside a function is local and lives only while that call runs. A variable created outside is global, and any function can read it. Assigning to a name inside a function makes a new local with that name, so this prints `5` and then `10`:

```python
x = 10

def show():
    x = 5
    print(x)

show()
print(x)
```

A function cannot change an outside number. `balance = balance + 100` inside a function changes a local copy, or raises `UnboundLocalError` if there is no parameter of that name. The two cases differ only in where the error shows. With a parameter, `balance = balance + 100` changes a local copy, which dies with the call, and there is no error. Without one, `count = count + 1` makes `count` local for the whole function, so reading it on the right side raises `UnboundLocalError`. Either way the outside variable never moves. Reading is always fine: a function that only reads `limit` sees the global; a function that assigns `limit = 1000` makes a throw-away local and the global stays 500. The habit that always works: pass the value in, return the new value, store it: `balance = add_bonus(balance)`.

**Which parameters go first?** In a definition, required parameters come first and parameters with defaults come last: `def pay(amount, mode="upi")` is fine, `def pay(mode="upi", amount)` is a `SyntaxError`, because Python could not tell what `pay(500)` means. In a call, positional arguments come first and keyword arguments last: `pay(500, mode="card")` is fine, `pay(mode="card", 500)` is a `SyntaxError`. Same shape on both sides. With `def pay(amount, mode="upi", note="")`: `pay(500)` uses both defaults, `pay(500, "card")` fills `mode` by position, and `pay(500, note="rent")` skips `mode`, which keeps `upi`, and names `note`.

## 1. Why lists

Five students, five variables. One hundred students, one hundred variables. A list stores many values under one name, in order:

```python
students = ["Hitender", "Parvatha", "Shubhodip", "Akash", "Vinay"]
```

Everything you scroll is a list: your UPI history, your chat messages, search results, the items flowing between n8n nodes, the messages an agent has seen so far. A Python list grows as you append to it.

## 2. Making a list, finding a box

```python
numbers = [10, 20, 30, 40, 50]
fruits = ["Apple", "Banana", "Mango", "Orange"]
print(len(numbers))     # 5
print(fruits[0])        # Apple: the first box is 0
print(fruits[2])        # Mango
print(fruits[-1])       # Orange: the last box is -1
print(fruits[-2])       # Mango
```

Square brackets make a list, commas separate the items, `len` counts them. A list has no fixed size: `len` can in theory reach `sys.maxsize`, over nine quintillion on a 64-bit machine, and memory runs out long before that.
> **Real world.** In October 2020, COVID test results in England were collected into Excel files in the old XLS format, which holds about 65,000 rows. Each result took several rows, so each file held about 1,400 cases, and everything past the limit was silently dropped. Nearly 16,000 cases went unreported and their contacts were never traced. A fixed-size container drops the rest and says nothing. [BBC: why using Excel caused Covid-19 results to be lost](https://www.bbc.com/news/technology-54423988)

 Indexes start at 0 from the front and at -1 from the back. A list of `n` items has indexes 0 to `n - 1`; ask for `fruits[5]` on three boxes and you get `IndexError: list index out of range`.

## 3. Lists can change

```python
fruits[1] = "Orange"            # replace a box
```

A list is mutable. That has a second consequence: `alias = original` does not copy the boxes, it gives the same list a second name, so changing `alias[0]` changes `original` too. A real copy is `original.copy()`. [Python FAQ: why did changing list y also change list x?](https://docs.python.org/3/faq/programming.html#why-did-changing-list-y-also-change-list-x)

## 4. Slicing

```python
numbers = [10, 20, 30, 40, 50]
numbers[1:4]      # [20, 30, 40]   start included, stop excluded
numbers[:3]       # [10, 20, 30]   from the start
numbers[2:]       # [30, 40, 50]   to the end
numbers[-2:]      # [40, 50]       the last two
numbers[:]        # a copy of the whole list
numbers[::2]      # every second box
numbers[::-1]     # reversed
```

The same exclusive-stop rule as `range`. A negative start is just a box number counted from the back: `history[-3:]` starts at the third-last box and runs to the end, in the original order. A step of 2 takes a box, skips one, takes the next; a step of -1 walks from the last box to the first.

## 5. Methods: add, remove, sort

| I want to | Use |
|---|---|
| add at the end | `append(value)` |
| add at a position, shifting the rest right | `insert(index, value)` |
| remove, and I know the value | `remove(value)` (raises `ValueError` if absent) |
| remove, and I know the position, and keep the item | `pop(index)`; `pop()` takes the last |
| sort the list itself | `sort()`, `sort(reverse=True)` |
| a sorted copy, original untouched | `sorted(list)` |

**The trap of the class.** `sorted_numbers = numbers.sort()` leaves `sorted_numbers` as `None`. `sort()` rearranges the list in place and hands nothing back, which is exactly the Class 5 rule: no `return` means `None`. Print `numbers` itself after sorting, or use `sorted(numbers)` when you want a new list and the original kept.

## 6. Walking through a list

```python
for student in students:
    print(student)

for i in range(len(students)):
    print(i, students[i])          # when you also need the position

for score in scores:
    if score >= 40:
        print(score, "Pass")
```

## 7. List comprehensions

```python
squares = []
for number in numbers:
    squares.append(number * number)

squares = [number * number for number in numbers]            # the same, in one line
evens = [number for number in numbers if number % 2 == 0]    # with a filter
```

Read it as English: for each number in numbers, put number × number in the new list. The pattern is `[expression for item in list if condition]`. A comprehension builds a new list; the old one is untouched. Short and clear: comprehension. Long or tricky: a normal loop. Both are correct, and both can be extended, but a loop is easier to debug with a `print` in the middle.

An industry habit worth copying: never remove items from a list while looping over it; the boxes shift and items get skipped. Build a new list instead. [Python tutorial: for statements](https://docs.python.org/3/tutorial/controlflow.html#for-statements)

## 8. Debug clinic

| Bug | What you see | Fix |
|---|---|---|
| `fruits[len(fruits)]` | `IndexError` | The last box is `len - 1`, or `-1` |
| `result = numbers.sort()` | `result` is `None` | Use `numbers` after sorting, or `sorted(numbers)` |
| `fruits.remove("Mango")` with no Mango | `ValueError` | Check first: `if "Mango" in fruits:` |
| `alias = original`, then change `alias` | both change | `alias = original.copy()` |

## Project: PaisaPay v6

Version 6 is v5 plus one list, `history`, and one function that reads it. `pay` appends every successful amount; `mini_statement` counts with `len`, adds with a loop, finds the biggest with `sorted`, takes the last five with a slice and lists the big payments with a comprehension. The list goes into `pay` as a parameter and comes out changed, because `append` changes the list itself; a number could not be changed that way.

```python
def pay(balance, history, payee, amount, mode="upi"):
    # ... the v5 checks ...
    cashback = cashback_for(amount)
    print("Paid ₹", amount, "to", payee, "via", mode_name(mode))
    print("Fee ₹", fee, "| Cashback ₹", cashback)
    history.append(amount)
    return balance - amount - fee + cashback

def mini_statement(history):
    if len(history) == 0:
        print("No payments yet.")
        return
    total = 0
    for amount in history:
        total += amount
    print("Payments:", len(history), "| Spent ₹", total)
    print("Biggest ₹", sorted(history)[-1])
    print("Last five:", history[-5:])
    big = [amount for amount in history if amount >= 500]
    print("Big payments:", big)
```

The full program is [`code/paisapay_v6.py`](code/paisapay_v6.py). A sample run:

```text
1. Pay  2. Balance  3. Statement  4. Exit  5. Add money
Choose: 3
Payments: 2 | Spent ₹ 2100
Biggest ₹ 1500
Last five: [600, 1500]
Big payments: [600, 1500]
```

What v6 cannot do yet: the statement knows amounts, not who was paid or when, because a payment as one record is Class 8; typed input is not cleaned and amounts are whole rupees (Class 7); and the history disappears when the app closes, until files in Class 12.

## Mini practices and mini challenge

A shopping list to grow and shrink, a number list to sort and slice, and the temperature analyzer: a sorted copy, the temperatures above 30, and each temperature in Fahrenheit, each in one line. Full code: [`code/10_practice.py`](code/10_practice.py), [`code/11_temperatures.py`](code/11_temperatures.py). Then do the twelve problems in [`PRACTICE.md`](PRACTICE.md).

## Recap

Before reading on, write your own three-point recap: what would you tell a friend who missed this class? Then compare.

- **A list**: `[ ]`, many values in order, grows as you append.
- **Index**: first box 0, last box -1. Past the end: `IndexError`.
- **Slice**: `[start:stop]`, stop excluded. `[-5:]` is the last five.
- **Methods** change the list: append, insert, remove, pop, sort. `sort()` gives back `None`.
- **`sorted()`**: a new list, the original untouched.
- **Comprehension**: `[x * 2 for x in numbers if x > 5]`, a new list in one line.
- **PaisaPay v6**: a history list, and a mini statement built from it.

Next class: strings. Cleaning input, masking a card number, formatted receipts, checking a UPI ID.
