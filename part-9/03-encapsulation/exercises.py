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


# TODO: Weather station

class WeatherStation:
    def __init__(self, name: str) -> None:
        self.__name = name
        self.__observations: list[str] = []

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        if name != 0:
            self.__name = name
        else:
            raise ValueError('The name may not be empty.')

    def add_observation(self, observation: str) -> None:
        if observation != '':
            self.__observations.append(observation)

    def latest_observation(self) -> str:
        if len(self.__observations) == 0:
            return ""
        return self.__observations[-1]

    def number_of_observations(self) -> int:
        return len(self.__observations)

    def __str__(self) -> str:
        return f"{self.__name} ({self.number_of_observations()} observations)"


station = WeatherStation("Houston")
station.add_observation("Rain 10mm")
station.add_observation("Sunny")
print(station.latest_observation())

station.add_observation("Thunderstorm")
print(station.latest_observation())

print(station.number_of_observations())
print(station)
