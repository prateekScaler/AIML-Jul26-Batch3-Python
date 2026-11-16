# try/except catches a named error and lets the program go on.
# First on errors from earlier classes, then on files.
bill = 1200
people = 0
try:
    share = bill / people
    print("Each pays", share)
except ZeroDivisionError:
    print("Nobody to split with.")

marks = [72, 85, 90]
try:
    print(marks[5])
except IndexError:
    print("No such position.")

contacts = {"sumit@ybl": "Sumit"}
try:
    print(contacts["vamsi@oksbi"])
except KeyError:
    print("Not in your contacts.")

# two excepts: each error finds the one with its own name
def split(bill, people_text):
    try:
        people = int(people_text)
        return bill / people
    except ValueError:
        return "Please type a number."
    except ZeroDivisionError:
        return "Nobody to split with."

print(split(1200, "4"))
print(split(1200, "four"))
print(split(1200, "0"))

# the same plan for a missing file
try:
    file = open("missing.txt")
    print("A")                    # skipped: the error happened on the line above
except FileNotFoundError:
    print("B")
print("C")

# more than one except: Python uses the first one that matches
def read_notes(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        return "Error: file not found."
    except PermissionError:
        return "Error: not allowed to read this file."

with open("passbook.txt", "w") as f:
    f.write("Paid 600 to Sumit\nPaid 250 to Vamsi\n")

print(read_notes("passbook.txt"))
print(read_notes("secret_diary.txt"))

# not only files fail: text that is not a number breaks int()
try:
    amount = int("abc")
    print("Amount:", amount)
except ValueError:
    print("Please type a number.")

# the except is chosen by the kind of error, not by position
try:
    amount = int("12a")
    file = open("passbook.txt")
except FileNotFoundError:
    print("A")
except ValueError:
    print("B")                      # B

# a bare except hides bugs: the typo below is reported as a missing file
try:
    with open("passbook.txt") as file:
        text = fille.read()
    print(len(text))
except:
    print("No passbook yet.")       # wrong message: the file is there
