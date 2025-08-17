from datetime import datetime, time

# The datetime object

my_time = datetime.now()
print("My time: %s" % my_time)

# Define the datetime object
today = datetime(2025, 10, 15)
print("Today:", today)

# Access to day, month and year of a datetime object
day = my_time.day
month = my_time.month
year = my_time.year

print(f"Date: {year}/{'0' + str(month) if month < 10 else month}/{'0' + str(day) if day < 10 else day}")