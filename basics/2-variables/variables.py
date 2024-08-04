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
