# A path with a folder in it: data/passbook.txt, inside the working folder.
import os

print("Working folder:", os.getcwd())

with open("data/passbook.txt") as file:
    print(file.read())
