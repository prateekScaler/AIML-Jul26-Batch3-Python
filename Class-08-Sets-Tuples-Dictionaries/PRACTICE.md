# Practice problems · Class 8 · Sets, Tuples, Dictionaries

Twelve problems, easy to hard. Each uses only what Classes 1 to 8 covered. Write every program yourself in [PyLens](https://scaler-pylens.vercel.app/) or with `python3`, run it against the sample, and only then open the hint or the solution.

How to work: before you type, name the structure. Fixed record, tuple. Unique items, set. Lookup by name, dictionary. When a dictionary "loses" a value, you assigned to the same key twice.

- [Warm-up](#warm-up) · problems 1 to 4
- [Core](#core) · problems 5 to 9
- [Challenge](#challenge) · problems 10 to 12

---

## Warm-up

### 1. A seat is a tuple

Store an exam-hall seat as a tuple of row letter and seat number, unpack it into two names, and print a sentence.

```text
Seat B, number 12
```

<details><summary>Solution</summary>

```python
seat = ("B", 12)
row, number = seat
print(f"Seat {row}, number {number}")
```
</details>

### 2. Unique payees

Given `payees = ["Rajani", "Sumit", "Rajani", "Vinay", "Sumit"]`, print how many different payees there are, and whether Vinay is one of them.

```text
Different payees: 3
Vinay paid: True
```

<details><summary>Hint</summary>

`set(payees)` drops the duplicates. `in` works on the set.
</details>

<details><summary>Solution</summary>

```python
payees = ["Rajani", "Sumit", "Rajani", "Vinay", "Sumit"]
unique = set(payees)
print("Different payees:", len(unique))
print("Vinay paid:", "Vinay" in unique)
```
</details>

### 3. A fee table

Store the fee for each payment mode in a dictionary: upi 0, card 5, netbanking 2. Ask for a mode and print its fee. If the mode is unknown, print `Unknown mode` without crashing.

```text
Mode: card
Fee: ₹5
```

<details><summary>Hint</summary>

`fees.get(mode)` gives `None` for a missing key. Or test `mode in fees` first.
</details>

<details><summary>Solution</summary>

```python
fees = {"upi": 0, "card": 5, "netbanking": 2}
mode = input("Mode: ").strip().lower()
if mode in fees:
    print(f"Fee: ₹{fees[mode]}")
else:
    print("Unknown mode")
```
</details>

### 4. Keys, then values, then both

Given `balances = {"Raghunathan": 1200, "Ravi": 450}`, print every name on one line, every balance on the next, and then one `name: ₹balance` line per person.

```text
Raghunathan Ravi
1200 450
Raghunathan: ₹1200
Ravi: ₹450
```

<details><summary>Solution</summary>

```python
balances = {"Raghunathan": 1200, "Ravi": 450}

for name in balances:
    print(name, end=" ")
print()

for balance in balances.values():
    print(balance, end=" ")
print()

for name, balance in balances.items():
    print(f"{name}: ₹{balance}")
```
</details>

---

## Core

### 5. Count the modes

Given `modes = ["upi", "card", "upi", "upi", "netbanking", "card"]`, build a dictionary that counts how many payments used each mode, then print it.

```text
{'upi': 3, 'card': 2, 'netbanking': 1}
```

<details><summary>Hint</summary>

The counting pattern: `counts[mode] = counts.get(mode, 0) + 1`.
</details>

<details><summary>Solution</summary>

```python
modes = ["upi", "card", "upi", "upi", "netbanking", "card"]
counts = {}
for mode in modes:
    counts[mode] = counts.get(mode, 0) + 1
print(counts)
```
</details>

### 6. Who is in both classes?

Given `python_batch = {"Aakash", "Shubhodip", "Vinay", "Rajani"}` and `sql_batch = {"Vinay", "Rajani", "Hithender"}`, print the students in both, the students only in Python, and the total number of different students. Print the sets sorted so the output is stable.

```text
Both: ['Rajani', 'Vinay']
Only Python: ['Aakash', 'Shubhodip']
Total students: 5
```

<details><summary>Hint</summary>

`&` for both, `-` for only the first, `|` for everyone. `sorted(a_set)` gives a sorted list.
</details>

<details><summary>Solution</summary>

```python
python_batch = {"Aakash", "Shubhodip", "Vinay", "Rajani"}
sql_batch = {"Vinay", "Rajani", "Hithender"}

print("Both:", sorted(python_batch & sql_batch))
print("Only Python:", sorted(python_batch - sql_batch))
print("Total students:", len(python_batch | sql_batch))
```
</details>

### 7. Spending per payee

Given a list of payment tuples, build a dictionary of the total spent per payee and print one line per payee.

```python
payments = [("Rajani", 600, "upi"), ("Sumit", 250, "card"), ("Rajani", 100, "upi"), ("Sumit", 1500, "upi")]
```

```text
Rajani: ₹700
Sumit: ₹1750
```

<details><summary>Hint</summary>

Unpack in the for line: `for name, amount, mode in payments:`. Then the counting pattern with `amount` instead of 1.
</details>

<details><summary>Solution</summary>

```python
payments = [("Rajani", 600, "upi"), ("Sumit", 250, "card"), ("Rajani", 100, "upi"), ("Sumit", 1500, "upi")]

spent = {}
for name, amount, mode in payments:
    spent[name] = spent.get(name, 0) + amount

for name, total in spent.items():
    print(f"{name}: ₹{total}")
```
</details>

### 8. Smallest and biggest, in one return

Write `smallest_and_biggest(amounts)` that returns both values as a tuple, without using `min` or `max`. Unpack the result when you call it.

```text
Smallest ₹100, biggest ₹1500
```

<details><summary>Hint</summary>

Start both at `amounts[0]`, loop, update each. `return smallest, biggest` packs a tuple.
</details>

<details><summary>Solution</summary>

```python
def smallest_and_biggest(amounts):
    smallest = amounts[0]
    biggest = amounts[0]
    for amount in amounts:
        if amount < smallest:
            smallest = amount
        if amount > biggest:
            biggest = amount
    return smallest, biggest

low, high = smallest_and_biggest([600, 250, 100, 1500])
print(f"Smallest ₹{low}, biggest ₹{high}")
```
</details>

### 9. Contacts with a safe lookup

Given `contacts = {"rajani@okaxis": "Rajani", "sumit@ybl": "Sumit"}`, ask for a UPI ID. If it is a saved contact, print the name. Otherwise print the part before the `@` in title case, and add it to the contacts. Print the number of contacts at the end.

```text
UPI ID: aakash@oksbi
Paying Aakash (new contact)
Contacts: 3
```

<details><summary>Hint</summary>

`contacts.get(upi_id)` is `None` for a new ID. Build the name with `split("@")[0].title()` and assign it to `contacts[upi_id]`.
</details>

<details><summary>Solution</summary>

```python
contacts = {"rajani@okaxis": "Rajani", "sumit@ybl": "Sumit"}

upi_id = input("UPI ID: ").strip().lower()
name = contacts.get(upi_id)
if name is None:
    name = upi_id.split("@")[0].title()
    contacts[upi_id] = name
    print(f"Paying {name} (new contact)")
else:
    print(f"Paying {name}")
print("Contacts:", len(contacts))
```
</details>

---

## Challenge

### 10. Marks per student, every mark kept

Read marks as `name,mark` lines until an empty line. Keep every mark for each student in a list under the name, then print each student's marks and average.

```text
Entry: Vinay,80
Entry: Ravi,70
Entry: Vinay,90
Entry: 
Vinay: [80, 90] average 85.0
Ravi: [70] average 70.0
```

<details><summary>Hint</summary>

Split each line at the comma. If the name is not in the dictionary yet, start with an empty list, then append. The average is `sum(marks) / len(marks)`.
</details>

<details><summary>Solution</summary>

```python
marks = {}

while True:
    entry = input("Entry: ").strip()
    if entry == "":
        break
    name, mark = entry.split(",")
    mark = int(mark)
    if name not in marks:
        marks[name] = []
    marks[name].append(mark)

for name, scores in marks.items():
    average = sum(scores) / len(scores)
    print(f"{name}: {scores} average {average}")
```
</details>

### 11. Invert a dictionary, and notice what is lost

Given `city_of = {"Rajani": "Pune", "Sumit": "Bengaluru", "Vinay": "Pune"}`, build the reverse dictionary from city to a list of names. Then explain in a comment why a plain reverse (`city -> name`) would lose a name.

```text
{'Pune': ['Rajani', 'Vinay'], 'Bengaluru': ['Sumit']}
```

<details><summary>Hint</summary>

Loop over `city_of.items()`. The value in the new dictionary is a list; start it when the city is seen the first time.
</details>

<details><summary>Solution</summary>

```python
city_of = {"Rajani": "Pune", "Sumit": "Bengaluru", "Vinay": "Pune"}

names_in = {}
for name, city in city_of.items():
    if city not in names_in:
        names_in[city] = []
    names_in[city].append(name)

print(names_in)
# A plain reverse, names_in[city] = name, would assign "Pune" twice.
# The second assignment replaces the first, so Rajani would disappear.
```
</details>

### 12. Predict, then run

Without running, write down what each line prints or which error it raises. Then run and compare.

```python
t = (1, 2, 3)
print(t[1:], len(t), t.count(2))
print(type((7)), type((7,)))
s = {3, 1, 3, 2, 1}
print(len(s), 2 in s)
d = {"a": 1}
d["a"] = 2
d["b"] = 3
print(d, len(d))
print(d.get("c"), d.get("c", 0))
print({} == set())
for k, v in d.items():
    print(k, v)
t[0] = 9
```

<details><summary>Answer</summary>

```text
(2, 3) 3 1
<class 'int'> <class 'tuple'>
3 True
{'a': 2, 'b': 3} 2
None 0
False
a 2
b 3
TypeError: 'tuple' object does not support item assignment
```

`(7)` is an int. The set keeps three distinct values. `d["a"] = 2` replaced 1. `{}` is a dictionary and is never equal to a set. The last line stops the program.
</details>

---

Finished all twelve? Rewrite problem 7 so the dictionary also keeps the list of modes each payee was paid with.
