"""
Access Dictionary Items
"""
from typing import Any


def main() -> None:
    def dictionary_items() -> None:
        car: dict = {
            "brand": "Ford",
            "model": "Mustang",
            "year": 2025
        }

        brand: str = car["brand"]
        model: str = car["model"]
        year: int = car["year"]

        print(f"""
        Car:
            brand => {brand}
            model => {model}
            year => {year}
        """)

    dictionary_items()

    def access_dictionary_items(data: dict) -> None:
        for key in data:
            if key != 'in_stock':
                print(f"{key} => {data.get(key)}")
            if key == 'in_stock' and data.get(key):
                print("Product in stock")
            elif key == 'in_stock' and not data.get(key):
                print("Product out of stock")

    product: dict[str, Any] = {
        "name": "Laptop",
        "brand": "Dell",
        "price": 1200,
        "in_stock": True
    }
    access_dictionary_items(product)

    def get_dict_keys(data: dict) -> tuple[str, ...]:
        return tuple(data.keys())

    for key in get_dict_keys(product):
        print(f"{key}: {product[key]}")

    def get_dict_values(data: dict):
        return data.values()

    print("Product infos:")
    for value in get_dict_values(product):
        print(f"\t{value}")


if __name__ == '__main__':
    main()
