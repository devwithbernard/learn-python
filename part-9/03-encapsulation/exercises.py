"""
Encapsulation: Exercises
"""


# TODO: Car

class Car:
    def __init__(self) -> None:
        self.__petrol_quantity = 0
        self.__odometer = 0

    def __str__(self) -> str:
        return f"Car: odometer reading {self.__odometer} km, petrol remaining {self.__petrol_quantity} litres"

    def fill_up(self) -> None:
        self.__petrol_quantity = 60

    def drive(self, velocity: float) -> None:
        CAR_CONSUMES_PER_KM = 1

        if velocity > 0:
            self.__odometer = velocity

        if self.__petrol_quantity - velocity > 0:
            self.__petrol_quantity -= velocity * CAR_CONSUMES_PER_KM
        else:
            self.__petrol_quantity = 0


car = Car()
print(car)
car.fill_up()
print(car)
car.drive(20)
print(car)
car.drive(50)
print(car)
car.drive(10)
print(car)
car.fill_up()
car.fill_up()
print(car)


# TODO: Recording

class Recording:
    def __init__(self, length: int) -> None:
        if length >= 0:
            self.__length = length
        else:
            raise ValueError('The length must not be below zero')

    @property
    def length(self) -> int:
        return self.__length

    @length.setter
    def length(self, length: int) -> None:
        if length >= 0:
            self.__length = length
        else:
            raise ValueError('The length must not be below zero')


the_wall = Recording(43)
print(the_wall.length)
the_wall.length = 44
print(the_wall.length)