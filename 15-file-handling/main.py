"""
File Handling: Read file
"""
import os
import pathlib


def add_text_decorator(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print("Text added!")

    return wrapper


def delete_file(filename):
    fullpath = pathlib.Path.joinpath(pathlib.Path.cwd(), filename)
    if pathlib.Path.exists(fullpath):
        os.remove(fullpath)
    else:
        print(f"the file '{fullpath}' doesn't exists!")


class WriteFile:
    filename: str = None

    @property
    def full_path(self):
        return pathlib.Path.joinpath(pathlib.Path.cwd(), self.filename)

    def __init__(self, filename: str):
        if not filename:
            self.filename = 'file.txt'
        self.filename = filename
        self.__create()

    def __create(self):
        if not pathlib.Path.exists(self.full_path):
            with open(self.full_path, 'x') as f:
                print("File created")

    @add_text_decorator
    def add_text(self, text):
        if text:
            with open(self.full_path, 'r+') as f:
                content = f.readlines()
                if content:
                    f.write(f"\n{text}")
                else:
                    f.write(f"{text}")
        else:
            print("Provide correct content")

    def read_file(self):
        with open(self.full_path, 'r+') as f:
            content = f.read()
            print(content)

    def check_if_content_exists(self, text: str):
        with open(self.filename, 'r+') as f:
            lines = f.readlines()
            new_lines = [line.replace("\n", "").lower() for line in lines]

            return text.lower() in new_lines

    def __str__(self):
        return NotImplemented


def main() -> None:
    writeFile: WriteFile = WriteFile("mon-fichier.txt")

    text: str = "I love F#"

    if not writeFile.check_if_content_exists(text):
        writeFile.add_text(text)
    else:
        print(f"'{text}' is already in {writeFile.full_path}")


if __name__ == '__main__':
    main()
