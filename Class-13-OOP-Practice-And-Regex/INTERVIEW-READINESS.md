# Interview Readiness · Class 13

Interviewers use inheritance and regex to test whether you can trace what Python does, not whether you can recite a definition. The questions below ask where an attribute was set, which method runs, and when inheritance is the wrong tool.

How to use this page: answer each question out loud or on paper first, then open the answer. For "predict the output" questions, run the code after you commit to an answer.

- [A. Questions interviewers ask](#a-questions-interviewers-ask)
- [B. Gotchas: predict the output](#b-gotchas-predict-the-output)
- [C. Explore, with AI in the loop](#c-explore-with-ai-in-the-loop)

---

## A. Questions interviewers ask

**A1. What is encapsulation, and does Python enforce it?**

<details><summary>Answer</summary>

Keeping an object's data inside and changing it only through methods, so the rules in those methods cannot be skipped. Python signals it with a leading double underscore, which renames the attribute (name mangling) so a plain outside read fails. It is a strong convention, not an enforced lock: `_ClassName__attr` still reaches it.
</details>

**A2. What is the difference between encapsulation and abstraction?**

<details><summary>Answer</summary>

Encapsulation hides the data: the balance sits behind `deposit` and `get_balance`. Abstraction hides the steps: whoever calls `deposit(50)` needs the name and the argument, not the rule inside or how the balance is stored. Most classes do both.
</details>

**A3. What is polymorphism? Does it need inheritance in Python?**

<details><summary>Answer</summary>

One call behaving differently per object: a loop calls `describe()` on each item and each class answers its own way. Python only needs the method to exist on each object; a shared parent is not required. Inheritance is for sharing code, not for permission to call. People call this duck typing.
</details>

**A4. What does `super()` do, and what does it return in a chain of three classes?**

<details><summary>Answer</summary>

It gives access to the next class up from the one the method is written in, on the same object. In `Director(Manager)`, `super()` inside a Director method reaches Manager; inside a Manager method it reaches Employee. Used in `__init__` so every level sets its own attributes on one object.
</details>

**A5. When would you override a method and call `super()`, and when would you not call it?**

<details><summary>Answer</summary>

Call it when the child adds to the parent's behaviour: a check before, or extra words after. Leave it out when the child replaces the rule entirely, such as a premium account whose fee is always zero. If you find yourself retyping the parent's lines, you wanted `super()`.
</details>

**A6. `isinstance` versus `type`: which should you use, and why?**

<details><summary>Answer</summary>

`isinstance(obj, Parent)` is True for the parent and every child, because it walks up the tree. `type(obj) == Parent` is True only for the exact class. Code that checks a class almost always wants children to count too, so `isinstance`. Better still, do not check at all and call the method: polymorphism.
</details>

**A7. How do you decide between inheritance and composition?**

<details><summary>Answer</summary>

Say the sentence. "A premium account is an account": inherit. "An account has transactions": hold a list of them, which is composition. Inheriting when the relationship is has-a gives the child methods and data that make no sense for it.
</details>

**A8. Can a parent class call a method that only a child defines?**

<details><summary>Answer</summary>

Not on a plain parent object: the lookup walks up from the object's class and never down, so `Employee().approve_leave()` is an `AttributeError`. A parent's method can call `self.something()` that only children define, but then it only works on child objects.
</details>

**A9. What is the difference between `re.search`, `re.match` and `re.fullmatch`?**

<details><summary>Answer</summary>

`search` finds the first fit anywhere. `match` tests only the start of the string. `fullmatch` needs the whole string to fit. To check a form field, use `fullmatch`; with `search`, `hello sumit@ybl!!!` would pass a UPI pattern.
</details>

**A10. Why write patterns as raw strings?**

<details><summary>Answer</summary>

Python processes backslashes in a normal string before regex sees them. In `"\bword"`, Python turns `\b` into a backspace character, but regex wanted a word boundary. `r"\bword"` hands the backslash to regex untouched. An unknown escape such as `"\d"` also raises a `SyntaxWarning`.
</details>

**A11. What does greedy mean, and how do you turn it off?**

<details><summary>Answer</summary>

`*` and `+` take as much as they can, then give back only what the rest of the pattern needs. `<.+>` on `<a><b>` matches the whole string. Add a `?` for the shortest fit: `<.+?>` matches `<a>`.
</details>

**A12. What is catastrophic backtracking?**

<details><summary>Answer</summary>

When a pattern can split text between its parts in many ways, such as `.*.*=.*`, the engine retries the ways when the match fails, and the work grows quickly with the input. Cloudflare's 27-minute outage in 2019 came from this. Prefer an exact class and count, and test on input that should fail.
</details>

**A13. When should you not use a regex?**

<details><summary>Answer</summary>

When the text has a real structure with a real parser: JSON, HTML, CSV. Use `json.loads` for JSON. Also when a plain string method is enough: `"@" in text` needs no pattern. Regex is for shapes in plain text.
</details>

---

## B. Gotchas: predict the output

Commit to an answer before you open each one.

**B1.**

```python
class A:
    def who(self):
        return "A"

class B(A):
    def who(self):
        return "B" + super().who()

class C(B):
    def who(self):
        return "C" + super().who()

print(C().who())
```

<details><summary>Answer</summary>

`CBA`. Each level calls the next one up. `super()` in C reaches B, and `super()` in B reaches A.
</details>

**B2.**

```python
class P:
    def __init__(self):
        self.x = 1

class C(P):
    def __init__(self):
        super().__init__()
        self.x = 2

print(C().x)
```

<details><summary>Answer</summary>

`2`. The parent set `x` to 1 on the object, then the child set the same attribute to 2. Order matters: swap the two lines and it prints 1.
</details>

**B3.**

```python
class A:
    pass

class B(A):
    pass

print(isinstance(B(), A), isinstance(A(), B), type(B()) == A)
```

<details><summary>Answer</summary>

`True False False`. A B is an A. An A is not a B. `type` names the exact class.
</details>

**B4.**

```python
class Account:
    def __init__(self):
        self.__pin = "1234"

a = Account()
a.__pin = "0000"
print(a._Account__pin, a.__pin)
```

<details><summary>Answer</summary>

`1234 0000`. The outside assignment made a new attribute literally named `__pin`; the real one is `_Account__pin` and never changed. Now both exist.
</details>

**B5.**

```python
class Dog:
    def speak(self):
        return "Woof"

class Stone:
    pass

for thing in [Dog(), Stone()]:
    print(thing.speak())
```

<details><summary>Answer</summary>

`Woof`, then `AttributeError: 'Stone' object has no attribute 'speak'`. Polymorphism needs the method on every object. The first line prints before the error.
</details>

**B6.**

```python
class Wallet:
    def pay(self, amount):
        return f"paid {amount}"

class Capped(Wallet):
    def pay(self, amount):
        if amount > 100:
            return "refused"
        return super().pay(amount)

print(Capped().pay(50), Capped().pay(500))
```

<details><summary>Answer</summary>

`paid 50 refused`. The check runs first; only amounts within the cap reach the parent.
</details>

**B7.**

```python
class Employee:
    count = 0

    def __init__(self):
        Employee.count += 1

class Manager(Employee):
    pass

Employee()
Manager()
Manager()
print(Employee.count, Manager.count)
```

<details><summary>Answer</summary>

`3 3`. Manager inherits `__init__`, which adds to `Employee.count`. `Manager.count` is read through the parent: the same single value.
</details>

**B8.**

```python
class A:
    def __init__(self):
        self.__secret = 1

class B(A):
    def reveal(self):
        return self.__secret

print(B().reveal())
```

<details><summary>Answer</summary>

`AttributeError: 'B' object has no attribute '_B__secret'`. Name mangling uses the class the code is written in: A stored `_A__secret`, but B's method looks for `_B__secret`. Double underscores hide attributes from child classes too; one underscore would have worked.
</details>

**B9.**

```python
import re

print(bool(re.search(r"^\d{3}$", "123\n")))
print(bool(re.fullmatch(r"\d{3}", "123\n")))
```

<details><summary>Answer</summary>

```text
True
False
```

`$` also matches just before a final newline, so a check with `^...$` lets `"123\n"` through. `fullmatch` does not. Prefer `fullmatch` for checking input.
</details>

**B10.**

```python
import re

print(re.search(r"<.+>", "<a><b>").group())
print(re.search(r"<.+?>", "<a><b>").group())
```

<details><summary>Answer</summary>

```text
<a><b>
<a>
```

`+` is greedy and takes as much as it can. `+?` takes the least.
</details>

**B11.**

```python
import re

print(re.findall(r"a*", "baaa"))
```

<details><summary>Answer</summary>

```text
['', 'aaa', '']
```

`*` allows zero, so an empty match counts: one before `b`, then `aaa`, then one at the end.
</details>

**B12.**

```python
import re

print(re.findall(r"\d-\d", "1-2 3-4"))
print(re.findall(r"(\d)-\d", "1-2 3-4"))
print(re.findall(r"(\d)-(\d)", "1-2 3-4"))
```

<details><summary>Answer</summary>

```text
['1-2', '3-4']
['1', '3']
[('1', '2'), ('3', '4')]
```

No group: whole matches. One group: only that group. Two groups: tuples.
</details>

**B13.**

```python
import re

print(bool(re.fullmatch(r"report.pdf", "reportXpdf")))
print(bool(re.fullmatch(r"report\.pdf", "reportXpdf")))
print(re.findall(r"[.]", "a.b"))
```

<details><summary>Answer</summary>

```text
True
False
['.']
```

An unescaped dot is any character. Inside square brackets, a dot is just a dot.
</details>

**B14.**

```python
import re

m = re.match(r"\d+", "Rs.600")
print(m)
print(re.search(r"\d+", "Rs.600").span())
```

<details><summary>Answer</summary>

```text
None
(3, 6)
```

`match` tests the start, and the string starts with `R`. `search` finds `600` from index 3 up to, not including, index 6.
</details>

---

## C. Explore, with AI in the loop

These connect today's ideas to what you built in the GenAI modules.

**C1. Tools as a family.** Every tool an agent can call has a name, a description and a `run(input)`. Design a `Tool` parent and two children (a calculator, a web search). Which parts are shared, which are overridden, and does `run` in a child call `super().run`? Then ask an assistant for its version and compare the split.

**C2. Catch the AI being wrong.** Ask an assistant, without running, what B8 prints. Many say `1`. Make it explain name mangling in a child class, then run the code.

**C3. is-a audit.** Paste an AI-written class hierarchy (ask for "an e-commerce system with classes") and for every `class X(Y)` write the sentence "an X is a Y". List the ones where the sentence is false and ask the assistant to fix only those.

**C4. Explain, don't fix.** Paste Part B6 of the assignment into an assistant and ask: "Why does this program fail? Explain all three problems without rewriting the code." Then fix it yourself.

**C5. Design review.** Paste PaisaPay v13 with your StudentAccount into an assistant and ask: "Does StudentAccount's pay call super()? If every account type adds one check before paying, is there a better place for the checks than each subclass?" Decide whether its answer keeps the rules in one place.

**C6. Memory as a hierarchy.** In the agents module, memory had kinds: short-term, long-term, a vector store. Design a `Memory` parent with `store(item)` and `recall(query)`, and children that override them. Which methods should call `super()` and which should replace the parent entirely?

**C7. A pattern in a tool schema.** JSON Schema, which you met in agent tool definitions, has a `pattern` keyword. Write the schema for a `pay` tool whose `upi_id` argument must match your UPI pattern. If the model sends a wrong value, what should happen: refuse, retry, or ask the user?

**C8. LLM output is text.** Ask a model for a total in a sentence, three times, and pull the number out with one regex. Does it survive small wording changes? Then ask the model for JSON and use `json.loads`. Which one would you put in production, and why?

**C9. Catch the AI being wrong.** Ask an assistant for a regex that checks an Indian mobile number. Test it on `5876543210`, `98765432101` and `"9876543210\n"`. Did it use `fullmatch`? Ask it to explain each failure, then fix the pattern yourself.
