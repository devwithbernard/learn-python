"""
Iterator in python
"""


class MyNumbers:
    max_iteration: int = 100

    def __init__(self):
        self.number = 0

    def __iter__(self):
        self.number += 1
        return self

    def __next__(self):
        if self.number < self.max_iteration:
            x = self.number
            self.number += 1
            return x
        else:
            raise StopIteration


def main() -> None:
    # Iterable
    cars: tuple = ('Peugeot', 'Bugatti', 'Mercedes', 'BMW')

    my_iter = iter(cars)

    print(next(my_iter))  # 'Peugeot'
    print(next(my_iter))  # 'Bugatti'
    print(next(my_iter))  # 'Mercedes'
    print(next(my_iter))  # 'BMW'
    # print(next(my_iter))    # StopIteration Error

    # Loop through iterable object
    car_brands: dict[str, list[str]] = {
        "Germany": ["BMW", "Mercedes-Benz", "Audi", "Volkswagen", "Porsche", "Opel"],
        "France": ["Renault", "Peugeot", "Citroën", "DS Automobiles", "Bugatti"],
        "Italy": ["Ferrari", "Lamborghini", "Maserati", "Alfa Romeo", "Fiat"],
        "Japon": ["Toyota", "Honda", "Nissan", "Mazda", "Subaru", "Mitsubishi", "Suzuki", "Lexus"],
        "USA": ["Ford", "Chevrolet", "Tesla", "Dodge", "Jeep", "Cadillac"],
        "England": ["Rolls-Royce", "Bentley", "Aston Martin", "Jaguar", "Land Rover", "McLaren"],
        "Sweden": ["Volvo", "Koenigsegg"],
        "North Korea": ["Hyundai", "Kia", "Genesis"],
        "China": ["BYD", "NIO", "Geely", "Chery"]
    }

    for country in car_brands:
        print(f"{country}:")

        for index, car_brand in enumerate(car_brands[country]):
            print(f"\t{index + 1}. {car_brand}")

    # using custom iterator
    my_number = MyNumbers()
    my_number_iter = iter(my_number)

    print(next(my_number_iter))
    print(next(my_number_iter))
    print(next(my_number_iter))


if __name__ == '__main__':
    main()
