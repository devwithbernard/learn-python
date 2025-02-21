"""
Class variables
"""


class Employee:
    _raise_amount = 1.05

    def __init__(self, firstname: str, lastname: str, pay: float) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.email = f"{firstname.lower()}.{lastname.lower()}@yahoo.com"
        self.pay = pay

    def fullname(self) -> str:
        return f"{self.firstname} {self.lastname}"

    def apply_raise(self) -> None:
        self.pay = round(float(self.pay * self._raise_amount), 2)


def main() -> None:
    emp_1 = Employee('John', 'Smith', 1_000)
    emp_2 = Employee('Jane', 'Doe', 1_500)

    emp_1.apply_raise()
    emp_2.apply_raise()

    print(f"""
    {emp_1.fullname()}
        pay: ${emp_1.pay}
    """)
    print(f"""
    {emp_2.fullname()}
        pay: ${emp_2.pay}
    """)


if __name__ == '__main__':
    main()
