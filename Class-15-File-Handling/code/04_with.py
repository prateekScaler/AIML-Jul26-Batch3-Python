# Why close: writes wait in a buffer in RAM until the file is closed.
file = open("receipt.txt", "w")
file.write("Paid 100 to Akshay")
print("[" + open("receipt.txt").read() + "]")   # []: not in storage yet
file.close()
print("[" + open("receipt.txt").read() + "]")   # [Paid 100 to Akshay]

# with opens the file and closes it for you, even if an error happens inside.
with open("passbook.txt", "w") as f:
    f.write("Paid 600 to Sumit\nPaid 250 to Vamsi\n")

with open("passbook.txt", "r") as file:
    contents = file.read()
    print(contents)

print("Is the file closed now?", file.closed)
