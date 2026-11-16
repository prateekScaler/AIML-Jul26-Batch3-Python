# csv reads and writes comma-separated rows. Every value read back is a string.
import csv

# why not split: a comma inside a value breaks it
line = '"Sumit Kumar, Jr",600'
print(len(line.split(",")))                  # 3: wrong
print(next(csv.reader([line])))              # ['Sumit Kumar, Jr', '600']

# writing: newline="" stops blank lines between rows on some systems
rows = [["payee", "amount"], ["Sumit", 600], ["Vamsi", 250]]
with open("payments.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(rows)

# reading: one list per row, header first
with open("payments.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# DictReader: the header gives the keys
total = 0
with open("payments.csv", "r") as file:
    for row in csv.DictReader(file):
        print(row["payee"], row["amount"])
        total += int(row["amount"])
print("Total:", total)
