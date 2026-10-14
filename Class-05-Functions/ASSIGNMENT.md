# Assignment · Class 5

Practice for `def`, parameters and arguments, `return`, scope, default and keyword arguments, and `lambda`. Do Part A on paper first. Write Parts B and C yourself before asking any AI assistant. For more coding problems with solutions, see [`PRACTICE.md`](PRACTICE.md).

Run your programs in [PyLens](https://scaler-pylens.vercel.app/) or with `python3 filename.py`.

## Part A · Predict the output (no running)

Write down what each snippet prints, or which error it raises. Then run it and compare.

**A1**
```python
def hello():
    print("Hello")

hello
hello()
```

**A2**
```python
def add(a, b):
    return a + b

print(add(2, 3) * 2)
```

**A3**
```python
def show(x):
    print(x)

y = show(7)
print(y)
```

**A4**
```python
def greet(name, message="Hi"):
    print(message, name)

greet("Ravi")
greet("Ravi", "Welcome")
greet(message="Bye", name="Ravi")
```

**A5**
```python
def first():
    return 1
    return 2

print(first())
```

**A6**
```python
def make():
    secret = 42
    return secret

make()
print(secret)
```

**A7**
```python
total = 100

def show_total():
    print(total)

show_total()
```

**A8**
```python
triple = lambda x: x * 3
print(triple(4) + 1)
```

**A9**
```python
def area(length, width=1):
    return length * width

print(area(5), area(5, 2), area(width=3, length=2))
```

**A10**
```python
def greet(name):
    print("Hello", name)

greet()
```

## Part B · Write the program

**B1. Temperature.** Write `to_fahrenheit(celsius)` that returns the Fahrenheit value (`celsius * 9 / 5 + 32`). Print it for 0, 37 and 100.

**B2. Absolute value.** Write `absolute(n)` that returns `n` without its sign, without using `abs`. Test with 5, −5 and 0.

**B3. Repeat a message.** Write `repeat(message, times=3)` that prints the message that many times. Call it with the default and with 5.

**B4. Password strength.** Write `is_strong(password)` that returns True when the password has at least 8 characters and is not `"password"`. Use `len(password)` for the length. Print the result for `"chai1234"` and `"abc"`.

**B5. Loan check.** Write `can_borrow(salary, emi)` that returns True when the EMI is at most 40% of the salary. Write `max_emi(salary)` that returns 40% of the salary in whole rupees. Use the second inside the first.

**B6. Fix the bugs.** This program should print `Cashback: 50`. It has three mistakes. Find and fix each one, and write what went wrong.

```python
def cashback(amount, rate=5)
    result = amount * rate // 100
    print(result)

value = cashback(1000)
print("Cashback:", value)
```

## Part C · Project: grow PaisaPay v5

Start from [`code/paisapay_v5.py`](code/paisapay_v5.py).

1. **A refund function.** Add `refund(balance, amount)` that checks the amount with `is_valid_amount`, prints `Refunded ₹ <amount>` and returns the new balance. Add menu choice 5, `Refund`, that calls it. Keep choice 4 as Exit.
2. **Cashback only on UPI.** Change `cashback_for` to take a second parameter `mode`, and return 0 for anything that is not `"upi"`. Give `mode` a default of `"upi"` so the old calls still work.
3. **A receipt function.** Move the two `print` lines inside `pay` into `print_receipt(payee, amount, mode, fee, cashback)` and call it from `pay`. Nothing else should change.

Target output for one run (balance ₹1000, PIN 4321):

```text
1. Pay   2. Balance   3. Add money   4. Exit   5. Refund
Choose: 1
Pay to: Aakash
Amount in rupees: 600
Mode (upi / card / netbanking): card
UPI PIN: 4321
Paid ₹ 600 to Aakash via Card
Fee ₹ 5 | Cashback ₹ 0
1. Pay   2. Balance   3. Add money   4. Exit   5. Refund
Choose: 5
Amount to refund: 100
Refunded ₹ 100
1. Pay   2. Balance   3. Add money   4. Exit   5. Refund
Choose: 2
Balance: ₹ 495
```

## Part D · Think it through

Write two or three lines for each.

1. `show_balance` prints and `add_money` returns. Why not make both print, or both return?
2. Every function in PaisaPay v5 that refuses a payment still returns the balance. What would go wrong at the call site if it returned nothing?
3. The tool schema of an agent lists a name, parameters and a result. Map each of those to a line of `pay(balance, payee, amount, mode="upi")`.
4. When would you write a `lambda` instead of a `def`, and when is that a bad idea?

## With AI (after your own attempt)

Paste your finished Part C program into an AI assistant and ask:

> "For each function in this program, tell me its parameters, what it returns, and one input that makes it return early. Do not change the code."

Check every claim by calling the function yourself with that input. Note any function where the assistant described a return value that the code does not actually produce.
