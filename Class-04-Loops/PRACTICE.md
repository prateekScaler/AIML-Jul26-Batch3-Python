# Practice problems · Class 4 · Loops

Twelve problems, easy to hard. Each uses only what Classes 1 to 4 covered. Write every program yourself in [PyLens](https://scaler-pylens.vercel.app/) or with `python3`, run it against the sample, and only then open the hint or the solution.

How to work: read the problem, write the program, run it, compare the output character by character. If it differs, trace your loop on paper before you change anything.

- [Warm-up](#warm-up) · problems 1 to 4
- [Core](#core) · problems 5 to 9
- [Challenge](#challenge) · problems 10 to 12

---

## Warm-up

### 1. Token display

Print `Token 1` to `Token 10`, one per line.

```text
Token 1
Token 2
...
Token 10
```

<details><summary>Hint</summary>

`range` stops before its end value. To reach 10, stop at 11.
</details>

<details><summary>Solution</summary>

```python
for token in range(1, 11):
    print("Token", token)
```
</details>

### 2. OTP countdown

Count down from 30 to 1 in steps of 5, then print `OTP expired`.

```text
30
25
20
15
10
5
OTP expired
```

<details><summary>Hint</summary>

A negative step counts down: `range(30, 0, -5)`. The last print is outside the loop.
</details>

<details><summary>Solution</summary>

```python
for sec in range(30, 0, -5):
    print(sec)
print("OTP expired")
```
</details>

### 3. Multiplication table

Ask for a number and print its table from 1 to 10.

```text
Enter a number: 7
7 x 1 = 7
7 x 2 = 14
...
7 x 10 = 70
```

<details><summary>Solution</summary>

```python
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(n, "x", i, "=", n * i)
```
</details>

### 4. Even numbers only

Print the even numbers from 2 to 20 on one line, separated by spaces.

```text
2 4 6 8 10 12 14 16 18 20
```

<details><summary>Hint</summary>

Two ways: `range(2, 21, 2)`, or `range(1, 21)` with `if i % 2 == 0`. Use `end=" "` to stay on one line.
</details>

<details><summary>Solution</summary>

```python
for i in range(2, 21, 2):
    print(i, end=" ")
print()
```
</details>

---

## Core

### 5. Sum and average

Ask how many payments, then ask for each amount. Print the total and the average.

```text
How many payments? 3
Amount: 250
Amount: 400
Amount: 150
Total: ₹ 800
Average: ₹ 266.6666666666667
```

<details><summary>Hint</summary>

Start `total = 0` above the loop. Add inside it. Divide after it.
</details>

<details><summary>Solution</summary>

```python
n = int(input("How many payments? "))
total = 0
for i in range(n):
    amount = int(input("Amount: "))
    total += amount
print("Total: ₹", total)
print("Average: ₹", total / n)
```
</details>

### 6. Three PIN attempts

The saved PIN is `4321`. Give the user three attempts. Print `Access granted` on success, `Card blocked` after three wrong tries.

```text
UPI PIN: 1111
Wrong PIN. 2 attempts left
UPI PIN: 2222
Wrong PIN. 1 attempts left
UPI PIN: 3333
Wrong PIN. 0 attempts left
Card blocked
```

<details><summary>Hint</summary>

A flag that starts `False`, a `for attempt in range(3)`, and a `break` when the PIN matches. Check the flag after the loop.
</details>

<details><summary>Solution</summary>

```python
saved_pin = "4321"
pin_ok = False

for attempt in range(3):
    pin = input("UPI PIN: ")
    if pin == saved_pin:
        pin_ok = True
        break
    print("Wrong PIN.", 2 - attempt, "attempts left")

if pin_ok:
    print("Access granted")
else:
    print("Card blocked")
```
</details>

### 7. Savings goal

Madhumaya saves ₹1,500 a month. How many months until the savings reach ₹10,000? Print each month's balance, then the answer.

```text
Month 1 : ₹ 1500
Month 2 : ₹ 3000
...
Month 7 : ₹ 10500
Goal reached in 7 months
```

<details><summary>Hint</summary>

The number of months is unknown, so use `while saved < 10000`. Count the months in a second variable.
</details>

<details><summary>Solution</summary>

```python
saved = 0
month = 0

while saved < 10000:
    month += 1
    saved += 1500
    print("Month", month, ": ₹", saved)

print("Goal reached in", month, "months")
```
</details>

### 8. Digit sum

Ask for a whole number and print the sum of its digits. Do it with maths, not strings: `% 10` gives the last digit, `// 10` removes it.

```text
Enter a number: 4321
Digit sum: 10
```

<details><summary>Hint</summary>

`while n > 0:` take `n % 10`, add it, then `n = n // 10`.
</details>

<details><summary>Solution</summary>

```python
n = int(input("Enter a number: "))
total = 0

while n > 0:
    total += n % 10
    n = n // 10

print("Digit sum:", total)
```
</details>

### 9. Menu until exit

A menu with three choices. Keep showing it until the user picks 3. Count how many times each of the other two was chosen.

```text
1. Check balance  2. Pay  3. Exit
Choose: 1
1. Check balance  2. Pay  3. Exit
Choose: 2
1. Check balance  2. Pay  3. Exit
Choose: 2
1. Check balance  2. Pay  3. Exit
Choose: 3
Balance checks: 1 | Payments: 2
```

<details><summary>Solution</summary>

```python
checks = 0
pays = 0
choice = ""

while choice != "3":
    print("1. Check balance  2. Pay  3. Exit")
    choice = input("Choose: ")
    if choice == "1":
        checks += 1
    elif choice == "2":
        pays += 1

print("Balance checks:", checks, "| Payments:", pays)
```
</details>

---

## Challenge

### 10. Prime or not

Ask for a number greater than 1. Print `Prime` if nothing from 2 up to the number minus 1 divides it, otherwise `Not prime`.

```text
Enter a number: 29
Prime
```

```text
Enter a number: 51
Not prime
```

<details><summary>Hint</summary>

The find pattern: a flag `is_prime = True`, a loop `for d in range(2, n)`, and when `n % d == 0` set the flag False and `break`.
</details>

<details><summary>Solution</summary>

```python
n = int(input("Enter a number: "))
is_prime = True

for d in range(2, n):
    if n % d == 0:
        is_prime = False
        break

if is_prime:
    print("Prime")
else:
    print("Not prime")
```
</details>

### 11. Number pyramid

Ask for a height and print a pyramid of numbers.

```text
Height: 4
1
1 2
1 2 3
1 2 3 4
```

<details><summary>Hint</summary>

Outer loop for rows 1 to height. Inner loop `range(1, row + 1)` with `end=" "`. A bare `print()` after the inner loop.
</details>

<details><summary>Solution</summary>

```python
height = int(input("Height: "))

for row in range(1, height + 1):
    for n in range(1, row + 1):
        print(n, end=" ")
    print()
```
</details>

### 12. Cashback until the budget ends

A merchant has a cashback budget of ₹500. Each payment earns 5% cashback in whole rupees. Keep asking for payment amounts. Pay the cashback while the budget covers it. When a cashback would exceed what is left, print `Budget over` and stop. Enter 0 to stop early.

```text
Amount: 2000
Cashback ₹ 100 | Budget left ₹ 400
Amount: 6000
Cashback ₹ 300 | Budget left ₹ 100
Amount: 4000
Budget over
```

<details><summary>Hint</summary>

`while True` is not covered yet, so use `while budget > 0`. Inside: read the amount, `break` if it is 0, compute `cashback = amount * 5 // 100`, then either pay it or print `Budget over` and `break`.
</details>

<details><summary>Solution</summary>

```python
budget = 500

while budget > 0:
    amount = int(input("Amount: "))
    if amount == 0:
        break
    cashback = amount * 5 // 100
    if cashback > budget:
        print("Budget over")
        break
    budget -= cashback
    print("Cashback ₹", cashback, "| Budget left ₹", budget)
```
</details>

---

Finished all twelve? Rewrite problem 5 with a `while` loop, and problem 7 with a `for` loop. Notice which one felt natural and why.
