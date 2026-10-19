# Interview Readiness · Class 7

Strings are where interviewers check whether you can handle real input: text with the wrong case, extra spaces and missing pieces, and whether you know that a string method never changes the string.

How to use this page: answer each question out loud or on paper first, then open the answer. For "predict the output" questions, run the code after you commit to an answer.

- [A. Questions interviewers ask](#a-questions-interviewers-ask)
- [B. Gotchas: predict the output](#b-gotchas-predict-the-output)
- [C. Explore, with AI in the loop](#c-explore-with-ai-in-the-loop)

---

## A. Questions interviewers ask

**A1. What does it mean that strings are immutable?**

<details><summary>Answer</summary>

Once created, a string cannot be changed in place: `word[0] = "J"` raises `TypeError`. Every string method therefore returns a new string and leaves the original as it was. To keep a result you store it: `text = text.upper()`.
</details>

**A2. How are strings and lists alike, and how do they differ?**

<details><summary>Answer</summary>

Both are ordered sequences: zero-based indexing, negative indexing, slicing with the exclusive stop, `len`, `in` and `for` loops all work the same. A list is mutable, so `numbers[0] = 100` works and its methods change it in place and return `None`. A string is immutable, so item assignment fails and its methods return new strings.
</details>

**A3. What is the difference between `find` and `in`?**

<details><summary>Answer</summary>

`"x" in text` answers yes or no with a bool. `text.find("x")` answers where, with the start index, and gives -1 when the piece is absent. Never test `find` as a bool: -1 counts as True.
</details>

**A4. What do `split` and `join` do, and why is `join` written on the separator?**

<details><summary>Answer</summary>

`split` cuts a string into a list, at spaces by default or at the separator you give. `join` glues a list of strings into one string, with the separator in between. It is a method of the separator string, `", ".join(items)`, because the separator is the one thing that is always a string, while the items may come from any iterable.
</details>

**A5. What is an f-string, and what can go inside the braces?**

<details><summary>Answer</summary>

A string literal prefixed with `f` whose `{...}` parts are evaluated and inserted: variables, expressions such as `{price * quantity}`, and format specs such as `{price:.2f}` for two decimals. No `str()` conversion is needed. Without the `f`, the braces are printed literally.
</details>

**A6. Why should user input be cleaned before it is compared?**

<details><summary>Answer</summary>

Text comparison is exact. `" UPI"` is not `"upi"`. Users add spaces and capitals; `strip()` and `lower()` remove that noise so the comparison tests the meaning, not the typing. Clean once, at the door, then compare.
</details>

**A7. What does `strip()` remove, and what does it leave?**

<details><summary>Answer</summary>

Whitespace at the start and end only: spaces, tabs and newlines. Spaces between words stay. `" Asha Sarkar ".strip()` is `"Asha Sarkar"`.
</details>

**A8. How do you put a quote character inside a string?**

<details><summary>Answer</summary>

Use the other kind of quote around the string, `"It's"`, or escape it with a backslash, `'It\'s'`. The backslash also makes `\n` a new line, `\t` a tab and `\\` a single backslash.
</details>

---

## B. Gotchas: predict the output

Commit to an answer before you open each one.

**B1.**

```python
s = "PaisaPay"
print(s[2:5], s[-3:], s[:-3])
```

<details><summary>Answer</summary>

`isa Pay Paisa`. Stop excluded each time; `[:-3]` is everything but the last three.
</details>

**B2.**

```python
text = "hello"
text.replace("h", "j")
print(text)
```

<details><summary>Answer</summary>

`hello`. The new string was not stored.
</details>

**B3.**

```python
print("a,b,,c".split(","))
print(len("".split()))
```

<details><summary>Answer</summary>

`['a', 'b', '', 'c']`, then `0`. Two commas in a row give an empty piece. Splitting an empty string at spaces gives an empty list.
</details>

**B4.**

```python
print("ab" * 3, "ab" + "3")
```

<details><summary>Answer</summary>

`ababab ab3`. A string times a number repeats it; a string plus a string joins them.
</details>

**B5.**

```python
name = "rashi"
print(f"{name.upper()} has {len(name)} letters")
```

<details><summary>Answer</summary>

`RASHI has 5 letters`. Method calls and function calls both work inside the braces.
</details>

**B6.**

```python
text = "Python"
if text.find("z"):
    print("found")
else:
    print("not found")
```

<details><summary>Answer</summary>

`found`. `find` returns -1, and -1 is a truthy value. The correct test is `!= -1`, or use `in`.
</details>

**B7.**

```python
print("Yes" == "yes", "Yes".lower() == "yes")
```

<details><summary>Answer</summary>

`False True`. Comparison is case-sensitive until you normalise.
</details>

**B8.**

```python
word = "level"
print(word == word[::-1])
```

<details><summary>Answer</summary>

`True`. Reversed, it is the same string.
</details>

**B9.**

```python
print(f"{1234.5:.2f}", f"{7 / 2}", f"{7 // 2}")
```

<details><summary>Answer</summary>

`1234.50 3.5 3`. The format spec pads to two decimals; the other two are ordinary division results.
</details>

**B10.**

```python
s = "a b  c"
print(len(s.split()), len(s.split(" ")))
```

<details><summary>Answer</summary>

`3 4`. `split()` with no argument treats runs of spaces as one separator. `split(" ")` cuts at every single space, so the double space gives an empty piece.
</details>

---

## C. Explore, with AI in the loop

These connect today's strings to what you built in the GenAI modules.

**C1. The model speaks in strings.** Ask any assistant for "the total of 600, 300 and 250, as a sentence". Paste its answer into a Python string and extract the number with `split` and a loop that checks `isdigit()` on each word, or with `find` and a slice. How many ways could the model phrase the answer that would break your code?

<details><summary>Things to find</summary>

Commas inside numbers, "Rs" or "₹" stuck to the digits, the number spelled in words. This is why production code asks the model for structured output and validates it, rather than parsing prose.
</details>

**C2. Structured output is still a string.** When an agent returns JSON, your program first receives it as text. Write the one check that tells you whether the text at least starts with `{` and ends with `}` before anything tries to parse it. Which two methods from today are those?

**C3. Prompts are strings too.** Build a prompt with an f-string: `f"Summarise this for a {audience} in {words} words: {text}"`. What happens if `text` itself contains braces or quotes? Try it. This is the string version of the injection problem you met in the security lecture.

**C4. AI as a reviewer.** Paste PaisaPay v7 into an assistant and ask: "List every string method call whose result is not stored or used. Do not change the code." Check each claim. Did it flag the `.strip()` inside `ask_pin` correctly as stored?

**C5. Catch the AI being wrong.** Ask an assistant, without running, what this prints:

```python
s = "hello"
s.upper()
print(s)
```

Some answer `HELLO`. It prints `hello`. Did yours get it right? Then ask it to explain why its first answer was wrong.

**C6. Explain, don't fix.** Paste B6 into an assistant and ask: "Why does this print found for a letter that is not in the string? Explain without rewriting the code." Then fix it yourself two ways: with `!= -1` and with `in`.
