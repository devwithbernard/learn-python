"""
In Python, tuples are immutable sequences commonly used for grouping data.
"""
from typing import Any
import requests
import openpyxl
from openpyxl.styles import Font
import pprint


def main() -> None:
    fruits: tuple[str, ...] = ('Apple', 'Banana', 'Cherry', 'Strawberry')

    def print_tuple(sequence: tuple) -> None:
        print(f"""
        type of sequence => {type(sequence).__name__}
        sequence => {sequence}
        """)

    print_tuple(fruits)

    def tuple_items(sequence: tuple[str, ...]) -> tuple[str, ...]:
        first_tuple, second_tuple, *rest = sequence
        last_tuple = sequence[-1]

        return first_tuple, second_tuple, last_tuple

    print(f"""tuple items => {tuple_items(fruits)}""")

    def duplicate_items(sequence: tuple[str, ...]) -> list[tuple[str, int]]:
        counts: dict = {item: sequence.count(item) for item in set(sequence)}
        duplicate_items: list[tuple[str, int]] = [
            (item, count) for item, count in counts.items() if count > 1
        ]
        duplicate_items.sort(key=lambda x: x[0], reverse=False)
        return duplicate_items

    print(duplicate_items(fruits + ('Apple', 'Banana', 'Cherry', 'Apple')))

    def calculate_distance(point1: tuple, point2: tuple) -> float:
        distance: float = ((point1[0] - point2[0]) ** 2) + ((point1[1] - point2[1]) ** 2) ** 0.5
        return round(distance, 3)

    calculated_distance: float = calculate_distance((10, 50), (30, 8))
    print(f"""Distance calculated => {calculated_distance}""")

    def length_of_tuple(sequence: tuple) -> None:
        length: float = len(sequence)
        if length == 0:
            print("There are no items in tuple.")
        elif length == 1:
            print("There are only one item in tuple.")
        else:
            for index, item in enumerate(sequence):
                print(f"""{index} => {item}""")

    length_of_tuple(fruits)

    def create_tuple_with_one_item(item: Any) -> tuple:
        iterable: tuple = (item,)
        return iterable, type(iterable)

    value, datatype = create_tuple_with_one_item('Banana')
    print(f"value: {value}, type: {datatype.__name__}")

    def create_tuple_with_multiple_items():
        def get_todos(url: str) -> list[dict]:
            try:
                response: requests.Response = requests.get(url)
                todos: list[dict] = response.json()
                return todos
            except requests.ConnectionError as conn_error:
                print(f"Errors occur while connecting to server.")
            except requests.HTTPError as http_error:
                print(f"Errors occur while fetching data")

        def save_into_excel(filename: str, data: list[tuple[int, str, bool]]) -> None:
            wb = openpyxl.Workbook()
            ws = wb.active
            ws.title = "Todo list"

            # Add header row with bold font
            header: tuple[str, ...] = ('Id', 'Title', 'Completed',)
            for col, value in enumerate(list(header), start=1):
                ws.cell(row=1, column=col, value=value).font = Font(bold=True)

            #Add data
            for row in data:
                ws.append(row)

            # Save the file
            wb.save(f"{filename}.xlsx")
            print(f"Data written to '{filename}.xlsx' with formatting")
        try:
            todos: list[dict] = get_todos("https://jsonplaceholder.typicode.com/todos")
            todos_tuple: list[tuple[int, str, bool]] = [(todo['id'], todo['title'], todo['completed']) for todo in todos]
            save_into_excel('Todo_List', todos_tuple)
        except Exception as e:
            print(e.__str__())

    create_tuple_with_multiple_items()


if __name__ == '__main__':
    main()
