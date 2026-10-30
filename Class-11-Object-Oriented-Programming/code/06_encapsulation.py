# Encapsulation: keep the data inside, change it only through methods.

# The open version: any line can set balance to anything.
class OpenAccount:
    def __init__(self, balance):
        self.balance = balance

account = OpenAccount(100)
account.balance = -500                # nothing stops it
print(account.balance)                # -500

# The fix: the data goes inside, the methods are the only door.
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance      # two underscores: internal

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

account = BankAccount(100)
account.deposit(50)
account.deposit(-500)                 # refused quietly by the rule inside
print(account.get_balance())          # 150

# print(account.__balance)            # AttributeError: no attribute '__balance'
print(account._BankAccount__balance)  # the real name: a speed bump, not a lock
