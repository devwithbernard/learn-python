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

    # Update dictionary
    def update_dict(origin_data:dict, coming_data: dict) -> dict:
        copy_origin_data: dict = origin_data.copy()
        copy_origin_data.update(coming_data)
        return copy_origin_data

    updated_dict: dict = update_dict(car, {'price': 1_000_000})
    print(f"Updated data: {updated_dict}")


if __name__ == '__main__':
    main()
