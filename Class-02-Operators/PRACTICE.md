# Practice problems · Class 2 · Operators

Twelve problems, easy to hard. Each uses only what Classes 1 and 2 covered: arithmetic (`+ - * / // % **`), assignment operators, comparisons, `and` / `or` / `not`, `is`, and operator precedence. No `if` yet: every answer is printed, including the True/False ones. Write every program yourself in [PyLens](https://scaler-pylens.vercel.app/) or with `python3`, run it against the sample, and only then open the hint or the solution.

- [Warm-up](#warm-up) · problems 1 to 4
- [Core](#core) · problems 5 to 9
- [Challenge](#challenge) · problems 10 to 12

---

## Warm-up

### 1. Bill with fee

Ask for an amount. Add a flat ₹2 fee and print the total.

```text
Amount: 450
Total: 452
```

<details><summary>Solution</summary>

```python
amount = int(input("Amount: "))
print("Total:", amount + 2)
```
</details>

### 2. Split the bill

Ask for a bill and the number of people. Print each person's share as a whole number and the rupees left over.

```text
Bill: 1000
People: 3
Each pays: 333
Left over: 1
```

<details><summary>Hint</summary>

`//` for the share, `%` for what is left.
</details>

<details><summary>Solution</summary>

```python
bill = int(input("Bill: "))
people = int(input("People: "))
print("Each pays:", bill // people)
print("Left over:", bill % people)
```
</details>

### 3. Cashback in whole rupees

Ask for an amount and print 5% cashback as a whole number of rupees.

```text
Amount: 1250
Cashback: 62
```

<details><summary>Hint</summary>

`amount * 5 // 100`. Multiply first, then floor-divide, so you never get 62.5.
</details>

<details><summary>Solution</summary>

```python
amount = int(input("Amount: "))
print("Cashback:", amount * 5 // 100)
```
</details>

### 4. Is the balance enough?

Balance is ₹1000. Ask for an amount and print whether the balance is enough, as `True` or `False`.

```text
Amount: 1200
Enough balance: False
```

<details><summary>Solution</summary>

```python
balance = 1000
amount = int(input("Amount: "))
print("Enough balance:", balance >= amount)
```
</details>

---

## Core

### 5. Seconds to h:m:s

Ask for a number of seconds and print hours, minutes and seconds.

```text
Seconds: 3725
1 h 2 m 5 s
```

<details><summary>Hint</summary>

Hours: `s // 3600`. The rest: `s % 3600`. Then minutes and seconds from the rest.
</details>

<details><summary>Solution</summary>

```python
s = int(input("Seconds: "))
hours = s // 3600
rest = s % 3600
print(hours, "h", rest // 60, "m", rest % 60, "s")
```
</details>

### 6. Compound interest

Ask for a principal, a yearly rate in percent and a number of years. Print the final amount using `**`.

```text
Principal: 10000
Rate %: 8
Years: 3
Final amount: 12597.12
```

<details><summary>Hint</summary>

`principal * (1 + rate / 100) ** years`. The sample shows the value rounded to two decimals with `round(x, 2)`.
</details>

<details><summary>Solution</summary>

```python
principal = int(input("Principal: "))
rate = int(input("Rate %: "))
years = int(input("Years: "))
final = principal * (1 + rate / 100) ** years
print("Final amount:", round(final, 2))
```
</details>

### 7. Running balance with assignment operators

Start with ₹1000. Add ₹500, pay ₹320, pay ₹180, then get ₹10 cashback. Use `+=` and `-=` only, and print the balance after each step.

```text
1500
1180
1000
1010
```

<details><summary>Solution</summary>

```python
balance = 1000
balance += 500
print(balance)
balance -= 320
print(balance)
balance -= 180
print(balance)
balance += 10
print(balance)
```
</details>

### 8. Can the payment go through?

A payment goes through when the balance is enough **and** the account is not frozen. Set `balance = 1000`, `is_frozen = False`, ask for an amount, and print the answer as True or False.

```text
Amount: 600
Can pay: True
```

<details><summary>Solution</summary>

```python
balance = 1000
is_frozen = False
amount = int(input("Amount: "))
print("Can pay:", balance >= amount and not is_frozen)
```
</details>

### 9. Which is bigger?

Ask for two amounts and print three lines: whether the first is bigger, whether they are equal, and the larger of the two using `max`.

```text
First: 450
Second: 450
First is bigger: False
Equal: True
Larger: 450
```

<details><summary>Solution</summary>

```python
a = int(input("First: "))
b = int(input("Second: "))
print("First is bigger:", a > b)
print("Equal:", a == b)
print("Larger:", max(a, b))
```
</details>

---

## Challenge

### 10. Big or digital

A payment is "worth a reminder" when it is ₹5,000 or more, **or** when it is by card **and** ₹2,000 or more. Set `mode = "card"`, ask for an amount, and print the answer. Use brackets so the order is clear.

```text
Amount: 2500
Reminder: True
```

<details><summary>Hint</summary>

`amount >= 5000 or (mode == "card" and amount >= 2000)`. `and` binds tighter than `or`, so the brackets only make it readable here, but they matter when the logic is the other way round.
</details>

<details><summary>Solution</summary>

```python
mode = "card"
amount = int(input("Amount: "))
print("Reminder:", amount >= 5000 or (mode == "card" and amount >= 2000))
```
</details>

### 11. Money in paise

Floats lose precision. Store money as whole paise instead. Ask for two amounts in rupees with decimals, convert each to paise with `round(x * 100)`, add them as integers, and print the total in rupees and paise.

```text
First: 0.10
Second: 0.20
Total: 0 rupees 30 paise
```

<details><summary>Hint</summary>

`0.1 + 0.2` is not exactly `0.3` in a float. Integer paise never drift. Rupees are `total // 100`, paise are `total % 100`.
</details>

<details><summary>Solution</summary>

```python
first = float(input("First: "))
second = float(input("Second: "))
total = round(first * 100) + round(second * 100)
print("Total:", total // 100, "rupees", total % 100, "paise")
```
</details>

### 12. Predict, then run

Without running, write down what each line prints. Then run the file and compare.

```python
print(7 / 2, 7 // 2, 7 % 2)
print(-7 // 2)
print(2 ** 3 ** 2)
print(10 - 4 - 3)
print(5 + 3 * 2 == 16)
print(not True or True)
print(1000 >= 1000 and 1000 > 1000)
print(0.1 + 0.2 == 0.3)
```

<details><summary>Answer</summary>

```text
3.5 3 1
-4
512
3
False
True
False
False
```

`//` rounds down, so `-7 // 2` is −4, not −3. `**` groups from the right: `3 ** 2` first, then `2 ** 9`. `-` groups from the left. `*` before `+`, so the comparison is `11 == 16`. `not` binds tighter than `or`: `(not True) or True`. The last line is why money is stored in paise.
</details>

---

Finished all twelve? Redo problem 2 with a bill of ₹1000 and 0 people and read the error. Which class fixes that?
