"""
Class attributes
"""

# Class variables: Example 1
class SavingsAccount:
    general_rate = 0.03

    def __init__(self, account_number: str, balance: float, interest_rate: float) -> None:
        self.__account_number = account_number
        self.__balance = balance
        self.__interest_rate = interest_rate

    def add_interest(self) -> None:

        self.__balance += self.__balance * self.total_interest

    @property
    def balance(self) -> float:
        return self.__balance

    @property
    def total_interest(self) -> float:
        return SavingsAccount.general_rate + self.__interest_rate


# The general rate exists independently of any object instances
print("The general interest rate is", SavingsAccount.general_rate)

account = SavingsAccount("12345", 1000, 0.05)
# Add the total interest accrued to the balance on the account
account.add_interest()
print(account.balance)


# Another example
account1 = SavingsAccount("12345", 100, 0.03)
account2 = SavingsAccount("54321", 200, 0.06)

print("General interest rate:", SavingsAccount.general_rate)
print(account1.total_interest)
print(account2.total_interest)

# The general rate of interest is now 10 percent
SavingsAccount.general_rate = 0.10

print("General interest rate:", SavingsAccount.general_rate)
print(account1.total_interest)
print(account2.total_interest)

# Class variables: Example 2
class PhoneNumber:
    country_codes = {"Finland": "+358", "Sweden": "+46", "United States": "+1", 'Ivory Coast': '+225'}

    def __init__(self, name: str, phone_number: str, country: str) -> None:
        self.__name = name
        self.__country = country
        self.__phone_number = phone_number

    @property
    def phone_number(self) -> str:
        # the initial zero is removed as the country code is prefixed
        return PhoneNumber.country_codes[self.__country] + " " + self.__phone_number[1:]

    @phone_number.setter
    def phone_number(self, number: str) -> None:
        for character in number:
            if character not in "1234567890 ":
                raise ValueError("A phone number can only contain numbers and spaces")

        self.__phone_number = number

    @property
    def local_number(self) -> str:
        return self.__phone_number

    @property
    def country(self) -> str:
         return self.__country

    @country.setter
    def country(self, country: str) -> None:
        if country not in PhoneNumber.country_codes:
            raise ValueError('This country is not on the list.')

        self.__country = country

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        if not name:
            raise ValueError('Name must not be empty')

        self.__name = name

    def __str__(self) -> str:
        return f"{self.phone_number} ({self.name})"


pn = PhoneNumber("Peter Pythons", "040 111 1111", "Sweden")
print(pn)
print(pn.phone_number)
print(pn.local_number)
