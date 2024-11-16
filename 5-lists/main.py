def main() -> None:
    # Create a list
    fruits: list[str] = ["Apple", "Banana", "Cherry"]
    print(list, "Type: ", type(fruits))

    # Accessing to list items
    first_item: str = fruits[0]
    second_item: str = fruits[1]
    last_item: str = fruits[len(fruits) - 1]

    print(f"""
    First item => {first_item}
    Second item => {second_item}
    Last item => {last_item}
    """)

    # List is changeable
    mango: str = 'Mango'
    fruits.append(mango)
    print("After appending item: ", fruits)

    fruits.remove("Banana")
    print("After removing item: ", fruits)

    fruits[1] = "Pineapple"
    print("After changing item: ", fruits)

    # Length of List
    number_of_items: int = len(fruits)
    print(f"They are {number_of_items} fruits in list")


if __name__ == '__main__':
    main()
