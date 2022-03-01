class Employee:
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary

    def __repr__(self) -> str:
        return f"{self.name} has a salary of {self.salary:.2f}"


class Manager(Employee):
    def __init__(self, name, salary, department):
        self.department = department
        super().__init__(name, salary)

    def __repr__(self) -> str:
        return f"{self.name} has a salary of {self.salary:.2f} and manages the {self.department} department"


class Executive (Manager):
    def __init__(self, name, salary, department):
        super().__init__(name, salary, department)

    def __repr__(self) -> str:
        return f"{self.name} has a salary of {self.salary:.2f} and is the excutive for the {self.department} department"
