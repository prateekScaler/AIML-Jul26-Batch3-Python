# Practice problems · Class 6 · Lists

Twelve problems, easy to hard. Each uses only what Classes 1 to 6 covered. Write every program yourself in [PyLens](https://scaler-pylens.vercel.app/) or with `python3`, run it against the sample, and only then open the hint or the solution.

How to work: trace the list on paper after every line that changes it. If a value comes out as `None`, you stored the result of `sort()`, `append()` or another method that gives nothing back.

- [Warm-up](#warm-up) · problems 1 to 4
- [Core](#core) · problems 5 to 9
- [Challenge](#challenge) · problems 10 to 12

---

## Warm-up

### 1. First, last, count

Make a list of five payees and print the first one, the last one, and how many there are.

```text
Chai Point
Uber
5
```

<details><summary>Solution</summary>

```python
payees = ["Chai Point", "Zomato", "Jio", "Flipkart", "Uber"]
print(payees[0])
print(payees[-1])
print(len(payees))
```
</details>

### 2. Grow and shrink

Start with `["Milk", "Bread"]`. Append `"Eggs"`, insert `"Rice"` at the front, remove `"Bread"`, then print the list.

```text
['Rice', 'Milk', 'Eggs']
```

<details><summary>Solution</summary>

```python
shopping = ["Milk", "Bread"]
shopping.append("Eggs")
shopping.insert(0, "Rice")
shopping.remove("Bread")
print(shopping)
```
</details>

### 3. Slices

From `[10, 20, 30, 40, 50, 60]` print the first two, the last two, and everything from index 2 onwards.

```text
[10, 20]
[50, 60]
[30, 40, 50, 60]
```

<details><summary>Solution</summary>

```python
numbers = [10, 20, 30, 40, 50, 60]
print(numbers[:2])
print(numbers[-2:])
print(numbers[2:])
```
</details>

### 4. Sort two ways

Sort `[40, 10, 30, 20]` in place and print it. Then make a descending copy with `sorted` and print both the copy and the original.

```text
[10, 20, 30, 40]
[40, 30, 20, 10]
[10, 20, 30, 40]
```

<details><summary>Hint</summary>

`sorted(numbers, reverse=True)` makes the copy. `numbers` itself stays as it was after the first sort.
</details>

<details><summary>Solution</summary>

```python
numbers = [40, 10, 30, 20]
numbers.sort()
print(numbers)
descending = sorted(numbers, reverse=True)
print(descending)
print(numbers)
```
</details>

---

## Core

### 5. Total and average

Ask how many amounts, read them into a list with a loop, then print the list, the total and the average.

```text
How many? 3
Amount: 250
Amount: 400
Amount: 150
[250, 400, 150]
Total: 800
Average: 266.6666666666667
```

<details><summary>Hint</summary>

Start with `amounts = []`, append inside a `for i in range(n)` loop, then a second loop for the total.
</details>

<details><summary>Solution</summary>

```python
n = int(input("How many? "))
amounts = []
for i in range(n):
    amounts.append(int(input("Amount: ")))

total = 0
for amount in amounts:
    total += amount

print(amounts)
print("Total:", total)
print("Average:", total / len(amounts))
```
</details>

### 6. Biggest and smallest, without max or min

Given `[600, 300, 1500, 250, 90]`, print the biggest and the smallest value. Do it once with a loop and once with `sorted`.

```text
1500 90
1500 90
```

<details><summary>Solution</summary>

```python
history = [600, 300, 1500, 250, 90]

biggest = history[0]
smallest = history[0]
for amount in history:
    if amount > biggest:
        biggest = amount
    if amount < smallest:
        smallest = amount
print(biggest, smallest)

in_order = sorted(history)
print(in_order[-1], in_order[0])
```
</details>

### 7. Is it there?

Ask for a payee name. Print `Known payee` if it is in the list, otherwise add it and print the new list. Use the `in` keyword.

```text
Payee: Jio
Known payee
```

```text
Payee: Ola
['Chai Point', 'Zomato', 'Jio', 'Ola']
```

<details><summary>Solution</summary>

```python
payees = ["Chai Point", "Zomato", "Jio"]
name = input("Payee: ")
if name in payees:
    print("Known payee")
else:
    payees.append(name)
    print(payees)
```
</details>

### 8. Comprehensions

From `scores = [35, 72, 45, 90, 28, 60]` build, each in one line: the passing scores (40 or more), every score plus 5 bonus marks, and the passing scores plus the bonus.

```text
[72, 45, 90, 60]
[40, 77, 50, 95, 33, 65]
[77, 50, 95, 65]
```

<details><summary>Solution</summary>

```python
scores = [35, 72, 45, 90, 28, 60]
passing = [s for s in scores if s >= 40]
bonus = [s + 5 for s in scores]
passing_bonus = [s + 5 for s in scores if s >= 40]
print(passing)
print(bonus)
print(passing_bonus)
```
</details>

### 9. Queue at the counter

Shubhodip, Prajnika and Akash are waiting. Serve them one by one with `pop(0)`, printing `Serving <name>` each time, until the list is empty. Then print `Counter closed`.

```text
Serving Shubhodip
Serving Prajnika
Serving Akash
Counter closed
```

<details><summary>Hint</summary>

`while len(queue) > 0:` and `pop(0)` inside. An empty list counts as False, so `while queue:` works too.
</details>

<details><summary>Solution</summary>

```python
queue = ["Shubhodip", "Prajnika", "Akash"]
while len(queue) > 0:
    person = queue.pop(0)
    print("Serving", person)
print("Counter closed")
```
</details>

---

## Challenge

### 10. Remove every small payment

From `[600, 50, 1500, 20, 250, 10]` build a list without the amounts under 100, two ways: a comprehension, and a loop that appends into a new list. Do **not** remove items from the list you are looping over.

```text
[600, 1500, 250]
[600, 1500, 250]
```

<details><summary>Hint</summary>

Removing from a list while looping over it skips items, because the boxes shift. Always build a new list instead.
</details>

<details><summary>Solution</summary>

```python
history = [600, 50, 1500, 20, 250, 10]

kept = [a for a in history if a >= 100]
print(kept)

kept = []
for a in history:
    if a >= 100:
        kept.append(a)
print(kept)
```
</details>

### 11. Second largest

Given `[600, 1500, 300, 1500, 250]`, print the second largest **distinct** value. `sorted` alone gives `[250, 300, 600, 1500, 1500]`, so the second-last box is not the answer.

```text
600
```

<details><summary>Hint</summary>

Build a list with no repeats first: loop and append only values that are not already `in` the new list. Then sort it.
</details>

<details><summary>Solution</summary>

```python
history = [600, 1500, 300, 1500, 250]

unique = []
for a in history:
    if a not in unique:
        unique.append(a)

unique.sort()
print(unique[-2])
```
</details>

### 12. Predict, then run

Without running, write down what each line prints or which error it raises. Then run and compare.

```python
a = [1, 2, 3]
b = a
b.append(4)
print(a)

c = a.copy()
c.append(5)
print(a)

print(a[1:3])
print(a[-1], a[len(a) - 1])

d = a.sort()
print(d)

print(a[10])
```

<details><summary>Answer</summary>

```text
[1, 2, 3, 4]
[1, 2, 3, 4]
[2, 3]
4 4
None
IndexError: list index out of range
```

`b` is the same list as `a`, so appending through `b` changes `a`. `copy()` makes a separate list. A slice stops before its end index. `-1` and `len - 1` are the same box. `sort()` gives back `None`. Index 10 does not exist.
</details>

---

Finished all twelve? Add a `payees` list to PaisaPay v6 that grows alongside `history`, and print both in the mini statement.
