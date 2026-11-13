# Which folder? This program reads passbook.txt by name only.
# Run it from inside paisapay/, then from the folder above, and compare.
import os

print("Working folder:", os.getcwd())

with open("passbook.txt") as file:
    print(file.read())
