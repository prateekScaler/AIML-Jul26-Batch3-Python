# Python · AIML Jul26 Batch 3

Class material for the Python module of **AIML Jul26 Batch 3**.
Instructor: **Prateek Vijay**

You come to this module from GenAI Foundations 1 and 2, where you prompted LLMs, built workflows and agents, and vibe-coded apps. Here you learn to write, read and debug Python yourself, so that you can check and direct the code AI writes for you.

## Classes

| # | Topic | Material | PaisaPay after this class |
|---|---|---|---|
| 1 | Data Types, Variables, Input/Output | [Open the class page](https://prateekscaler.github.io/AIML-Jul26-Batch3-Python/Class-01-Data-Types-Variables-Input-Output/) · [notes and code](Class-01-Data-Types-Variables-Input-Output/README.md) | **v1** takes one payment and prints a receipt |
| 2 | Operators | [Open the class page](https://prateekscaler.github.io/AIML-Jul26-Batch3-Python/Class-02-Operators/) · [notes and code](Class-02-Operators/README.md) | **v2** money maths: bill split, cashback, "is the balance enough?" |
| 3 | Control Statements | coming up | **v3** decisions: refuse, approve, cashback tiers |
| 4 | Loops | coming up | **v4** keeps running: menu, PIN retries, mini statement |
| 5 | Functions | coming up | **v5** reusable actions: `pay()`, `add_money()`, `show_balance()` |
| 6 | Lists | coming up | **v6** transaction history |
| 7 | Strings | coming up | **v7** clean input, masked account numbers, formatted receipts |
| 8 | Sets, Tuples, Dictionaries | coming up | **v8** real records: accounts and transactions as structured data |
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
