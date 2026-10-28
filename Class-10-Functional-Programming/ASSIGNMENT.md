# Assignment · Class 10

Practice for functional programming: higher-order functions, `map`, `filter`, `reduce`, `sorted` with a key, and lambdas. Do Part A on paper first. Write Parts B and C yourself before asking any AI assistant. For more coding problems with solutions, see [`PRACTICE.md`](PRACTICE.md).

Run your programs in [PyLens](https://scaler-pylens.vercel.app/) or with `python3 filename.py`.

## Part A · Predict the output (no running)

Write down what each snippet prints, or which error it raises. Then run it and compare.

**A1**
```python
nums = [1, 2, 3]
print(list(map(lambda n: n * 10, nums)))
```

**A2**
```python
nums = [1, 2, 3]
doubled = map(lambda n: n * 2, nums)
print(doubled)
```

**A3**
```python
print(list(filter(lambda w: len(w) > 3, ["upi", "card", "wallet"])))
```

**A4**
```python
from functools import reduce
print(reduce(lambda a, b: a - b, [10, 3, 2]))
```

**A5**
```python
pairs = [("Parveen", 3), ("Amit", 1), ("Aanand", 2)]
print(sorted(pairs, key=lambda p: p[1])[0])
```

**A6**
```python
def twice(f, x):
    return f(f(x))

print(twice(lambda s: s + "!", "hi"))
```

**A7**
```python
def make_adder(n):
    return lambda x: x + n

add5 = make_adder(5)
print(add5(10), make_adder(1)(1))
```

**A8**
```python
nums = [4, 5, 6]
evens = filter(lambda n: n % 2 == 0, nums)
print(list(evens), list(evens))
```

**A9**
```python
print(list(map(lambda a, b: a + b, [1, 2], [10, 20])))
```

**A10**
```python
total = reduce(lambda a, b: a + b, [1, 2, 3])
print(total)
```

## Part B · Write the program

**B1. Discounts.** Given `prices = [120, 450, 980, 60]`, use `map` to apply a 10% discount to each price and print the new list of whole-rupee prices (use `//`).

**B2. Valid UPI IDs.** Given `ids = ["amit@okaxis", "aanand", "praveen@ybl", "@oksbi"]`, use `filter` with a lambda to keep only the IDs with exactly one `@` and text on both sides. Print the kept list.

**B3. Word lengths.** Ask for a sentence. Use `map` to build the list of word lengths, `max` with a key to find the longest word, and `reduce` to add the lengths. Print all three.

**B4. Top three.** Given a dictionary of payee totals, print the three biggest payees as `name: ₹total` lines, biggest first, using `sorted` on `items()` with a key and a slice.

```python
spent = {"Rahul": 700, "Vamsi": 1750, "Akshay": 1500, "Sathvik": 90, "Amit": 300}
```

**B5. Payments per mode.** Given a list of `(name, amount, mode)` tuples, use `filter` with a lambda to count the UPI payments and the card payments, and `sum` over a `map` to total each. Print one line per mode as `upi: 3 payments, ₹2190`.

**B6. Fix the bugs.** This program should print `[1200, 3000]`, the doubled amounts of ₹500 or more. It has three mistakes. Find and fix each one, and write what went wrong.

```python
amounts = [600, 250, 1500]
big = filter(lambda a: a >= 500, amounts)
doubled = map(lambda a: return a * 2, big)
print(doubled)
```

## Part C · Project: grow PaisaPay v10

Start from [`code/paisapay_v10.py`](code/paisapay_v10.py).

1. **Per-mode totals, functionally.** In `mini_statement`, for each mode in `("upi", "card", "netbanking")`, use `filter` to select that mode's payments and `sum` over a `map` of their amounts. Print one line per mode that has payments, as `UPI: ₹700`.
2. **Smallest payment.** Print the smallest payment with `min` and a key, in the same form as the biggest.
3. **A threshold the user chooses.** Add menu item 8: ask for a minimum amount, and with `filter` and a lambda print how many payments are at or above it.

Target output for one run (balance ₹5000 after adding money, PIN 4321, three payments: 600 UPI to rajani@okaxis, 250 card to vamsi@oksbi, 1500 UPI to sumit@ybl):

```text
Choose: 3
Payments: 3 | Spent ₹2350
Big payments (₹500 or more): 2
Biggest: ₹1500 to Sumit
Smallest: ₹250 to Vamsi
UPI: ₹2100
Card: ₹250
  ₹250 Vamsi (Card)
  ₹600 Rajani (UPI)
  ₹1500 Sumit (UPI)
Choose: 8
Minimum amount: 1000
Payments of ₹1000 or more: 1
```

## Part D · Think it through

Write two or three lines for each.

1. `map` and `filter` give back a lazy object instead of a list. Name one situation where that is useful and one where it bites.
2. Why did Python move `reduce` out of the built-ins? When would you still use it, and when would you write `sum` instead?
3. `sorted(payments, key=lambda p: p[1])` and `payments.sort(key=lambda p: p[1])` give the same order. What is different about them, and when does the difference matter?
4. A lambda cannot contain an assignment or an `if` block. Why is that a feature rather than a limitation?

## With AI (after your own attempt)

Paste your finished Part C program into an AI assistant and ask:

> "List every place this program uses map, filter, reduce or sorted. For each one, say in one sentence what a loop version would look like, and whether the functional version is clearer. Do not change the code."

Check each claim. Then ask it to rewrite one of them as a loop, and run both to confirm they agree.
