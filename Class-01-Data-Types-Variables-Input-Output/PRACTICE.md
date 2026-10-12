# Practice problems · Class 1 · Data Types, Variables, Input and Output

Twelve problems, easy to hard. Each uses only what Class 1 covered: `print`, variables, `int`, `float`, `str`, `bool`, `type`, `input` and type casting. Write every program yourself in [PyLens](https://scaler-pylens.vercel.app/) or with `python3`, run it against the sample, and only then open the hint or the solution.

How to work: read the problem, write the program, run it, compare the output character by character.

- [Warm-up](#warm-up) · problems 1 to 4
- [Core](#core) · problems 5 to 9
- [Challenge](#challenge) · problems 10 to 12

---

## Warm-up

### 1. Hello, name

Store your name in a variable and print a greeting.

```text
Hello, Kishor! Welcome to PaisaPay.
```

<details><summary>Solution</summary>

```python
name = "Kishor"
print("Hello,", name + "!", "Welcome to PaisaPay.")
```
</details>

### 2. Four values, four types

Create one variable of each type, `int`, `float`, `str` and `bool`, and print each value with its type.

```text
1000 <class 'int'>
2.5 <class 'float'>
UPI <class 'str'>
True <class 'bool'>
```

<details><summary>Solution</summary>

```python
balance = 1000
fee = 2.5
mode = "UPI"
is_active = True
print(balance, type(balance))
print(fee, type(fee))
print(mode, type(mode))
print(is_active, type(is_active))
```
</details>

### 3. Swap two values

Two variables hold ₹500 and ₹800. Swap them and print both.

```text
Before: 500 800
After: 800 500
```

<details><summary>Hint</summary>

Use a third variable to hold one value while you move the other. Python also allows `a, b = b, a`.
</details>

<details><summary>Solution</summary>

```python
a = 500
b = 800
print("Before:", a, b)
temp = a
a = b
b = temp
print("After:", a, b)
```
</details>

### 4. Echo with a twist

Ask for the user's city and print it twice on one line with a dash between.

```text
Your city: Pune
Pune - Pune
```

<details><summary>Solution</summary>

```python
city = input("Your city: ")
print(city, "-", city)
```
</details>

---

## Core

### 5. Age next year

Ask for an age and print the age next year. Remember that `input` gives text.

```text
Your age: 24
Next year you will be 25
```

<details><summary>Hint</summary>

`int(input(...))`, then add 1. Without `int`, `"24" + 1` is a `TypeError`.
</details>

<details><summary>Solution</summary>

```python
age = int(input("Your age: "))
print("Next year you will be", age + 1)
```
</details>

### 6. Receipt line

Ask for a payee and an amount. Print a one-line receipt.

```text
Pay to: Zomato
Amount: 450
Paid ₹ 450 to Zomato
```

<details><summary>Solution</summary>

```python
payee = input("Pay to: ")
amount = int(input("Amount: "))
print("Paid ₹", amount, "to", payee)
```
</details>

### 7. Rupees to paise

Ask for an amount in rupees (it may have decimals) and print it in paise as a whole number.

```text
Amount in rupees: 12.50
Paise: 1250
```

<details><summary>Hint</summary>

`float(input(...))`, multiply by 100, then `int(...)` to drop the decimal point.
</details>

<details><summary>Solution</summary>

```python
rupees = float(input("Amount in rupees: "))
paise = int(rupees * 100)
print("Paise:", paise)
```
</details>

### 8. Minutes to hours and minutes

Ask for a number of minutes and print it as hours and minutes.

```text
Minutes: 135
2 hours 15 minutes
```

<details><summary>Hint</summary>

`//` gives the whole hours, `%` gives what is left over.
</details>

<details><summary>Solution</summary>

```python
minutes = int(input("Minutes: "))
print(minutes // 60, "hours", minutes % 60, "minutes")
```
</details>

### 9. Text or number?

Ask for a value and print the value, its type, and the value after `int()`. Try it with `42`, then with `42.0`, and read the error carefully.

```text
Enter: 42
42 <class 'str'>
42 <class 'int'>
```

<details><summary>Solution</summary>

```python
value = input("Enter: ")
print(value, type(value))
number = int(value)
print(number, type(number))
```

With `42.0`, `int("42.0")` raises `ValueError: invalid literal for int() with base 10: '42.0'`. `int()` on text accepts only whole-number digits.
</details>

---

## Challenge

### 10. Two-line receipt with a total

Ask for a name, a payee, an amount and a fee. Print the receipt below. The total is a number, not text joined together.

```text
Your name: Rashi
Pay to: Chai Point
Amount: 120
Fee: 2
Rashi paid ₹ 120 to Chai Point
Total charged: ₹ 122
```

<details><summary>Hint</summary>

Both `amount` and `fee` need `int(...)`. If you forget one, `+` joins text: `"1202"`.
</details>

<details><summary>Solution</summary>

```python
name = input("Your name: ")
payee = input("Pay to: ")
amount = int(input("Amount: "))
fee = int(input("Fee: "))
print(name, "paid ₹", amount, "to", payee)
print("Total charged: ₹", amount + fee)
```
</details>

### 11. The string surprise, on purpose

Write a program that asks for two numbers and prints them joined as text on the first line, and added as numbers on the second.

```text
First: 7
Second: 5
Joined: 75
Added: 12
```

<details><summary>Hint</summary>

Keep the raw `input` values for the first line. Cast with `int` only for the second.
</details>

<details><summary>Solution</summary>

```python
first = input("First: ")
second = input("Second: ")
print("Joined:", first + second)
print("Added:", int(first) + int(second))
```
</details>

### 12. Predict, then run

Without running, write down what each line prints or which error it raises. Then run the file and compare.

```python
print(type(10 / 2))
print(type(10 // 2))
print(int(9.99))
print(float("3"))
print(str(5) + str(5))
print(bool(0), bool("0"))
print(int("ten"))
```

<details><summary>Answer</summary>

```text
<class 'float'>
<class 'int'>
9
3.0
55
False True
ValueError: invalid literal for int() with base 10: 'ten'
```

`/` always gives a float. `int()` on a float cuts off the decimals, it does not round. `"0"` is a non-empty string, so it counts as True. The last line stops the program.
</details>

---

Finished all twelve? Rewrite problem 10 so the fee is a float like `2.5`, and look closely at what the total prints.
