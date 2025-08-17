"""
Times and Dates: Exercises
"""

# TODO: How old

from datetime import datetime

def how_old():
    day = int(input("Day: "))
    month = int(input("Month: "))
    year = int(input("Year: "))

    birth_day = datetime(year, month, day)
    new_millenium = datetime(2000, 1, 1)

    if new_millenium < birth_day:
        print("You weren't born yet on the eve of the new millennium.")
    else:
        difference = new_millenium - birth_day
        print(f"You were {difference.days} days old on the eve of the new millennium.")


how_old()