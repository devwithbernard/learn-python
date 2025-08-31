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
