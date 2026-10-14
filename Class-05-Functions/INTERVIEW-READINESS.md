# Interview Readiness · Class 5

Functions are where interviewers check whether you understand how a program is organised: what goes in, what comes out, and what lives where.

How to use this page: answer each question out loud or on paper first, then open the answer. For "predict the output" questions, run the code after you commit to an answer.

- [A. Questions interviewers ask](#a-questions-interviewers-ask)
- [B. Gotchas: predict the output](#b-gotchas-predict-the-output)
- [C. Explore, with AI in the loop](#c-explore-with-ai-in-the-loop)

---

## A. Questions interviewers ask

**A1. What is the difference between a parameter and an argument?**

<details><summary>Answer</summary>

A parameter is the variable named in the definition, `def greet(name)`. An argument is the actual value passed at the call, `greet("Uma")`. Arguments are matched to parameters by position, or by name with keyword arguments.
</details>

**A2. What is the difference between `print` and `return`?**

<details><summary>Answer</summary>

`print` shows a value on the screen for the human and gives nothing back to the program. `return` hands a value back to the caller so it can be stored or used, and it ends the function at once. A function with no `return`, or that reaches its end without one, returns `None`.
</details>

**A3. What does a function return if it has no `return` statement?**

<details><summary>Answer</summary>

`None`. The same happens if `return` sits on one path only, for example inside an `if` with no `else`: the other path falls off the end and returns `None`.
</details>

**A4. Explain local and global scope.**

<details><summary>Answer</summary>

A variable created inside a function is local: it exists only while that call runs and is gone afterwards. A variable created outside any function is global and can be read inside functions. Assigning to a global's name inside a function creates a new local instead; the clean habit is to pass values in as arguments and hand them out with `return`.
</details>

**A5. What is a default argument, and what is a keyword argument?**

<details><summary>Answer</summary>

A default argument gives a parameter a fallback, `def pay(amount, mode="upi")`, used when the caller does not supply that argument. A keyword argument names the parameter at the call, `pay(mode="card", amount=500)`, so order does not matter. Positional arguments must come before keyword arguments in a call.
</details>

**A6. What is a lambda, and when would you use one?**

<details><summary>Answer</summary>

A small anonymous function made of parameters, a colon and one expression whose value is returned: `lambda x: x * 2`. Use it for short, throw-away operations, for example when a function is passed to another function. Anything with more than one expression, or that deserves a name, should be a `def`.
</details>

**A7. Why should a function do one thing?**

<details><summary>Answer</summary>

A function with one job has a clear name, is easy to test alone, and can be reused and changed without touching anything else. PaisaPay v5 splits `pay` from `fee_for`, `cashback_for` and the validation helpers for exactly that reason.
</details>

**A8. What happens if you call a function with the wrong number of arguments?**

<details><summary>Answer</summary>

`TypeError`. Too few: `missing 1 required positional argument`. Too many: `takes 1 positional argument but 2 were given`. Defaults reduce the required count; they do not remove the check.
</details>

---

## B. Gotchas: predict the output

Commit to an answer before you open each one.

**B1.**

```python
def f():
    return "a"
    return "b"

print(f())
```

<details><summary>Answer</summary>

`a`. The first `return` ends the function.
</details>

**B2.**

```python
def g(x):
    x = x + 1

n = 5
g(n)
print(n)
```

<details><summary>Answer</summary>

`5`. `x` is the function's own local variable. Changing it does not change `n`.
</details>

**B3.**

```python
def h(a, b=2, c=3):
    return a + b + c

print(h(1), h(1, 1), h(1, c=1))
```

<details><summary>Answer</summary>

`6 5 4`. Defaults fill what is missing; the keyword picks which parameter gets the 1.
</details>

**B4.**

```python
def say():
    print("hi")

x = say()
print(x)
```

<details><summary>Answer</summary>

`hi`, then `None`. The call prints, but hands nothing back.
</details>

**B5.**

```python
def count():
    n = 0
    n += 1
    return n

print(count(), count())
```

<details><summary>Answer</summary>

`1 1`. Each call starts fresh: `n` is created at 0 every time.
</details>

**B6.**

```python
def outer():
    def inner():
        return "in"
    return inner()

print(outer())
```

<details><summary>Answer</summary>

`in`. A function may be defined inside another and called there. `inner` is local to `outer`.
</details>

**B7.**

```python
square = lambda x: x * x
print(square)
```

<details><summary>Answer</summary>

Something like `<function <lambda> at 0x...>`. Without parentheses you print the function itself, not a result.
</details>

**B8.**

```python
def total(a, b):
    return a + b

print(total(b=1, 2))
```

<details><summary>Answer</summary>

`SyntaxError: positional argument follows keyword argument`. Nothing runs.
</details>

**B9.**

```python
limit = 100

def check(amount):
    return amount <= limit

limit = 50
print(check(75))
```

<details><summary>Answer</summary>

`False`. The function reads the global `limit` when it runs, not when it was defined, and by then it is 50.
</details>

**B10.**

```python
def pay(balance, amount):
    if amount > balance:
        print("Refused")
    return balance - amount

print(pay(100, 500))
```

<details><summary>Answer</summary>

`Refused`, then `-400`. The `return` is outside the `if`, so the subtraction happens anyway. Put `return balance` inside the `if`.
</details>

---

## C. Explore, with AI in the loop

These connect today's functions to what you built in the GenAI modules.

**C1. A tool is a function.** Pick one tool you gave an agent in n8n or an MCP server. Write its Python signature: `def name(param1, param2=default):` and one line saying what it returns. Which parts of the tool schema map to which parts of the line? What does the schema have that the Python line does not?

<details><summary>Things to find</summary>

The schema carries a description and a type for every parameter; Python's plain `def` line does not. Class 7 and later add type hints and docstrings that close that gap. The model reads the schema the way a teammate reads your function name and parameters.
</details>

**C2. Why `return` and not `print` in a tool.** An agent calls `get_balance()`. If the function prints the balance and returns nothing, what does the agent receive? Write a four-line version of each and say which one the agent can reason about.

**C3. Defaults are policy.** `pay(balance, payee, amount, mode="upi")` makes UPI the default. Where else in PaisaPay would a default be a product decision rather than a convenience? Name two and say who should decide them.

**C4. AI as a reviewer.** Paste PaisaPay v5 into an assistant and ask: "List every function, its parameters, what it returns, and whether any path can return None. Do not change the code." Check each claim by reading the code. Did it notice that every refusal path in `pay` returns the balance?

**C5. Catch the AI being wrong.** Ask an assistant, without running, what this prints:

```python
def update(balance):
    balance = balance + 100

balance = 1000
update(balance)
print(balance)
```

Many answer 1100. It prints `1000`. The parameter is a local copy; nothing was returned or stored. Did yours get it right on the first try?

**C6. Explain, don't fix.** Paste B10 into an assistant and ask: "Why does this print −400 after Refused? Explain without rewriting the function." Then fix it yourself and run `pay(100, 500)` again.
