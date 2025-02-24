"""
Class and Static Method
"""

import requests


class HTTP:
    url: str = ''

    @staticmethod
    def get(cls):
        try:
            response: requests.Response = requests.get(cls.url)
            data = response.json()
            return data
        except requests.ConnectionError as con_error:
            print(f"Connection error occurs: {con_error}")
        except requests.HTTPError as http_error:
            print(f"Request Error occurs: {http_error}")


class MathOperation:
    PI: float = 3.14

    @staticmethod
    def circle_area(cls, radius: float) -> float:
        return cls.PI * (radius ** 2)

    @staticmethod
    def circle_perimeter(cls, radius: float) -> float:
        return 2 * cls.PI * radius

    @staticmethod
    def add(cls, x: float, y: float) -> float:
        return x + y

    @staticmethod
    def times(cls, x: float, y: float) -> float:
        return x * y

    @staticmethod
    def subtraction(cls, x: float, y: float) -> float:
        return x - y

    @staticmethod
    def divide(cls, x: float, y: float) -> float:
        try:
            return x / y
        except ZeroDivisionError as error:
            print(f"Impossible to divide by 0: {error}")


def main() -> None:
    HTTP.url = 'https://jsonplaceholder.typicode.com/posts/1'
    post: dict = HTTP.get(HTTP)

    if post:
        for key, value in post.items():
            print(f"{key} => {value}") if key != 'userId' else None

    # Math calculus
    radius: float = float(input("Enter circle radius: "))
    number_1: float = float(input("Enter first number: "))
    number_2: float = float(input("Enter second number: "))

    # Circle Perimeter and Area
    print(f"""
    Circle:
        Perimeter: {MathOperation.circle_perimeter(MathOperation, radius)}
        Area: {MathOperation.circle_area(MathOperation, radius)}
    """)

    # Basic Math Operation
    print(f"""
    Math operation:
      {number_1} + {number_2} = {MathOperation.add(MathOperation, number_1, number_2)}
      {number_1} - {number_2} = {MathOperation.subtraction(MathOperation, number_1, number_2)}
      {number_1} x {number_2} = {MathOperation.times(MathOperation, number_1, number_2)}
      {number_1} / {number_2} = {MathOperation.times(MathOperation, number_1, number_2)}
    """)


if __name__ == '__main__':
    main()
