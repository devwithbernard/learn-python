"""
Encapsulation in OOP
"""


# Introduction to Encapsulation

class CreditCard:
    def __init__(self, name: str, owner: str, number: str) -> None:
        self.name = name
        self.__number = number
        self.__owner = owner


card = CreditCard('SGCI-BanK', 'James Lylian', '12345xdf')

print('Card name:', card.name)
print("Card's owner:", card.__owner)
print("Card number:", card.__number)