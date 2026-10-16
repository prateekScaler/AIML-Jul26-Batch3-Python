# Assignment · Class 6

Practice for lists: indexing, slicing, the methods, loops over lists and comprehensions, plus the two Class 5 revisions. Do Part A on paper first. Write Parts B and C yourself before asking any AI assistant. For more coding problems with solutions, see [`PRACTICE.md`](PRACTICE.md).

Run your programs in [PyLens](https://scaler-pylens.vercel.app/) or with `python3 filename.py`.

## Part A · Predict the output (no running)

Write down what each snippet prints, or which error it raises. Then run it and compare.

**A1**
```python
fruits = ["Apple", "Banana", "Mango", "Orange"]
print(fruits[1], fruits[-1], len(fruits))
```

**A2**
```python
numbers = [10, 20, 30, 40, 50]
print(numbers[1:3])
print(numbers[3:])
```

**A3**
```python
numbers = [10, 20, 30]
numbers.append(40)
numbers.insert(0, 5)
print(numbers)
```

**A4**
```python
numbers = [30, 10, 20]
result = numbers.sort()
print(result)
print(numbers)
```

**A5**
```python
a = [1, 2, 3]
b = a
b.append(4)
print(len(a))
```

**A6**
```python
names = ["Uma", "Akash"]
print(names[2])
```

**A7**
```python
scores = [35, 72, 45]
passing = [s for s in scores if s >= 40]
print(passing, scores)
```

**A8**
```python
queue = ["Vinit", "Prince", "Ravi"]
first = queue.pop(0)
print(first, queue)
```

**A9**
```python
total = 100

def spend(amount):
    total = total - amount

spend(30)
print(total)
```

**A10**
```python
def book(seat, meal="veg"):
    print(seat, meal)

book(12)
book(meal="jain", seat=14)
```

## Part B · Write the program

**B1. Reverse without a slice.** Given `[1, 2, 3, 4, 5]`, build the reversed list with a loop and `insert(0, ...)`. Then check your answer with `[::-1]`.

**B2. Count the matches.** Given `["upi", "card", "upi", "netbanking", "upi"]`, count how many payments were by UPI using a loop. Then do it again with `len` and a comprehension.

**B3. Only the new ones.** Given `payees = ["Chai Point", "Zomato"]` and `new = ["Zomato", "Jio", "Chai Point", "Uber"]`, append to `payees` only the names it does not already have. Print the result.

**B4. Every second payment.** Given `[600, 300, 1500, 250, 90, 2000]`, print the payments at even positions (0, 2, 4) with a slice, and the payments at odd positions with another slice.

**B5. Running balance.** Start with balance ₹1,000 and `payments = [250, 400, 150]`. Build a list of the balance after each payment.

**B6. Fix the bugs.** This program should print the three largest scores in descending order. It has three mistakes. Find and fix each one, and write what went wrong.

```python
scores = [45, 90, 72, 88, 60]
top = scores.sort(reverse=True)
print(top[0:3])
print(scores[5])
```

## Part C · Project: grow PaisaPay v6

Start from [`code/paisapay_v6.py`](code/paisapay_v6.py).

1. **Payees too.** Add a second list, `payees`, that `pay` appends to alongside `history`. In the mini statement print the last five payees.
2. **Undo the last payment.** Add menu choice 6, `Undo`. It takes the last amount out of `history` with `pop()`, adds it back to the balance, removes the last payee, and prints `Undone ₹ <amount>`. If there is nothing to undo, say so.
3. **Smallest payment.** Add the smallest payment to the mini statement using `sorted`.

Target output for one run (balance ₹1000, PIN 4321, after paying ₹600 to Chai Point and ₹250 to Zomato by UPI):

```text
1. Pay  2. Balance  3. Statement  4. Exit  5. Add money  6. Undo
Choose: 3
Payments: 2 | Spent ₹ 850
Biggest ₹ 600 | Smallest ₹ 250
Last five: [600, 250]
Last five payees: ['Chai Point', 'Zomato']
Big payments: [600]
1. Pay  2. Balance  3. Statement  4. Exit  5. Add money  6. Undo
Choose: 6
Undone ₹ 250
1. Pay  2. Balance  3. Statement  4. Exit  5. Add money  6. Undo
Choose: 2
Balance: ₹ 410
```

## Part D · Think it through

Write two or three lines for each.

1. `pay` changes `history` without returning it, but must return the balance. Why the difference?
2. `history[-5:]` on a list of two payments gives two items, not an error. Why is that convenient for the mini statement?
3. An agent keeps the conversation so far as a list of messages and sends the last few to the model. Which list tool is that, and what could go wrong if the list never gets shorter?
4. When would you choose a loop over a comprehension even though the comprehension is shorter?

## With AI (after your own attempt)

Paste your finished Part C program into an AI assistant and ask:

> "List every line that changes a list in place and every line that builds a new list. For each one, say what the list looks like after that line, assuming the sample run above. Do not change the code."

Check each claim by tracing the list yourself. Note any line where the assistant confused an in-place change with a new list.
