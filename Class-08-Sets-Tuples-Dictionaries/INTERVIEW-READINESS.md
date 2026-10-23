# Interview Readiness · Class 8

Interviewers use tuples, sets and dictionaries to check whether you choose a structure for a reason, whether you know what a dictionary does with a repeated key, and whether you can read nested data without guessing.

How to use this page: answer each question out loud or on paper first, then open the answer. For "predict the output" questions, run the code after you commit to an answer.

- [A. Questions interviewers ask](#a-questions-interviewers-ask)
- [B. Gotchas: predict the output](#b-gotchas-predict-the-output)
- [C. Explore, with AI in the loop](#c-explore-with-ai-in-the-loop)

---

## A. Questions interviewers ask

**A1. What is the difference between a list and a tuple, and when do you use each?**

<details><summary>Answer</summary>

Both are ordered and indexed. A list is mutable: you can append, remove, sort and assign to a position. A tuple is immutable: once built it cannot change, and it has only `count` and `index`. Use a tuple for a fixed record such as a coordinate, a date or a database row, for returning several values from a function, and as a dictionary key. Use a list when the collection grows or changes.
</details>

**A2. Why does `(5)` not make a tuple?**

<details><summary>Answer</summary>

Brackets alone group an expression, so `(5)` is the integer 5. The comma makes the tuple: `(5,)` or just `5,`. This is a silent mistake because it gives a different type, not an error.
</details>

**A3. What does a set guarantee, and what does it not guarantee?**

<details><summary>Answer</summary>

It guarantees that each value appears once, and it gives fast membership tests with `in`. It does not keep an order and has no positions, so `s[0]` is a `TypeError`. Elements must be immutable: numbers, strings and tuples are fine, lists are not.
</details>

**A4. How do you create an empty set, and why not with `{}`?**

<details><summary>Answer</summary>

`set()`. Curly brackets were used for dictionaries before sets existed in the language, so `{}` is an empty dictionary.
</details>

**A5. What happens when you assign to a dictionary key that already exists?**

<details><summary>Answer</summary>

The old value is replaced. A key maps to exactly one value, so a second assignment updates rather than adds, and the previous value is lost with no error. If every value must be kept, store a list under the key and append to it.
</details>

**A6. What is the difference between `d["k"]` and `d.get("k")`?**

<details><summary>Answer</summary>

Both return the value when the key exists. When it does not, square brackets raise `KeyError`; `get` returns `None`, or the default you pass as the second argument. Use `get` when the key may be missing and that is normal; use square brackets when a missing key is a bug you want to hear about.
</details>

**A7. What does a `for` loop over a dictionary give you, and how do you get the values too?**

<details><summary>Answer</summary>

The keys. Use `d.values()` for the values and `d.items()` for key-value pairs, which come as tuples you unpack in the for line: `for key, value in d.items():`.
</details>

**A8. Why can a tuple be a dictionary key but a list cannot?**

<details><summary>Answer</summary>

A dictionary finds a key by its hash, a number computed from its contents. If the contents could change after insertion, the hash would no longer match and the key would be lost. Lists can change, so they are unhashable. Tuples, strings and numbers cannot change, so they can be keys.
</details>

**A9. How do you choose between list, tuple, set and dictionary?**

<details><summary>Answer</summary>

Ask what the data must do. Lookup by a name or key: dictionary. Every item unique and order not needed: set. Fixed after creation: tuple. Otherwise: list.
</details>

---

## B. Gotchas: predict the output

Commit to an answer before you open each one.

**B1.**

```python
t = 1, 2
print(type(t), len(t))
```

<details><summary>Answer</summary>

`<class 'tuple'> 2`. The comma made the tuple; no brackets needed.
</details>

**B2.**

```python
x, y, z = (1, 2)
```

<details><summary>Answer</summary>

`ValueError: not enough values to unpack (expected 3, got 2)`. Unpacking needs one name per item.
</details>

**B3.**

```python
s = {1, 2, 3}
s.add(2)
s.discard(7)
print(len(s))
```

<details><summary>Answer</summary>

`3`. Adding an existing value does nothing; discarding a missing one does nothing. `remove(7)` would have raised `KeyError`.
</details>

**B4.**

```python
d = {}
d["a"] = 1
d["a"] = d["a"] + 1
print(d)
```

<details><summary>Answer</summary>

`{'a': 2}`. The second line reads the old value, adds one and stores the result under the same key. That is the counting pattern, done on purpose.
</details>

**B5.**

```python
d = {"a": 1, "b": 2}
for k in d:
    print(k, d[k], end="; ")
```

<details><summary>Answer</summary>

`a 1; b 2; `. The loop gives keys; the lookup gives each value.
</details>

**B6.**

```python
print({1, 2} == {2, 1}, (1, 2) == (2, 1))
```

<details><summary>Answer</summary>

`True False`. Sets have no order, so the same members make equal sets. Tuples are ordered, so the order matters.
</details>

**B7.**

```python
d = {"a": [1, 2]}
d["a"].append(3)
print(d["a"][-1])
```

<details><summary>Answer</summary>

`3`. The value is a list, and lists change in place. `d["a"]` is that list, so appending to it changes what the dictionary holds.
</details>

**B8.**

```python
d = {(1, 2): "ok"}
print(d[(1, 2)], d[1, 2])
```

<details><summary>Answer</summary>

`ok ok`. The key is a tuple, and `d[1, 2]` is the same tuple because the comma makes one.
</details>

**B9.**

```python
d = {"x": 1}
print(d.pop("x"), d)
```

<details><summary>Answer</summary>

`1 {}`. `pop` removes the key and returns its value.
</details>

**B10.**

```python
t = (1, [2, 3])
t[1].append(4)
print(t)
```

<details><summary>Answer</summary>

`(1, [2, 3, 4])`. The tuple did not change: it still holds the same list object. The list inside it is mutable and changed. Immutable means the tuple's slots cannot be reassigned, not that everything inside is frozen.
</details>

---

## C. Explore, with AI in the loop

These connect today's structures to what you built in the GenAI modules.

**C1. A tool call is a dictionary.** Take any tool you defined in n8n or in an agent builder and write the arguments an agent would send as a Python dictionary. Then write the three checks your Python function should do before using it: is every required key present (`in`), is each value the right type, and what should happen for an unexpected extra key?

**C2. Repeated keys from a model.** Ask an assistant to produce JSON for a payment with the amount given twice, once as a number and once as a string. Paste the JSON into `json.loads` and print the result. Which value survived, and why? Read [the Python docs on repeated names](https://docs.python.org/3/library/json.html#repeated-names-within-an-object), then decide what your program should do when a key repeats.

**C3. Catch the AI being wrong.** Ask an assistant, without running, what this prints:

```python
empty = {}
empty.add("x")
print(type(empty))
```

Some answer `<class 'set'>`. It raises `AttributeError`, because `{}` is a dictionary. Did yours get it right? Then ask it to explain its first answer.

**C4. Structure review.** Paste PaisaPay v8 into an assistant and ask: "For each collection in this program, say which structure it is and whether a different one would be better. Do not change the code." Check each claim against the decision guide. Did it suggest a list of dictionaries for the history? Which would you choose, and why?

**C5. Explain, don't fix.** Paste Part B6 of the assignment into an assistant and ask: "Why does the count stay at 1 for every mode? Explain without rewriting the code." Then fix it yourself with `get`.

**C6. Memory as a dictionary.** In the agents module, memory was a store of facts the agent could read back. Design it as a Python dictionary: what are the keys, what are the values, and what happens the second time the agent "remembers" the same fact under the same key? Which structure would you use if every version must be kept?
