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


if __name__ == "__main__":
    emp_1: Employee = Employee("John", "Doe", 80_000)
    emp_2: Employee = Employee("David", "William", 90_000)
