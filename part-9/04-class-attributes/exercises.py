"""
Class attributes: Exercises
"""


# TODO: Postcodes
class City:
    post_codes = {
        'Helsinki': '00100',
        'Turku': '20100',
        'Tampere': '33100',
        'Rovaniemi': '96100',
        'Oulu': '90100'
    }

    def __init__(self, name: str, post_code: str) -> None:
        self.__name = name
        self.__post_code = post_code

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        if name not in City.post_codes:
            raise ValueError('City not in list of cities')

        self.__name = name

    @property
    def post_code(self) -> str:
        return self.__post_code

    @post_code.setter
    def post_code(self, post_code) -> None:
        if post_code not in City.post_codes.values():
            raise ValueError(f"The post_code must be in {City.post_codes.values()}")
        else:
            self.__post_code = post_code

    def __str__(self) -> str:
        return f"{self.__name} ({self.__post_code})"


# TODO: List helper

class ListHelper:

    @classmethod
    def __helper(cls, items: list):
        frequency_items = {}

        if items:
            for item in items:
                frequency_items[item] = frequency_items.get(item, 0) + 1
        return frequency_items

    @classmethod
    def greatest_frequency(cls, items: list):
        frequency_items = ListHelper.__helper(items)

        if not frequency_items:
            return None

        max_count = max(frequency_items.values())

        # Return the first item with maximum frequency
        for item, count in frequency_items.items():
            if count == max_count:
                return item

    @classmethod
    def doubles(cls, items: list):
        frequency_items = ListHelper.__helper(items)

        values = []

        for item, count in frequency_items.items():
            if count == 2:
                values.append(item)

        return ', '.join([str(value) for value in values])


numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
print(ListHelper.greatest_frequency(numbers))
print(ListHelper.doubles(numbers))
