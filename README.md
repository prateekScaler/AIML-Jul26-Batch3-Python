# Python · AIML Jul26 Batch 3

Class material for the Python module of **AIML Jul26 Batch 3**.
Instructor: **Prateek Vijay**

You come to this module from GenAI Foundations 1 and 2, where you prompted LLMs, built workflows and agents, and vibe-coded apps. Here you learn to write, read and debug Python yourself, so that you can check and direct the code AI writes for you.

## Classes

| # | Topic | Material | PaisaPay after this class |
|---|---|---|---|
| 1 | Data Types, Variables, Input/Output | [Open the class page](https://prateekscaler.github.io/AIML-Jul26-Batch3-Python/Class-01-Data-Types-Variables-Input-Output/) · [notes and code](Class-01-Data-Types-Variables-Input-Output/README.md) · [practice](Class-01-Data-Types-Variables-Input-Output/PRACTICE.md) | **v1** takes one payment and prints a receipt |
| 2 | Operators | [Open the class page](https://prateekscaler.github.io/AIML-Jul26-Batch3-Python/Class-02-Operators/) · [notes and code](Class-02-Operators/README.md) · [practice](Class-02-Operators/PRACTICE.md) | **v2** money maths: bill split, cashback, "is the balance enough?" |
| 3 | Control Statements | [Open the class page](https://prateekscaler.github.io/AIML-Jul26-Batch3-Python/Class-03-Control-Statements/) · [notes and code](Class-03-Control-Statements/README.md) · [practice](Class-03-Control-Statements/PRACTICE.md) | **v3** decisions: refuse, approve, cashback tiers |
| 4 | Loops | [Open the class page](https://prateekscaler.github.io/AIML-Jul26-Batch3-Python/Class-04-Loops/) · [notes and code](Class-04-Loops/README.md) · [practice](Class-04-Loops/PRACTICE.md) | **v4** keeps running: menu, PIN retries, mini statement |
| 5 | Functions | [Open the class page](https://prateekscaler.github.io/AIML-Jul26-Batch3-Python/Class-05-Functions/) · [notes and code](Class-05-Functions/README.md) · [practice](Class-05-Functions/PRACTICE.md) | **v5** reusable actions: `pay()`, `add_money()`, `show_balance()` |
| 6 | Lists | [Open the class page](https://prateekscaler.github.io/AIML-Jul26-Batch3-Python/Class-06-Lists/) · [notes and code](Class-06-Lists/README.md) · [practice](Class-06-Lists/PRACTICE.md) | **v6** transaction history |
| 7 | Strings | [Open the class page](https://prateekscaler.github.io/AIML-Jul26-Batch3-Python/Class-07-Strings/) · [notes and code](Class-07-Strings/README.md) · [practice](Class-07-Strings/PRACTICE.md) | **v7** clean input, masked account numbers, formatted receipts |
| 8 | Sets, Tuples, Dictionaries | [Open the class page](https://prateekscaler.github.io/AIML-Jul26-Batch3-Python/Class-08-Sets-Tuples-Dictionaries/) · [notes and code](Class-08-Sets-Tuples-Dictionaries/README.md) · [practice](Class-08-Sets-Tuples-Dictionaries/PRACTICE.md) | **v8** a tuple per payment, a set of payees, contacts and totals as dictionaries |
| 9 | Functional Programming | coming up | **v9** spending insights with `map`, `filter` and `sorted` |
| 10 | OOP | coming up | **v10** `Account`, `Wallet` and `Transaction` classes |
| 11 | Regex | coming up | **v11** validates UPI IDs and reads bank SMS alerts |
| 12 | File Handling and Modules | coming up | **v12** saves its data and is split into modules |

## What is in every class folder

| File | Use it for |
|---|---|
| `index.html` | The interactive class page: questions, predictions, real incidents and the project build. Open it from the link in the table above; no download needed. **Step by step** reveals one thing at a time (press → or Next); **Show everything** gives the whole class on one page. |
| `README.md` | The full class notes, readable on GitHub. |
| `code/` | Every example from the class as a runnable file, in order, plus that class's PaisaPay version. |
| `Python-Class-NN-….ipynb` | The same examples as one notebook. Open it in Google Colab from the class notes and run the cells; nothing to install. |
| `ASSIGNMENT.md` | Practice problems. |
| `INTERVIEW-READINESS.md` | Questions interviewers ask, predict-the-output gotchas, and questions that connect the topic to AI systems. |
| `PRACTICE.md` | Twelve coding problems on the class topics, easy to hard, with sample output, hints and solutions. |

## The project: PaisaPay

One app, built across all twelve classes: a small UPI-style payments program. Every class adds one capability, so each new topic has an immediate use. Each class folder holds the version reached that day (`code/paisapay_vN.py`), which makes the growth easy to follow from one class to the next.

## Running the code

- **In the browser:** [PyLens](https://scaler-pylens.vercel.app/) shows what Python does at every line. Copy any file from a `code/` folder into it.
- **On your machine:** install Python 3.10 or newer, then run `python3 filename.py` inside the `code/` folder.

## Studying with an AI assistant

Point your assistant at a class folder and make it work for your understanding rather than replace it.

- "Read `Class-01-Data-Types-Variables-Input-Output/README.md` and quiz me with ten predict-the-output questions, one at a time. Do not show answers until I reply."
- "Here is an error I got. Explain it in plain English. Do not give me the fix yet."
- "Here is my solution to Part B of the assignment. List inputs that would break it. Do not rewrite it."

Then run the code yourself. A fix is accepted when your own run proves it.
