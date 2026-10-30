# Mini project: every idea of the class in one program.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def describe(self):
        return f"{self.name} is an employee."


class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def describe(self):
        return f"{self.name} manages a team of {self.team_size}."


class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def describe(self):
        return f"{self.name} writes code in {self.language}."


employees = [
    Manager("Chitransh", 90000, 5),
    Developer("Rahul", 75000, "Python"),
    Employee("Prajnika", 60000),
]

for emp in employees:
    print(emp.describe())
    print("Salary:", emp.get_salary())
