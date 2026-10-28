# Class 10 · Functional Programming

Almost every loop you have written does one of three things: change every item, keep some items, or combine everything into one answer. Today each of those gets a named tool, `map`, `filter` and `reduce`, plus `sorted` with a key, and PaisaPay finally answers "what was my biggest payment?".

**By the end of this class you can:**

- Explain what a higher-order function is, and pass a function by name instead of calling it.
- Use `map` to change every item, `filter` to keep some, and `reduce` to combine a list into one value.
- Explain why `map` and `filter` give back a lazy object, when that matters, and how `list()` fixes it.
- Sort records by one field with `sorted` and a key, and find the biggest with `max` and a key.
- Write a lambda where logic is used once, and a `def` where it is not.

## How to use this folder

| File | What it is |
|---|---|
| [`index.html`](index.html) | The interactive class page. [Open it here](https://prateekscaler.github.io/AIML-Jul26-Batch3-Python/Class-10-Functional-Programming/), no download needed. **Step by step** shows a little at a time (press → or Next). **Show everything** gives the whole class on one page. |
| [`code/`](code/) | Every example from the class as a runnable file, in order. |
| [`code/paisapay_v10.py`](code/paisapay_v10.py) | Today's version of our course project. |
| [`Python-Class-10-Functional-Programming.ipynb`](Python-Class-10-Functional-Programming.ipynb) | The same examples as one notebook. [Open it in Google Colab](https://colab.research.google.com/github/prateekScaler/AIML-Jul26-Batch3-Python/blob/main/Class-10-Functional-Programming/Python-Class-10-Functional-Programming.ipynb) and run the cells, nothing to install. |
| [`PRACTICE.md`](PRACTICE.md) | Twelve coding problems on map, filter, reduce, sorted and lambda, easy to hard, with sample output, hints and solutions. |
| [`ASSIGNMENT.md`](ASSIGNMENT.md) | Predict the output, write programs, grow PaisaPay, think it through. |
| [`INTERVIEW-READINESS.md`](INTERVIEW-READINESS.md) | Interview questions, gotchas and AI-era questions on today's topics. |

Run the code in [PyLens](https://scaler-pylens.vercel.app/), or on your own machine with `python3 filename.py` (Python 3.10 or newer, because PaisaPay uses `match`).

Official post-read for this class: https://scaler-content.github.io/python-Foundations-9/

---

## 1. Three loops you have written ten times

```python
amounts = [600, 250, 1500]

in_paise = []                  # change every item
for a in amounts:
    in_paise.append(a * 100)

big = []                       # keep some items
for a in amounts:
    if a >= 500:
        big.append(a)

total = 0                      # combine everything
for a in amounts:
    total += a
```

Three patterns: a new list of the same length, a shorter list with the items unchanged, and one value. Functional programming gives each a name: `map`, `filter`, `reduce`. Loops stay; this is a second vocabulary for the same three jobs.

**Why "functional"?** It is a style where functions are the main tool: a function is a value like a number or a string, so you can store it, pass it to another function and return it from one, and a program is built by handing functions to functions. Each function makes a new result and leaves its input alone, instead of changing variables step by step as a loop does. Everything in this class fits that one idea: a lambda writes a small function value, a higher-order function takes one, and `map`, `filter`, `reduce` and `sorted` apply it. Python is not a pure functional language; it lends you the style where it reads well and keeps loops for the rest.

> **Real world, 2004.** To index the whole web, Google needed thousands of machines on one job. Jeffrey Dean and Sanjay Ghemawat split every job into the same two steps, map each page to (word, count) pairs and reduce all the pairs for a word into one total, and named the system MapReduce after the two functional-programming tools. Hadoop and most big-data systems copied the idea. The pattern you learn on three numbers is the one that counts every word on the web. [Google Research: MapReduce, Simplified Data Processing on Large Clusters](https://research.google/pubs/mapreduce-simplified-data-processing-on-large-clusters/)

## 2. Lambda, and a function that takes a function

```python
def square(x):
    return x * x

square_lambda = lambda x: x * x
print(square(5), square_lambda(5))      # 25 25
```

A lambda is a function with no name: parameters, a colon, one expression that is returned. Today you rarely store one; you write it where it is needed and throw it away.

```python
def apply_twice(func, value):
    return func(func(value))

def add_three(x):
    return x + 3

print(apply_twice(add_three, 10))       # 16: add_three(10) is 13, add_three(13) is 16
```

We passed `add_three`, not `add_three()`: the function itself, not its answer. `apply_twice` does not know what the function does; it only knows it can call it. A function that takes a function as an argument is a **higher-order function** (one that returns a function is the other direction, covered next class). `map`, `filter`, `reduce` and `sorted` are all higher-order functions. Writing `apply_twice(add_three(), 10)` calls `add_three` with no argument and fails with a `TypeError` before `apply_twice` runs.

## 3. map: the same change to every item

```python
numbers = [1, 2, 3, 4]
squared = map(lambda x: x ** 2, numbers)
print(squared)              # <map object at 0x...>
print(list(squared))        # [1, 4, 9, 16]
```

`map(function, list)` applies the function to each item. But `print(squared)` does not show a list: `map` hands back a **promise** to do the squaring, one item at a time, when something asks. This is **lazy evaluation**. `list()` asks for every value and collects them; a `for` loop asks too; printing does not. So do `tuple()`, `set()`, `sum()`, `sorted()` and `max()`: anything that walks a collection, and each one empties the promise. The address in the message changes every run; the type does not.

Three consequences. A map object has no length and no positions: `len(squared)` and `squared[0]` are `TypeError`s, so wrap it in `list()` first. A map object hands out each value once: `list(squared)` a second time gives `[]`, so store the list when you need it twice. And `map` changes every item into whatever the lambda returns: `map(lambda a: a >= 500, amounts)` gives a list of bools, not the big amounts.

## 4. filter: keep the items where the rule is True

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))          # [2, 4, 6, 8]

amounts = [600, 250, 1500, 90]
print(list(filter(lambda a: a >= 500, amounts)))     # [600, 1500]
```

The lambda is a rule: True keeps the item, False drops it; the items themselves do not change. `filter` is lazy too. The rule must answer a yes-or-no question: `filter(lambda a: a - 500, amounts)` keeps everything, because every non-zero number counts as True.

| Task | Tool |
|---|---|
| every amount in paise | `map` |
| only the payments over ₹500 | `filter` |
| every name in capitals | `map` |
| only the names that start with S | `filter` |
| every payment's amount, out of the tuple | `map` |



## 5. reduce: combine everything into one value

```python
from functools import reduce

numbers = [1, 2, 3, 4]
total = reduce(lambda a, b: a + b, numbers)       # 1+2 is 3, 3+3 is 6, 6+4 is 10
product = reduce(lambda a, b: a * b, numbers, 1)  # 24, starting from 1
```

`reduce` combines the first two items, then that result with the next, and so on. In the lambda, `a` is the running answer and `b` is the next item. A third argument is the starting value: 1 for a product, 0 for a total. **The import line matters**: `map` and `filter` are built in, `reduce` lives in `functools`, and without the import you get `NameError: name 'reduce' is not defined`. `functools` is a module: a file of ready-made functions that ships with Python, here tools for working with functions. Python keeps most of its tools in modules so the language itself stays small; `math` has `sqrt`, `random` has `randint`. Built-in functions such as `len`, `print`, `map` and `sorted` are loaded before your first line runs, about 70 of them, the ones nearly every program needs; module functions live in a file you import, thousands of them grouped by job. The split keeps a small script fast and the names few. A package is a folder of modules. Class 13 covers both properly.

> **Real world, 2005.** In Python 2, `reduce` was a built-in next to `map` and `filter`. Guido van Rossum, Python's creator, wrote that almost every `reduce` he saw made him stop and work out what it did, where a plain loop or `sum` read better. Python 3 moved it into `functools`: still there, one import away, no longer the first tool you reach for. For a total, `sum(amounts)` beats a reduce. [Guido van Rossum, "The fate of reduce() in Python 3000"](https://www.artima.com/weblogs/viewpost.jsp?thread=98196) · [Python docs: functools.reduce](https://docs.python.org/3/library/functools.html#functools.reduce)

**Chaining** reads from the inside out:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
print(result)               # [4, 16, 36, 64, 100]
```

`filter` runs first and keeps the evens; `map` squares what `filter` hands it; `list` collects. Hard to read? Two lines are allowed.

In PaisaPay the history is a list of `(name, amount, mode)` tuples; `amounts = list(map(lambda p: p[1], history))` pulls the amounts out, and `total = reduce(lambda a, b: a + b, amounts)` gives the same answer as the running-total loop from Class 4 and as `sum(amounts)`.

## 6. sorted with a key

```python
payments = [("Hitender", 600, "upi"),
            ("Saurabh", 250, "card"),
            ("Prajnika", 1500, "upi")]

print(sorted(payments, key=lambda p: p[1]))
# [('Saurabh', 250, 'card'), ('Hitender', 600, 'upi'), ('Prajnika', 1500, 'upi')]
print(sorted(payments, key=lambda p: p[1], reverse=True)[0])    # ('Prajnika', 1500, 'upi')
print(max(payments, key=lambda p: p[1]))                        # ('Prajnika', 1500, 'upi')
```

`sorted` has two switches: `reverse=True` says which way, `sorted(amounts, reverse=True)` gives biggest first and leaves `amounts` alone; `key` says what to compare. Without a key, tuples sort by their first item, the names. The key is a function that hands `sorted` one value per record to compare; the records themselves come back, in that order. `max` and `min` take the same key. When two keys tie, the original order is kept. `sort()` with a key changes the list in place and gives None; `sorted` makes a new list, exactly as in Class 6. [Python docs: Sorting HOWTO, key functions](https://docs.python.org/3/howto/sorting.html#key-functions)

In PaisaPay, `biggest = sorted(history, key=lambda p: p[1], reverse=True)[0]` answers the question v8 could not, and the statement prints the payments in amount order.

## 7. When a lambda, when a def

| The logic | Write | Why |
|---|---|---|
| used once, one expression | a lambda in the call | no clutter |
| used in two places | `def` with a name | one place to fix it |
| needs an `if` block, a loop, or two lines | `def` | a lambda holds one expression only |
| needs a comment to be understood | `def` | the name is the comment |

`lambda a: return a * 100` is a `SyntaxError`: the return is built in. `lambda: 42` with no parameters is fine.

## 8. Loop or functional?

```python
squared_loop = []                                   # loop
for n in numbers:
    squared_loop.append(n ** 2)
squared_func = list(map(lambda n: n ** 2, numbers))  # functional

evens_loop = []
for n in numbers:
    if n % 2 == 0:
        evens_loop.append(n)
evens_func = list(filter(lambda n: n % 2 == 0, numbers))

total_loop = 0
for n in numbers:
    total_loop += n
total_func = reduce(lambda a, b: a + b, numbers)
```

| You need to | Reach for |
|---|---|
| do one simple step per item | `map`, `filter`, `reduce` |
| print in the middle to see what is happening | a loop |
| branch on two or three conditions per item | a loop |
| a total, a max, a min | `sum`, `max`, `min`: the names say it |

Neither style is universally right. Professional code uses both.

## 9. Mini project: who passed, and their average

```python
from functools import reduce

students = [
    {"name": "Hitender", "score": 92},
    {"name": "Saurabh", "score": 58},
    {"name": "Prajnika", "score": 74},
    {"name": "Vinay", "score": 39},
]

passing = list(filter(lambda s: s["score"] >= 40, students))
names = list(map(lambda s: s["name"], passing))         # ['Hitender', 'Saurabh', 'Prajnika']
total = reduce(lambda acc, s: acc + s["score"], passing, 0)
average = total / len(passing)
print("Total:", total)                                    # 224
print("Average:", round(average, 2))                      # 74.67
```

`filter` selects, `map` extracts, `reduce` combines. The starting value 0 matters here: the running answer is a number while the items are dictionaries. Full code: [`code/09_student_scores.py`](code/09_student_scores.py).

## 10. Errors and debug clinic

| You see | It means | Fix |
|---|---|---|
| `<map object at 0x...>` where a list was expected | a promise, not values | wrap it in `list()` |
| `TypeError: object of type 'map' has no len()` or `'map' object is not subscriptable` | asking a promise for a length or a position | `list()` first |
| `NameError: name 'reduce' is not defined` | no import | `from functools import reduce` |
| `SyntaxError` in a lambda | a `return`, an `if` block or two lines inside it | one expression, or a `def` |
| `TypeError: <lambda>() missing 1 required positional argument` | the lambda wants two inputs and the tool gives one, or the reverse | `map` and `filter` give one item; `reduce` gives two |
| a filter that keeps everything | the rule returns a number, not a bool | make it a yes-or-no question |

## Project: PaisaPay v10

Version 10 is v8 plus insights, built in one step at the end of the class. The statement uses `map` for the amounts, `filter` with a stored lambda for the big payments, `reduce` for the total, and `sorted` with a key for the biggest payment and the ordered list.

```python
from functools import reduce

is_big = lambda payment: payment[1] >= 500

def mini_statement(history):
    if len(history) == 0:
        print("No payments yet.")
        return
    amounts = list(map(lambda p: p[1], history))
    total = reduce(lambda a, b: a + b, amounts)
    big = list(filter(is_big, history))
    biggest = sorted(history, key=lambda p: p[1], reverse=True)[0]
    print(f"Payments: {len(history)} | Spent ₹{total}")
    print(f"Big payments (₹500 or more): {len(big)}")
    print(f"Biggest: ₹{biggest[1]} to {biggest[0]}")
    for name, amount, mode in sorted(history, key=lambda p: p[1]):
        print(f"  ₹{amount} {name} ({mode_name(mode)})")
```

The full program is [`code/paisapay_v10.py`](code/paisapay_v10.py). A sample run after adding ₹2000 and making three payments (₹600 by UPI, ₹250 by card, ₹1500 by UPI):

```text
1 Pay  2 Balance  3 Statement  4 Exit  5 Add  6 Card  7 Save
Choose: 3
Payments: 3 | Spent ₹2350
Big payments (₹500 or more): 2
Biggest: ₹1500 to Sumit
  ₹250 Karthikeyan (Card)
  ₹600 Rajani (UPI)
  ₹1500 Sumit (UPI)
```

What v10 cannot do yet: keep an account's rules and its data together, which is classes in Class 11; check a UPI ID or a card number properly, which is regex in Class 12; and remember anything after the program ends, which is files in Class 13.

## Recap

Before reading on, write your own three-point recap: what would you tell a friend who missed this class? Then compare.

- **Higher-order function**: takes a function as an argument. Pass the name, not the call.
- **map** changes every item. **filter** keeps some. **reduce** combines into one. **sorted** with a key orders by one part.
- **Lazy**: `map` and `filter` give a promise; `list()` or a loop asks for the values, once.
- **reduce** comes from `functools`. For a total, `sum` reads better.
- **lambda** is for logic used once, in the call. Two uses or two lines: `def`.
- **PaisaPay v10**: amounts by map, big payments by filter, the total by reduce, the biggest by sorted with a key.

Next class: classes and objects. An Account that carries its balance and its rules together.
