# Assignment · Class 3

Practice for `if`, `else`, `elif`, `match`, conditions with `and` / `or` / `not`, nesting and the ternary operator. Do Part A on paper first. Write Parts B and C yourself before asking any AI assistant.

Run your programs in [PyLens](https://scaler-pylens.vercel.app/) or with `python3 filename.py`.

## Part A · Predict the output (no running)

Write down what each snippet prints, or which error it raises. Then run it and compare.

**A1**
```python
balance = 750
if balance >= 500:
    print("Gold")
print("Thanks")
```

**A2**
```python
amount = 3000
if amount >= 500:
    print("Tier 1")
elif amount >= 2000:
    print("Tier 2")
elif amount >= 5000:
    print("Tier 3")
```

**A3**
```python
amount = 3000
if amount >= 500:
    print("Tier 1")
if amount >= 2000:
    print("Tier 2")
```

**A4**
```python
pin_ok = False
balance = 9000
if pin_ok:
    if balance >= 100:
        print("Paid")
else:
    print("Wrong PIN")
```

**A5**
```python
mode = "Card"
match mode:
    case "card":
        print("Enter PIN")
    case _:
        print("Unknown")
```

**A6**
```python
is_frozen = False
amount = 200
print("Allowed" if not is_frozen and amount <= 500 else "Blocked")
```

**A7**
```python
city = "Pune"
if city == "Pune" or "Mumbai":
    print("Metro")
else:
    print("Other")
```

**A8**
```python
x = 10
if x > 5:
print("big")
```

## Part B · Write the program

**B1. Pass or fail.** Ask for a score. Print `You passed!` for 40 or more, otherwise `You failed.`

**B2. Grades.** Ask for a score and print the grade: 90 or more A, 80 or more B, 70 or more C, 60 or more D, otherwise F. Test with 95, 85, 60 and 59.

**B3. Traffic light.** Ask for a colour and use `match` to print `Stop` for red, `Get ready` for yellow, `Go` for green, and `Invalid colour` for anything else.

**B4. Even or odd, in words.** Ask for a whole number and print `Even` or `Odd`. Then write the same program in one line with a ternary expression.

**B5. ATM withdrawal.** Ask for the amount. Refuse it with a clear message if it is not a multiple of ₹100, or if it is more than ₹10,000, or if it is more than the balance of ₹8,500. Otherwise print the new balance. Decide the order of the checks and explain it in a comment.

**B6. Fix the bugs.** This program should print the cashback tier. It has four mistakes. Find and fix each one, and write what went wrong.

```python
amount = input("Amount: ")
if amount >= 500
    print("Tier 1")
elif amount >= 2000:
print("Tier 2")
elif amount = 5000:
    print("Tier 3")
```

## Part C · Project: grow PaisaPay v3

Start from [`code/paisapay_v3.py`](code/paisapay_v3.py).

1. **Daily limit.** UPI allows at most ₹1,00,000 per payment. Refuse anything above it, with its own message, before the balance check.
2. **Cashback only on UPI.** Cashback applies when the mode is UPI. For card and net banking the cashback is ₹0. Use the `mode_text` that the `match` already produced.
3. **A different tone for big payments.** If the amount is ₹5,000 or more, print an extra line: `Big payment. Please check the details.` Use a ternary for the status line: `status = "BIG" if amount >= 5000 else "NORMAL"`.

Target output for one run:

```text
Welcome to PaisaPay
Your name: Parveen
Pay to: Zomato
Amount in rupees: 600
Mode (upi / card / netbanking): card
UPI PIN: 4321
----- Receipt -----
Paid: ₹ 600 to Zomato via Card
Cashback: ₹ 0
Status: NORMAL
Balance left: ₹ 398
```

## Part D · Think it through

Write two or three lines for each.

1. PaisaPay checks the PIN before the balance. Why is that a better order than balance first?
2. A friend fixes the ₹8,000 cashback bug by changing `elif` to `if`. What goes wrong now?
3. `if kyc == "yes"` rejects a user who typed `Yes`. What are two different ways to handle this, and which would you choose?
4. When would you refuse to use a ternary even though the decision has only two outcomes?

## With AI (after your own attempt)

Paste your finished Part C program into an AI assistant and ask:

> "List every path through the decisions in this program and one input that reaches each path. Do not change the code."

Run every input it gives you. Record the message each one prints, and note any path the assistant missed.
