# PaisaPay v10: insights
# Built in Class 10. v8 plus functional tools: the statement uses map for the
# amounts, filter for the big payments, reduce for the total, sorted with a key
# for the biggest payment, and a stored lambda as the big-payment rule.
from functools import reduce

print("Welcome to PaisaPay")

saved_pin = "4321"
history = []
contacts = {"rajani@okaxis": "Rajani", "sumit@ybl": "Sumit"}

def clean(text):
    return text.strip().lower()

def is_valid_amount(amount):
    return amount > 0 and amount <= 100000

def is_valid_pin(pin):
    return pin == saved_pin

def is_valid_upi_id(upi_id):
    parts = upi_id.split("@")
    return len(parts) == 2 and len(parts[0]) > 0 and len(parts[1]) > 0

def mask(card):
    return "**** **** **** " + card[-4:]

def fee_for(mode):
    if mode == "card":
        return 5
    elif mode == "netbanking":
        return 2
    return 0

def cashback_for(amount):
    if amount >= 5000:
        return 100
    elif amount >= 2000:
        return 50
    elif amount >= 500:
        return 10
    return 0

def mode_name(mode):
    match mode:
        case "upi":
            return "UPI"
        case "card":
            return "Card"
        case "netbanking":
            return "Net banking"
        case _:
            return "Unknown mode"

def name_for(upi_id):
    return contacts.get(upi_id, upi_id.split("@")[0].title())

is_big = lambda payment: payment[1] >= 500

def print_receipt(name, amount, mode, fee, cashback, balance):
    print(f"Paid ₹{amount} to {name} via {mode_name(mode)}")
    print(f"Fee ₹{fee} | Cashback ₹{cashback} | Balance ₹{balance}")

def ask_pin():
    for attempt in range(3):
        pin = input("UPI PIN: ").strip()
        if is_valid_pin(pin):
            return True
        print(f"Wrong PIN. {2 - attempt} attempts left")
    return False

def pay(balance, history, upi_id, amount, mode="upi"):
    if not is_valid_upi_id(upi_id):
        print(f"'{upi_id}' is not a valid UPI ID. Payment refused.")
        return balance
    if not is_valid_amount(amount):
        print("Invalid amount. Payment refused.")
        return balance
    if mode_name(mode) == "Unknown mode":
        print(f"Unknown payment mode '{mode}'. Payment refused.")
        return balance
    fee = fee_for(mode)
    if amount + fee > balance:
        print("Insufficient balance. Payment refused.")
        return balance
    cashback = cashback_for(amount)
    balance = balance - amount - fee + cashback
    name = name_for(upi_id)
    print_receipt(name, amount, mode, fee, cashback, balance)
    history.append((name, amount, mode))
    return balance

def mini_statement(history):
    if len(history) == 0:
        print("No payments yet.")
        return
    amounts = list(map(lambda p: p[1], history))
    total = reduce(lambda a, b: a + b, amounts)
    big = list(filter(is_big, history))
    biggest = sorted(history, key=lambda p: p[1], reverse=True)[0]
    print(f"Payments: {len(history)} | Spent ₹{total}")
    print(f"Big payments (₹500 or more): {len(big)}")
    print(f"Biggest: ₹{biggest[1]} to {biggest[0]}")
    for name, amount, mode in sorted(history, key=lambda p: p[1]):
        print(f"  ₹{amount} {name} ({mode_name(mode)})")

balance = 1000
choice = ""
while choice != "4":
    print()
    print("1 Pay  2 Balance  3 Statement  4 Exit  5 Add  6 Card  7 Save")
    choice = clean(input("Choose: "))

    if choice == "1":
        upi_id = clean(input("Pay to (UPI ID): "))
        amount = int(input("Amount in rupees: ").strip())
        mode = clean(input("Mode (upi / card / netbanking): "))
        if ask_pin():
            balance = pay(balance, history, upi_id, amount, mode)
        else:
            print("Three wrong PINs. Payment refused.")

    elif choice == "2":
        print(f"Balance: ₹{balance}")

    elif choice == "3":
        mini_statement(history)

    elif choice == "5":
        amount = int(input("Amount to add: ").strip())
        if is_valid_amount(amount):
            balance = balance + amount
            print(f"Added ₹{amount}. Balance ₹{balance}")
        else:
            print("Invalid amount. Nothing added.")

    elif choice == "6":
        card = input("Card number: ").replace(" ", "").strip()
        if len(card) == 16:
            print(f"Card linked: {mask(card)}")
        else:
            print("A card number has 16 digits.")

    elif choice == "7":
        upi_id = clean(input("Contact UPI ID: "))
        name = input("Name: ").strip().title()
        if is_valid_upi_id(upi_id):
            contacts[upi_id] = name
            print(f"Saved. {len(contacts)} contacts.")
        else:
            print(f"'{upi_id}' is not a valid UPI ID.")

    elif choice != "4":
        print(f"Unknown choice '{choice}'. Try again.")

print("Thank you for using PaisaPay")

# What v10 cannot do yet:
#   - keep an account's rules and its data together (classes, Class 11)
#   - check a UPI ID or a card number properly (regex, Class 12)
#   - remember anything after the program ends (files, Class 13)
