"""
Defining classes
"""

# Define class

class BankAccount:
    pass

peter_account = BankAccount()
peter_account.owner = "Peter Python"
peter_account.balance = 500.0

print(peter_account.owner)
print(peter_account.balance)

peter_account.balance = 1_000

print(f"{peter_account.owner} new balance: ${peter_account.balance}")