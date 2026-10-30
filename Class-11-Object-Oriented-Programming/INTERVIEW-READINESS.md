# Interview Readiness · Class 11

Object-oriented questions test whether you can say what `self` is without hand-waving, whether you know what a class variable shares, and whether you can read inheritance without running it.

How to use this page: answer each question out loud or on paper first, then open the answer. For "predict the output" questions, run the code after you commit to an answer.

- [A. Questions interviewers ask](#a-questions-interviewers-ask)
- [B. Gotchas: predict the output](#b-gotchas-predict-the-output)
- [C. Explore, with AI in the loop](#c-explore-with-ai-in-the-loop)

---

## A. Questions interviewers ask

**A1. What is the difference between a class and an object?**

<details><summary>Answer</summary>

A class is the definition: what every object of that kind has and can do. An object, or instance, is one thing built from it, with its own data. `Dog` is the class; `rex = Dog("Rex")` makes an object. One class, any number of objects.
</details>

**A2. What is `self`?**

<details><summary>Answer</summary>

The object a method is running on. When you call `rex.bark()`, Python passes `rex` as the first argument, and the method receives it as `self`. You write `self` when defining a method and never when calling one. It is a convention, not a keyword.
</details>

**A3. What does `__init__` do, and when does it run?**

<details><summary>Answer</summary>

It sets up a new object's starting state, usually by storing the arguments as `self.` attributes. It runs automatically, once, every time the class is called to make an object. You never call it yourself.
</details>

**A4. What is the difference between a class variable and an instance variable?**

<details><summary>Answer</summary>

A class variable is written in the class body and shared by every object. An instance variable is set through `self.` and belongs to one object. Reading either through an object works. A mutable class variable such as a list is one list shared by all, which is almost always a bug; create lists and dictionaries in `__init__`.
</details>

**A5. What is encapsulation, and does Python enforce it?**

<details><summary>Answer</summary>

Keeping an object's data inside and changing it only through methods, so the rules in those methods cannot be skipped. Python signals it with a leading double underscore, which renames the attribute (name mangling) so a direct read fails. It is a strong convention, not an enforced lock: `_ClassName__attr` still reaches it.
</details>

**A6. What does `super().__init__()` do, and what happens if you forget it?**

<details><summary>Answer</summary>

It runs the parent class's `__init__` on the same object, so the parent's attributes get set. If the child defines its own `__init__` and forgets the call, the parent's setup never runs and the parent's attributes are missing: `AttributeError` on the first read.
</details>

**A7. What is polymorphism? Does it need inheritance?**

<details><summary>Answer</summary>

One method name behaving differently depending on the object: a loop calls `describe()` on each item and each class answers its own way. In Python it does not need inheritance; it needs the method to exist on each object. Inheritance is for sharing code, not for permission to call.
</details>

**A8. What is the difference between overriding and overloading?**

<details><summary>Answer</summary>

Overriding is a child class replacing a parent's method with the same name; Python looks in the child first. Overloading means several versions of one function with different parameter lists, which Python does not do by name; default arguments and `*args` cover the same ground.
</details>

**A9. What is abstraction, in one sentence?**

<details><summary>Answer</summary>

Hiding the steps behind a simple name: the caller of `account.deposit(50)` needs the name and the argument, not the rule inside or how the balance is stored.
</details>

---

## B. Gotchas: predict the output

Commit to an answer before you open each one.

**B1.**

```python
class Dog:
    def __init__(self, name):
        self.name = name

a = Dog("Rex")
b = Dog("Rex")
print(a == b, a.name == b.name)
```

<details><summary>Answer</summary>

`False True`. Two separate objects are not equal by default, even with the same data; their names are.
</details>

**B2.**

```python
class Dog:
    def speak(self):
        return "Woof"

print(Dog.speak)
```

<details><summary>Answer</summary>

`<function Dog.speak at 0x...>`. No brackets, no call: the method itself, printed as a function.
</details>

**B3.**

```python
class Dog:
    legs = 4

a = Dog()
a.legs = 3
print(a.legs, Dog.legs)
```

<details><summary>Answer</summary>

`3 4`. Assigning on the object makes an instance attribute that hides the class one for `a`. The class value is untouched.
</details>

**B4.**

```python
class Dog:
    sounds = []

a = Dog()
b = Dog()
a.sounds.append("woof")
print(len(b.sounds))
```

<details><summary>Answer</summary>

`1`. One shared list on the class; `append` changed it for everyone.
</details>

**B5.**

```python
class P:
    def __init__(self):
        self.x = 1

class C(P):
    def __init__(self):
        self.y = 2

print(C().x)
```

<details><summary>Answer</summary>

`AttributeError: 'C' object has no attribute 'x'`. `C.__init__` replaced `P.__init__` without calling it.
</details>

**B6.**

```python
class P:
    def who(self):
        return "P"

class C(P):
    def who(self):
        return "C" + super().who()

print(C().who())
```

<details><summary>Answer</summary>

`CP`. The child's version runs and calls the parent's through `super()`.
</details>

**B7.**

```python
class Account:
    def __init__(self):
        self.__pin = "1234"

a = Account()
a.__pin = "0000"
print(a._Account__pin)
```

<details><summary>Answer</summary>

`1234`. The assignment from outside made a new attribute literally named `__pin`; the real one is `_Account__pin` and never changed.
</details>

**B8.**

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def rename(self, name):
        name = name

d = Dog("Rex")
d.rename("Max")
print(d.name)
```

<details><summary>Answer</summary>

`Rex`. `name = name` is a local variable. Only `self.name = name` would change the object.
</details>

**B9.**

```python
print(isinstance(True, int), True + True, type(True).__name__)
```

<details><summary>Answer</summary>

`True 2 bool`. `bool` inherits from `int`, so a bool is an int and adds like one.
</details>

**B10.**

```python
class Dog:
    def __init__(self, name):
        self.name = name

d = Dog("Rex")
e = d
e.name = "Max"
print(d.name)
```

<details><summary>Answer</summary>

`Max`. `e = d` is two names for one object, exactly like two names for one list in Class 6.
</details>

---

## C. Explore, with AI in the loop

These connect today's classes to what you built in the GenAI modules.

**C1. A tool is a class.** Take a tool you defined for an agent, a weather lookup or a calculator. Write it as a Python class: the configuration it needs goes in `__init__`, the action is a method. Which parts belong to one tool object and which are shared by every tool of that kind?

**C2. Catch the AI being wrong.** Ask an assistant, without running, what this prints:

```python
class Box:
    items = []

a = Box()
b = Box()
a.items.append(1)
print(b.items)
```

Some answer `[]`. It prints `[1]`. Did yours get it right? Ask it to explain why, then to rewrite the class so the answer becomes `[]`.

**C3. AI-written classes.** Ask an assistant to write an `Account` class with deposit and withdraw. Before running its code, check three things: does every method start with `self`, is every list or dictionary created inside `__init__`, and can anything outside the class set the balance directly? Fix what it got wrong by hand.

**C4. Explain, don't fix.** Paste Part B6 of the assignment into an assistant and ask: "Why does this program fail at `a.add(200)`? Explain all three problems without rewriting the code." Then fix it yourself.

**C5. Design review.** Paste PaisaPay v11 into an assistant and ask: "Which attributes and methods of Account would you move into a separate class, and why? Do not change the code." Decide for each suggestion whether it follows the one-thing-one-job idea or just adds classes.

**C6. Memory as an object.** In the agents module, memory was a store the agent could read and write. Design it as a class: what goes in `__init__`, what are the methods, and what should be private? Then ask an assistant for its version and compare which parts it chose to hide.
