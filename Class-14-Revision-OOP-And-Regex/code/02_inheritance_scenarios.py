# Inheritance scenarios: which code runs, and why.

# 1. A parent method calls a method the child overrides: the child's version runs
class Account:
    def fee_for(self, mode):
        return 5 if mode == "card" else 0

    def total(self, amount, mode):
        return amount + self.fee_for(mode)    # self is whatever object called total

class PremiumAccount(Account):
    def fee_for(self, mode):
        return 0

print(Account().total(1000, "card"))          # 1005
print(PremiumAccount().total(1000, "card"))   # 1000

# 2. A child class variable hides the parent's
class Deposit:
    rate = 4

class FixedDeposit(Deposit):
    rate = 7

print(Deposit.rate, FixedDeposit.rate, FixedDeposit().rate)   # 4 7 7

# 3. super() works in any method, not only __init__
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def describe(self):
        return f"{self.name} earns {self.salary}"

class Manager(Employee):
    def describe(self):
        return super().describe() + " and leads a team"

print(Manager("Chitransh", 90000).describe())

# 4. super().__init__ needs every argument the parent asks for
class Intern(Employee):
    def __init__(self, name):
        super().__init__(name)                # Employee also needs salary

try:
    Intern("Karthikeyan")
except TypeError as e:
    print("TypeError:", e)
