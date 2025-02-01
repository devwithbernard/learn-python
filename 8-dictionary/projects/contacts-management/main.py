import os
from contact import add_contact, search_contact, delete_contact
from storage import load_data, store_data

FILE: str = os.path.join(os.path.curdir, 'data.json')


def main() -> None:
    contacts: dict = load_data(FILE) if os.path.exists(FILE) and os.path.getsize(FILE) > 0 else {}

    print(contacts)

    print("""
    Contact Management:
    1 -> Add a contact
    2 -> Search a contact by provide a name
    """)

    while True:
        choice: str = input('Enter your choice: ')

        if choice in {'1', '2'}:
            break
        else:
            print("Choose a correct option.")

    if choice == '1':
        new_contacts: dict = add_contact(contacts)
        store_data(FILE, new_contacts)
        print(new_contacts)

    elif choice == '2':
        contact: dict | bool = search_contact(contacts)

        if isinstance(contact, bool):
            print("Contact not found!")

        if contact:
            print(f"Infos about {contact.get('name')}: ")
            for key, value in contacts.items():
                print(f"\t{key.capitalize()} => {value}")


if __name__ == '__main__':
    main()
