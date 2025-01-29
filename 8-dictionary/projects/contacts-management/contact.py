def add_contact(contacts: dict) -> dict | None:
    copy_contacts: dict = contacts.copy()

    name: str = input("Enter your name: ")
    telephone: str = input("Enter your phone number: ")
    email: str = input("Enter your email: ")
    address: str = input("Provide your address: ")

    if name:
        new_contact: Contact = Contact(name, telephone, email, address)
        copy_contacts.update(new_contact.format_contact())
        print(f"Contact '{name}' added with success")
        return copy_contacts
    else:
        print("Provide the name of contact")

    return None


def search_contact(contacts: dict) -> bool:
    name: str = input("Contact name: ")

    if name in contacts:
        print(f"Infos about {name}: ")
        for key, value in contacts.get("name"):
            print(f"{key}: {value}")
        return True
    else:
        print("Contact not found")

    return False


def delete_contact(contacts: dict) -> dict | None:
    name: str = input("Enter your name: ")
    copy_contacts: dict = contacts.copy()

    if search_contact(copy_contacts):
        copy_contacts.pop(name)
        return copy_contacts
    else:
        print(f"Can delete contact")

    return None


class Contact:

    def __init__(self, name: str, telephone: str, email: str, address: str) -> None:
        self.name: str = name
        self.telephone: str = telephone
        self.email: str = email
        self.address: str = address

    def __str__(self) -> str:
        return f"Contact(name='{self.name}', telephone='{self.telephone}')"

    def format_contact(self):
        return {
            self.name: {
                "telephone": self.telephone,
                "email": self.email,
                "address": self.address
            }
        }
