# Assignment · Class 8

Practice for tuples, sets and dictionaries: fixed records, unique items, lookup by key, the silent overwrite, nested collections and choosing the right structure. Do Part A on paper first. Write Parts B and C yourself before asking any AI assistant. For more coding problems with solutions, see [`PRACTICE.md`](PRACTICE.md).

Run your programs in [PyLens](https://scaler-pylens.vercel.app/) or with `python3 filename.py`.

## Part A · Predict the output (no running)

Write down what each snippet prints, or which error it raises. Then run it and compare.

**A1**
```python
point = 3, 4
x, y = point
print(type(point), x + y)
```

**A2**
```python
a = (5)
b = (5,)
print(type(a) == type(b))
```

**A3**
```python
visits = {1, 2, 2, 3, 3, 3}
visits.add(2)
print(len(visits))
```

**A4**
```python
empty = {}
empty.add("Ravi")
```

**A5**
```python
fees = {"upi": 0, "card": 5}
print(fees.get("card"), fees.get("wallet"), fees.get("wallet", 0))
```

**A6**
```python
scores = {}
scores["Aakash"] = 70
scores["Aakash"] = 80
scores["Shubhodip"] = 90
print(len(scores), scores["Aakash"])
```

**A7**
```python
student = {"name": "Vinay", "age": 20}
for item in student:
    print(item, end=" ")
```

**A8**
```python
a = {"x", "y", "z"}
b = {"y", "z", "w"}
print(sorted(a & b), sorted(a - b), len(a | b))
```

**A9**
```python
marks = {"Ravi": [60, 70]}
marks["Ravi"].append(80)
print(marks["Ravi"][-1], len(marks))
```

**A10**
```python
coords = (10, 20, 30)
coords[1] = 25
print(coords)
```

## Part B · Write the program

**B1. Date as a tuple.** Store today's date as a tuple `(year, month, day)`. Unpack it and print it as `21/10/2026`.

**B2. Duplicate UPI IDs.** Given `ids = ["a@okaxis", "b@ybl", "a@okaxis", "c@oksbi", "b@ybl"]`, print how many IDs appear more than once. Use a set of seen IDs and a set of repeated IDs.

**B3. Phonebook with a menu.** Loop: ask for a name. If it is in the dictionary, print the number. If not, ask for a number and save it. An empty name ends the loop. Start with `book = {"Raghunathan": "98xxxxxx01"}`.

**B4. Group by first letter.** Given `names = ["Rajani", "Ravi", "Sumit", "Shubhodip", "Vinay"]`, build a dictionary from the first letter to the list of names starting with it, and print it.

**B5. Word count, cleaned.** Ask for a sentence. Count each word ignoring case and ignoring a trailing full stop or comma on a word. Print the three most common words. (`sorted` with a key is Class 9; for now, find the biggest count three times with a loop.)

**B6. Fix the bugs.** This program should count how many times each mode appears and print `{'upi': 2, 'card': 1}`. It has three mistakes. Find and fix each one, and write what went wrong.

```python
modes = ("upi", "card", "upi")
counts = {}
for mode in modes
    counts[mode] = 1
print(counts.get)
```

## Part C · Project: grow PaisaPay v8

Start from [`code/paisapay_v8.py`](code/paisapay_v8.py).

1. **Per-mode totals.** In `mini_statement`, build a second dictionary from mode to the total spent with that mode, and print one line per mode as `UPI: ₹700`.
2. **Blocked payees.** Add a set `blocked = {"scam@ybl"}`. In `pay`, refuse a payment to a blocked UPI ID with `Payee is blocked. Payment refused.` before any other check.
3. **A contact that already exists.** In menu item 7, if the UPI ID is already a contact, print `Updated <old name> to <new name>` instead of `Saved`.

Target output for one run (balance ₹1000, PIN 4321):

```text
Choose: 1
Pay to (UPI ID): scam@ybl
Amount in rupees: 100
Mode (upi / card / netbanking): upi
UPI PIN: 4321
Payee is blocked. Payment refused.
Choose: 1
Pay to (UPI ID): rajani@okaxis
Amount in rupees: 600
Mode (upi / card / netbanking): upi
UPI PIN: 4321
Paid ₹600 to Rajani via UPI
Fee ₹0 | Cashback ₹10 | Balance ₹410
Choose: 7
Contact UPI ID: rajani@okaxis
Name: rajani n
Updated Rajani to Rajani N
Choose: 3
Payments: 1 | Spent ₹600
Payees: 1
  Rajani: ₹600
  UPI: ₹600
Last: ('Rajani', 600, 'upi')
```

## Part D · Think it through

Write two or three lines for each.

1. A payment in PaisaPay is a tuple, not a list. What bug does that prevent, and what would you lose if the payment were a list?
2. `scores["Aakash"] = 80` after `scores["Aakash"] = 70` gives no error. Why is that worse than an error, and how do you keep both scores?
3. An agent sends your tool `{"amount": 500, "amount": 50}`. What does your Python program receive, and what should it do about it?
4. Why can a tuple be a dictionary key but a list cannot? What does "unhashable" mean in one sentence?

## With AI (after your own attempt)

Paste your finished Part C program into an AI assistant and ask:

> "List every dictionary assignment in this program. For each one, say whether assigning to a key that already exists is what the program wants, or a bug that loses data. Do not change the code."

Check each claim against the code. The `spent[name] = spent.get(name, 0) + amount` line is an overwrite on purpose; did it see that?
