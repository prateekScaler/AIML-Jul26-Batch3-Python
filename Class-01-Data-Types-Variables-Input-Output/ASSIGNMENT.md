# Assignment · Class 1

Practice for data types, variables, input, output and type casting. Do Part A on paper first. Write Parts B and C yourself before asking any AI assistant.

Run your programs in [PyLens](https://scaler-pylens.vercel.app/) or with `python3 filename.py`.

## Part A · Predict the output (no running)

Write down what each snippet prints, or which error it raises. Then run it and compare.

**A1**
```python
print("10 + 20")
print(10 + 20)
```

**A2**
```python
city = "Pune"
print("city")
print(city)
```

**A3**
```python
points = 50
points = points + 25
points = points - 5
print(points)
```

**A4**
```python
x = 7
y = x
x = 100
print(y)
```

**A5**
```python
print(type("3.14"))
print(type(3.14))
print(type(3))
```

**A6**
```python
marks = input("Marks: ")   # the user types 80
print(marks + marks)
```

**A7**
```python
is_member = false
print(is_member)
```

**A8**
```python
print(int("12") + int("8"))
print("12" + "8")
```

## Part B · Write the program

**B1. Visiting card.** Ask for a name, a city and a favorite food. Print three lines:

```text
Name: Rashi
City: Indore
Loves: Poha
```

**B2. Ten years from now.** Ask for a name and an age. Print the age now, and the age ten years from now.

```text
Enter your name: Akshay
Enter your age: 22
Akshay is 22 now.
In ten years Akshay will be 32
```

**B3. Bill adder.** Ask for the prices of two items in whole rupees and print the total. Test with 100 and 50. If you see 10050, you know what to fix.

```text
Price of item 1: 100
Price of item 2: 50
Total: ₹ 150
```

**B4. Type detective.** Ask the user to type anything. Print what they typed and its type. Then convert it to an `int` and print the new type. Run it three times with `25`, `25.5` and `hello`, and note which runs crash and with which error.

**B5. Fix the bugs.** This program has four mistakes. Find and fix each one. Write the error type next to each fix.

```python
Print("Welcome to the canteen")
item = input("What would you like? )
price = input("Price in rupees: ")
total = price + 10        # ₹10 packing charge
print("You ordered", Item)
print("Total: ₹", total)
```

## Part C · Project: grow PaisaPay v1

Start from [`code/paisapay_v1.py`](code/paisapay_v1.py).

1. **Add a note.** Ask "Add a note: " and print it on the receipt as `Note: ...`.
2. **Add a convenience fee.** Every payment has a fixed fee of ₹2. Store it in a well-named variable. The receipt shows the amount, the fee and the total debited, and the balance drops by the total.
3. **Add a status line.** Create a `bool` variable for whether the payment succeeded and print it on the receipt.

Target output:

```text
Welcome to PaisaPay
Your name: Sangeeta
Pay to: Chai Point
Amount in rupees: 120
Add a note: evening chai
----- Receipt -----
From: Sangeeta
To: Chai Point
Note: evening chai
Paid: ₹ 120
Fee: ₹ 2
Total debited: ₹ 122
Balance left: ₹ 878
Successful: True
```

## Part D · Think it through

Write two or three lines for each.

1. Why is a phone number better stored as a `str` than as an `int`?
2. PaisaPay v1 stores the amount as an `int`. What happens when a user types `99.50`? Should the fix be `float(...)`? What did the class say about money and floats?
3. Pay ₹5000 from the ₹1000 wallet. What does the receipt show? What would the program need in order to refuse?

## With AI (after your own attempt)

Paste your finished Part C program into an AI assistant and ask:

> "List ten inputs a user could type that would crash this program or produce a wrong receipt. Do not fix the code."

Test every input yourself. For each one, record whether the assistant was right and which error type you saw.
