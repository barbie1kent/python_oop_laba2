class Employee:
    def __init__(self, name: str, salary: int):
        self.name = name
        self.salary = salary

    def Salary(self):
        print(self.salary)

employee = Employee('Gosha', 10000000000)