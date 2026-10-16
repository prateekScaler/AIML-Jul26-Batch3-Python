# Interview Readiness · Class 6

Lists are where interviewers check whether you can keep track of a changing collection: which box you are pointing at, what a method gives back, and whether you made a copy or a second name.

How to use this page: answer each question out loud or on paper first, then open the answer. For "predict the output" questions, run the code after you commit to an answer.

- [A. Questions interviewers ask](#a-questions-interviewers-ask)
- [B. Gotchas: predict the output](#b-gotchas-predict-the-output)
- [C. Explore, with AI in the loop](#c-explore-with-ai-in-the-loop)

---

## A. Questions interviewers ask

**A1. What is a list, and how is it different from five separate variables?**

<details><summary>Answer</summary>

An ordered collection of values under one name, which can grow and shrink. You can index it, slice it, loop over it and pass it around as one thing. Five variables cannot be looped over or counted, and a sixth needs new code.
</details>

**A2. Why does indexing start at 0, and what is index -1?**

<details><summary>Answer</summary>

The index is the distance from the start, so the first box is 0 away. Negative indexes count from the end: -1 is the last box, -2 the one before. A list of `n` items has valid indexes 0 to `n - 1`; anything else raises `IndexError`.
</details>

**A3. What is the difference between `sort()` and `sorted()`?**

<details><summary>Answer</summary>

`list.sort()` is a method: it rearranges the list in place and returns `None`. `sorted(list)` is a function: it leaves the original untouched and returns a new sorted list. Storing the result of `sort()` is a classic bug that leaves you holding `None`.
</details>

**A4. What is the difference between `remove()` and `pop()`?**

<details><summary>Answer</summary>

`remove(value)` deletes the first box with that value and returns nothing; it raises `ValueError` if the value is absent. `pop(index)` deletes the box at that position and returns the item; `pop()` with no index takes the last one.
</details>

**A5. What is a list comprehension, and when would you avoid one?**

<details><summary>Answer</summary>

A one-line way to build a new list from an existing one: `[expression for item in iterable if condition]`. Avoid it when the logic needs several statements, more than one condition, or a mid-way `print` to debug; a normal loop is clearer then.
</details>

**A6. What does slicing return, and is the stop index included?**

<details><summary>Answer</summary>

A new list containing the boxes from `start` up to but not including `stop`, the same exclusive rule as `range`. Leaving `start` empty means from the beginning, leaving `stop` empty means to the end, and `[:]` copies the whole list.
</details>

**A7. Why did changing one list change another?**

<details><summary>Answer</summary>

Because `b = a` does not copy; it makes a second name for the same list. Changing it through either name changes the one list. To get an independent list use `a.copy()` or `a[:]`. This is called aliasing.
</details>

**A8. Can a function change a list that is passed to it?**

<details><summary>Answer</summary>

Yes. The parameter is another name for the same list, so `append`, `remove` or `sort` inside the function change the caller's list. Reassigning the parameter to a new list does not. A number passed in cannot be changed this way, only returned.
</details>

---

## B. Gotchas: predict the output

Commit to an answer before you open each one.

**B1.**

```python
numbers = [1, 2, 3, 4, 5]
print(numbers[1:-1])
```

<details><summary>Answer</summary>

`[2, 3, 4]`. From index 1 up to, but not including, the last box.
</details>

**B2.**

```python
numbers = [3, 1, 2]
print(sorted(numbers), numbers)
```

<details><summary>Answer</summary>

`[1, 2, 3] [3, 1, 2]`. `sorted` makes a new list; the original keeps its order.
</details>

**B3.**

```python
fruits = ["Apple", "Banana"]
fruits.append(["Mango", "Orange"])
print(len(fruits))
```

<details><summary>Answer</summary>

`3`. `append` adds one item, and that item is a whole list. The third box holds `["Mango", "Orange"]`.
</details>

**B4.**

```python
a = [1, 2, 3]
b = a[:]
b.append(4)
print(a, b)
```

<details><summary>Answer</summary>

`[1, 2, 3] [1, 2, 3, 4]`. `[:]` makes a copy, so `b` is a separate list.
</details>

**B5.**

```python
numbers = [1, 2, 3, 4]
for n in numbers:
    if n % 2 == 0:
        numbers.remove(n)
print(numbers)
```

<details><summary>Answer</summary>

`[1, 3]` here, but this is luck: removing while looping shifts the boxes and can skip items. With `[1, 2, 2, 3]` the result would be `[1, 2, 3]`, one 2 left behind. Build a new list instead.
</details>

**B6.**

```python
numbers = [10, 20, 30]
print(numbers[-4])
```

<details><summary>Answer</summary>

`IndexError: list index out of range`. Three boxes allow -1 to -3.
</details>

**B7.**

```python
def add_item(items):
    items.append("x")

def replace_items(items):
    items = ["y"]

a = []
add_item(a)
replace_items(a)
print(a)
```

<details><summary>Answer</summary>

`['x']`. `append` changes the shared list. Reassigning the parameter inside `replace_items` only rebinds the local name.
</details>

**B8.**

```python
words = ["b", "a", "c"]
result = words.sort()
print(result, words)
```

<details><summary>Answer</summary>

`None ['a', 'b', 'c']`. The list is sorted, and `sort()` returned nothing.
</details>

**B9.**

```python
numbers = [1, 2, 3]
doubled = [n * 2 for n in numbers]
print(numbers, doubled)
```

<details><summary>Answer</summary>

`[1, 2, 3] [2, 4, 6]`. A comprehension never changes the source list.
</details>

**B10.**

```python
matrix = [[1, 2], [3, 4]]
print(matrix[1][0], len(matrix))
```

<details><summary>Answer</summary>

`3 2`. A list can hold lists. `matrix[1]` is `[3, 4]`, and its box 0 is 3. The outer list has two boxes.
</details>

---

## C. Explore, with AI in the loop

These connect today's lists to what you built in the GenAI modules.

**C1. The conversation is a list.** An agent keeps every message so far in a list and sends the last few to the model. Write a `messages` list of six short strings and print the last three with a slice. Then ask: what happens to cost and memory if the list only ever grows? Which list tool keeps it bounded?

<details><summary>Things to find</summary>

A slice such as `messages[-20:]` keeps a window; `pop(0)` drops the oldest. Real frameworks call this context window management, and it is slicing and popping underneath.
</details>

**C2. n8n items are a list.** A Loop Over Items node runs the next nodes once per item. Take a workflow you built and write the same thing as a Python `for` over a list. Where would a comprehension replace a whole branch of nodes?

**C3. Tool results are lists.** A `search` tool returns a list of results. Write a five-line function that takes that list and returns only the top three by score, using `sorted` with `reverse=True`. Why `sorted` and not `sort` here?

<details><summary>Things to find</summary>

The caller may still need the original order, and a function that quietly reorders its input surprises the next function in the chain.
</details>

**C4. AI as a reviewer.** Paste PaisaPay v6 into an assistant and ask: "Find every place a list is changed in place, and every place a new list is built. Do not change the code." Check each claim against the code. Did it catch that `pay` changes `history` without returning it?

**C5. Catch the AI being wrong.** Ask an assistant, without running, what this prints:

```python
numbers = [3, 1, 2]
numbers = numbers.sort()
print(numbers)
```

Many answer `[1, 2, 3]`. It prints `None`. Did yours get it right? Then ask it to explain why its first answer was wrong.

**C6. Explain, don't fix.** Paste B5 into an assistant and ask: "Walk me through what the loop sees on each pass if the list is `[1, 2, 2, 3]`. Do not rewrite the code." Check its trace against your own, box by box.
