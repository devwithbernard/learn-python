"""
Learn classes and instance of classes
"""


class Employee:
    def __init__(self, firstname: str, lastname: str, email: str, pay: float) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.pay = pay

    def fullname(self) -> str:
        return f"{self.firstname} {self.lastname}"


def main() -> None:
    employee_1: Employee = Employee("Bernard", "Konan", "bernard.konan@yahoo.fr", 50_000)
    employee_2: Employee = Employee("Nguessan", "Koffi", "nguessan.koffi@gmail.com", 70_000)

    print(f"Employee 1: {employee_1}")
    print(f"Employee 2: {employee_2}")

    # Print some infos
    print("Employee 1 email: ", employee_1.email)
    print("Employee 2 email: ", employee_2.email)

    print(f"Full name of employee 1: {employee_1.fullname()}")
    print(f"Full name of employee 2: {employee_2.fullname()}")


if __name__ == '__main__':
    main()
