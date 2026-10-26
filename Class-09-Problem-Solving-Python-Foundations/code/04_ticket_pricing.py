# Q2. Movie ticket pricing engine (Classes 2 and 3)
age = int(input("Age: "))
is_weekend = input("Weekend (yes/no): ").strip().lower()
is_member = input("Member (yes/no): ").strip().lower()

if age < 0 or is_weekend not in ("yes", "no") or is_member not in ("yes", "no"):
    print("Invalid input.")
else:
    price = 300
    if age < 5:
        price = 0
    elif age <= 12:
        price = price * 50 // 100
    elif age >= 60:
        price = price * 60 // 100

    price = price + price * 20 // 100 if is_weekend == "yes" else price   # ternary

    if is_member == "yes" and price > 200:
        price = price - 25

    print(f"Ticket price: {price}")
