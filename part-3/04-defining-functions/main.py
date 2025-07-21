# TODO: Function definition
def greeting():
    print("Hello everyone!")


greeting()


# Exercise
# TODO: Seven Brothers
def display_name(name: str) -> None:
    print(name)


names: list[str] = ['Aapo', 'Eero', 'Juhani', 'Lauri',
                    'Simeoni', 'Timo', 'Tuomas']

for name in names:
    display_name(name)