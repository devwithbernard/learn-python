"""
Change dictionary items
"""

from typing import Dict, Any


def main() -> None:
    car: dict['str', ...] = {
        "brand": 'Ford',
        "model": 'Mustang',
        "year": 1964
    }

    def change_dict_items(data: Dict, key: str, value: Any) -> dict:
        if key in data:
            data[key] = value

        return data

    new_data: Any = change_dict_items(car, 'brad', 'Bugatti')
    print(f"updated data: ", new_data)


if __name__ == '__main__':
    main()
