# Assignment · Class 7

Practice for strings: indexing, slicing, the methods, `split` and `join`, f-strings, escape characters and immutability. Do Part A on paper first. Write Parts B and C yourself before asking any AI assistant. For more coding problems with solutions, see [`PRACTICE.md`](PRACTICE.md).

Run your programs in [PyLens](https://scaler-pylens.vercel.app/) or with `python3 filename.py`.

## Part A · Predict the output (no running)

Write down what each snippet prints, or which error it raises. Then run it and compare.

**A1**
```python
word = "PaisaPay"
print(word[0], word[-1], word[5:], len(word))
```

**A2**
```python
text = "  Chai Point  "
print(text.strip().lower())
print(len(text))
```

**A3**
```python
s = "Mumbai"
s.upper()
print(s)
```

**A4**
```python
upi = "akash@okicici"
parts = upi.split("@")
print(parts[0].title(), len(parts))
```

**A5**
```python
amount = 450
fee = 2
print(f"Total ₹{amount + fee}")
print("Total ₹{amount + fee}")
```

**A6**
```python
print("a-b-c".replace("-", ""))
print("a-b-c".find("c"), "a-b-c".find("z"))
```

**A7**
```python
print("Rupees\tPaise")
print("Line 1\nLine 2")
```

**A8**
```python
word = "Python"
word[0] = "J"
print(word)
```

**A9**
```python
words = ["pay", "now"]
print("-".join(words), " ".join(words).title())
```

**A10**
```python
price = 2.5
print(f"{price * 3:.2f}", f"{price * 3}")
```

## Part B · Write the program

**B1. Count a letter.** Ask for a sentence and a letter. Print how many times the letter appears, ignoring case.

**B2. Email check.** Ask for an email address. Print `Looks like an email` only when it contains exactly one `@`, has something before it, and ends with `.com` or `.in`. Otherwise print `Not an email`.

**B3. Censor a word.** Given `message = "this offer is a scam, total scam"`, replace every `scam` with `****` and print the result. Then print the position of the first `scam` in the original.

**B4. Reverse each word.** Given `"Welcome to PaisaPay"`, print the sentence with each word reversed but the order of words kept: `emocleW ot yaPasiaP`. Use `split`, a loop, `[::-1]` and `join`.

**B5. Rupees in words, one digit at a time.** Ask for an amount as text, such as `405`. Print each digit's name on one line: `four zero five`. Use a loop over the string and an `if` / `elif` chain, or a list of names indexed by `int(digit)`.

**B6. Fix the bugs.** This program should print `Hello, Sangeeta!` for the input `  sangeeta  `. It has three mistakes. Find and fix each one, and write what went wrong.

```python
name = input("Name: ")
name.strip()
name = name.title
print("Hello, {name}!")
```

## Part C · Project: grow PaisaPay v7

Start from [`code/paisapay_v7.py`](code/paisapay_v7.py).

1. **Stricter UPI ID.** The bank part must be one of `okaxis`, `okicici`, `oksbi` or `ybl`. Keep the existing check and add this one. Refuse anything else with the message `Unknown bank handle '<handle>'`.
2. **Amount with commas.** Let the user type `1,500` for the amount. Remove the commas before `int()`.
3. **A formatted statement.** In `mini_statement`, print each of the last five amounts on its own line as `₹<amount>` right-aligned to 8 characters, using `f"{amount:>8}"`.

Target output for one run (balance ₹1000, PIN 4321):

```text
Choose: 1
Pay to (UPI ID): sangeeta@paytm
Amount in rupees: 1,500
Mode (upi / card / netbanking): upi
UPI PIN: 4321
Unknown bank handle 'paytm'
Choose: 1
Pay to (UPI ID): sangeeta@ybl
Amount in rupees: 600
Mode (upi / card / netbanking): upi
UPI PIN: 4321
Paid ₹600 to Sangeeta via UPI
Fee ₹0 | Cashback ₹10 | Balance ₹410
Choose: 3
Payments: 1 | Spent ₹600 | Biggest ₹600
Last five:
    ₹600
```

## Part D · Think it through

Write two or three lines for each.

1. Why does `clean()` lower-case the mode but `title()` the payee name? What would go wrong if both used `lower()`?
2. `text.upper()` on its own line is not an error. Why is that worse than an error?
3. An LLM returns `"The amount is 1,250 rupees."`. Write the steps, in words, to get the number 1250 out of it. Which string tools do you need?
4. `find` returns -1 when nothing is found. Why is `if text.find("x"):` a bug, and what should it be?

## With AI (after your own attempt)

Paste your finished Part C program into an AI assistant and ask:

> "List every place this program compares text. For each one, say what user input would wrongly fail the comparison, and whether the program cleans the input before comparing. Do not change the code."

Try each input it names. Note any comparison it claimed was unsafe that is actually cleaned.
