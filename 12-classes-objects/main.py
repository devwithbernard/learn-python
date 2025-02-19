"""
Object-Oriented Programming (OOP) is a paradigm that helps structure programs using classes and objects.
It promotes code reusability, encapsulation, abstraction, inheritance, and polymorphism.
"""


# Class Creation

class Car:
    def __init__(self, brand: str, color: str) -> None:
        self.brand: str = brand
        self.color: str = color


def main() -> None:
    car: Car = Car('Tesla', 'red')
    print(f"{car.brand} Car of {car.color} ")


if __name__ == '__main__':
    main()
