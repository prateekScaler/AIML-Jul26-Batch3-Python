# Practice problems · Class 5 · Functions

Twelve problems, easy to hard. Each uses only what Classes 1 to 5 covered. Write every program yourself in [PyLens](https://scaler-pylens.vercel.app/) or with `python3`, run it against the sample, and only then open the hint or the solution.

How to work: write the function first, then the calls under it. Run it, compare the output character by character. If a value comes out as `None`, look for a missing `return`.

- [Warm-up](#warm-up) · problems 1 to 4
- [Core](#core) · problems 5 to 9
- [Challenge](#challenge) · problems 10 to 12

---

## Warm-up

### 1. Greeting with a default

Write `greet(name)` that prints `Hello <name>`. Give it a default so `greet()` prints `Hello Student`.

```text
Hello Student
Hello Raghunathan
```

<details><summary>Solution</summary>

```python
def greet(name="Student"):
    print("Hello", name)

greet()
greet("Raghunathan")
```
</details>

### 2. Square and cube

Write `square(n)` and `cube(n)` that **return** their results. Print `square(4)`, `cube(3)` and `square(2) + cube(2)`.

```text
16
27
12
```

<details><summary>Hint</summary>

`return`, not `print`. The third line only works if the functions hand values back.
</details>

<details><summary>Solution</summary>

```python
def square(n):
    return n * n

def cube(n):
    return n * n * n

print(square(4))
print(cube(3))
print(square(2) + cube(2))
```
</details>

### 3. Even or odd

Write `check_even(number)` that returns `"Even"` or `"Odd"`. Then rewrite it as a lambda and check both give the same answer for 7.

```text
Even
Odd
Odd
```

<details><summary>Solution</summary>

```python
def check_even(number):
    if number % 2 == 0:
        return "Even"
    return "Odd"

is_even = lambda n: "Even" if n % 2 == 0 else "Odd"

print(check_even(10))
print(check_even(7))
print(is_even(7))
```
</details>

### 4. Rupees to paise

Write `to_paise(rupees)` that returns the amount in paise as a whole number. `rupees` may have decimals.

```text
1250
50
```

<details><summary>Hint</summary>

`round(rupees * 100)` avoids float surprises such as `0.29 * 100` being `28.999...`.
</details>

<details><summary>Solution</summary>

```python
def to_paise(rupees):
    return round(rupees * 100)

print(to_paise(12.50))
print(to_paise(0.5))
```
</details>

---

## Core

### 5. Cashback with a default rate

Write `cashback(amount, rate=5)` that returns the cashback in whole rupees. Call it three ways: with the default, with a positional rate, and with a keyword rate.

```text
50
100
200
```

<details><summary>Solution</summary>

```python
def cashback(amount, rate=5):
    return amount * rate // 100

print(cashback(1000))
print(cashback(1000, 10))
print(cashback(1000, rate=20))
```
</details>

### 6. Largest of three

Write `largest(a, b, c)` that returns the largest value without using `max`.

```text
1200
7
```

<details><summary>Hint</summary>

Start with `result = a`, then two separate `if`s.
</details>

<details><summary>Solution</summary>

```python
def largest(a, b, c):
    result = a
    if b > result:
        result = b
    if c > result:
        result = c
    return result

print(largest(450, 1200, 800))
print(largest(7, 7, 3))
```
</details>

### 7. Count the vowels

Write `count_vowels(text)` that returns how many of the letters a, e, i, o, u appear in `text`. Loop over the text with `for letter in text`, the way you looped over a list.

```text
Enter text: PaisaPay
4
```

<details><summary>Hint</summary>

A counter that starts at 0, a `for` over the text, and `if letter in "aeiouAEIOU"`.
</details>

<details><summary>Solution</summary>

```python
def count_vowels(text):
    count = 0
    for letter in text:
        if letter in "aeiouAEIOU":
            count += 1
    return count

text = input("Enter text: ")
print(count_vowels(text))
```
</details>

### 8. Is it prime?

Write `is_prime(n)` that returns True or False. Use it to print all primes from 2 to 30 on one line.

```text
2 3 5 7 11 13 17 19 23 29
```

<details><summary>Hint</summary>

Inside `is_prime`, `for d in range(2, n)`: if `n % d == 0`, `return False` at once. After the loop, `return True`. The `return` inside the loop replaces the flag you used in Class 4.
</details>

<details><summary>Solution</summary>

```python
def is_prime(n):
    if n < 2:
        return False
    for d in range(2, n):
        if n % d == 0:
            return False
    return True

for n in range(2, 31):
    if is_prime(n):
        print(n, end=" ")
print()
```
</details>

### 9. Sum of digits, as a function

Write `digit_sum(n)` that returns the sum of the digits of a whole number, using `% 10` and `// 10`. Then print `digit_sum(4321)` and `digit_sum(digit_sum(99999))`.

```text
10
9
```

<details><summary>Solution</summary>

```python
def digit_sum(n):
    total = 0
    while n > 0:
        total += n % 10
        n = n // 10
    return total

print(digit_sum(4321))
print(digit_sum(digit_sum(99999)))
```
</details>

---

## Challenge

### 10. Validate, then act

Write three functions: `is_valid_amount(amount)` (more than 0, at most ₹1,00,000), `is_valid_pin(pin)` (equal to `"4321"`), and `pay(balance, amount, pin)` that uses both checks and returns the new balance. A refused payment returns the balance unchanged and prints why.

```text
Wrong PIN. Payment refused.
1000
Invalid amount. Payment refused.
1000
Paid ₹ 600
400
```

<details><summary>Solution</summary>

```python
def is_valid_amount(amount):
    return amount > 0 and amount <= 100000

def is_valid_pin(pin):
    return pin == "4321"

def pay(balance, amount, pin):
    if not is_valid_pin(pin):
        print("Wrong PIN. Payment refused.")
        return balance
    if not is_valid_amount(amount):
        print("Invalid amount. Payment refused.")
        return balance
    print("Paid ₹", amount)
    return balance - amount

balance = 1000
balance = pay(balance, 600, "1111")
print(balance)
balance = pay(balance, -5, "4321")
print(balance)
balance = pay(balance, 600, "4321")
print(balance)
```
</details>

### 11. EMI calculator

Write `emi(principal, months, rate=12)` that returns the monthly payment in whole rupees for a simple-interest loan: total interest is `principal * rate * months // (100 * 12)`, and the EMI is the principal plus interest, divided by the months. Print the EMI for ₹1,20,000 over 12 months at the default rate, and over 24 months at 10%.

```text
11200
6000
```

<details><summary>Hint</summary>

Compute `interest` first, then `return (principal + interest) // months`.
</details>

<details><summary>Solution</summary>

```python
def emi(principal, months, rate=12):
    interest = principal * rate * months // (100 * 12)
    return (principal + interest) // months

print(emi(120000, 12))
print(emi(120000, 24, rate=10))
```
</details>

### 12. Predict, then run

Without running, write down what each snippet prints or which error it raises. Then run and compare.

```python
def f(x):
    return x + 1
    return x + 2

print(f(1))

def g(x):
    print(x * 2)

y = g(5)
print(y)

def h(a, b=10):
    return a - b

print(h(b=3, a=20))

def k():
    total = 5

k()
print(total)
```

<details><summary>Answer</summary>

```text
2
10
None
17
NameError: name 'total' is not defined
```

Only the first `return` in `f` runs. `g` prints 10 but returns nothing, so `y` is `None`. Keyword arguments may come in any order. `total` was local to `k` and no longer exists outside it.
</details>

---

Finished all twelve? Take problem 10 and add a `mode="upi"` parameter with a fee of ₹5 for `"card"`, the way PaisaPay v5 does it.
