# PaisaPay v16: PaisaPay now remembers. The balance is saved in a text file and every
# payment is added to a CSV file, so a second run starts where the first one stopped.
# The checks moved into their own module, paisapay_checks.py, in the same folder.
import csv
import datetime
import os
from functools import reduce
from paisapay_checks import (clean, is_valid_upi_id, is_valid_pan,
                             read_bank_sms, mode_name)

BALANCE_FILE = "paisapay_balance.txt"
HISTORY_FILE = "paisapay_history.csv"

print("Welcome to PaisaPay")

contacts = {"rajani@okaxis": "Rajani", "sumit@ybl": "Sumit"}


def name_for(upi_id):
    return contacts.get(upi_id, upi_id.split("@")[0].title())


def load_balance(default):
    try:
        with open(BALANCE_FILE, "r") as file:
            return int(file.read().strip())
    except FileNotFoundError:
        return default                       # first run: no file yet
    except ValueError:
        print(f"The balance file is damaged. Starting from ₹{default}.")
        return default


def save_balance(balance):
    with open(BALANCE_FILE, "w") as file:    # w: replace the old number
        file.write(str(balance))


def load_history():
    try:
        with open(HISTORY_FILE, "r") as file:
            rows = list(csv.DictReader(file))
    except FileNotFoundError:
        return []
    # every value comes back as a string, so the numbers need int()
    return [Transaction(r["payee"], int(r["amount"]), r["mode"],
                        int(r["fee"]), int(r["cashback"]), r["date"])
            for r in rows]


def save_payment(t):
    new_file = not os.path.exists(HISTORY_FILE)
    with open(HISTORY_FILE, "a", newline="") as file:   # a: add, never erase
        writer = csv.writer(file)
        if new_file:
            writer.writerow(["date", "payee", "amount",
                             "mode", "fee", "cashback"])
        writer.writerow([t.date, t.payee, t.amount,
                         t.mode, t.fee, t.cashback])


class Transaction:
    def __init__(self, payee, amount, mode, fee, cashback, date):
        self.payee = payee
        self.amount = amount
        self.mode = mode
        self.fee = fee
        self.cashback = cashback
        self.date = date

    def describe(self):
        return f"{self.date}  ₹{self.amount} to {self.payee} ({mode_name(self.mode)})"


class Account:
    def __init__(self, owner, balance, pin):
        self.owner = owner
        self.__balance = balance
        self.__pin = pin
        self.history = []

    def get_balance(self):
        return self.__balance

    def check_pin(self, pin):
        return pin == self.__pin

    def fee_for(self, mode):
        if mode == "card":
            return 5
        elif mode == "netbanking":
            return 2
        return 0

    def cashback_for(self, amount):
        if amount >= 5000:
            return 100
        elif amount >= 2000:
            return 50
        elif amount >= 500:
            return 10
        return 0

    def add_money(self, amount):
        if amount <= 0:
            print("Invalid amount. Nothing added.")
            return
        self.__balance += amount
        save_balance(self.__balance)
        print(f"Added ₹{amount}. Balance ₹{self.__balance}")

    def pay(self, upi_id, amount, mode="upi"):
        if not is_valid_upi_id(upi_id):
            print(f"'{upi_id}' is not a valid UPI ID. Payment refused.")
            return
        if amount <= 0 or amount > 100000:
            print("Invalid amount. Payment refused.")
            return
        if mode_name(mode) == "Unknown mode":
            print(f"Unknown payment mode '{mode}'. Payment refused.")
            return
        fee = self.fee_for(mode)
        if amount + fee > self.__balance:
            print("Insufficient balance. Payment refused.")
            return
        cashback = self.cashback_for(amount)
        self.__balance = self.__balance - amount - fee + cashback
        payee = name_for(upi_id)
        t = Transaction(payee, amount, mode, fee, cashback, datetime.date.today().isoformat())
        self.history.append(t)
        save_payment(t)
        save_balance(self.__balance)
        print(f"Paid ₹{amount} to {payee} via {mode_name(mode)}")
        print(f"Fee ₹{fee} | Cashback ₹{cashback} | Balance ₹{self.__balance}")

    def statement(self):
        if len(self.history) == 0:
            print("No payments yet.")
            return
        amounts = list(map(lambda t: t.amount, self.history))
        total = reduce(lambda a, b: a + b, amounts)
        biggest = max(self.history, key=lambda t: t.amount)
        print(f"{self.owner}: {len(self.history)} payments | Spent ₹{total}")
        print(f"Biggest: {biggest.describe()}")
        for t in sorted(self.history, key=lambda t: t.amount):
            print("  " + t.describe())


class PremiumAccount(Account):
    def fee_for(self, mode):
        return 0                      # premium: no fees on any mode

    def cashback_for(self, amount):
        return super().cashback_for(amount) * 2


def ask_pin(account):
    for attempt in range(3):
        pin = input("UPI PIN: ").strip()
        if account.check_pin(pin):
            return True
        print(f"Wrong PIN. {2 - attempt} attempts left")
    return False


kind = clean(input("Account type (basic / premium): "))
balance = load_balance(1000)
if kind == "premium":
    account = PremiumAccount("Rajani", balance, "4321")
else:
    account = Account("Rajani", balance, "4321")
account.history = load_history()
print(f"Loaded {len(account.history)} saved payments. Balance ₹{account.get_balance()}")

choice = ""
while choice != "4":
    print()
    print("1 Pay  2 Balance  3 Statement  4 Exit  5 Add  6 Read SMS  7 Check PAN")
    choice = clean(input("Choose: "))

    if choice == "1":
        upi_id = clean(input("Pay to (UPI ID): "))
        amount = int(input("Amount in rupees: ").strip())
        mode = clean(input("Mode (upi / card / netbanking): "))
        if ask_pin(account):
            account.pay(upi_id, amount, mode)
        else:
            print("Three wrong PINs. Payment refused.")

    elif choice == "2":
        print(f"Balance: ₹{account.get_balance()}")

    elif choice == "3":
        account.statement()

    elif choice == "5":
        account.add_money(int(input("Amount to add: ").strip()))

    elif choice == "6":
        parsed = read_bank_sms(input("Paste the bank SMS: "))
        if parsed is None:
            print("Could not read that SMS.")
        else:
            amount, tail, payee = parsed
            print(f"₹{amount} to {payee} from the account ending {tail}")

    elif choice == "7":
        pan = clean(input("PAN: ")).upper()
        print("Valid PAN" if is_valid_pan(pan) else "Not a valid PAN")

    elif choice != "4":
        print(f"Unknown choice '{choice}'. Try again.")

print("Thank you for using PaisaPay")

# What v16 cannot do yet:
#   - stay correct if two copies run at the same time (both write the same files)
#   - keep the balance safe: anyone can open paisapay_balance.txt and type a new number
#   Real payment apps keep this data in a database on a server, for both reasons.
