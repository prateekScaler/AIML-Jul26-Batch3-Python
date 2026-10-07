# Assignment · Class 2

Practice for input, type casting and operators. Do Part A on paper first. Write Parts B and C yourself before asking any AI assistant.

Run your programs in [PyLens](https://scaler-pylens.vercel.app/) or with `python3 filename.py`.

## Part A · Predict the output (no running)

Write down what each snippet prints. Then run it and compare.

**A1**
```python
print(17 / 5)
print(17 // 5)
print(17 % 5)
```

**A2**
```python
print(5 + 3 * 2 ** 2)
print((5 + 3) * 2 ** 2)
```

**A3**
```python
print(20 - 6 // 4)
```

**A4**
```python
balance = 500
balance -= 120
balance += 20
balance *= 2
print(balance)
```

**A5**
```python
print(8 % 2 == 0)
print(7 % 2 == 0)
```

**A6**
```python
age = 18
answer = "yes"
print(age >= 18 and answer == "yes")
```

**A7**
```python
print("paisa" == "Paisa")
print("@" in "amit@paisapay")
```

**A8**
```python
amount = "99.9"
print(int(float(amount)))
print(int(99.9))
print(str(250) + str(50))
```

**A9**
```python
a = input("First: ")     # the user types 12
b = input("Second: ")    # the user types 8
print(a + b)
print(int(a) + int(b))
```

## Part B · Write the program

**B1. Bill splitter.** Ask for the bill amount and the number of people, both whole numbers. Print each person's share and what is left over.

```text
Bill amount: 1000
Number of people: 3
Each pays: ₹ 333
Left over: ₹ 1
```

**B2. Even or odd.** Ask for a whole number. Print whether it is even, as `True` or `False`.

```text
Enter a number: 42
Is even: True
```

**B3. ATM check.** An ATM gives only ₹100 notes. Ask for an amount and print whether the ATM can give it.

```text
Amount to withdraw: 2550
Can dispense: False
```

**B4. Simple interest.** Ask for the principal, the rate in percent and the time in years. Print the interest, using `principal * rate * time / 100`.

```text
Principal: 1000
Rate (%): 7
Time (years): 2
Interest: ₹ 140.0
```

**B5. Loan eligibility.** A bank gives a loan only to people who are at least 21 and earn at least ₹25,000 a month. Ask for age and salary. Print the result as `True` or `False`.

```text
Enter your age: 23
Monthly salary: 30000
Eligible: True
```

**B6. Fix the bugs.** This program should print whether Praveen can pay. It has four mistakes. Find and fix each one, and write what went wrong.

```python
balance = 1000
amount = input("Amount: ")
fee == 2
total = amount + fee
balance =- total
can_pay = balance > 0 or balance = 0
print("Can pay:", can_pay)
```

## Part C · Project: grow PaisaPay v2

Start from [`code/paisapay_v2.py`](code/paisapay_v2.py).

1. **Add a tip.** Ask for a tip percentage. Compute the tip in whole rupees with `//` and add it to the total.
2. **Check the UPI ID.** Ask for the payee's UPI ID. Store whether it is valid: it must contain `@` and must not contain a space.
3. **Check the limit.** UPI allows at most ₹1,00,000 per payment. Store whether the amount is within the limit.
4. **One final answer.** Create `payment_ok`, which is True only when the balance is enough, the UPI ID is valid and the amount is within the limit. Print it on the receipt.

Target output for one run:

```text
Welcome to PaisaPay
Your name: Saurabh
Pay to (UPI ID): chaipoint@paisapay
Amount in rupees: 200
Tip percent: 10
Split between how many people? 2
----- Receipt -----
From: Saurabh
To: chaipoint@paisapay
Paid: ₹ 200 + tip ₹ 20 + fee ₹ 2
Cashback: ₹ 10
Each person owes: ₹ 100 | left over: ₹ 0
Valid UPI ID: True
Within limit: True
Enough balance: True
Payment OK: True
Balance left: ₹ 788
```

## Part D · Think it through

Write two or three lines for each.

1. PaisaPay computes cashback with `amount * 5 // 100`. What would change if it used `/`? Why does that matter for money?
2. Run PaisaPay v2 with an amount of 5000. It prints `Enough balance: False` and still pays. What is missing from the program?
3. A friend writes `if_valid = amount = 500` when they meant to check whether the amount is 500. What does that line actually do?
4. In `can_pay and is_valid or is_admin`, which part does Python evaluate first? Rewrite it with parentheses for each of the two possible meanings.

## With AI (after your own attempt)

Paste your finished Part C program into an AI assistant and ask:

> "Give me eight test inputs that cover every case of payment_ok, including boundary values. Do not change the code."

Run all eight yourself. For each one, record the value of `payment_ok` and whether it is what the rules say it should be.
