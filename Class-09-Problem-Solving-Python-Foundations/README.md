# Class 9 · Problem Solving: Python Foundations

A revision session. It finishes Class 8 (dictionaries, nested collections, choosing a structure, the word counter and PaisaPay v8), then revises Classes 1 to 8 with quick-fire output predictions, concept checks and two programs written in class. Six practice problems with solutions are in [`PRACTICE.md`](PRACTICE.md).

**By the end of this session you can:**

- Build and read a dictionary, add and update keys, use `get`, and loop over keys, values and items.
- Explain the silent overwrite and choose a dictionary of lists when every value must be kept.
- Pick a list, tuple, set or dictionary from what the data must do.
- Predict the output of short snippets on types, truthiness, aliasing, slicing, sets and dictionaries.
- Write a small input-to-output program from a specification, with type conversion and f-strings.

## How to use this folder

| File | What it is |
|---|---|
| [`index.html`](index.html) | The interactive session page. [Open it here](https://prateekscaler.github.io/AIML-Jul26-Batch3-Python/Class-09-Problem-Solving-Python-Foundations/), no download needed. **Step by step** shows a little at a time (press → or Next). **Show everything** gives the whole session on one page. |
| [`code/`](code/) | The quick-fire snippets and a solution for every practice problem, as runnable files. |
| [`Python-Class-09-Problem-Solving-Python-Foundations.ipynb`](Python-Class-09-Problem-Solving-Python-Foundations.ipynb) | The same files as one notebook. [Open it in Google Colab](https://colab.research.google.com/github/prateekScaler/AIML-Jul26-Batch3-Python/blob/main/Class-09-Problem-Solving-Python-Foundations/Python-Class-09-Problem-Solving-Python-Foundations.ipynb). |
| [`PRACTICE.md`](PRACTICE.md) | Six problems on Classes 1 to 8, easy to hard, with sample runs, hints and solutions. |

Run the code in [PyLens](https://scaler-pylens.vercel.app/), or on your own machine with `python3 filename.py`.

The dictionary material is also in the Class 8 notes: [Class 8 README, sections 9 to 13](../Class-08-Sets-Tuples-Dictionaries/README.md#9-dictionaries-look-up-by-name).

---

## 1. Finishing Class 8: dictionaries

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

**The silent overwrite.** A key points to one value. Assign to the same key twice and the first value is replaced with no warning:

```python
scores = {}
scores["Aanand"] = 90
scores["Saurabh"] = 85
scores["Aanand"] = 95
print(scores, len(scores))     # {'Aanand': 95, 'Saurabh': 85} 2
```

To keep both scores, store a list under the key: `scores["Aanand"] = [90]`, then `scores["Aanand"].append(95)`. Used on purpose, the same mechanism is the counting pattern: `counts[word] = counts.get(word, 0) + 1`.

An LLM or an API returns JSON, and `json.loads` turns it into a dictionary. If the JSON repeats a key, Python keeps the last value, silently: `'{"x": 1, "x": 2, "x": 3}'` becomes `{'x': 3}`. [Python docs: repeated names within an object](https://docs.python.org/3/library/json.html#repeated-names-within-an-object)

**Curly brackets.** `{}` is an empty dictionary, not an empty set. An empty set is `set()`.

**Looping.** `for key in student` gives the keys. `student.items()` gives (key, value) pairs to unpack in the for line. `student.values()` gives only the values. A tuple keeps its order in a loop; a set makes no promise.

**Nested.** `scores = {"Prasad": [90, 85, 95]}`, then `scores["Prasad"][0]` is 90: the key gives the list, the index gives the item. `contacts["sumit@ybl"]["city"]` is a lookup inside a lookup. A list of tuples is unpacked in the for line: `for name, amount, mode in payments:`. Read nested access from the outside in. A key must be immutable: a string, a number or a tuple, never a list.

**Choosing.** Lookup by a name or key: dictionary. Every item unique and order not needed: set. Fixed after creation: tuple. Otherwise: list.

**Word frequency counter.**

```python
sentence = "the cat sat on the mat the cat ran"
words = sentence.split()
counts = {}
for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1
print(counts)                              # {'the': 3, 'cat': 2, 'sat': 1, 'on': 1, 'mat': 1, 'ran': 1}
print("Unique words:", len(set(words)))    # 6
```

**PaisaPay v8** is complete: a tuple per payment, a set of payees, contacts as a dictionary with a safe default, spending per payee with the counting pattern, and a menu item that saves a contact. The program is [`../Class-08-Sets-Tuples-Dictionaries/code/paisapay_v8.py`](../Class-08-Sets-Tuples-Dictionaries/code/paisapay_v8.py).

## 2. Eight classes, one idea each

| Class | Topic | The one idea |
|---|---|---|
| 1 | Data types, variables, input | `input()` always gives text; convert it on purpose |
| 2 | Operators | `/` gives a float, `//` and `%` give whole-number answers; a comparison is a bool |
| 3 | Control statements | only the first true branch runs; order the `elif`s from strict to loose |
| 4 | Loops | `range` stops before the end; `break` leaves, `continue` skips |
| 5 | Functions | `print` shows, `return` hands back; a function without `return` gives None |
| 6 | Lists | two names can share one list; `sort()` changes it and gives None, `sorted()` makes a new one |
| 7 | Strings | a string never changes; store what every method gives back |
| 8 | Sets, tuples, dictionaries | tuple: fixed; set: unique, no order; dictionary: one value per key |

## 3. Quick-fire: predict the output

Write each answer before you run it. The file is [`code/01_quick_fire.py`](code/01_quick_fire.py).

| # | Code | Output | Why |
|---|---|---|---|
| 1 | `print(type(3/2), type(3//2), 2**3**2)` | `<class 'float'> <class 'int'> 512` | `/` gives a float; `**` works from the right, 3**2 then 2**9 |
| 2 | `x = "5"` then `print(x*3, int(x)*3)` | `555 15` | text repeats, a number multiplies |
| 3 | `print(bool(""), bool("0"), bool([]), bool([0]))` | `False True False True` | empty is False; `"0"` and `[0]` are not empty |
| 4 | `a = [1, 2, 3]; b = a; b.append(4); print(a)` | `[1, 2, 3, 4]` | two names, one list |
| 5 | `t = (1, 2, [3, 4]); t[2].append(5); print(t)` | `(1, 2, [3, 4, 5])` | the tuple's slots are fixed; the list inside can change |
| 6 | `print({1, 2, 3} & {2, 3, 4}, {1, 2, 3} - {2, 3, 4})` | `{2, 3} {1}` | in both; in the first only (homework: see PRACTICE.md) |
| 7 | `s = "python"; print(s[::-2], s[1:4])` | `nhy yth` | backwards two at a time; boxes 1 to 3 |
| 8 | `d = {"a": 1}; print(d.get("b", 0), d.get("b"), d)` | `0 None {'a': 1}` | `get` reads with a default; it never adds a key |

## 4. Concept checks

- `input()` always gives a string, even when the user types digits.
- `range(1, 10, 3)` gives 1, 4, 7: three numbers, because 10 is the stop and is excluded.
- A function that prints but does not `return` gives None to whoever called it.
- `sorted(nums)` makes a new sorted list and leaves `nums` alone; `nums.sort()` changes `nums` and gives None.
- `text.strip()` on its own line changes nothing; store the result.
- Marks per student, by name, growing over time: a dictionary of lists.

## 5. Written in class

**The bill splitter** ([`code/02_bill_splitter.py`](code/02_bill_splitter.py)): name, bill, tip percentage and people in; tip, grand total, each person's share to two decimals and a bool out. Convert at the door: `float` for money, `int` for counts. `each > 500` is already a bool, so it goes straight into the f-string.

**The text cleaner** ([`code/03_text_cleaner.py`](code/03_text_cleaner.py)): strip, lower and three `replace` calls, each result stored; `split` into words; a comprehension for the words longer than three characters (8 of them); unique words in first-seen order with a list and `not in`, because a set would forget the order; and the sentence reversed word by word with `" ".join(words[::-1])`.

## Recap

- **Dictionary**: key to value, `get` for a safe lookup, `items()` to loop over both, one value per key.
- **Nested**: read from the outside in; a key must be immutable.
- **Choose**: by name, dictionary; unique, set; fixed, tuple; otherwise, list.
- **Quick-fire habits**: convert input, remember that `/` makes a float, that two names can share one list, and that a method's result must be stored.

Next class: functional programming. `map`, `filter`, `sorted` with a key, and `lambda`, on PaisaPay's history.
