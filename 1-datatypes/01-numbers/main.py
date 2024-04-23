"""
Les nombres en python sont de 2 types:
    Les entiers : int
    Les nombres decimaux: float
"""
integer = 10

for i in range(1, integer + 1):
    print(str(i) + ' ==> ' + str(i * integer))


print("Caculator:....")
print("""
    Quelle opération arithmétique souhaitez-vous faire ?:
    \t 1- L'addition (+) 
    \t 2- La multiplication (*)
    \t 3- La soustraction (-)
    \t 4- La division (/)
    \t 5- La puissance (^)
""")

arithmetic_operation = None
operation_choice = input("Veuillez choisir une operation: (1, 2, 3, 4, "
                         "5): ")
try:
    operation_choice = int(operation_choice)
    number1 = float(input('Entrer le premier nombre: '))
    number2 = float(input('Entrer le second nombre: '))
    
    if 1 < operation_choice and operation_choice > 5:
        raise ValueError('L\'option choisie doit être entre 1 et 5')
except ValueError as error:
    print('Le choix fait ou un nombre saisi est incorrect!\nVeuillez choisir '
          'un chiffre en 1 et 5')
    raise error

if operation_choice == 1:
    arithmetic_operation = '+'
    print(f"{number1} + {number2} = {number1 + number2}")
elif operation_choice == 2:
    arithmetic_operation = '*'
    print(f"{number1} * {number2} = {number1 * number2}")
elif operation_choice == 3:
    arithmetic_operation = '-'
    print(f"{number1} - {number2} = {number1 - number2}")
elif operation_choice == 4:
    arithmetic_operation = '/'
    try:
        print(f"{number1} / {number2} = {number1 / number2}")
    except ZeroDivisionError:
        print('Divisiion par 0: Impossible...')
elif operation_choice == 5:
    arithmetic_operation = '^'
    print(f"{number1} ^ {number2} = { round(number1 ** number2, 3)}")
    
    
