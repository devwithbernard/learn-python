from contact import Contact
from contact import add_contact, search_contact, delete_contact
from json import load, dumps


def main() -> None:
    contacts: dict = {}

    print("""
    Contact Management:
    1 -> Add a contact
    2 -> Search a contact by provide a name
    3 -> Delete a contact by provide a name
    """)

    while True:
        choice: str = input('Enter your choice: ')

        if choice in {'1', '2', '3'}:
            break
        else:
            print("Choose a correct option.")

    if choice == '1':
        new_contacts: dict = add_contact(contacts)
        print(new_contacts)


if __name__ == '__main__':
    main()
