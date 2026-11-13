# Practice problems · Class 15 · File Handling

Four problems on files, easy to hard. Each uses only what Classes 1 to 15 covered. Every solution first creates the sample file it reads, so it runs anywhere. Write each program yourself, run it against the sample, and only then open the hint or the solution.

More problems, on `try`/`except`, CSV files and modules, come with Class 16.

---

## Warm-up

### 1. Uma's shopping list

Write the three items `Milk`, `Bread` and `Rice` to `shopping.txt`, one per line. Then read the file back and print each item with its number.

```text
1 Milk
2 Bread
3 Rice
```

<details><summary>Hint</summary>

`write()` does not add a newline, so add `"\n"` yourself. Each line you read back still ends with `"\n"`, so `strip()` it before printing.
</details>

<details><summary>Solution</summary>

```python
items = ["Milk", "Bread", "Rice"]
with open("shopping.txt", "w") as file:
    for item in items:
        file.write(item + "\n")

number = 1
with open("shopping.txt", "r") as file:
    for line in file:
        print(number, line.strip())
        number += 1
```
</details>

### 2. Add, do not erase

Create `payees.txt` with two payees, `Sangeeta` and `Akash`. Then, in a second `with` block, add `Vinay` without losing the first two. Print every payee and then the count.

```text
Sangeeta
Akash
Vinay
3 payees
```

<details><summary>Hint</summary>

`"w"` for the first block, `"a"` for the second. If the second block used `"w"`, only `Vinay` would be left.
</details>

<details><summary>Solution</summary>

```python
with open("payees.txt", "w") as file:
    file.write("Sangeeta\nAkash\n")

with open("payees.txt", "a") as file:
    file.write("Vinay\n")

count = 0
with open("payees.txt", "r") as file:
    for line in file:
        print(line.strip())
        count += 1
print(count, "payees")
```
</details>

## Core

### 3. Shubhodip's spends

`amounts.txt` holds one payment amount per line. Some lines are blank and some have extra spaces. Create it with these five lines: `250`, `1200`, an empty line, `80`, and `  500 ` (with spaces). Print how many payments there are and the total.

```text
4 payments, total ₹2030
```

<details><summary>Hint</summary>

Every line is a string. `strip()` it, skip it with `continue` if it is empty, then `int()` it before adding.
</details>

<details><summary>Solution</summary>

```python
with open("amounts.txt", "w") as file:
    file.write("250\n1200\n\n80\n  500 \n")

total = 0
count = 0
with open("amounts.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line == "":
            continue
        total += int(line)
        count += 1
print(f"{count} payments, total ₹{total}")
```
</details>

## Challenge

### 4. A log family

Write a `FileLog` class that remembers a file name. Its `write(message)` method adds one line to the file with `"a"`, and the line it adds comes from `self.line(message)`. On `FileLog`, `line` returns the message as it is. Write `AlertLog(FileLog)` that overrides only `line`: it returns `ALERT: ` followed by the parent's line in capitals, using `super()`. Start `activity.txt` fresh with the line `PaisaPay activity`, write three messages through the two kinds of log, and print the file.

```text
PaisaPay activity
Paid Rs.600 to Hitender
ALERT: THREE WRONG PINS FOR SATHVIK
Paid Rs.250 to Akash
```

<details><summary>Hint</summary>

`write` lives only on the parent. When an `AlertLog` calls it, `self` is the `AlertLog`, so `self.line(...)` runs the child's version. That is the first inheritance scenario from the class.
</details>

<details><summary>Solution</summary>

```python
class FileLog:
    def __init__(self, filename):
        self.filename = filename

    def line(self, message):
        return message

    def write(self, message):
        with open(self.filename, "a") as file:
            file.write(self.line(message) + "\n")

class AlertLog(FileLog):
    def line(self, message):
        return "ALERT: " + super().line(message).upper()

with open("activity.txt", "w") as file:
    file.write("PaisaPay activity\n")

normal = FileLog("activity.txt")
alerts = AlertLog("activity.txt")
normal.write("Paid Rs.600 to Hitender")
alerts.write("Three wrong PINs for Sathvik")
normal.write("Paid Rs.250 to Akash")

with open("activity.txt", "r") as file:
    for line in file:
        print(line.strip())
```
</details>

---

Finished them all? Give problem 11 a second file, `history.txt`. Every payment adds one line to it with `"a"`, and every run starts by printing the last three payments, or `No payments yet.` when the file does not exist.
