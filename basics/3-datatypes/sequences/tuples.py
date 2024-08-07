from typing import Tuple, Final

if __name__ == '__main__':
    PYTHON: Final[str] = 'PYTHON'
    programming_languages: Tuple[str, ...] = ('Python', 'JavaScript', 'C#', 'Java', 'Rust')

    print("List of programming languages: ", programming_languages)
    print("type of variables: ", type(programming_languages))

    # Loop through tuple

    for index, programming_language in enumerate(programming_languages):
        print(f"{index} => {programming_language}")