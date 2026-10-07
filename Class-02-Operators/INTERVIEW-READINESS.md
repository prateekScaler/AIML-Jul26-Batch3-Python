# Interview Readiness · Class 2

Operators look simple. Interviewers use them to see whether you can read an expression the way Python does.

How to use this page: answer each question out loud or on paper first, then open the answer. For "predict the output" questions, run the code after you commit to an answer.

- [A. Questions interviewers ask](#a-questions-interviewers-ask)
- [B. Gotchas: predict the output](#b-gotchas-predict-the-output)
- [C. Explore, with AI in the loop](#c-explore-with-ai-in-the-loop)

---

## A. Questions interviewers ask

**A1. What is the difference between `/`, `//` and `%`?**

<details><summary>Answer</summary>

`/` is true division and always returns a float: `7 / 2` is `3.5`, `6 / 2` is `3.0`.
`//` is floor division: it returns the whole part, `7 // 2` is `3`.
`%` is modulus: it returns the remainder, `7 % 2` is `1`.

`//` and `%` belong together: `7 == (7 // 2) * 2 + (7 % 2)`.

A stronger answer adds that `//` rounds **down**, not toward zero: `-7 // 2` is `-4`.
</details>

**A2. What is the difference between `==` and `is`?**

<details><summary>Answer</summary>

`==` compares **values**: do these two things hold the same data?
`is` compares **identity**: are these two names pointing at the very same object?

```python
a = [100, 200]
b = [100, 200]
a == b   # True
a is b   # False
```

Use `==` to compare values. `is` is mainly used as `x is None`.
</details>

**A3. What is the difference between `=` and `==`?**

<details><summary>Answer</summary>

`=` assigns a value to a name. `==` asks whether two values are equal and returns a bool. `age = 20` stores; `age == 20` checks.
</details>

**A4. What is operator precedence? Where do `not`, `and` and `or` sit?**

<details><summary>Answer</summary>

It is the fixed order in which Python evaluates the operators of one expression: parentheses, then `**`, then `* / // %`, then `+ -`, then comparisons, then `not`, then `and`, then `or`.

So `True or False and False` is `True or (False and False)`, which is `True`. When an expression mixes `and` and `or`, write the parentheses.
</details>

**A5. What is short-circuit evaluation?**

<details><summary>Answer</summary>

Python stops evaluating a logical expression as soon as the answer is known.

- `A and B`: if `A` is False, `B` is never evaluated.
- `A or B`: if `A` is True, `B` is never evaluated.

This is useful for safe checks: `people != 0 and amount / people > 100` never divides by zero.
</details>

**A6. How do you check whether a number is even? How do you get its last digit?**

<details><summary>Answer</summary>

`number % 2 == 0` is True for an even number. `number % 10` gives the last digit: `2579 % 10` is `9`.
</details>

**A7. Is `x += 1` exactly the same as `x = x + 1`?**

<details><summary>Answer</summary>

For numbers and strings, yes: both compute the new value and store it under `x`. (For lists, which come later, `+=` changes the existing list in place, which is a real difference.)
</details>

**A8. Why would you use `//` instead of `/` when working with money?**

<details><summary>Answer</summary>

`/` returns a float, and floats cannot store many decimals exactly. Money is kept as an integer in the smallest unit (paise), and integer arithmetic uses `//` and `%`: `share = total // people`, `left_over = total % people`. Nothing is lost and the remainder is handled on purpose.
</details>

---

## B. Gotchas: predict the output

Commit to an answer before you open each one.

**B1.**

```python
print(7 / 2, 7 // 2, 7 % 2)
```

<details><summary>Answer</summary>

`3.5 3 1`
</details>

**B2.**

```python
print(-7 // 2)
```

<details><summary>Answer</summary>

`-4`. Floor division rounds down, toward the smaller number. It does not simply drop the decimals.
</details>

**B3.**

```python
print(2 ** 3 ** 2)
```

<details><summary>Answer</summary>

`512`. Power is evaluated from right to left: `2 ** (3 ** 2)` is `2 ** 9`.
</details>

**B4.**

```python
print(-2 ** 2)
```

<details><summary>Answer</summary>

`-4`. Power goes before the minus sign: `-(2 ** 2)`. Write `(-2) ** 2` to get `4`.
</details>

**B5.**

```python
print(10 == 10.0)
print("10" == 10)
```

<details><summary>Answer</summary>

`True`, then `False`. An int and a float with the same value are equal. A string is never equal to a number.
</details>

**B6.**

```python
print(3 > 2 > 1)
print(1 < 3 < 2)
```

<details><summary>Answer</summary>

`True`, then `False`. Python lets you chain comparisons: `3 > 2 > 1` means `3 > 2 and 2 > 1`.
</details>

**B7.**

```python
x = 5
x =+ 2
print(x)
```

<details><summary>Answer</summary>

`2`. `=+ 2` is plain assignment of `+2`. The shortcut is `+=`.
</details>

**B8.**

```python
print(0 or 5)
print("" or "guest")
print(3 and 7)
```

<details><summary>Answer</summary>

`5`, `guest`, `7`. `or` returns the first value that counts as true; `and` returns the last value if all count as true. This is why `name = typed_name or "guest"` works as a default.
</details>

**B9.**

```python
print("a" in "paisa")
print("A" in "paisa")
```

<details><summary>Answer</summary>

`True`, then `False`. Membership in text is case-sensitive.
</details>

**B10.**

```python
print(10 % 3 * 2)
print(10 % (3 * 2))
```

<details><summary>Answer</summary>

`2`, then `4`. `%` and `*` have the same precedence and run left to right: `(10 % 3) * 2`.
</details>

**B11.**

```python
print(not True == False)
```

<details><summary>Answer</summary>

`True`. Comparison goes before `not`: `not (True == False)` is `not False`.
</details>

---

## C. Explore, with AI in the loop

These connect today's operators to what you built in the GenAI modules.

**C1. Why agents use a code tool for maths.** Ask an assistant, without letting it run code: "What is 23957 * 4873? Answer directly." Then run `print(23957 * 4873)`. Try three more large multiplications. How often was it exactly right? What does that tell you about when an agent should call a tool?

<details><summary>Things to find</summary>

The exact answer is `116742461`. A language model predicts text; it does not calculate. Python calculates exactly, every time. Agent builders give the model a calculator or code tool for this reason.
</details>

**C2. An IF node is a boolean expression.** In a workflow you set: "amount is greater than 5000" AND "customer is verified", OR "customer is premium". Write it as one Python expression. Then answer: is a premium customer with an unverified account and a ₹100 payment allowed?

<details><summary>Things to find</summary>

`amount > 5000 and is_verified or is_premium`. Because `and` goes before `or`, this is `(amount > 5000 and is_verified) or is_premium`, so the premium customer is allowed whatever the amount. If you meant something else, parentheses are the only way to say it.
</details>

**C3. A guardrail for an agent.** Your agent may send money only when the amount is at most ₹5,000, the recipient is verified and the account is not frozen. Write `can_send` as a single expression using three variables. Test all the cases where exactly one condition fails.

<details><summary>Things to find</summary>

`can_send = amount <= 5000 and is_verified and not is_frozen`. With `and`, one False anywhere makes the whole result False. That is the property you want from a safety check.
</details>

**C4. When the model answers "true".** You ask an LLM "Is this transaction suspicious? Answer true or false." It may reply `True`, `true`, `TRUE` or `Yes, it is.` Your code does `is_suspicious = reply == "True"`. Which replies does your code treat as suspicious? What would you change?

<details><summary>Things to find</summary>

Only the exact text `True`. Every other reply becomes `False`, silently, which here means "not suspicious". Text comparison is exact. Options to research: normalise the text before comparing, or ask for structured output with a declared boolean type.
</details>

**C5. AI as a tester.** Give an assistant your `can_enter` program and ask: "Give me eight test inputs that cover every case, including the boundary values. Do not change the code." Run all eight. Did it include age 18 exactly? Did it include `Yes` with a capital letter?

**C6. Catch the AI being wrong.** Without running anything, ask an assistant what `-7 // 2`, `2 ** 3 ** 2` and `-2 ** 2` return. Then run them. Note which ones it got wrong and why each is surprising.

**C7. Token budgets are arithmetic.** A request used 1,250 prompt tokens and 430 completion tokens. The limit is 8,000. Write two lines of Python: one that computes the total, one that stores whether the request is within the limit.

<details><summary>Things to find</summary>

```python
total_tokens = 1250 + 430              # 1680
within_limit = total_tokens <= 8000    # True
```

Cost tracking, rate limits and context-window checks in AI systems are all this: arithmetic, then a comparison.
</details>
