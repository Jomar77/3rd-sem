class Employee:
    def __init__(self):
        self.name = ""
        self.salary = 0

    def __repr__(self) -> str:
        return f"{self.name} has a salary of {self.salary}"


class Manager(Employee):
    def __init__(self):
        self._department = ""

    def __repr__(self) -> str:
        return f"{self.name} has a salary of {self.salary} and manages the {self._department} department"


class Executive (Manager):
    def __init__(self):
        super().__init__()

    def __repr__(self) -> str:
        return f"{self.name} has a salary of {self.salary} and is the excutive for the {self._department} department"
