"""
Function definition
"""


def hello_func():
    """
        print hello world
    """
    print("Hello world")


# DRY : Don't Repeat Yourself
hello_func()
hello_func()
hello_func()
hello_func()


# Function execution


def capitalize(phrase: str) -> str:
    """
    Capitalize a sentence passing in parameter
    :param phrase: a string
    :return: capital case of hrase
    """

    return phrase.capitalize()


print(capitalize('Hello world Everyone!').upper())


def hello(greeting: str, name: str = 'You') -> str:
    """
    Return a hello world message
    :param name:
    :param greeting:
    :return:
    """
    return "{}, {}".format(greeting, name)


print(hello('Hello', 'Damian'))


# Positional keywords arguments
def student_infos(*args, **kwargs):
    """
    :param args:
    :param kwargs:
    """
    print(args, kwargs)


student_infos('Math', 'Art', name='John', age=28)

# Unpack parameters

courses = ['Math', 'Art']
info = {'name': 'Mark', 'age': 28}

student_infos(*courses, **info)

# A leap year
month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
months = ['January', 'February', 'March', 'April',
          'May', 'June', 'July', 'August',
          'September', 'October', 'November', 'December'
          ]


def is_leap(year: int) -> bool:
    """
    Return True if year is a leap year, False otherwise
    :param year: int
    :return: bool
    """
    return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year: int, month: int):
    """
    Return number of days in that month in that year
    :param year:
    :param month:
    :return:
    """

    if not 1 <= month <= 12:
        return 'Invalid Month'
    if month == 2 and is_leap(year):
        return 29
    return month_days[month - 1]


if is_leap(2000):
    month = 2
    print(f"{months[2 - 1]} has {days_in_month(2000, 2)} days")
