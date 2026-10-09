# PaisaPay v3: the app can say no
# Built in Class 3. Adds decisions to v2: wrong PIN, unknown mode and
# insufficient balance are refused, cashback comes in tiers, and the
# payment mode is matched against exact values.

print("Welcome to PaisaPay")

balance = 1000
saved_pin = "4321"

name = input("Your name: ")
payee = input("Pay to: ")
amount = int(input("Amount in rupees: "))
mode = input("Mode (upi / card / netbanking): ")
pin = input("UPI PIN: ")

fee = 2
total = amount + fee

if amount >= 5000:
    cashback = 100
elif amount >= 2000:
    cashback = 50
elif amount >= 500:
    cashback = 10
else:
    cashback = 0

match mode:
    case "upi":
        mode_text = "UPI"
    case "card":
        mode_text = "Card"
    case "netbanking":
        mode_text = "Net banking"
    case _:
        mode_text = "Unknown mode"

print("----- Receipt -----")
if pin != saved_pin:
    print("Wrong PIN. Payment refused.")
elif mode_text == "Unknown mode":
    print("Unknown payment mode. Payment refused.")
elif total > balance:
    print("Insufficient balance. Payment refused.")
else:
    balance = balance - total + cashback
    print("Paid: ₹", amount, "to", payee, "via", mode_text)
    print("Cashback: ₹", cashback)
    print("Balance left: ₹", balance)

# What v3 cannot do yet:
#   - take a second payment: it handles one and stops (needs loops, Class 4)
#   - give the user another try after a wrong PIN (loops again)
