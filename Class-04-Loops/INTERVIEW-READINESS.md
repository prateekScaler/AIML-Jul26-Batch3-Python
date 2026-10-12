# Interview Readiness · Class 4

Loops are where interviewers check whether you can trace code: how many times a block runs, what the variable holds on each pass, and whether the loop ends at all.

How to use this page: answer each question out loud or on paper first, then open the answer. For "predict the output" questions, run the code after you commit to an answer.

- [A. Questions interviewers ask](#a-questions-interviewers-ask)
- [B. Gotchas: predict the output](#b-gotchas-predict-the-output)
- [C. Explore, with AI in the loop](#c-explore-with-ai-in-the-loop)

---

## A. Questions interviewers ask

**A1. What does `range(start, stop, step)` produce?**

<details><summary>Answer</summary>

The numbers from `start`, moving by `step`, stopping *before* `stop`. `range(5)` is 0 to 4. `range(1, 6)` is 1 to 5. `range(10, 0, -1)` is 10 down to 1. With one argument the start is 0 and the step is 1. `range(10, 0)` is empty, because the default step is +1 and 10 is already past 0.
</details>

**A2. When do you use `for` and when `while`?**

<details><summary>Answer</summary>

`for` when you know the sequence or the number of passes: every item in a list, months 1 to 12. `while` when you know the stopping condition but not the count: ask until the PIN is correct, keep going until the balance runs out, keep the agent working until the task is done.
</details>

**A3. What is an infinite loop and how do you avoid one?**

<details><summary>Answer</summary>

A `while` loop whose condition never becomes False. Two causes: nothing inside the loop changes the variable the condition reads, or the variable changes but jumps over the value the condition waits for (`!= 0` with steps of 300). Avoid it by updating the right variable on every path through the body, and by preferring `>=` or `<=` to `!=`.
</details>

**A4. What is the difference between `break`, `continue` and `pass`?**

<details><summary>Answer</summary>

`break` leaves the whole loop at once. `continue` skips the rest of the current pass and goes to the next one. `pass` does nothing at all; it is a placeholder where Python requires a statement. `break` ends only the loop, not the program.
</details>

**A5. Why can `continue` be dangerous in a `while` loop?**

<details><summary>Answer</summary>

Because it jumps straight back to the condition, skipping everything below it, including the line that updates the counter. The variable stays the same, the condition stays True, and the loop is stuck. In a `for` loop `range` moves on by itself.
</details>

**A6. In a nested loop, how many times does the inner body run?**

<details><summary>Answer</summary>

Outer passes multiplied by inner passes. For `range(3)` outside and `range(2)` inside, 6 times. The inner loop restarts from its first value on every outer pass, and it may use the outer loop's variable, for example `range(row)` to print a triangle.
</details>

**A7. What is the accumulator pattern, and where does the starting value go?**

<details><summary>Answer</summary>

A variable that collects a result across passes: `total = 0` before the loop, `total += amount` inside it, use `total` after it. The starting value must sit above the loop; inside, it would be reset on every pass and only the last item would count.
</details>

**A8. What value does the loop variable hold after a `for` loop ends?**

<details><summary>Answer</summary>

The last value it was given. It is an ordinary variable and is not deleted or reset. If the loop ran zero times, the variable was never created and using it raises `NameError`.
</details>

---

## B. Gotchas: predict the output

Commit to an answer before you open each one.

**B1.**

```python
for i in range(1, 11, 3):
    print(i, end=" ")
```

<details><summary>Answer</summary>

`1 4 7 10`. Start 1, step 3, stop before 11. 10 is included because 10 is less than 11.
</details>

**B2.**

```python
for i in range(3, 3):
    print("hello")
print("done")
```

<details><summary>Answer</summary>

`done` only. `range(3, 3)` is empty, so the body runs zero times. No error.
</details>

**B3.**

```python
count = 5
while count > 0:
    count -= 2
print(count)
```

<details><summary>Answer</summary>

`-1`. 5, 3, 1, then −1. The condition is checked only between passes, so the value can go past 0.
</details>

**B4.**

```python
for i in range(1, 6):
    if i == 3:
        break
    print(i)
else_text = "after"
print(else_text)
```

<details><summary>Answer</summary>

`1`, `2`, `after`. `break` leaves the loop; the two lines after the loop still run.
</details>

**B5.**

```python
total = 0
for i in range(1, 4):
    for j in range(1, 3):
        total += 1
print(total)
```

<details><summary>Answer</summary>

`6`. The inner body runs 3 × 2 times.
</details>

**B6.**

```python
n = 0
while n < 3:
    n += 1
    if n == 2:
        continue
    print(n)
```

<details><summary>Answer</summary>

`1`, `3`. The update happens before the `continue`, so the loop is not stuck; 2 is simply not printed.
</details>

**B7.**

```python
found = False
for x in [1, 2, 3]:
    if x == 2:
        found = True
    else:
        found = False
print(found)
```

<details><summary>Answer</summary>

`False`. At 2 it becomes True, then 3 is not 2 and the `else` sets it back. Without the `else`, or with a `break` after `found = True`, it would print True.
</details>

**B8.**

```python
for i in range(3):
    pass
print(i)
```

<details><summary>Answer</summary>

`2`. `pass` does nothing, the loop runs three times, and the variable keeps its last value.
</details>

**B9.**

```python
for i in range(1, 4):
    print(i)
    i = 10
```

<details><summary>Answer</summary>

`1`, `2`, `3`. Changing `i` inside the body does not affect the loop; on the next pass `range` assigns the next value.
</details>

**B10.**

```python
amount = 1000
while amount > 0:
    amount = amount // 2
    print(amount, end=" ")
```

<details><summary>Answer</summary>

`500 250 125 62 31 15 7 3 1 0`. Integer division keeps halving until it reaches 0, then `0 > 0` is False.
</details>

---

## C. Explore, with AI in the loop

These connect today's loops to what you built in the GenAI modules.

**C1. The agent loop.** Every agent framework you used runs something like `while not done: think, act, observe`. Write that loop in Python with `input()` standing in for the model: ask "Is the task done? (yes/no)" each pass and count the passes. Then add a maximum of 5 passes. Why do real frameworks have that limit?

<details><summary>Things to find</summary>

A model can keep answering "not done" for ever, or keep calling the same tool. A maximum number of steps is the `break` that protects you from an infinite loop and an infinite bill.
</details>

**C2. Retries.** When an API call fails, well-written code retries a few times and then gives up. Write a loop that "calls" a tool by asking `Did it work? (yes/no)`, retries up to three times, and prints `Giving up` after the third failure. Which loop did you choose, and where is the `break`?

**C3. n8n loops.** In n8n a Loop Over Items node runs the next nodes once per item. Take a workflow you built and write the same thing as a Python `for` over a list. Which n8n setting corresponds to `break`?

**C4. AI as a tester.** Give an assistant your PaisaPay v4 program and ask: "List every input sequence that makes a loop in this program run for ever or exit early. Do not change the code." Run each sequence. Did it find that typing letters for the amount crashes the program with `ValueError`? That is not a loop bug, but it ends the menu loop. What would you need to protect against it? (Class 7 covers input cleaning.)

**C5. Catch the AI being wrong.** Without running anything, ask an assistant what this prints:

```python
for i in range(10, 0):
    print(i)
print("end")
```

Many assistants say "10 down to 1". The answer is `end` only. Did yours get it right? Then ask it to explain why its first answer was wrong.

**C6. Explain, don't fix.** Paste the stuck `while` loop with `continue` (B6 from the class, where the update comes after the `continue`) into an assistant and ask: "Walk me through the first five passes of this loop without changing it." Check its trace against your own.
