"""
POO: Inheritance
"""


class Employee:
    raise_amount: float = 1.04

    def __init__(self, firstname: str, lastname: str, pay: float) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.email = f"{firstname.lower()}.{lastname.lower()}@gmail.com"
        self.pay = pay

    def __str__(self) -> str:
        return f"<{self.fullname()}>"

    def fullname(self) -> str:
        """Get full name of this person"""
        return f"{self.firstname} {self.lastname}"

    def apply_raise(self):
        """Apply raise amount to the pay"""
        self.pay = round(self.pay * self.raise_amount, 2)


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, firstname: str, lastname: str, pay: float, progr_language: str) -> None:
        super().__init__(firstname, lastname, pay)
        self.progr_language = progr_language


class Manager(Employee):
    def __init__(self, firstname: str, lastname: str, pay: float, employees: list[Employee] = None) -> None:
        super().__init__(firstname, lastname, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, employee: Employee) -> None:
        if employee not in self.employees:
            self.employees.append(employee)

    def remove_employee(self, employee: Employee) -> None:
        if employee in self.employees:
            self.employees.remove(employee)

    def print_employees(self) -> None:
        for employee in self.employees:
            print(f"-> {employee.fullname()}")


if __name__ == "__main__":
    dev_1: Developer = Developer("David", "Kahn", 50_000, "Python")
    dev_2: Developer = Developer("John", "Doe", 60_000, "C#")

    manager_1: Manager = Manager('John', 'Doe', 100_000)

    if isinstance(dev_1, Developer):
        print("Yes, it is!")
    else:
        print("No, it isn't!")

    if issubclass(Manager, Employee):
        print("<Manager class> inherit from <Employee>")
    else:
        print("That's not the case.")