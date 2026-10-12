# Assignment · Class 4

Practice for `for`, `range`, `while`, `break`, `continue`, `pass`, nested loops and the four loop patterns. Do Part A on paper first. Write Parts B and C yourself before asking any AI assistant. For more coding problems with solutions, see [`PRACTICE.md`](PRACTICE.md).

Run your programs in [PyLens](https://scaler-pylens.vercel.app/) or with `python3 filename.py`.

## Part A · Predict the output (no running)

Write down what each snippet prints, or which error it raises, or whether it ever ends. Then run it and compare.

**A1**
```python
for i in range(3):
    print("Cashback sent")
print("All done")
```

**A2**
```python
for i in range(1, 10, 3):
    print(i)
```

**A3**
```python
for sec in range(5, 0):
    print(sec)
print("Expired")
```

**A4**
```python
balance = 1000
while balance >= 400:
    balance -= 400
print(balance)
```

**A5**
```python
for i in range(1, 6):
    if i == 4:
        break
    print(i)
print("Done")
```

**A6**
```python
for i in range(1, 6):
    if i % 2 == 0:
        continue
    print(i)
```

**A7**
```python
count = 0
while count < 3:
    print(count)
```

**A8**
```python
for row in range(2):
    for col in range(3):
        print(row, col)
```

**A9**
```python
total = 0
for amount in [100, 200, 300]:
    total += amount
print(total)
```

**A10**
```python
payees = ["Chai Point", "Zomato"]
for payee in payees:
    print(payee)
print(payee)
```

## Part B · Write the program

**B1. Countdown.** Print 10 down to 1, then `Go!`.

**B2. Squares table.** Print `1 squared is 1` up to `10 squared is 100`.

**B3. Total of n amounts.** Ask how many amounts, then ask for each one. Print the total and the largest.

**B4. Password with a limit.** The saved password is `python`. Give the user three attempts with a `while` loop and a counter. Print `Welcome` or `Locked out`.

**B5. Coin triangle.** Ask for a height and print a triangle of `₹` symbols: one on the first row, two on the second, and so on.

**B6. Fix the bugs.** This program should print the numbers 1 to 10 that are not multiples of 4. It has three mistakes. Find and fix each one, and write what went wrong.

```python
for i in range(1, 10):
    if i % 4 == 0:
        break
    print(i)
print("Done)
```

## Part C · Project: grow PaisaPay v4

Start from [`code/paisapay_v4.py`](code/paisapay_v4.py).

1. **Add money.** Add menu choice 5, `Add money`. Ask for an amount, refuse anything above ₹10,000 or below ₹1, otherwise add it to the balance. Keep choice 4 as Exit.
2. **Daily limit.** Allow at most three successful payments per run. After the third, choice 1 prints `Daily limit reached` and does nothing else. Use the `count` that already exists.
3. **Smallest payment.** The mini statement already shows the biggest payment. Add the smallest. Think about its starting value: 0 will never be replaced. Start it at a large number, or set it on the first payment.

Target output for one run (balance ₹1000, PIN 4321):

```text
1. Pay   2. Balance   3. Mini statement   4. Exit   5. Add money
Choose: 5
Amount to add: 500
Added ₹ 500 | Balance: ₹ 1500
1. Pay   2. Balance   3. Mini statement   4. Exit   5. Add money
Choose: 1
Pay to: Prasad
Amount in rupees: 200
UPI PIN: 4321
Paid ₹ 200 to Prasad | Left ₹ 1300
1. Pay   2. Balance   3. Mini statement   4. Exit   5. Add money
Choose: 3
Count: 1 | Spent ₹ 200
Biggest ₹ 200 | Smallest ₹ 200
```

## Part D · Think it through

Write two or three lines for each.

1. The PIN loop uses `for attempt in range(3)` with a flag. A friend uses `while attempts < 3` instead. What extra line does the friend need, and what happens if they forget it?
2. `while balance != 0` with payments of ₹300 from ₹1000 never ends. Name two different conditions that would end it, and say which one a real bank would use.
3. Why must `total = 0` sit above the loop and not inside it? Explain with a three-item example.
4. An agent loop is `while not done`. What could make `done` never become True, and what would you add to protect against it?

## With AI (after your own attempt)

Paste your Part C program into an AI assistant and ask:

> "Find every way this loop could run for ever or stop early by mistake. Do not change the code. List the inputs that trigger each case."

Run every input it gives you. Record what happened, and note any case the assistant invented that cannot actually happen.
