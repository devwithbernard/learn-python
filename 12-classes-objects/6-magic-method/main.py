class Employee:
    raise_amount: float = 1.04
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            print("class instance created")
        return cls._instance

    def __init__(self, firstname: str, lastname: str, pay: float) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.email = f"{firstname.lower()}.{lastname.lower()}@gmail.com"
        self.pay = pay

    def __str__(self) -> str:
        return f"<{self.fullname()}>"

    def __repr__(self):
        return f"Employee({self.firstname}, {self.lastname},{self.pay})"

    def __format__(self, format_spec):
        return f"{self.pay:.2f}"

    def __add__(self, other):
        return float(self.pay + other.pay)

    def __len__(self) -> int:
        return len(self.fullname())

    def fullname(self) -> str:
        """Get full name of this person"""
        return f"{self.firstname} {self.lastname}"

    def apply_raise(self):
        """Apply raise amount to the pay"""
        self.pay = round(self.pay * self.raise_amount, 2)


if __name__ == "__main__":
    emp_1: Employee = Employee("John", "Doe", 80_000)
    print(repr(emp_1))
    print(format(emp_1))

    emp_2: Employee = Employee("David", "William Alby", 90_000)

    print(emp_1 + emp_2)

    print(len(emp_2))