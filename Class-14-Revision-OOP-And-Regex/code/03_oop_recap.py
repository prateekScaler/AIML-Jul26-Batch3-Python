# OOP recap: one blueprint, class variables and instance variables,
# encapsulation, and self choosing the right object.
class Account:
    bank = "PaisaPay"                 # class variable: shared by every object

    def __init__(self, owner, balance):
        self.owner = owner            # instance variables: each object's own
        self.__balance = balance      # private: change it only through methods

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

rajani = Account("Rajani", 1000)
sumit = Account("Sumit", 2500)

Account.bank = "PaisaPay Plus"        # changed on the class: everyone sees it
print(rajani.bank, sumit.bank)

rajani.bank = "OtherPay"              # changed on one object: a new instance variable
print(rajani.bank, sumit.bank, Account.bank)

rajani.deposit(500)                   # self is rajani, so only her balance changes
print(rajani.get_balance(), sumit.get_balance())

try:
    print(rajani.__balance)
except AttributeError as e:
    print("AttributeError:", e)
