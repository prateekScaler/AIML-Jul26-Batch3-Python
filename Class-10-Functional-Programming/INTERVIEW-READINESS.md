# Interview Readiness · Class 10

Functional programming questions test whether you can read a line of `map`, `filter` and `lambda` without running it, whether you know that these tools are lazy, and whether you can say when a plain loop is the better choice.

How to use this page: answer each question out loud or on paper first, then open the answer. For "predict the output" questions, run the code after you commit to an answer.

- [A. Questions interviewers ask](#a-questions-interviewers-ask)
- [B. Gotchas: predict the output](#b-gotchas-predict-the-output)
- [C. Explore, with AI in the loop](#c-explore-with-ai-in-the-loop)

---

## A. Questions interviewers ask

**A1. What is a higher-order function? Give two examples from the standard library.**

<details><summary>Answer</summary>

A function that takes another function as an argument. `map`, `filter`, `sorted` (through its key) and `functools.reduce` all take a function. The other direction, a function that builds and returns a function, is covered in the next class.
</details>

**A2. What is the difference between passing `f` and passing `f()`?**

<details><summary>Answer</summary>

`f` is the function itself, a value that can be stored and called later. `f()` calls it now and passes whatever it returns. A higher-order function wants `f`; passing `f()` either fails because `f` needed arguments, or passes a result instead of a function.
</details>

**A3. What is a lambda, and when should you not use one?**

<details><summary>Answer</summary>

An anonymous function made of parameters, a colon and one expression that is returned. Use it for logic needed once, written directly in a call. Use `def` when the logic is reused, needs more than one expression, needs a statement such as an assignment or an `if` block, or needs a name to be understood.
</details>

**A4. What do `map` and `filter` return, and why does it matter?**

<details><summary>Answer</summary>

Lazy iterator objects, not lists. Nothing is computed until something consumes them, such as `list()` or a `for` loop. It matters because printing them shows `<map object ...>`, they have no `len` or indexing, and they can be consumed only once. Wrap in `list()` when you need a list.
</details>

**A5. Why is `reduce` not a built-in in Python 3?**

<details><summary>Answer</summary>

It was moved to `functools` because most uses were harder to read than a loop or a built-in such as `sum`, `max` or `min`. It still exists, imported with `from functools import reduce`, for combining steps that have no built-in name.
</details>

**A6. How does `sorted` with a key work?**

<details><summary>Answer</summary>

The key function is called once per item and returns the value to compare; the items themselves are returned in the resulting order. `key=lambda p: p[1]` sorts tuples by their second field. Ties keep the original order, because the sort is stable. `max` and `min` accept the same key.
</details>

**A7. What is the difference between a list comprehension and `map` with a lambda?**

<details><summary>Answer</summary>

`[x * 2 for x in nums]` and `list(map(lambda x: x * 2, nums))` produce the same list. The comprehension is eager and usually easier to read; `map` is lazy and takes an existing function without a lambda, as in `map(str, nums)`. Most Python code prefers the comprehension for simple cases.
</details>

**A8. When is a loop the better choice?**

<details><summary>Answer</summary>

When you need to print or inspect values in the middle, branch on several conditions per item, change more than one thing per iteration, or when the functional version needs an explanation. One simple step per item: `map`, `filter` or a comprehension. Anything else: a loop.
</details>

---

## B. Gotchas: predict the output

Commit to an answer before you open each one.

**B1.**

```python
squares = map(lambda x: x * x, [1, 2, 3])
print(type(squares).__name__, list(squares))
```

<details><summary>Answer</summary>

`map [1, 4, 9]`. The object is a map; `list` pulls the values out.
</details>

**B2.**

```python
nums = [1, 2, 3, 4]
print(list(filter(lambda n: n % 2, nums)))
```

<details><summary>Answer</summary>

`[1, 3]`. `n % 2` is 1 for odd numbers, which counts as True, and 0 for even, which counts as False. It works, but `n % 2 == 1` says what it means.
</details>

**B3.**

```python
from functools import reduce
print(reduce(lambda a, b: a + b, ["a", "b", "c"]))
```

<details><summary>Answer</summary>

`abc`. The combining function works on strings too; the running answer grows from the left.
</details>

**B4.**

```python
from functools import reduce
print(reduce(lambda a, b: a + b, [], 0))
```

<details><summary>Answer</summary>

`0`. With a starting value, an empty list gives that value. Without one, `reduce` on an empty list raises `TypeError`.
</details>

**B5.**

```python
f = lambda x, y=10: x + y
print(f(1), f(1, 2))
```

<details><summary>Answer</summary>

`11 3`. A lambda can have default parameters like any function.
</details>

**B6.**

```python
funcs = [lambda x: x + 1, lambda x: x * 2]
print([g(5) for g in funcs])
```

<details><summary>Answer</summary>

`[6, 10]`. Functions are values; a list can hold them and a loop can call each one.
</details>

**B7.**

```python
pairs = [("b", 2), ("a", 2), ("c", 1)]
print(sorted(pairs, key=lambda p: p[1]))
```

<details><summary>Answer</summary>

`[('c', 1), ('b', 2), ('a', 2)]`. Sorted by the number. `b` and `a` tie on 2 and keep their original order: the sort is stable.
</details>

**B8.**

```python
nums = [1, 2, 3]
print(list(map(lambda n: n * 2, nums)), nums)
```

<details><summary>Answer</summary>

`[2, 4, 6] [1, 2, 3]`. `map` builds new values; the original list is untouched.
</details>

**B9.**

```python
names = ["sumit", "Rajani", "akshay"]
print(sorted(names), sorted(names, key=lambda n: n.lower()))
```

<details><summary>Answer</summary>

`['Rajani', 'akshay', 'sumit'] ['akshay', 'Rajani', 'sumit']`. Without a key, capital letters sort before lower-case ones. The key compares lower-cased copies, so the names come back in alphabetical order, unchanged.
</details>

**B10.**

```python
words = ["bb", "a", "ccc"]
print(max(words), max(words, key=len))
```

<details><summary>Answer</summary>

`ccc ccc`. Without a key, strings compare alphabetically and `ccc` is last. With `key=len` the longest wins, also `ccc`. Change the list to `["bb", "z", "ccc"]` and the two answers differ: `z` and `ccc`.
</details>

---

## C. Explore, with AI in the loop

These connect today's tools to what you built in the GenAI modules.

**C1. A pipeline is map and filter.** An n8n workflow that takes a list of leads, keeps the ones from India, and formats each as a message is `filter` then `map`. Write it in Python on a list of dictionaries with `country` and `name` keys. Then ask an assistant to turn your Python into a description of the n8n nodes, and check whether it kept the order right.

**C2. Tool results as records.** An agent calls a search tool five times and gets back a list of result dictionaries with `title` and `score`. Use `filter` to drop scores under 0.5, `sorted` with a key to order by score, and `map` to pull out the titles. Which of the three would you do first, and why does the order of the other two not matter?

**C3. Catch the AI being wrong.** Ask an assistant, without running, what this prints:

```python
squares = map(lambda x: x * x, [1, 2, 3])
print(list(squares))
print(list(squares))
```

Some answer `[1, 4, 9]` twice. The second list is `[]`. Did yours get it right? Ask it to explain why a map object can only be consumed once.

**C4. Explain, don't fix.** Paste Part B6 of the assignment into an assistant and ask: "Why does this program fail, and why would it print a map object even after the syntax is fixed? Explain without rewriting the code." Then fix it yourself.

**C5. AI as a reviewer.** Paste PaisaPay v10 into an assistant and ask: "For each map, filter, reduce and sorted call, say whether a comprehension, sum, max or min would read better. Do not change the code." Decide for each claim whether you agree, and change at most one.

**C6. The web-scale version.** Read the one-paragraph abstract of Google's MapReduce paper and write, in your own words, what the map step and the reduce step are for counting words across millions of pages. Then write the same word count on one sentence in Python with `map`, a dictionary and `reduce`, and note what the paper adds that your version does not need.
