# Practice problems · Class 9 · Problem Solving: Python Foundations

Six problems that use Classes 1 to 8, easy to hard. The first and the fifth were started in class. Write every program yourself in [PyLens](https://scaler-pylens.vercel.app/) or with `python3`, run it against the sample, and only then open the hint or the solution.

How to work: read the whole task, name the structures you need (a list, a set, a dictionary, a tuple), write the input lines first, and test with the sample before adding the bonus parts.

- [1. Smart bill splitter](#1-smart-bill-splitter) · Classes 1, 2 · easy
- [2. Movie ticket pricing engine](#2-movie-ticket-pricing-engine) · Classes 2, 3 · easy to medium
- [3. Pattern printing and prime hunter](#3-pattern-printing-and-prime-hunter) · Class 4 · medium
- [4. Password strength validator](#4-password-strength-validator) · Classes 5, 7 · medium
- [5. Text cleaner and analyzer](#5-text-cleaner-and-analyzer) · Classes 6, 7 · medium
- [6. Mini library management system](#6-mini-library-management-system) · Classes 1 to 8 · hard

---

## 1. Smart bill splitter

Ask for a customer name, the total bill (a float), a tip percentage (an int) and the number of people sharing. Print the tip amount, the grand total, the amount each person pays rounded to two decimals, and whether each person pays more than 500, as a bool. Convert every input on purpose, use f-strings, and comment each step.

```text
Name: Sathvik
Bill: 2400
Tip: 10
People: 4
Hello Sathvik! Here is your bill summary:
Tip amount: 240.0
Grand total: 2640.0
Each person pays: 660.0
Pays more than 500? True
```

<details><summary>Hint</summary>

`float(input(...))` for the bill, `int(input(...))` for the tip and the people. `round(value, 2)` for two decimals. `each > 500` is already a bool.
</details>

<details><summary>Solution</summary>

```python
name = input("Name: ")                      # text stays text
bill = float(input("Bill: "))               # rupees can have paise
tip_percent = int(input("Tip: "))           # a whole-number percentage
people = int(input("People: "))

tip = bill * tip_percent / 100              # percentage maths
grand_total = bill + tip
each = round(grand_total / people, 2)       # two decimal places

print(f"Hello {name}! Here is your bill summary:")
print(f"Tip amount: {tip}")
print(f"Grand total: {grand_total}")
print(f"Each person pays: {each}")
print(f"Pays more than 500? {each > 500}")  # a comparison is a bool
```
</details>

## 2. Movie ticket pricing engine

A cinema prices tickets with these rules. The base price is 300. Under 5, free. 5 to 12, 50% off. 60 and above, 40% off. Everyone else pays full price. On a weekend (the user types yes or no), add a 20% surcharge on the price after the age discount. A member (yes or no) whose final price is above 200 gets a flat 25 off. Take the age, the weekend answer and the member answer, and print the final price.

Bonus: write the weekend check as a ternary, and refuse a negative age or an answer other than yes or no with a message.

| Age | Weekend | Member | Price |
|---|---|---|---|
| 4 | yes | yes | 0 |
| 10 | no | no | 150 |
| 65 | yes | yes | 191 |
| 30 | yes | yes | 335 |

```text
Age: 65
Weekend (yes/no): yes
Member (yes/no): yes
Ticket price: 191
```

<details><summary>Hint</summary>

Work in order: age discount, then the weekend surcharge on the discounted price, then the member discount on the result. Whole-rupee maths with `//` keeps everything an int: 300 → 180 → 216 → 191.
</details>

<details><summary>Solution</summary>

```python
age = int(input("Age: "))
is_weekend = input("Weekend (yes/no): ").strip().lower()
is_member = input("Member (yes/no): ").strip().lower()

if age < 0 or is_weekend not in ("yes", "no") or is_member not in ("yes", "no"):
    print("Invalid input.")
else:
    price = 300
    if age < 5:
        price = 0
    elif age <= 12:
        price = price * 50 // 100
    elif age >= 60:
        price = price * 60 // 100

    price = price + price * 20 // 100 if is_weekend == "yes" else price   # ternary

    if is_member == "yes" and price > 200:
        price = price - 25

    print(f"Ticket price: {price}")
```
</details>

## 3. Pattern printing and prime hunter

**(a)** Take a number n and print a right-aligned pyramid of numbers, for n = 5:

```text
        1
      1 2
    1 2 3
  1 2 3 4
1 2 3 4 5
```

**(b)** Take a start and an end and print every prime number in that range. Use a nested loop, `break` as soon as a divisor is found, `continue` to skip numbers below 2, and print the count at the end.

**(c)** With a `while` loop, take numbers until the user enters 0, then print their sum and average (the 0 excluded).

```text
start: 10
end: 30
11 13 17 19 23 29
Primes found: 6
Number (0 to stop): 4
Number (0 to stop): 8
Number (0 to stop): 0
Sum 12, average 6.0
```

<details><summary>Hint</summary>

(a) Row `r` of `n` needs `n - r` gaps of two spaces, then the numbers 1 to r. (b) A number is prime when no divisor from 2 up to itself divides it; `for ... else` is not needed, a flag works. (c) `while True` with `break` on 0; count the numbers so the average divides by the right amount.
</details>

<details><summary>Solution</summary>

```python
# (a) a right-aligned pyramid
n = int(input("n: "))
for row in range(1, n + 1):
    spaces = "  " * (n - row)
    numbers = ""
    for k in range(1, row + 1):
        numbers += str(k) + " "
    print(spaces + numbers.rstrip())

# (b) primes in a range
start = int(input("start: "))
end = int(input("end: "))
count = 0
for number in range(start, end + 1):
    if number < 2:
        continue
    is_prime = True
    for divisor in range(2, number):
        if number % divisor == 0:
            is_prime = False
            break
    if is_prime:
        print(number, end=" ")
        count += 1
print()
print("Primes found:", count)

# (c) numbers until 0
total = 0
entered = 0
while True:
    value = int(input("Number (0 to stop): "))
    if value == 0:
        break
    total += value
    entered += 1
if entered > 0:
    print(f"Sum {total}, average {total / entered}")
else:
    print("No numbers entered.")
```
</details>

## 4. Password strength validator

Write `validate_password(password, min_length=8, require_special=True)` that returns a tuple `(is_strong, issues)`: a bool and a list of what is missing. Rules: at least `min_length` characters; at least one uppercase letter, one lowercase letter and one digit; when `require_special` is True, at least one of `!@#$%^&*`; no spaces.

Then call it with positional arguments, with keyword arguments, and with only the defaults. Write a second function that takes a list of passwords and prints a report line for each, such as `Pass1234! -> STRONG` or `abc -> WEAK: too short, no uppercase, no digit, no special character`. Sort the passwords by length, longest first, with `sorted` and a lambda key (a preview of Class 9). In a comment, say what happens when a function assigns to a global variable without the `global` keyword.

```text
(True, [])
(False, ['too short', 'no uppercase', 'no digit'])
(False, ['too short'])
Pass1234! -> STRONG
abc -> WEAK: too short, no uppercase, no digit, no special character
no spaces here 1A! -> WEAK: has a space
['no spaces here 1A!', 'Pass1234!', 'abc']
```

<details><summary>Hint</summary>

Loop over the characters once with four flags: `ch.isupper()`, `ch.islower()`, `ch.isdigit()`, `ch in "!@#$%^&*"`. Build the `issues` list as you go. `return len(issues) == 0, issues` packs the tuple.
</details>

<details><summary>Solution</summary>

```python
def validate_password(password, min_length=8, require_special=True):
    issues = []
    if len(password) < min_length:
        issues.append("too short")
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    for ch in password:
        if ch.isupper():
            has_upper = True
        if ch.islower():
            has_lower = True
        if ch.isdigit():
            has_digit = True
        if ch in "!@#$%^&*":
            has_special = True
    if not has_upper:
        issues.append("no uppercase")
    if not has_lower:
        issues.append("no lowercase")
    if not has_digit:
        issues.append("no digit")
    if require_special and not has_special:
        issues.append("no special character")
    if " " in password:
        issues.append("has a space")
    return len(issues) == 0, issues          # two values: a tuple

def report(passwords):
    for password in passwords:
        is_strong, issues = validate_password(password)
        if is_strong:
            print(f"{password} -> STRONG")
        else:
            print(f"{password} -> WEAK: {', '.join(issues)}")

print(validate_password("Pass1234!"))                        # positional
print(validate_password("abc", min_length=4, require_special=False))   # keyword
print(validate_password("Short1!"))                          # defaults

report(["Pass1234!", "abc", "no spaces here 1A!"])

# sorted with a lambda key: longest first (a preview of Class 9)
by_length = sorted(["Pass1234!", "abc", "no spaces here 1A!"], key=lambda p: len(p), reverse=True)
print(by_length)

# Reading a global inside a function works. Assigning to it without the
# global keyword makes a new local variable instead, and the global is unchanged.
```
</details>

## 5. Text cleaner and analyzer

Start from this text:

```python
text = "  Python is simple. python is POWERFUL! Learning Python for AI is fun, and AI needs Python.  "
```

Strip the outer spaces and lower-case it. Remove the punctuation `.` `,` `!` with `replace`. Split into words. With a comprehension, make the list of words longer than three characters, and the list of word lengths. Find the longest and the shortest word. Build the list of unique words in the order they first appeared, without a set. Print the cleaned sentence in title case. Write a small helper that says whether a word is a palindrome and test the first and the last word. Print the sentence reversed word by word.

```text
['python', 'is', 'simple', 'python', 'is', 'powerful', 'learning', 'python', 'for', 'ai', 'is', 'fun', 'and', 'ai', 'needs', 'python']
['python', 'simple', 'python', 'powerful', 'learning', 'python', 'needs', 'python']
[6, 2, 6, 6, 2, 8, 8, 6, 3, 2, 2, 3, 3, 2, 5, 6]
powerful is
['python', 'is', 'simple', 'powerful', 'learning', 'for', 'ai', 'fun', 'and', 'needs']
Python Is Simple Python Is Powerful Learning Python For Ai Is Fun And Ai Needs Python
False False
python needs ai and fun is ai for python learning powerful is python simple is python
```

<details><summary>Hint</summary>

Every string method returns a new string: `clean = clean.replace(".", "")` must be stored, which is why `replace` "needs reassignment". For first-seen order, append to a list only when the word is `not in` it. A word is a palindrome when `word == word[::-1]`.
</details>

<details><summary>Solution</summary>

```python
text = "  Python is simple. python is POWERFUL! Learning Python for AI is fun, and AI needs Python.  "

clean = text.strip().lower()                       # 1. outer spaces off, one case
clean = clean.replace(".", "").replace(",", "").replace("!", "")   # 2. no punctuation
words = clean.split()                              # 3. a list of words
print(words)

long_words = [w for w in words if len(w) > 3]     # 4. keep the long ones
print(long_words)

lengths = [len(w) for w in words]                  # 5. one number per word
print(lengths)

longest = words[0]                                 # 6. longest and shortest
shortest = words[0]
for w in words:
    if len(w) > len(longest):
        longest = w
    if len(w) < len(shortest):
        shortest = w
print(longest, shortest)

unique = []                                        # 7. unique, in first-seen order
for w in words:
    if w not in unique:
        unique.append(w)
print(unique)

print(clean.title())                               # 8. title case

def is_palindrome(word):                           # 9. first and last word
    return word == word[::-1]

print(is_palindrome(words[0]), is_palindrome(words[-1]))

print(" ".join(words[::-1]))                       # 10. reversed word by word
```
</details>

## 6. Mini library management system

Build a menu-driven program that manages a library stored as a dictionary of dictionaries:

```python
library = {
    "B101": {"title": "Python Basics", "author": "R. Rao", "copies": 3, "tags": {"python", "beginner"}},
    "B102": {"title": "Data Science 101", "author": "S. Iyer", "copies": 1, "tags": {"data", "python"}}
}
```

The menu, inside a `while` loop: add a book (id, title, author, copies and comma-separated tags, stored as a set); issue a book (reduce copies, or print `Not available` when there are none); return a book (increase copies); search by tag (print the titles of every book with that tag); show all books with f-strings; exit. One function per option. Check that the id exists before issuing or returning. `break` on exit, `continue` on an invalid choice.

Bonus: show the books sorted by copies available, with `sorted` and a lambda key.

```text
1 Add  2 Issue  3 Return  4 Search tag  5 Show all  6 Exit
Choose: 2
Id: b102
Issued Data Science 101. 0 left.

1 Add  2 Issue  3 Return  4 Search tag  5 Show all  6 Exit
Choose: 2
Id: b102
Not available

1 Add  2 Issue  3 Return  4 Search tag  5 Show all  6 Exit
Choose: 4
Tag: python
Python Basics
Data Science 101
```

<details><summary>Hint</summary>

Each book is a dictionary inside the big dictionary: `library[book_id]["copies"] -= 1` changes the copies in place. Tags: `set(input(...).lower().replace(" ", "").split(","))`. The search loops over `library.values()` and tests `tag in book["tags"]`.
</details>

<details><summary>Solution</summary>

```python
library = {
    "B101": {"title": "Python Basics", "author": "R. Rao", "copies": 3, "tags": {"python", "beginner"}},
    "B102": {"title": "Data Science 101", "author": "S. Iyer", "copies": 1, "tags": {"data", "python"}}
}

def add_book():
    book_id = input("Id: ").strip().upper()
    if book_id in library:
        print("That id already exists.")
        return
    title = input("Title: ").strip()
    author = input("Author: ").strip()
    copies = int(input("Copies: "))
    tags = set(input("Tags (comma separated): ").lower().replace(" ", "").split(","))
    library[book_id] = {"title": title, "author": author, "copies": copies, "tags": tags}
    print(f"Added {title}.")

def issue_book():
    book_id = input("Id: ").strip().upper()
    if book_id not in library:
        print("No such book.")
        return
    book = library[book_id]
    if book["copies"] == 0:
        print("Not available")
        return
    book["copies"] -= 1
    print(f"Issued {book['title']}. {book['copies']} left.")

def return_book():
    book_id = input("Id: ").strip().upper()
    if book_id not in library:
        print("No such book.")
        return
    library[book_id]["copies"] += 1
    print(f"Returned {library[book_id]['title']}.")

def search_by_tag():
    tag = input("Tag: ").strip().lower()
    found = False
    for book in library.values():
        if tag in book["tags"]:
            print(book["title"])
            found = True
    if not found:
        print("No book has that tag.")

def show_all():
    for book_id, book in library.items():
        print(f"{book_id}  {book['title']} by {book['author']}  copies: {book['copies']}  tags: {sorted(book['tags'])}")

while True:
    print()
    print("1 Add  2 Issue  3 Return  4 Search tag  5 Show all  6 Exit")
    choice = input("Choose: ").strip()
    if choice == "1":
        add_book()
    elif choice == "2":
        issue_book()
    elif choice == "3":
        return_book()
    elif choice == "4":
        search_by_tag()
    elif choice == "5":
        show_all()
    elif choice == "6":
        break
    else:
        print("Unknown choice.")
        continue

print("Bye.")
```

Bonus: `for book_id, book in sorted(library.items(), key=lambda pair: pair[1]["copies"]):` shows the books with the fewest copies first.
</details>

---

## Homework: predict first, then run

Write the answer before you run it.

```python
print({1, 2, 3} & {2, 3, 4}, {1, 2, 3} - {2, 3, 4})
```

<details><summary>Answer</summary>

`{2, 3} {1}`. `&` keeps what is in both sets. `-` keeps what is in the first set only.

| Operator | Keeps | `{1, 2, 3}` and `{2, 3, 4}` |
|---|---|---|
| `a \| b` (pipe, "or") | everything in either | `{1, 2, 3, 4}` |
| `a & b` (ampersand, "and") | only what is in both | `{2, 3}` |
| `a - b` (minus) | the first without the second | `{1}` |
| `a ^ b` (caret) | in one, not both | `{1, 4}` |

Mixed in one line, `-` goes first, then `&`, then `^`, then `|`, so `a | b & c` is `a | (b & c)`. Do not rely on it: put brackets.
</details>

---

Finished all six? Add a seventh menu option to the library that prints how many different tags exist across all books, using one set.
