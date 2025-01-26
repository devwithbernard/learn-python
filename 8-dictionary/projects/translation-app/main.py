from typing import Dict
from translation import translations, translate_english, translate_to_french


def main() -> None:
    print("Bienvenue dans le Traducteur Basique!")
    print("Options disponibles:")
    print("1. Traduire de l'anglais au français")
    print("2. Traduire du français à l'anglais")
    print("3. Quitter")

    while True:
        choice: str = input("Choississez une option: ")
        phrase: str = input("Texte à traduire: ")

        original_text: str = ''
        translated_text: str = ''

        if choice == '1':
            if phrase.lower() in translations:
                original_text = phrase
                translated_text = translations[phrase]
            else:
                print(f"Impossible à traduire via notre algorithme")
        if choice == '2':
            if phrase.lower() in translations.values():
                original_text = phrase
                translated_text = [key for key, value in translations.items() if value == phrase][0]
            else:
                print(f"Impossible à traduire via notre algorithme")
        if choice == '3':
            print(f"Traduction terminée!")
            break

        print(f"""{original_text}  => {translated_text}""")


if __name__ == '__main__':
    main()
