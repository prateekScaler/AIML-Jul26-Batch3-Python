# Interview Readiness · Class 3

Conditionals are where interviewers check whether you can read code the way Python runs it: which branch runs, which never runs, and why.

How to use this page: answer each question out loud or on paper first, then open the answer. For "predict the output" questions, run the code after you commit to an answer.

- [A. Questions interviewers ask](#a-questions-interviewers-ask)
- [B. Gotchas: predict the output](#b-gotchas-predict-the-output)
- [C. Explore, with AI in the loop](#c-explore-with-ai-in-the-loop)

---

## A. Questions interviewers ask

**A1. How does Python know which lines belong to an `if`?**

<details><summary>Answer</summary>

By indentation. Every line indented under the `if` is its block; the first line back at the old indentation is outside it. Other languages use braces for this; in Python the indentation is the syntax, and a missing or inconsistent indent is an `IndentationError`.
</details>

**A2. What is the difference between `if` / `elif` / `else` and several separate `if` statements?**

<details><summary>Answer</summary>

A chain is **one** decision: Python checks top to bottom, runs the first block whose condition is True, and skips the rest. Separate `if`s are **independent** decisions: every condition is checked and every True one runs. For cashback tiers you want a chain; two separate `if`s would pay two cashbacks.
</details>

**A3. Why does the order of conditions matter in an `elif` chain?**

<details><summary>Answer</summary>

Because the first True condition wins. If a broad condition such as `amount >= 500` comes before a narrow one such as `amount >= 5000`, the narrow one can never be reached. Put the most specific or highest-priority condition first.
</details>

**A4. When would you use `match` / `case` instead of `if` / `elif`?**

<details><summary>Answer</summary>

When one variable is compared against several **exact values**, such as a payment mode or a menu choice. `case _` is the wildcard that plays the role of `else`. For ranges and combined conditions, `if` / `elif` is the right tool. `match` needs Python 3.10 or newer.
</details>

**A5. What values count as False in a condition?**

<details><summary>Answer</summary>

`False`, `None`, zero (`0`, `0.0`), and empty things: `""`, `[]`, `{}`. Everything else counts as True, including the string `"0"` and the string `"False"`. This is why `if mode == "upi" or "card":` is always True: `"card"` is a non-empty string.
</details>

**A6. Nested `if` or `and`: which is better?**

<details><summary>Answer</summary>

Both are correct. `and` is shorter when the checks are independent and one failure message is enough. Nesting is better when the second check only makes sense after the first passes, or when each level needs its own message ("Wrong PIN" vs "Insufficient balance").
</details>

**A7. What does the ternary operator look like in Python, and when is it a bad idea?**

<details><summary>Answer</summary>

`value_if_true if condition else value_if_false`, for example `status = "SUCCESS" if balance >= amount else "FAILED"`. It is a bad idea when chained for three or more outcomes; an `if` / `elif` / `else` block is far easier to read.
</details>

**A8. What is `pass` for?**

<details><summary>Answer</summary>

A placeholder statement that does nothing. Python requires a block after `if ...:`, so `pass` lets you write the structure first and fill in the code later.
</details>

---

## B. Gotchas: predict the output

Commit to an answer before you open each one.

**B1.**

```python
amount = 8000
if amount >= 500:
    print("₹10")
elif amount >= 5000:
    print("₹100")
```

<details><summary>Answer</summary>

`₹10`. The broad condition is first and is True, so the chain stops there.
</details>

**B2.**

```python
mode = "cash"
if mode == "upi" or "card":
    print("Digital")
else:
    print("Cash")
```

<details><summary>Answer</summary>

`Digital`. Python reads it as `(mode == "upi") or ("card")`, and a non-empty string counts as True. Write `mode == "upi" or mode == "card"`.
</details>

**B3.**

```python
pin_correct = True
balance = 300
if pin_correct:
    if balance >= 800:
        print("Paid")
else:
    print("Wrong PIN")
```

<details><summary>Answer</summary>

Nothing. The `else` lines up with the outer `if`, so it belongs to `pin_correct`, which is True. The inner check is False and has no `else`.
</details>

**B4.**

```python
score = 85
print("A" if score >= 90 else "B" if score >= 80 else "C")
```

<details><summary>Answer</summary>

`B`. Read left to right: `score >= 90` is False, so look at the rest: `score >= 80` is True → `"B"`.
</details>

**B5.**

```python
a = 0
if a:
    print("yes")
else:
    print("no")
```

<details><summary>Answer</summary>

`no`. Zero counts as False in a condition. `if a:` is the same question as `if a != 0:` here.
</details>

**B6.**

```python
balance = 500
amount = 500
if balance > amount:
    print("Paid")
else:
    print("Refused")
```

<details><summary>Answer</summary>

`Refused`. `>` is strictly greater, and 500 is not greater than 500. Paying your whole balance needs `>=`.
</details>

**B7.**

```python
kyc = "Yes"
if kyc == "yes":
    print("eligible")
else:
    print("not eligible")
```

<details><summary>Answer</summary>

`not eligible`. Text comparison is exact and case-sensitive.
</details>

**B8.**

```python
x = 5
if x > 3:
    print("big")
    print("done")
print("end")
```

<details><summary>Answer</summary>

`big`, `done`, `end`. The first two lines are inside the `if`; `end` is outside and would print either way.
</details>

**B9.**

```python
mode = "UPI"
match mode:
    case "upi":
        print("UPI app")
    case _:
        print("Unknown")
```

<details><summary>Answer</summary>

`Unknown`. A `case` is an exact match, and `"UPI"` is not `"upi"`.
</details>

**B10.**

```python
if 5 > 3:
print("yes")
```

<details><summary>Answer</summary>

`IndentationError: expected an indented block after 'if' statement on line 1`. The program does not run at all.
</details>

---

## C. Explore, with AI in the loop

These connect today's decisions to what you built in the GenAI modules.

**C1. Every router is an `if`.** In n8n and Zapier you used IF nodes, filters and routers. Take one workflow you built and write its branching as Python `if` / `elif` / `else` on paper. How many branches did it really have? Was there an `else`, or did some inputs fall through silently?

**C2. Guardrails are conditions in a fixed order.** An agent may send money only if the PIN is correct, the account is not frozen, and the amount is at most ₹5,000. Write it as a chain that gives a **different message** for each failure. Then answer: does the order of the checks change which message a user sees when two things are wrong at once?

<details><summary>Things to find</summary>

Yes. With a wrong PIN and a frozen account, the first failing check in the chain decides the message. Security code usually checks identity (the PIN) first, so it never reveals anything about the account to someone who is not its owner.
</details>

**C3. Routing a model's reply.** You ask an LLM to classify a support message as `"refund"`, `"complaint"` or `"question"`, then route it with `match`. The model replies `"Refund."` with a capital letter and a full stop. Which `case` runs? What would you add before the `match`?

<details><summary>Things to find</summary>

`case _`, the wildcard, because the text does not match exactly. Options to research: clean the text before matching (lower-case it, strip punctuation; the strings class covers this), or ask for structured output with a fixed list of allowed values.
</details>

**C4. AI as a tester.** Give an assistant your PaisaPay v3 program and ask: "List every path through the decisions in this program and one input that reaches each path. Do not change the code." Run every input. Did it find the path where the PIN is right, the mode is unknown and the balance is low? Which message does that run print, and why that one?

**C5. Catch the AI being wrong.** Without running anything, ask an assistant what this prints:

```python
if "False":
    print("yes")
else:
    print("no")
```

Then run it. The answer is `yes`, because a non-empty string counts as True. Did the assistant get it right? Did it explain why?

**C6. Explain, don't fix.** Paste the ₹8,000 cashback bug from B1 into an assistant and ask: "I expected ₹100 but got ₹10. Walk me through why, without telling me to reorder the conditions." Then reorder them yourself and run it to confirm ₹100.
