# The four modes, each with both cases: the file exists, and the file does not.
def show(name):
    with open(name) as f:
        print(f"{name}: {f.read().splitlines()}")

def fresh_passbook():
    with open("passbook.txt", "w") as f:
        f.write("Paid 600 to Sumit\nPaid 250 to Vamsi\n")

# "r": read only. Writing fails; a missing file fails.
fresh_passbook()
try:
    file = open("passbook.txt", "r")
    file.write("Paid 100 to Akshay")
except Exception as e:
    print("r, write:", type(e).__name__, e)
try:
    open("missing.txt", "r")
except FileNotFoundError as e:
    print("r, missing:", e)

# "w": creates a missing file; erases a file that exists
file = open("receipt.txt", "w")
file.write("Paid 100 to Akshay")
file.close()
show("receipt.txt")
file = open("passbook.txt", "w")
file.write("Paid 100 to Akshay")
file.close()
show("passbook.txt")             # the two old payments are gone

# "a": adds at the end; creates a missing file
fresh_passbook()
file = open("passbook.txt", "a")
file.write("Paid 100 to Akshay\n")
file.close()
show("passbook.txt")

# "x": creates a new file; refuses a file that exists
try:
    open("passbook.txt", "x")
except FileExistsError as e:
    print("x, exists:", e)
