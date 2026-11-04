# Six inheritance scenarios: a chain of parents, extending a method, isinstance,
# a child's own method, a child that adds a check, and is-a versus has-a.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def describe(self):
        return f"{self.name} is an employee."


class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def describe(self):
        return f"{self.name} manages a team of {self.team_size}."

    def approve_leave(self, who):
        return f"{self.name} approved leave for {who}."


# 1. A chain: Director is a Manager, and a Manager is an Employee
class Director(Manager):
    def __init__(self, name, salary, team_size, region):
        super().__init__(name, salary, team_size)
        self.region = region

    # 2. Extend, do not replace: the parent's sentence, plus one more
    def describe(self):
        return super().describe() + f" Region: {self.region}."


d = Director("Sangeeta", 150000, 40, "South")
print(d.describe())
print(d.salary)                       # set by Employee.__init__, two levels up

# 3. isinstance: a Director is a Manager and an Employee; an Employee is not a Manager
e = Employee("Prajnika", 60000)
print(isinstance(d, Employee), isinstance(e, Manager))
print(type(d) == Manager, type(d).__name__)

# 4. A child's own method is not on the parent
print(d.approve_leave("Rahul"))
try:
    e.approve_leave("Rahul")
except AttributeError as err:
    print("AttributeError:", err)

# 5. A child adds a check, then hands over to the parent
class Wallet:
    def __init__(self, balance):
        self.balance = balance

    def pay(self, amount):
        self.balance -= amount
        print(f"Paid {amount}. Balance {self.balance}")


class StudentWallet(Wallet):
    def pay(self, amount):
        if amount > 2000:
            print("Student wallets are limited to 2000 per payment.")
            return
        super().pay(amount)


w = StudentWallet(5000)
w.pay(3000)
w.pay(1500)

# 6. is-a versus has-a: a Transaction is not a kind of Account, so no inheritance
class Transaction:
    def __init__(self, payee, amount):
        self.payee = payee
        self.amount = amount


class Account:
    def __init__(self, owner):
        self.owner = owner
        self.history = []          # has-a: an Account has Transactions

    def pay(self, payee, amount):
        self.history.append(Transaction(payee, amount))


a = Account("Vinay")
a.pay("Sumit", 600)
print(len(a.history), a.history[0].payee)
