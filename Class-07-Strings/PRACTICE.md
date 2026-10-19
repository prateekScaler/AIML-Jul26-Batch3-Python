# Practice problems · Class 7 · Strings

Twelve problems, easy to hard. Each uses only what Classes 1 to 7 covered. Write every program yourself in [PyLens](https://scaler-pylens.vercel.app/) or with `python3`, run it against the sample, and only then open the hint or the solution.

How to work: when a method "does nothing", check whether you stored its result. String methods never change the string; they hand back a new one.

- [Revision: short forms](#revision-short-forms) · problems R1 to R4
- [Warm-up](#warm-up) · problems 1 to 4
- [Core](#core) · problems 5 to 9
- [Challenge](#challenge) · problems 10 to 12

---

## Revision: short forms

One problem for each short form revised at the start of the class. Write the long form first if you need to, then the short form, and check that both print the same thing.

### R1. Ternary: the fee label

Ask for an amount. Print `Fee ₹5` when the amount is more than ₹2,000, otherwise `No fee`, using one ternary inside the print.

```text
Amount: 2500
Fee ₹5
```

<details><summary>Solution</summary>

```python
amount = int(input("Amount: "))
print("Fee ₹5" if amount > 2000 else "No fee")
```
</details>

### R2. For over a list: reminders

Given `payees = ["Chai Point", "Zomato", "Jio"]`, print one reminder line per payee with the payee's name in capitals, using `for payee in payees`, no index.

```text
Reminder: CHAI POINT
Reminder: ZOMATO
Reminder: JIO
```

<details><summary>Solution</summary>

```python
payees = ["Chai Point", "Zomato", "Jio"]
for payee in payees:
    print("Reminder:", payee.upper())
```
</details>

### R3. Comprehension: clean the answers

An LLM returned `answers = [" Yes", "no ", "YES", " maybe "]`. In one comprehension, build a list of the answers stripped and lower-cased, then a second one that keeps only the ones equal to `"yes"`. Print both.

```text
['yes', 'no', 'yes', 'maybe']
['yes', 'yes']
```

<details><summary>Hint</summary>

Make, from, keep: `[a.strip().lower() for a in answers]`, then add `if a.strip().lower() == "yes"` to the second one.
</details>

<details><summary>Solution</summary>

```python
answers = [" Yes", "no ", "YES", " maybe "]
clean = [a.strip().lower() for a in answers]
yes_only = [a for a in clean if a == "yes"]
print(clean)
print(yes_only)
```
</details>

### R4. Lambda: a one-line rule

Write `is_big` as a lambda that is True for amounts of ₹1,000 or more. Use it in a comprehension to keep the big amounts from `[600, 1500, 300, 2500]`.

```text
True False
[1500, 2500]
```

<details><summary>Solution</summary>

```python
is_big = lambda amount: amount >= 1000
print(is_big(1500), is_big(600))
print([a for a in [600, 1500, 300, 2500] if is_big(a)])
```
</details>

---

## Warm-up

### 1. First, last, length

Ask for a word and print its first character, its last character and its length.

```text
Word: PaisaPay
P y 8
```

<details><summary>Solution</summary>

```python
word = input("Word: ")
print(word[0], word[-1], len(word))
```
</details>

### 2. Shout and whisper

Ask for a sentence. Print it in capitals, then in lower case, then in title case.

```text
Sentence: welcome to paisaPay
WELCOME TO PAISAPAY
welcome to paisapay
Welcome To Paisapay
```

<details><summary>Solution</summary>

```python
sentence = input("Sentence: ")
print(sentence.upper())
print(sentence.lower())
print(sentence.title())
```
</details>

### 3. Reverse it

Ask for a word and print it backwards. Then print whether the word reads the same both ways.

```text
Word: level
level
Same both ways: True
```

<details><summary>Hint</summary>

`word[::-1]` reverses. Compare it with the original using `==`.
</details>

<details><summary>Solution</summary>

```python
word = input("Word: ")
backwards = word[::-1]
print(backwards)
print("Same both ways:", word == backwards)
```
</details>

### 4. Clean the name

Ask for a name. Remove the spaces at both ends, make it title case, and greet with an f-string.

```text
Name:    vinit dave
Hello, Vinit Dave!
```

<details><summary>Solution</summary>

```python
name = input("Name: ").strip().title()
print(f"Hello, {name}!")
```
</details>

---

## Core

### 5. Mask the card

Ask for a 16-digit card number, typed with or without spaces. Print it masked, showing only the last four digits.

```text
Card: 4111 2222 3333 4444
**** **** **** 4444
```

<details><summary>Hint</summary>

Remove the spaces first with `replace(" ", "")`, then slice the last four with `[-4:]`.
</details>

<details><summary>Solution</summary>

```python
card = input("Card: ").replace(" ", "")
print("**** **** **** " + card[-4:])
```
</details>

### 6. Split the UPI ID

Ask for a UPI ID such as `prince@okaxis`. Print the user part and the bank part on separate lines. If there is no `@`, print `Not a UPI ID`.

```text
UPI ID: prince@okaxis
User: prince
Bank: okaxis
```

<details><summary>Solution</summary>

```python
upi_id = input("UPI ID: ").strip()
if "@" in upi_id:
    parts = upi_id.split("@")
    print("User:", parts[0])
    print("Bank:", parts[1])
else:
    print("Not a UPI ID")
```
</details>

### 7. Count the words and the vowels

Ask for a sentence. Print how many words it has and how many vowels.

```text
Sentence: Python is easy to learn
Words: 5
Vowels: 7
```

<details><summary>Hint</summary>

`len(sentence.split())` for the words. A loop over `sentence.lower()` with `if character in "aeiou"` for the vowels.
</details>

<details><summary>Solution</summary>

```python
sentence = input("Sentence: ")
words = len(sentence.split())

vowels = 0
for character in sentence.lower():
    if character in "aeiou":
        vowels += 1

print("Words:", words)
print("Vowels:", vowels)
```
</details>

### 8. Receipt line

Ask for a payee, an amount and a mode. Print one receipt line with an f-string, with the payee in title case and the mode in capitals.

```text
Payee: chai point
Amount: 120
Mode: upi
Paid ₹120 to Chai Point via UPI
```

<details><summary>Solution</summary>

```python
payee = input("Payee: ").strip().title()
amount = int(input("Amount: "))
mode = input("Mode: ").strip().upper()
print(f"Paid ₹{amount} to {payee} via {mode}")
```
</details>

### 9. Read the bank SMS

Given `sms = "Rs 600 debited from A/c XX4444 via UPI on 16-10"`, pull out the amount and the last four digits of the account using `split()` and indexing. Print them.

```text
Amount: 600
Account: 4444
```

<details><summary>Hint</summary>

`sms.split()` gives a list of words. The amount is word 1. The account word is `XX4444`; slice its last four characters.
</details>

<details><summary>Solution</summary>

```python
sms = "Rs 600 debited from A/c XX4444 via UPI on 16-10"
words = sms.split()
amount = words[1]
account = words[5][-4:]
print("Amount:", amount)
print("Account:", account)
```
</details>

---

## Challenge

### 10. Initials

Ask for a full name with two or more words and print the initials in capitals, separated by dots.

```text
Name: uma maheswari
U.M.
```

<details><summary>Hint</summary>

Split into words, take `word[0].upper()` from each with a loop, and `".".join(...)` the list, then add a final dot.
</details>

<details><summary>Solution</summary>

```python
name = input("Name: ").strip()
initials = []
for word in name.split():
    initials.append(word[0].upper())
print(".".join(initials) + ".")
```
</details>

### 11. Hide the middle

Ask for a UPI ID and print it with the user part masked except for its first and last character, and the bank part unchanged.

```text
UPI ID: parvatha@okaxis
p******a@okaxis
```

<details><summary>Hint</summary>

Split at `@`. For the user part, the hidden length is `len(user) - 2`. Build the stars with a loop that appends `"*"` to a string, or with `"*" * count`.
</details>

<details><summary>Solution</summary>

```python
upi_id = input("UPI ID: ").strip()
user, bank = upi_id.split("@")

stars = ""
for i in range(len(user) - 2):
    stars += "*"

print(user[0] + stars + user[-1] + "@" + bank)
```
</details>

### 12. Predict, then run

Without running, write down what each line prints or which error it raises. Then run and compare.

```python
word = "Python"
print(word[-3:])
print(word.replace("P", "J").lower())
print(word.find("z"))
print("a,b,,c".split(","))
print(len("  hi  ".strip()))
print(f"{7 / 2:.1f}")
s = "hello"
s.upper()
print(s)
print("x" in "example", "X" in "example")
word[0] = "J"
```

<details><summary>Answer</summary>

```text
hon
jython
-1
['a', 'b', '', 'c']
2
3.5
hello
True False
TypeError: 'str' object does not support item assignment
```

Two commas next to each other give an empty string in the middle. `s.upper()` built a new string that nothing kept. The last line stops the program: strings cannot be changed in place.
</details>

---

Finished all twelve? Rewrite problem 11 so it also works when the user part has only one or two characters, without crashing.
