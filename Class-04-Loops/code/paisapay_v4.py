# PaisaPay v4: the app keeps running
# Built in Class 4. Adds loops to v3: a menu that repeats until Exit,
# three PIN attempts, and a mini statement (count, total, biggest).
print("Welcome to PaisaPay")

balance = 1000
saved_pin = "4321"
count = 0
total_spent = 0
biggest = 0

choice = ""
while choice != "4":
    print()
    print("1. Pay   2. Balance   3. Mini statement   4. Exit")
    choice = input("Choose: ")

    if choice == "1":
        payee = input("Pay to: ")
        amount = int(input("Amount in rupees: "))

        pin_ok = False
        for attempt in range(3):
            pin = input("UPI PIN: ")
            if pin == saved_pin:
                pin_ok = True
                break
            print("Wrong PIN.", 2 - attempt, "attempts left")

        if not pin_ok:
            print("Three wrong PINs. Payment refused.")
        elif amount > balance:
            print("Insufficient balance. Payment refused.")
        else:
            balance -= amount
            print("Paid ₹", amount, "to", payee, "| Left ₹", balance)
            count += 1
            total_spent += amount
            if amount > biggest:
                biggest = amount

    elif choice == "2":
        print("Balance: ₹", balance)

    elif choice == "3":
        print("Count:", count, "| Spent ₹", total_spent)
        print("Biggest ₹", biggest)

    elif choice != "4":
        print("Unknown choice. Try again.")

print("Thank you for using PaisaPay")

# What v4 cannot do yet:
#   - fee, cashback and payment modes from v3 are out; they return in v5 as functions
#   - the statement knows totals, not every line (needs a growing list, Class 6)
#   - the same 20 lines repeat for every payment; naming a block once is Class 5
