# Class 8 · Sets, Tuples, Dictionaries

PaisaPay v7 keeps a list of amounts. It cannot say who was paid, cannot count the different payees, and cannot look a payee up by name. Lists are flexible, and that flexibility is not always what a program needs. This class adds three structures, one for each job: the tuple, the set and the dictionary.

The class opens by finishing Class 7, which stopped at f-strings. Sections 0 to 5 are that material.

**By the end of this class you can:**

- Build a tuple, unpack it, and explain why it cannot change.
- Build a set, use `in`, `add`, `discard` and the four set operations, and write an empty set correctly.
- Build a dictionary, read it with square brackets and `get`, add and update keys, and loop over keys, values and items.
- Explain the silent overwrite: a key holds one value, and a second assignment replaces the first.
- Nest collections and read them from the outside in.
- Choose between a list, a tuple, a set and a dictionary from what the data must do.

## How to use this folder

| File | What it is |
|---|---|
| [`index.html`](index.html) | The interactive class page. [Open it here](https://prateekscaler.github.io/AIML-Jul26-Batch3-Python/Class-08-Sets-Tuples-Dictionaries/), no download needed. **Step by step** shows a little at a time (press → or Next). **Show everything** gives the whole class on one page. |
| [`code/`](code/) | Every example from the class as a runnable file, in order. |
| [`code/paisapay_v8.py`](code/paisapay_v8.py) | Today's version of our course project. |
| [`Python-Class-08-Sets-Tuples-Dictionaries.ipynb`](Python-Class-08-Sets-Tuples-Dictionaries.ipynb) | The same examples as one notebook. [Open it in Google Colab](https://colab.research.google.com/github/prateekScaler/AIML-Jul26-Batch3-Python/blob/main/Class-08-Sets-Tuples-Dictionaries/Python-Class-08-Sets-Tuples-Dictionaries.ipynb) and run the cells, nothing to install. |
| [`PRACTICE.md`](PRACTICE.md) | Twelve coding problems on tuples, sets and dictionaries, easy to hard, with sample output, hints and solutions. |
| [`ASSIGNMENT.md`](ASSIGNMENT.md) | Predict the output, write programs, grow PaisaPay, think it through. |
| [`INTERVIEW-READINESS.md`](INTERVIEW-READINESS.md) | Interview questions, gotchas and AI-era questions on today's topics. |

Run the code in [PyLens](https://scaler-pylens.vercel.app/), or on your own machine with `python3 filename.py` (Python 3.10 or newer, because PaisaPay uses `match`).

Official post-read for this class: https://scaler-content.github.io/python-Foundations-8/

---

## 0. Finishing Class 7: escape characters

A backslash makes the next character special: `\n` is a new line, `\t` a tab, `\"` and `\'` a quote inside the string, `\\` one backslash. `'It's a nice day'` is a `SyntaxError` because the string ends after `It`; write `"It's a nice day"` with the other quote, or `'It\'s a nice day'`. Which quote to use: Python does not care, the two only have to match. Text with an apostrophe goes in double quotes, text with double quotes inside goes in single quotes, and text with both needs a backslash before the clashing one. Most code uses double quotes by habit. `len("a\nb")` is 3: the new line is one character.

## 1. Finishing Class 7: strings cannot change

`word[0] = "J"` raises `TypeError: 'str' object does not support item assignment`. A string is immutable. To "change" it, build a new one: `word = "J" + word[1:]`.

That has a consequence that is the trap of the class:

```python
text = "hello"
text.upper()        # builds "HELLO" and throws it away
print(text)         # hello
text = text.upper() # caught
```

Class 6: `sort()` changes the list in place and gives back `None`. Class 7: `upper()` cannot change the string and gives back a new one. Opposite mechanisms, the same bug: the real result is the return value, so store it. Because each method returns a usable string, they chain: `input("Name: ").strip().title()`.

## 2. Finishing Class 7: walking through a string

```python
word = "education"
count = 0
for character in word:
    if character in "aeiou":
        count += 1
print("Vowels:", count)    # 5
```

Cleaning user input is the same idea in three lines: `name = input("Enter your name: ")`, then `name = name.strip()`, then `name = name.title()`, storing each result.

## 3. Finishing Class 7: PaisaPay v7

Every answer goes through `clean`, which strips and lower-cases it. A UPI ID is checked with `split("@")`. A card number is masked with a slice. Every message is an f-string. The full program is [`../Class-07-Strings/code/paisapay_v7.py`](../Class-07-Strings/code/paisapay_v7.py), and today's v8 starts from it.

## 4. Finishing Class 7: a word is not nothing

> **Real world.** A man in California chose the car number plate NULL. In many computer systems the word NULL means "nothing here", so every fine with a missing plate number was sent to him, $12,049 at one point, and the renewal website treated his plate as empty and refused him. The text NULL is four letters; an empty value is a different thing. In Python, `"None"` is a string of four letters, `""` is a string with nothing in it, and `None` is not a string at all. [Wired: how a NULL licence plate landed one hacker in ticket hell](https://www.wired.com/story/null-license-plate-landed-one-hacker-ticket-hell/)

## 5. Finishing Class 7: the string debug clinic

| Bug | What you see | Fix |
|---|---|---|
| `'It's late'` | `SyntaxError: unterminated string literal` | Use the other quote, or `\'` |
| `word[0] = "J"` | `TypeError` | Build a new string: `"J" + word[1:]` |
| `text.upper()` on its own line | nothing changes, no error | `text = text.upper()` |
| `if text.find("x"):` | True even when not found | compare with -1: `if text.find("x") != -1:` |
| `"Hello {name}"` | prints the braces | add the `f` |

---

## 6. Why more than lists

PaisaPay's history is `[600, 250, 100]`: three numbers with no names and no modes. A list of amounts is not a list of payments. Three jobs a list does badly, and the structure for each:

| Job | Structure | Looks like |
|---|---|---|
| Keep name, amount and mode together, and never let a receipt change | tuple | `("Rajani", 600, "upi")` |
| Count the different payees, with no duplicates to clean | set | `{"Rajani", "Sumit"}` |
| Look a payee up by name, not by position | dictionary | `{"rajani@okaxis": "Rajani"}` |

Every tool call an agent makes sends its arguments as a JSON object. In Python that object is a dictionary. Today you meet the type your agents have been speaking all along.

## 7. Tuples: a fixed collection

```python
point = (3, 4)
print(point[0])        # 3, read like a list

point = 3, 4           # the comma makes the tuple; brackets are for your eyes
print(type(point))     # <class 'tuple'>

x = (5)                # an int: brackets alone make nothing
y = (5,)               # a one-item tuple

coords = (10, 20, 30, 40)
print(coords[1:3])     # (20, 30), a slice of a tuple is a tuple

x, y = (3, 4)          # unpacking: one name per position
print(coords.count(10), coords.index(30))   # the only two methods

coords[0] = 99         # TypeError: 'tuple' object does not support item assignment
```

Reading a tuple is reading a list. The difference is writing: a tuple is immutable, like a string. A list would change silently; the tuple fails loudly, which is the safer behaviour for a record that must not change: a coordinate, a date, a receipt. `min` and `max` are built-in functions like `len`: give them a list and they return the smallest or the biggest value. A function that returns two values returns a tuple, because the comma after `return min(numbers)` makes one; unpack it with `smallest, biggest = min_and_max(numbers)`. Note that `payment = ("Rajani", 650)` after `payment = ("Rajani", 600)` is not a change to a tuple: the name was pointed at a new tuple, exactly like `text = text.upper()`.

> **Industry practice.** Python's built-in `sqlite3` module hands back every database row as a tuple by default: fixed columns, fixed order, read by unpacking. A record nobody should edit by accident is a tuple. [Python docs: row factories](https://docs.python.org/3/library/sqlite3.html#how-to-create-and-use-row-factories)

**PaisaPay v8, build 1.** `history.append((name, amount, mode))`, and the statement reads `for name, amount, mode in history:`.

## 8. Sets: every item once

```python
numbers = {1, 2, 2, 3, 3, 3}
print(numbers, len(numbers))       # {1, 2, 3} 3: duplicates dropped, silently

empty = {}                         # a dictionary! {} was claimed by dicts first
empty_set = set()                  # the empty set

fruits = {"apple", "banana"}
fruits.add("cherry")
fruits.discard("mango")            # not there: nothing happens
fruits.remove("mango")             # not there: KeyError: 'mango'
print("apple" in fruits)           # True, and fast even for a huge set
```

| Expression | The symbol | Reads as | Result for `{"Praveen", "Rahul", "Vamsi"}` and `{"Rahul", "Vamsi", "Akshay"}` |
|---|---|---|---|
| `a \| b` | pipe, say "or" | union: in either | `{'Praveen', 'Rahul', 'Vamsi', 'Akshay'}` |
| `a & b` | ampersand, say "and" | intersection: in both | `{'Rahul', 'Vamsi'}` |
| `a - b` | minus, say "without" | difference: in the first only | `{'Praveen'}` |
| `a ^ b` | caret, say "one or the other, not both" | symmetric difference: in exactly one | `{'Praveen', 'Akshay'}` |

A set has no order and no positions: `a[0]` is a `TypeError`, and two runs may print the elements in a different order. Never write code that depends on the order of a set.

> **Real incident, 2011.** Python, PHP, Java and Ruby all stored sets and dictionaries by hashing each key. Researchers crafted thousands of keys that hashed to the same place, so lookups slowed from instant to crawling, and one HTTP request carrying those keys as form fields could pin a web server's CPU at 100% for hours. Python's fix, in 3.3, was a random hash seed on every run. That is why your set prints in a different order each time: the order was never a promise. [oCERT advisory 2011-003](https://ocert.org/advisories/ocert-2011-003.html) · [Python docs: hash randomization](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONHASHSEED)

**PaisaPay v8, build 2.** The statement collects names in `payees = set()` and prints `len(payees)`. Pay the same person three times, she is counted once, with no `if name not in payees` needed.

## 9. Dictionaries: look up by name

A list answers "what is at position 2?". A dictionary answers "what is stored under `age`?".

```python
student = {"name": "Rajani", "age": 20, "course": "AIML"}
print(student["name"])                 # Rajani
student["age"] = 21                    # update an existing key
student["city"] = "Pune"               # add a new key
print(student.get("grade"))            # None: safe lookup
print(student.get("grade", "Not assigned"))
print(student["grade"])                # KeyError: 'grade'

print(student.keys())                  # dict_keys(['name', 'age', 'course', 'city'])
print(student.values())
print(student.items())                 # pairs, each a tuple
student.update({"age": 22, "grade": "A"})
removed = student.pop("grade")         # removes the key, gives back "A"
```

### The silent overwrite

```python
scores = {}
scores["Aanand"] = 90
scores["Saurabh"] = 85
scores["Aanand"] = 95
print(scores, len(scores))     # {'Aanand': 95, 'Saurabh': 85} 2
```

A key points to one value. The second assignment replaces the first; 90 is gone with no warning, no error and no way back. To keep both, store a list under the key: `scores["Aanand"] = [90]`, then `scores["Aanand"].append(95)`. This is the same shape of bug as Class 5's `print` versus `return` and Class 7's unstored `upper()`: code that runs, says nothing, and does something different from what you expected.

> **Industry practice.** An LLM or an API returns JSON, and `json.loads` turns it into a dictionary. If the JSON repeats a key, Python keeps the last value and drops the rest, with no error: `'{"x": 1, "x": 2, "x": 3}'` becomes `{'x': 3}`. The silent overwrite is how every JSON object enters your program. Validate what an agent sends before you trust it. [Python docs: repeated names within an object](https://docs.python.org/3/library/json.html#repeated-names-within-an-object)

### Looping

```python
for key in student:                      # the keys, not the values
    print(key)
for key, value in student.items():       # both, unpacked from each pair
    print(key, "->", value)
for value in student.values():
    print(value)
```

A loop over a tuple keeps the order you stored. A loop over a set makes no promise.

**PaisaPay v8, build 3.** Contacts are a dictionary from UPI ID to name, read with a safe default: `contacts.get(upi_id, upi_id.split("@")[0].title())`. Spending per payee is the counting pattern: `spent[name] = spent.get(name, 0) + amount`. Here the same key twice is what we want: add to the total, do not replace it.

## 10. Nested collections

```python
scores = {"Prasad": [90, 85, 95], "Madhumaya": [70, 75, 80]}
print(scores["Prasad"][0])               # 90: the key gives the list, the index gives the item

contacts = {"sumit@ybl": {"name": "Sumit", "city": "Bengaluru"}}
print(contacts["sumit@ybl"]["city"])     # Bengaluru: a lookup inside a lookup

payments = [("Sumit", 600, "upi"), ("Parveen", 250, "card")]
for name, amount, mode in payments:      # a list of tuples, unpacked in the for line
    print(name, amount, mode)
```

Read nested access from the outside in. `len` of a dictionary counts its keys. A key must be something that cannot change: a string, a number or a tuple. A list as a key is `TypeError: unhashable type: 'list'`; a list as a value is fine.

## 11. Choosing the right structure

| Store | Pick |
|---|---|
| A student's exam-hall seat, row and number | tuple |
| Every unique word in an essay | set |
| A phonebook: name to number | dictionary |
| A shopping list where order and repeats both matter | list |

The decision guide: look things up by a name or key, dictionary. Every item unique and order not needed, set. Will not change after it is made, tuple. Otherwise, list. Ask what the data must do, not which syntax you remember. Form your own answer before asking an AI assistant for a second opinion; then you can judge its reasoning instead of agreeing with it.

## 12. Mini project: word frequency counter

```python
sentence = "the cat sat on the mat the cat ran"
words = sentence.split()

counts = {}
for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1
print(counts)            # {'the': 3, 'cat': 2, 'sat': 1, 'on': 1, 'mat': 1, 'ran': 1}

unique_words = set(words)
print("Unique words:", len(unique_words))    # 6
```

The dictionary updates an existing key on purpose this time, and the set does the deduplication in one line. Full code: [`code/10_word_counts.py`](code/10_word_counts.py).

## 13. Errors and debug clinic

| You see | It means | Fix |
|---|---|---|
| `KeyError: 'grade'` | no such key in the dictionary, or no such item to remove from the set | `get` with a default; `discard` |
| `TypeError: unhashable type: 'list'` | a list used as a key or inside a set | use a tuple |
| `TypeError: 'tuple' object does not support item assignment` | changing a tuple in place | build a new tuple, or use a list |
| `ValueError: too many values to unpack` | wrong number of names on the left | one name per item |
| `AttributeError: 'dict' object has no attribute 'add'` | `seen = {}` made a dictionary | `seen = set()` |
| a count that stays at 1 | `visits[page] = 1` overwrites every time | `visits[page] = visits.get(page, 0) + 1` |

## Project: PaisaPay v8

Version 8 is v7 plus real records. Every payment is a `(name, amount, mode)` tuple in the history, the statement counts unique payees with a set, contacts are a dictionary from UPI ID to name with a safe default, spending per payee is a dictionary built with `get`, and menu item 7 saves a contact (an add, or an update when the UPI ID is already there).

```python
contacts = {"rajani@okaxis": "Rajani", "sumit@ybl": "Sumit"}

def name_for(upi_id):
    return contacts.get(upi_id, upi_id.split("@")[0].title())

def mini_statement(history):
    if len(history) == 0:
        print("No payments yet.")
        return
    total = 0
    payees = set()
    spent = {}
    for name, amount, mode in history:
        total += amount
        payees.add(name)
        spent[name] = spent.get(name, 0) + amount
    print(f"Payments: {len(history)} | Spent ₹{total}")
    print(f"Payees: {len(payees)}")
    for name, amount in spent.items():
        print(f"  {name}: ₹{amount}")
    print(f"Last: {history[-1]}")
```

The full program is [`code/paisapay_v8.py`](code/paisapay_v8.py). A sample run:

```text
1 Pay  2 Balance  3 Statement  4 Exit  5 Add  6 Card  7 Save
Choose: 1
Pay to (UPI ID): karthikeyan@oksbi
Amount in rupees: 250
Mode (upi / card / netbanking): card
UPI PIN: 4321
Paid ₹250 to Karthikeyan via Card
Fee ₹5 | Cashback ₹0 | Balance ₹155

1 Pay  2 Balance  3 Statement  4 Exit  5 Add  6 Card  7 Save
Choose: 3
Payments: 3 | Spent ₹950
Payees: 2
  Rajani: ₹700
  Karthikeyan: ₹250
Last: ('Rajani', 100, 'upi')

1 Pay  2 Balance  3 Statement  4 Exit  5 Add  6 Card  7 Save
Choose: 7
Contact UPI ID: karthikeyan@oksbi
Name: karthikeyan
Saved. 3 contacts.
```

What v8 cannot do yet: find the biggest payment or sort payments by amount, which needs `sorted` with a key, `map` and `filter` in Class 9; keep an account's rules and its data together, which is classes in Class 10; and remember anything after the program ends, which is files in Class 12.

## Recap

Before reading on, write your own three-point recap: what would you tell a friend who missed this class? Then compare.

- **Tuple**: a fixed record. The comma makes it. Unpack it. It cannot change.
- **Set**: unique items, fast `in`, no order. `{}` is not an empty set; `set()` is.
- **Dictionary**: key to value. A key holds one value; assign again and the old one is gone. `get` for safe lookups, `items()` for loops.
- **Nested**: a dictionary of lists, a dictionary of dictionaries, a list of tuples. Read from the outside in.
- **Choose**: by name, dictionary; unique, set; fixed, tuple; otherwise, list.
- **PaisaPay v8**: a tuple per payment, a set of payees, contacts and totals as dictionaries.

Next class: functional programming. The insights v8 cannot give, with `map`, `filter`, `sorted` and `lambda`.
