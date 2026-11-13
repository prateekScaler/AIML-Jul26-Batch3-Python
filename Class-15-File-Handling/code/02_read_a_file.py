# open() asks the operating system for the file and gives back a file object (a handle).
# .read() gives the whole file as one string. Reading moves a bookmark forward.
# The first lines only make the sample file, so this runs anywhere.
with open("passbook.txt", "w") as f:
    f.write("Paid 600 to Sumit\nPaid 250 to Vamsi\n")

file = open("passbook.txt")
print(file)                    # a file object, not the text

contents = file.read()
print(contents)
print(type(contents))          # <class 'str'>
file.close()

# the bookmark: a second read on the same open file gets nothing
file = open("passbook.txt")
first = file.read()
second = file.read()
print(len(first), len(second))  # 36 0
file.close()
