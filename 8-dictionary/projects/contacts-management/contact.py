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


def search_contact(contacts: dict) -> dict | bool:
    name: str = input("Contact name: ")

    for contact_name in contacts.keys():
        if name.lower() in contact_name.lower():
            name = contact_name
            contact: dict = contacts.get(name)
            return Contact(name, contact['telephone'], contact['email'], contact['address']).format_contact()

    return False


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
