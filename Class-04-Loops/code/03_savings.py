# A real table: ten months of a savings plan.
# Input, casting, a loop, maths and print in five lines.
monthly = int(input("Monthly deposit: "))

for month in range(1, 11):
    print("Month", month, "→ ₹", monthly * month)
