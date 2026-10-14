# PaisaPay v5: named blocks
# Built in Class 5. The v4 menu loop stays. Every job is a function:
# two checks, fee, cashback, mode name, show_balance, add_money, ask_pin, pay.
# Fee, cashback and payment modes from v3 are back. Money is whole rupees.
print("Welcome to PaisaPay")

saved_pin = "4321"

def is_valid_amount(amount):
    return amount > 0 and amount <= 100000

def is_valid_pin(pin):
    return pin == saved_pin

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

def show_balance(balance):
    print("Balance: ₹", balance)

def add_money(balance, amount):
    if not is_valid_amount(amount):
        print("Invalid amount. Nothing added.")
        return balance
    print("Added ₹", amount)
    return balance + amount

def ask_pin():
    for attempt in range(3):
        pin = input("UPI PIN: ")
        if is_valid_pin(pin):
            return True
        print("Wrong PIN.", 2 - attempt, "attempts left")
    return False

def pay(balance, payee, amount, mode="upi"):
    if not is_valid_amount(amount):
        print("Invalid amount. Payment refused.")
        return balance
    if mode_name(mode) == "Unknown mode":
        print("Unknown payment mode. Payment refused.")
        return balance
    fee = fee_for(mode)
    if amount + fee > balance:
        print("Insufficient balance. Payment refused.")
        return balance
    cashback = cashback_for(amount)
    print("Paid ₹", amount, "to", payee, "via", mode_name(mode))
    print("Fee ₹", fee, "| Cashback ₹", cashback)
    return balance - amount - fee + cashback

balance = 1000
choice = ""
while choice != "4":
    print()
    print("1. Pay   2. Balance   3. Add money   4. Exit")
    choice = input("Choose: ")

    if choice == "1":
        payee = input("Pay to: ")
        amount = int(input("Amount in rupees: "))
        mode = input("Mode (upi / card / netbanking): ")
        if ask_pin():
            balance = pay(balance, payee, amount, mode)
        else:
            print("Three wrong PINs. Payment refused.")

    elif choice == "2":
        show_balance(balance)

    elif choice == "3":
        amount = int(input("Amount to add: "))
        balance = add_money(balance, amount)

    elif choice != "4":
        print("Unknown choice. Try again.")

print("Thank you for using PaisaPay")

# What v5 cannot do yet:
#   - remember payments: the mini statement needs a list that grows (Class 6)
#   - clean up typed input or show paise (strings and formatting, Class 7)
#   - validate a UPI ID or PAN properly (regex, Class 11)
