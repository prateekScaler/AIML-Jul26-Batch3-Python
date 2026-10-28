# Practice problems · Class 10 · Functional Programming

Twelve problems, easy to hard. Each uses only what Classes 1 to 10 covered. Write every program yourself in [PyLens](https://scaler-pylens.vercel.app/) or with `python3`, run it against the sample, and only then open the hint or the solution.

How to work: name the pattern first. Change every item, `map`. Keep some, `filter`. One value, `reduce` (or `sum`, `max`, `min`). Order by a field, `sorted` with a key. Then write the lambda as the one-line rule for one item.

- [Warm-up](#warm-up) · problems 1 to 4
- [Core](#core) · problems 5 to 9
- [Challenge](#challenge) · problems 10 to 12

---

## Warm-up

### 1. Rupees to paise

Given `amounts = [600, 250, 1500]`, use `map` to make the list in paise and print it.

```text
[60000, 25000, 150000]
```

<details><summary>Solution</summary>

```python
amounts = [600, 250, 1500]
in_paise = list(map(lambda a: a * 100, amounts))
print(in_paise)
```
</details>

### 2. Only the big ones

Given `amounts = [600, 250, 1500, 90, 500]`, use `filter` to keep the amounts of ₹500 or more and print them, then print how many there are.

```text
[600, 1500, 500]
3
```

<details><summary>Solution</summary>

```python
amounts = [600, 250, 1500, 90, 500]
big = list(filter(lambda a: a >= 500, amounts))
print(big)
print(len(big))
```
</details>

### 3. Names, cleaned

Given `names = [" amit", "AANAND ", "praveen"]`, use `map` to strip and title-case every name and print the list.

```text
['Amit', 'Aanand', 'Praveen']
```

<details><summary>Hint</summary>

Methods chain inside the lambda: `n.strip().title()`.
</details>

<details><summary>Solution</summary>

```python
names = [" amit", "AANAND ", "praveen"]
clean = list(map(lambda n: n.strip().title(), names))
print(clean)
```
</details>

### 4. The total, three ways

Given `amounts = [600, 250, 1500]`, print the total with a loop, with `reduce`, and with `sum`. All three must agree.

```text
2350 2350 2350
```

<details><summary>Solution</summary>

```python
from functools import reduce

amounts = [600, 250, 1500]

total_loop = 0
for a in amounts:
    total_loop += a

total_reduce = reduce(lambda a, b: a + b, amounts)
total_sum = sum(amounts)
print(total_loop, total_reduce, total_sum)
```
</details>

---

## Core

### 5. Sort the payments

Given the list of payment tuples below, print them sorted by amount, smallest first, then print the name of the biggest payment using `max` with a key.

```python
payments = [("Rahul", 600, "upi"), ("Vamsi", 250, "card"), ("Akshay", 1500, "upi"), ("Sathvik", 90, "upi")]
```

```text
[('Sathvik', 90, 'upi'), ('Vamsi', 250, 'card'), ('Rahul', 600, 'upi'), ('Akshay', 1500, 'upi')]
Akshay
```

<details><summary>Hint</summary>

The key looks at position 1 of each tuple: `key=lambda p: p[1]`. `max(payments, key=...)` gives the whole tuple; take `[0]` for the name.
</details>

<details><summary>Solution</summary>

```python
payments = [("Rahul", 600, "upi"), ("Vamsi", 250, "card"), ("Akshay", 1500, "upi"), ("Sathvik", 90, "upi")]

print(sorted(payments, key=lambda p: p[1]))
biggest = max(payments, key=lambda p: p[1])
print(biggest[0])
```
</details>

### 6. UPI only, amounts only

From the same `payments` list, build the list of amounts paid by UPI, with `filter` then `map`, and print it with its total.

```text
[600, 1500, 90] 2190
```

<details><summary>Hint</summary>

Inside out: `filter` keeps the tuples whose mode is `"upi"`, `map` takes position 1 from each. `sum` for the total.
</details>

<details><summary>Solution</summary>

```python
payments = [("Rahul", 600, "upi"), ("Vamsi", 250, "card"), ("Akshay", 1500, "upi"), ("Sathvik", 90, "upi")]

upi_amounts = list(map(lambda p: p[1], filter(lambda p: p[2] == "upi", payments)))
print(upi_amounts, sum(upi_amounts))
```
</details>

### 7. Fee per payment

Card payments cost ₹5 and net banking ₹2; UPI is free. Use `map` with a lambda that holds a ternary (Class 7 revision) to build the list of fees for the payments above, then the total fee.

```text
[0, 5, 0, 0] 5
```

<details><summary>Hint</summary>

A lambda can hold one ternary: `5 if p[2] == "card" else (2 if p[2] == "netbanking" else 0)`.
</details>

<details><summary>Solution</summary>

```python
payments = [("Rahul", 600, "upi"), ("Vamsi", 250, "card"), ("Akshay", 1500, "upi"), ("Sathvik", 90, "upi")]

fees = list(map(lambda p: 5 if p[2] == "card" else (2 if p[2] == "netbanking" else 0), payments))
print(fees, sum(fees))
```
</details>

### 8. Longest word

Given `words = ["upi", "netbanking", "card", "wallet"]`, print the longest word with `max` and a key, then the words sorted by length, longest first.

```text
netbanking
['netbanking', 'wallet', 'card', 'upi']
```

<details><summary>Solution</summary>

```python
words = ["upi", "netbanking", "card", "wallet"]
print(max(words, key=lambda w: len(w)))
print(sorted(words, key=lambda w: len(w), reverse=True))
```
</details>

### 9. The lazy trap

This program is meant to print the squares twice. Run it, explain in a comment why the second line is empty, and fix it with one change.

```python
squares = map(lambda x: x * x, [1, 2, 3])
print(list(squares))
print(list(squares))
```

```text
[1, 4, 9]
[1, 4, 9]
```

<details><summary>Solution</summary>

```python
squares = list(map(lambda x: x * x, [1, 2, 3]))   # store the list, not the promise
print(list(squares))
print(list(squares))
# A map object hands out each value once. After the first list(), it is empty.
# list(map(...)) stored once can be printed as often as needed.
```
</details>

---

## Challenge

### 10. Biggest payment per mode

For each mode in `("upi", "card")`, use `filter` to select that mode's payments and `max` with a key to find its biggest, then print one line per mode. Skip a mode with no payments.

```text
upi: Akshay ₹1500
card: Vamsi ₹250
```

<details><summary>Hint</summary>

`filter(lambda p: p[2] == mode, payments)` gives the payments for one mode; wrap it in `list()` so you can test whether it is empty, then `max(..., key=lambda p: p[1])`.
</details>

<details><summary>Solution</summary>

```python
payments = [("Rahul", 600, "upi"), ("Vamsi", 250, "card"), ("Akshay", 1500, "upi"), ("Sathvik", 90, "upi")]

for mode in ("upi", "card"):
    in_mode = list(filter(lambda p: p[2] == mode, payments))
    if len(in_mode) == 0:
        continue
    top = max(in_mode, key=lambda p: p[1])
    print(f"{mode}: {top[0]} ₹{top[1]}")
```
</details>

### 11. Spending per payee, functional

Given payments where some names repeat, build a dictionary of the total per payee without a `for` loop over the payments: use `reduce` with a dictionary as the starting value. Then print the payees sorted by total, biggest first.

```python
payments = [("Rahul", 600, "upi"), ("Vamsi", 250, "card"), ("Rahul", 100, "upi"), ("Vamsi", 1500, "upi")]
```

```text
{'Rahul': 700, 'Vamsi': 1750}
[('Vamsi', 1750), ('Rahul', 700)]
```

<details><summary>Hint</summary>

The combining function gets the dictionary so far and the next payment. It must return the dictionary. A lambda cannot hold an assignment, so write a small `def` that updates `acc[name] = acc.get(name, 0) + amount` and returns `acc`. For the sort, `spent.items()` gives (name, total) tuples; key on position 1.
</details>

<details><summary>Solution</summary>

```python
from functools import reduce

payments = [("Rahul", 600, "upi"), ("Vamsi", 250, "card"), ("Rahul", 100, "upi"), ("Vamsi", 1500, "upi")]

def add_payment(acc, payment):
    name, amount, mode = payment
    acc[name] = acc.get(name, 0) + amount
    return acc

spent = reduce(add_payment, payments, {})
print(spent)
print(sorted(spent.items(), key=lambda pair: pair[1], reverse=True))
```
</details>

### 12. Predict, then run

Without running, write down what each line prints or which error it raises. Then run and compare.

```python
from functools import reduce
nums = [3, 1, 2]
print(list(map(lambda n: n + 1, nums)))
print(list(filter(lambda n: n > 1, nums)))
print(reduce(lambda a, b: a * b, nums))
print(sorted(nums, key=lambda n: -n))
m = map(lambda n: n * 2, nums)
print(list(m), list(m))
print(list(map(lambda n: n > 1, nums)))
print(len(filter(lambda n: n > 1, nums)))
```

<details><summary>Answer</summary>

```text
[4, 2, 3]
[3, 2]
6
[3, 2, 1]
[6, 2, 4] []
[True, False, True]
TypeError: object of type 'filter' has no len()
```

The key `-n` sorts biggest first. The map object is empty the second time. `map` with a comparison gives bools, not the kept items. A filter object has no length until it is a list.
</details>

---

Finished all twelve? Rewrite problem 11 with a plain `for` loop and decide, in one sentence, which version you would want to read at 2 a.m. during an incident.
