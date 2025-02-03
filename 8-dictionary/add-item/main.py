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


def update_data(data: Dict, item: dict[str, Any]) -> Dict:
    """
    Update a dictionary with {key: value} pair
    :param data: dictionary that will be updated
    :param item: dictionary to add to data
    :return: dictionary after updated data
    """

    copy_data: Dict = data.copy()
    copy_data.update(item)
    return copy_data


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

    car_price: str = input("Enter car price: ")
    new_car: Dict = update_data(data, {'price': car_price})
    print("Updated car: ", new_car)


if __name__ == '__main__':
    main()
