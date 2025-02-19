"""
Object-Oriented Programming (OOP) is a paradigm that helps structure programs using classes and objects.
It promotes code reusability, encapsulation, abstraction, inheritance, and polymorphism.
"""


# Class Creation

class Car:
    def __init__(self, brand: str, color: str) -> None:
        self.brand: str = brand
        self.color: str = color
        self.__mean_speed = 80.0

    @property
    def mean_speed(self) -> float:
        return self.__mean_speed

    @mean_speed.setter
    def mean_speed(self, value: float):
        self.__mean_speed = value

    def description(self) -> str:
        return f"{self.brand} car of {self.color} color"


def main() -> None:
    car: Car = Car('Tesla', 'red')
    print(f"{car.brand} Car of {car.color}")

    car_2: Car = Car('Peugeot', 'blue')
    print(car_2.description())

    car_2.mean_speed = 80.0

    print(f"""
    Car 
       brand: {car_2.brand}
       color: {car_2.color}
       mean_speed: {car_2.mean_speed} km/h
    """)


if __name__ == '__main__':
    main()
