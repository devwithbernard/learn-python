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



if __name__ == '__main__':
    main()
