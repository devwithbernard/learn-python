from typing import Dict, Any


def add_item(data: Dict, key: str, value: Any) -> Dict:
    """
    Add item to a dictionary and return the update data
    :param data: dictionary that represents a car
    :param key: key of dictionary
    :param value: value that corresponds to key
    :return: dictionary of car properties

    :raise ValueError: Raise a value error if the value in {key: value} pair is an empty string
    """
    if value:
        data[key] = value
        return data
    raise ValueError(f"{key}:'{value}' is not valid to store in {data}.")


def main() -> None:
    data: Dict = {
        'brand': 'Mustang',
        'year': 1957,
    }
    try:
        car_color: str = input("Enter the color of Car: ")
        car: Dict = add_item(data, 'color', car_color)
        print("Car: ", car)
    except ValueError as v_error:
        print(v_error.__str__())


if __name__ == '__main__':
    main()
