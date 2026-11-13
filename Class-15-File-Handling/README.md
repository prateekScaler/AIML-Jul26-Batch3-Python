# Class 15 · File Handling

Every program so far forgot everything when it ended. This class gives programs a memory: files in storage. You learn where a program looks for a file, open and read one, choose the right mode to write, close files safely with `with`, and read a file line by line to turn text into data.

**By the end of this class you can:**

- Tell memory (RAM) from storage, and explain how a program reaches a file.
- Say which folder Python looks in for a file, and check it with `os.getcwd()`.
- Open and read a file, and explain the bookmark.
- Open a file in the right mode, `"r"`, `"w"`, `"a"` or `"x"`, and say what each does when the file exists and when it does not.
- Say why a file must be closed, and use `with`.
- Read a file line by line and turn each line into data.

## How to use this folder

| File | What it is |
|---|---|
| [`index.html`](index.html) | The interactive class page. [Open it here](https://prateekscaler.github.io/AIML-Jul26-Batch3-Python/Class-15-File-Handling/), no download needed. **Step by step** shows a little at a time (press → or Next). **Show everything** gives the whole class on one page. |
| [`code/`](code/) | Every example from the class as a runnable file, in order. Each file first creates the sample files it reads, so it runs anywhere. |
| [`paisapay/`](paisapay/) | A small practice folder for the which-folder step: run `app.py` from inside it, then from this folder, and compare. |
| [`Python-Class-15-File-Handling.ipynb`](Python-Class-15-File-Handling.ipynb) | The same examples as one notebook. [Open it in Google Colab](https://colab.research.google.com/github/prateekScaler/AIML-Jul26-Batch3-Python/blob/main/Class-15-File-Handling/Python-Class-15-File-Handling.ipynb) and run the cells in order, nothing to install. |
| [`PRACTICE.md`](PRACTICE.md) | Four coding problems on files, with sample output, hints and solutions. |

Run the code on your own machine with `python3 filename.py` (Python 3.10 or newer, because PaisaPay uses `match`), in Google Colab, or in [PyLens](https://scaler-pylens.vercel.app/). Files are made in the folder the program runs in.

<details>
<summary><b>Install Python on your computer</b></summary>

**Windows**

1. Go to [python.org/downloads](https://www.python.org/downloads/) and click the yellow Download button.
2. Run the installer. On the first screen, tick **Add python.exe to PATH**, then click **Install Now**.
3. Open Command Prompt and check: `py --version`. If that fails, try `python --version`.
4. Run a file: `py passbook.py`

**macOS**

1. Go to [python.org/downloads](https://www.python.org/downloads/), download the macOS installer and open it. Click Continue until it finishes.
2. Open Terminal and check: `python3 --version`
3. Run a file: `python3 passbook.py`

This course needs Python 3.10 or newer. Any version the site offers today is fine.

**Why the 3 in `python3`?** Python 2 and Python 3 are two different versions, and Python 2 ended in 2020. Many Mac and Linux computers kept the name `python` for the old one, so `python3` asks clearly for Python 3. On Windows the command is `py` or `python`.

</details>

<details>
<summary><b>The terminal, and seven commands to start with</b></summary>

**What is a terminal?** A window where you type commands instead of clicking. It is how you run Python files, move between folders, and see which folder you are in: the working folder.

- **macOS:** press Cmd + Space, type **Terminal**, press Enter.
- **Windows:** press the Windows key, type **PowerShell**, press Enter. Command Prompt also works.

| Mac and Linux | Windows (PowerShell) | What it does |
|---|---|---|
| `pwd` | `pwd` | which folder am I in? |
| `ls` | `ls` (or `dir`) | list the files and folders here |
| `cd paisapay` | `cd paisapay` | go into the folder paisapay |
| `cd ..` | `cd ..` | go up one folder |
| `python3 app.py` | `py app.py` | run a Python file |
| `mkdir notes` | `mkdir notes` | make a new folder |
| `clear` | `clear` (or `cls`) | clear the screen |

Two keys save time: **Tab** finishes a file or folder name for you, and the **Up arrow** brings back your last command. These seven are enough for this course.

**Practise in your browser, nothing to install:**

- [Terminus (MIT)](https://web.mit.edu/mprat/Public/web/Terminus/Web/main.html): a small adventure game. You walk through rooms with `ls` and `cd`. Start here.
- [Learn Shell](https://www.learnshell.org/): short lessons, and you type each command in a box on the page.
- [Linux Survival](https://linuxsurvival.com/): four short lessons with a practice terminal.
- [Command Challenge](https://cmdchallenge.com/): one small task at a time; type the command that solves it.
- Later, for fun: [OverTheWire Bandit](https://overthewire.org/wargames/bandit/), a puzzle game played with real commands (harder).

</details>

Official post-read for this class: https://scaler-content.github.io/python-Foundations-12/

---

## 1. Where Class 14 stopped

Class 14 was a revision class: object-oriented programming, choosing a string method, a regex or an LLM, and inheritance scenarios ([notes](../Class-14-Revision-OOP-And-Regex/README.md)). This class starts file handling.

## 2. Memory and storage

A running program keeps its variables in **memory (RAM)**: fast, and cleared when the program ends. Files live in **storage** (an SSD, a hard disk, phone storage): slower, and they stay even with no power.

```python
accounts = {
    "rajani@okaxis": {"name": "Rajani", "balance": 1000, "pin": "4321"},
    "sumit@ybl": {"name": "Sumit", "balance": 2500, "pin": "1234"},
}
accounts["rajani@okaxis"]["balance"] -= 600     # Rajani pays ₹600
print("Rajani's balance:", accounts["rajani@okaxis"]["balance"])   # 400, until the program ends
```

Run this again and Rajani's new balance is gone: the dictionary was in RAM. To keep every user's details, save them in a file, one row per user. Real apps never store a PIN as readable text; they store a scrambled form called a hash.

Phone shops say "8 GB RAM, 128 GB ROM". That 128 GB is really storage, where files live.

## 3. What a file is, and how a program reaches it

Today's example is a passbook of payments, `passbook.txt`:

```text
Paid 600 to Sumit
Paid 250 to Vamsi
```

A text file is one long string in storage: `Paid 600 to Sumit\nPaid 250 to Vamsi\n`. Each `\n` ends a line. A program cannot touch storage itself; it asks the operating system, and `open()` is how Python asks.

**Which folder?** `open("passbook.txt")` gives only a name, and Python looks for it in one folder: the **working folder**, the folder your program was started from. `os.getcwd()` prints it. In Google Colab it is `/content`.

| You write | Python looks in |
|---|---|
| `open("passbook.txt")` | the working folder |
| `open("data/passbook.txt")` | the folder `data`, inside the working folder |
| `open("/Users/ravi/Downloads/passbook.txt")` | exactly that place: a full path |
| `open(r"C:\Users\ravi\passbook.txt")` | a full path on Windows; `r` keeps the backslashes |

Python does not search other folders. A common surprise: `app.py` and `passbook.txt` sit together in `paisapay/`, but you type `python3 paisapay/app.py` from the folder above. The working folder is then the folder above, and `open("passbook.txt")` raises `FileNotFoundError`. Start the program from inside its folder, or give a path.

**Try it yourself.** This folder has a small practice folder, [`paisapay/`](paisapay/), with `app.py`, `passbook.txt`, `read_data.py` and `data/passbook.txt`. Open a terminal in this class folder:

```text
cd paisapay
python3 app.py              # Working folder: .../paisapay, then the two payments

cd ..
python3 paisapay/app.py     # Working folder: the class folder, then FileNotFoundError
```

`pwd` (Mac, Linux) or `cd` (Windows) shows where you are. In PyCharm the working folder is set in Run, Edit Configurations, Working directory.

```python
file = open("passbook.txt")
print(file)                # <_io.TextIOWrapper name='passbook.txt' mode='r' encoding='utf-8'>
contents = file.read()     # the whole file as one string
print(contents)
file.close()
```

`open()` gives a **file object**, a handle to the file, not the text. Its `encoding='UTF-8'` is the rule for turning characters into the numbers (bytes) that storage keeps, and back. **UTF-8** is the standard today: it stores every language, हिंदी and ₹ included. Older rules store less: `ascii` has no ₹ (`UnicodeEncodeError` if you write it), and `cp1252`, an older Windows default, has no हिंदी. Safe habit: `open("passbook.txt", encoding="utf-8")`, because on Windows the default may not be UTF-8. `.read()` gives the text as one string, so everything from Class 7 works on it. The file object also keeps a **bookmark**: after one `.read()` it sits at the end, and a second `.read()` on the same open file returns an empty string. Open again to read again.

## 4. Modes: one example each

The second argument of `open()` says what you plan to do. For every mode, ask: what if the file exists, and what if it does not?

```python
open("passbook.txt", "r").write("Paid 100 to Akshay")  # io.UnsupportedOperation: not writable
open("missing.txt", "r")                               # FileNotFoundError: "r" never creates

open("receipt.txt", "w")     # a missing file is created
open("passbook.txt", "w")    # a file that exists is ERASED first

open("passbook.txt", "a")    # writes go at the end; old lines stay
open("log.txt", "a")         # a missing file is created, then added to

open("receipt_101.txt", "x") # a new file is created
open("passbook.txt", "x")    # FileExistsError: "x" never touches a file that exists
```

| Mode | Means | If the file exists | If it does not |
|---|---|---|---|
| `"r"` | read (the default) | reads from the start | `FileNotFoundError` |
| `"w"` | write | **erases it first** | creates it |
| `"a"` | append | adds at the end | creates it |
| `"x"` | create only | `FileExistsError`, nothing erased | creates it |

Which mode for the job: show the passbook, `"r"`; add today's payment, `"a"`; save a new balance over the old one, `"w"`; make a receipt that must never overwrite another, `"x"`. A real bug: opening with `"w"` inside a loop, once per item, leaves only the last item. Full examples: [`code/03_file_modes.py`](code/03_file_modes.py).

## 5. Why close a file, and `with`

An open file is a live link between your program and the operating system.

```python
file = open("receipt.txt", "w")
file.write("Paid 100 to Akshay")
print("[" + open("receipt.txt").read() + "]")   # []: still in a buffer in RAM
file.close()
print("[" + open("receipt.txt").read() + "]")   # [Paid 100 to Akshay]
```

- **Writes wait in RAM first.** Writing to storage is slow, so Python collects writes in a buffer. `close()` sends them to storage. A crash before `close()` can lose them.
- **An open file can stay locked.** On Windows, Excel or another program cannot change or delete it.
- **There is a limit.** Thousands of files left open give `OSError: [Errno 24] Too many open files`.

`with` closes the file for you when the indented block ends, even after an error:

```python
with open("passbook.txt", "r") as file:
    contents = file.read()
    print(contents)

print("Is the file closed now?", file.closed)   # True
```

Read inside the block. A `file.read()` after the block gives `ValueError: I/O operation on closed file.` Two separate `with` blocks each get a new file object with the bookmark back at the start.

## 6. Line by line: lines become data

```python
with open("passbook.txt", "r") as file:
    for line in file:
        print(line)            # a blank line after each payment
```

The loop cuts the file after each `\n`, and each piece keeps its `\n`. `print` adds another, so you see a blank line. `print(line.strip())` removes it. Each line is a string, so you can split it and use the parts:

```python
total = 0
with open("passbook.txt") as file:
    for line in file:
        words = line.split()          # ['Paid', '600', 'to', 'Sumit']
        total += int(words[1])        # the amount is text: int() first
print("Total spent:", total)          # Total spent: 850
```

`write()` adds no newline, unlike `print`, so put `\n` yourself: `file.write("Paid 100 to Akshay\n")`.

## Errors you will meet

| You see | It means | Fix |
|---|---|---|
| `FileNotFoundError: [Errno 2] No such file or directory: 'missing.txt'` | the file is not in the working folder, or the name is wrong | check the name and the folder: `os.getcwd()` |
| `FileExistsError: [Errno 17] File exists: 'notes.txt'` | `"x"` mode refused to overwrite | pick another name, or use `"w"` on purpose |
| `io.UnsupportedOperation: not writable` | you wrote to a file opened with `"r"` | open it with `"w"` or `"a"` |
| `IsADirectoryError: [Errno 21] Is a directory: 'reports'` | you opened a folder, not a file | add the file name to the path |
| `ValueError: I/O operation on closed file.` | you used the file after `with` closed it | do the work inside the `with` block |
| `UnicodeEncodeError: 'ascii' codec can't encode character '\u20b9'` | the encoding cannot store ₹ | open with `encoding="utf-8"` |

## Recap

- **Memory forgets, storage remembers.** Variables live in RAM; a file lives in storage and outlives the program.
- **The working folder** is where a bare file name is looked up: the folder you started the program from.
- `open()` gives a file object. `.read()` gives one string, and the bookmark only moves forward.
- **Modes:** `"r"` read, `"w"` erase and write, `"a"` add at the end, `"x"` create only.
- **Close the file**, or let `with` do it. Writes are not safe until then.
- **Line by line:** each line keeps its `\n`; `strip()` it, `split()` it, `int()` the numbers.

Next class: what to do when a file is missing (`try` and `except`), CSV files, and modules.
