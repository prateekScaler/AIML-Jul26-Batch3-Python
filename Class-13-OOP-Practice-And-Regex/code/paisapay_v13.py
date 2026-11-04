# PaisaPay v13: classes from Class 12, finished here, plus regular expressions.
# A Transaction and an Account hold their own data, the balance and PIN are private,
# a PremiumAccount inherits everything and overrides the fee rule.
# New with regex: a real UPI ID check, a PAN check (menu 7), reading a bank SMS (menu 6).
import re
from functools import reduce

print("Welcome to PaisaPay")

contacts = {"rajani@okaxis": "Rajani", "sumit@ybl": "Sumit"}


def clean(text):
    return text.strip().lower()


def is_valid_upi_id(upi_id):
    # letters, digits or dots, then @, then a bank handle of letters only
    return re.fullmatch(r"[a-z0-9.]+@[a-z]+", upi_id) is not None


def is_valid_pan(pan):
    # five letters, four digits, one letter: ABCDE1234F
    return re.fullmatch(r"[A-Z]{5}\d{4}[A-Z]", pan) is not None


def read_bank_sms(sms):
    # "Rs.600 debited from a/c XX4321 to SUMIT on 04-11-26 via UPI"
    m = re.search(r"Rs\.(\d+) debited from a/c XX(\d{4}) to (\w+)", sms)
    if m is None:
        return None
    amount, tail, payee = m.groups()
    return int(amount), tail, payee.title()


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


class Transaction:
    def __init__(self, payee, amount, mode, fee, cashback):
        self.payee = payee
        self.amount = amount
        self.mode = mode
        self.fee = fee
        self.cashback = cashback

    def describe(self):
        return f"₹{self.amount} to {self.payee} ({mode_name(self.mode)})"


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
        self.history.append(Transaction(payee, amount, mode, fee, cashback))
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
if kind == "premium":
    account = PremiumAccount("Rajani", 1000, "4321")
else:
    account = Account("Rajani", 1000, "4321")

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

# What v13 cannot do yet:
#   - remember anything after the program ends (files and modules, next)
