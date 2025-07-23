even_numbers, odd_numbers = [], []

for number in range(11):
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

print(even_numbers, odd_numbers)