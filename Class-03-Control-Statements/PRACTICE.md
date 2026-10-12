# Practice problems · Class 3 · Control Statements

Twelve problems, easy to hard. Each uses only what Classes 1 to 3 covered: `if`, `elif`, `else`, `match` / `case`, conditions with `and` / `or` / `not`, nested decisions and the ternary expression. Write every program yourself in [PyLens](https://scaler-pylens.vercel.app/) or with `python3`, run it against the sample, and only then open the hint or the solution.

- [Warm-up](#warm-up) · problems 1 to 4
- [Core](#core) · problems 5 to 9
- [Challenge](#challenge) · problems 10 to 12

---

## Warm-up

### 1. Positive, negative or zero

Ask for a number and print `Positive`, `Negative` or `Zero`.

```text
Number: -5
Negative
```

<details><summary>Solution</summary>

```python
n = int(input("Number: "))
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")
```
</details>

### 2. Even or odd

Ask for a whole number and print `Even` or `Odd`. Then write it again as one line with a ternary.

```text
Number: 7
Odd
```

<details><summary>Solution</summary>

```python
n = int(input("Number: "))
if n % 2 == 0:
    print("Even")
else:
    print("Odd")

print("Even" if n % 2 == 0 else "Odd")
```
</details>

### 3. Pass or fail

Ask for marks. 40 or more passes.

```text
Marks: 39
Fail
```

<details><summary>Solution</summary>

```python
marks = int(input("Marks: "))
if marks >= 40:
    print("Pass")
else:
    print("Fail")
```
</details>

### 4. Largest of three

Ask for three amounts and print the largest, without using `max`.

```text
First: 450
Second: 1200
Third: 800
Largest: 1200
```

<details><summary>Hint</summary>

Start with `largest = a`. Then `if b > largest`, then `if c > largest`. Two separate `if`s, not `elif`: both must be checked.
</details>

<details><summary>Solution</summary>

```python
a = int(input("First: "))
b = int(input("Second: "))
c = int(input("Third: "))
largest = a
if b > largest:
    largest = b
if c > largest:
    largest = c
print("Largest:", largest)
```
</details>

---

## Core

### 5. Grade letter

Ask for a score and print the grade: 90 or more A, 80 or more B, 70 or more C, 60 or more D, otherwise F. Test with 95, 80, 59.

```text
Score: 80
Grade: B
```

<details><summary>Hint</summary>

Highest first. If `>= 60` comes first, 95 lands on D.
</details>

<details><summary>Solution</summary>

```python
score = int(input("Score: "))
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print("Grade:", grade)
```
</details>

### 6. Leap year

Ask for a year. A leap year is divisible by 4, except years divisible by 100, unless also divisible by 400. Test with 2024, 1900, 2000.

```text
Year: 1900
Not a leap year
```

<details><summary>Hint</summary>

One condition: `(year % 4 == 0 and year % 100 != 0) or year % 400 == 0`.
</details>

<details><summary>Solution</summary>

```python
year = int(input("Year: "))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Leap year")
else:
    print("Not a leap year")
```
</details>

### 7. Payment mode with match

Ask for a mode and use `match` to print `Enter UPI PIN` for `upi`, `Enter card PIN` for `card`, `Redirecting to bank` for `netbanking`, and `Unknown mode` for anything else.

```text
Mode: card
Enter card PIN
```

<details><summary>Solution</summary>

```python
mode = input("Mode: ")
match mode:
    case "upi":
        print("Enter UPI PIN")
    case "card":
        print("Enter card PIN")
    case "netbanking":
        print("Redirecting to bank")
    case _:
        print("Unknown mode")
```
</details>

### 8. ATM withdrawal

Balance is ₹8,500. Ask for an amount. Refuse it with its own message if it is not a multiple of 100, or more than ₹10,000, or more than the balance. Otherwise print the new balance. Check in that order.

```text
Amount: 250
Amount must be a multiple of 100
```

```text
Amount: 9000
Insufficient balance
```

<details><summary>Solution</summary>

```python
balance = 8500
amount = int(input("Amount: "))
if amount % 100 != 0:
    print("Amount must be a multiple of 100")
elif amount > 10000:
    print("Limit is 10000 per withdrawal")
elif amount > balance:
    print("Insufficient balance")
else:
    balance -= amount
    print("New balance:", balance)
```
</details>

### 9. Login with two checks

The saved PIN is `4321` and the account is not frozen. Ask for the PIN. Use a nested `if`: check the PIN first, then the frozen flag, each with its own message.

```text
PIN: 4321
Welcome
```

```text
PIN: 1111
Wrong PIN
```

<details><summary>Solution</summary>

```python
saved_pin = "4321"
is_frozen = False
pin = input("PIN: ")
if pin == saved_pin:
    if is_frozen:
        print("Account frozen. Call the bank.")
    else:
        print("Welcome")
else:
    print("Wrong PIN")
```
</details>

---

## Challenge

### 10. Cashback tiers with a cap

Cashback is 20% for ₹5,000 or more, 10% for ₹2,000 or more, otherwise 0. But the cashback is never more than ₹500. Print the cashback.

```text
Amount: 8000
Cashback: 500
```

<details><summary>Hint</summary>

Compute the tier first, then a second `if cashback > 500`, or `cashback = min(cashback, 500)`.
</details>

<details><summary>Solution</summary>

```python
amount = int(input("Amount: "))
if amount >= 5000:
    cashback = amount * 20 // 100
elif amount >= 2000:
    cashback = amount * 10 // 100
else:
    cashback = 0
if cashback > 500:
    cashback = 500
print("Cashback:", cashback)
```
</details>

### 11. Ticket price

A metro ticket costs ₹40. Children under 5 ride free. Ages 5 to 12 and 60 or above pay half. On Sundays everyone pays ₹10 less, but never below 0. Ask for the age and whether it is Sunday (`yes` / `no`). Print the fare.

```text
Age: 65
Sunday? yes
Fare: 10
```

<details><summary>Hint</summary>

Work out the base fare with an `if` / `elif` / `else` chain, then apply the Sunday discount with a second `if`, then a third `if fare < 0`.
</details>

<details><summary>Solution</summary>

```python
age = int(input("Age: "))
sunday = input("Sunday? ")
if age < 5:
    fare = 0
elif age <= 12 or age >= 60:
    fare = 20
else:
    fare = 40
if sunday == "yes":
    fare -= 10
if fare < 0:
    fare = 0
print("Fare:", fare)
```
</details>

### 12. Predict, then run

Without running, write down what each snippet prints. Then run and compare.

```python
x = 0
if x:
    print("A")
else:
    print("B")

mode = "cash"
if mode == "upi" or "card":
    print("C")

score = 85
print("D" if score > 90 else "E" if score > 80 else "F")

a = 5
if a > 3:
    if a > 10:
        print("G")
else:
    print("H")
print("I")
```

<details><summary>Answer</summary>

```text
B
C
E
I
```

`0` counts as False. `"card"` is a non-empty string, so the second condition is always True. The ternary reads left to right: not above 90, above 80, so `E`. In the last block the outer `if` is True, the inner is False and has no `else`, and the `else` belongs to the outer `if`; only `I` prints.
</details>

---

Finished all twelve? Redo problem 8 and refuse a negative amount too. Where in the chain does that check belong, and why?
