""""
Variables in python
"""

if __name__ == '__main__':
    mango_quantity: int = 50
    memory_address: int = id(mango_quantity)

    today_date: str = '2014/08/03'
    today_date_memory_address: int = id(today_date)

    print({'memory address': memory_address, 'variable': mango_quantity})
    print({'memory address': today_date_memory_address, 'variable': today_date})

    # Print variables and their types

    counter: int = 10
    distance: float = 100.0
    driver_name: str = 'Usain Bolt'

    print(f'counter => {counter} hours, distance => {distance} km , driver => {driver_name}')

    variables_definition: list[dict] = [
        {'variable': counter, 'type': type(counter)},
        {'variable': distance, 'type': type(distance)},
        {'variable': driver_name, 'type': type(driver_name)},
    ]

    print(variables_definition)

    # Deleting variables
    full_name: str = 'John Cena'
    print(f"The famous athlete name is {full_name}")

    del full_name
    print(full_name)  # Raise a NameError exception with the message 'name full_name is not defined

