# Inheritance: a class reuses another class's code.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def describe(self):
        return f"{self.name} is an employee."

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)     # let Employee set up name and salary
        self.team_size = team_size

    def describe(self):                    # overriding: this version wins for a Manager
        return f"{self.name} manages a team of {self.team_size}."

class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def describe(self):
        return f"{self.name} writes code in {self.language}."

emp = Employee("Prajnika", 60000)
mgr = Manager("Chitransh", 90000, 5)
dev = Developer("Rahul", 75000, "Python")

print(emp.describe())
print(mgr.describe())
print(mgr.team_size)

# Polymorphism: one call, many forms.
for person in [mgr, dev, emp]:
    print(person.describe())
