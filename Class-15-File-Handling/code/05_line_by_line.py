# Looping over a file gives one line at a time. Each line keeps its \n.
with open("passbook.txt", "w") as f:
    f.write("Paid 600 to Sumit\nPaid 250 to Vamsi\n")

with open("passbook.txt", "r") as file:
    for line in file:
        print(line)                # two newlines: the line's own, and print's

with open("passbook.txt", "r") as file:
    for line in file:
        print(line.strip())        # strip removes the line's \n

# lines become data: split each line, convert the amount, add it up
total = 0
with open("passbook.txt") as file:
    for line in file:
        words = line.split()
        total += int(words[1])
print("Total spent:", total)
