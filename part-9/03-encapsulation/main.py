"""
Encapsulation in OOP
"""


# Introduction to Encapsulation

class CreditCard:
    def __init__(self, name: str, owner: str, number: str) -> None:
        self.name = name
        self.__number = number
        self.__owner = owner
        self.__balance = 0

    def deposit_money(self, amount: float) -> None:
        if amount > 0:
            self.__balance += amount
        else:
            print("Amount is negative. Not allowed.")

    def withdraw_money(self, amount: float) -> None:
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def retrieve_balance(self) -> float:
        return self.__balance


card = CreditCard('Bank of Africa','Konan Bernard', '182233aqsd')
card.deposit_money(5000)
print(card.retrieve_balance())
card.deposit_money(100)
print(card.retrieve_balance())
card.withdraw_money(500)
print(card.retrieve_balance())
# The following will not work because the balance is not sufficient
card.withdraw_money(10000)
print(card.retrieve_balance())

card = CreditCard('SGCI-BanK', 'James Lylian', '12345xdf')

print('Card name:', card.name)
print("Card's owner:", card.__owner)
print("Card number:", card.__number)

