"""
Defining classes
"""

# Define class

class BankAccount:
    def __init__(self, owner: str, balance: float) -> None:
        self.owner = owner
        self.balance = balance

peter_account = BankAccount("Peter Python", 500.0)
peter_account.owner = "Peter Python"
peter_account.balance = 500.0

print(peter_account.owner)
print(peter_account.balance)

peter_account.balance = 1_000

print(f"{peter_account.owner} new balance: ${peter_account.balance}")

# Construct other objects

jack_account: BankAccount = BankAccount("Jack Sheridan", 5000)
mark_account: BankAccount = BankAccount("Mark Monroe", 3500)

print(f"{jack_account.owner}: ${jack_account.balance}")
print(f"{mark_account.owner}: ${mark_account.balance}")

jack_account.balance = 7400
mark_account.balance += 2000

print(f"New balance({jack_account.owner}): ${jack_account.balance}")
print(f"New balance({mark_account.owner}): ${mark_account.balance}")