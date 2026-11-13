# write() adds no newline: put \n yourself. "w" inside a loop keeps only the last write.
with open("passbook.txt", "w") as f:
    f.write("Paid 600 to Sumit\nPaid 250 to Vamsi\n")

with open("passbook.txt", "a") as file:
    file.write("Paid 100 to Akshay\n")

with open("passbook.txt") as f:
    print(f.read())

for name in ["Sumit", "Vamsi", "Akshay"]:      # the bug: "w" in a loop
    f = open("paid.txt", "w")
    f.write(name + "\n")
    f.close()
with open("paid.txt") as f:
    print(f.read())                            # only Akshay
