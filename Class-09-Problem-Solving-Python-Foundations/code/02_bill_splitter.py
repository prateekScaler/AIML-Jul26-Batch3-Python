# Q1. Smart bill splitter (Classes 1 and 2)
name = input("Name: ")                      # text stays text
bill = float(input("Bill: "))               # rupees can have paise
tip_percent = int(input("Tip: "))           # a whole-number percentage
people = int(input("People: "))

tip = bill * tip_percent / 100              # percentage maths
grand_total = bill + tip
each = round(grand_total / people, 2)       # two decimal places

print(f"Hello {name}! Here is your bill summary:")
print(f"Tip amount: {tip}")
print(f"Grand total: {grand_total}")
print(f"Each person pays: {each}")
print(f"Pays more than 500? {each > 500}")  # a comparison is a bool
