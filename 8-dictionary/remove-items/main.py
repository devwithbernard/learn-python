"""
Remove item from dictionary
"""

from typing import Dict, Any


def remove_item(data: Dict, key: Any) -> Dict:
    copy_data: Dict = data.copy()
    if key in data:
        copy_data.pop(key)
        return copy_data


def main() -> None:
    person: Dict = {
        "name": "Bernard Konan",
        "age": 28,
        "degree": "Master in Civil Engineering"
    }

    print(f"Person without degree: {remove_item(person, 'degree')}")


if __name__ == '__main__':
    main()
