import random
import string


class Password:
    def __init__(self, length: int):
        self.length = length
        self.add_char = False

    def add_special_char(self, added_special: bool = False):
        if added_special:
            self.add_char = True
        return self

    def generate(self) -> str:
        full_string = string.ascii_lowercase + string.ascii_uppercase + string.digits

        if self.add_char:
            full_string += string.punctuation

        list_sequence = list(full_string)
        random.shuffle(list_sequence)

        return "".join(list_sequence[:self.length])


def add_special_character() -> bool:
    user_input = input("Add special characters while generating password? (yes/no or y/n): ").strip().lower()
    return user_input in ('y', 'yes')

def set_password_length() -> int:
    while True:
        try:
            password_length = int(input("Choose password length: ").strip())
            if 4<= password_length <= 20:
                return password_length
            else:
                print("4<= password length <= 20")
        except ValueError:
            print("You must choose length between 4 and 20")


def run_process():
    while True:
        password_length = set_password_length()
        add_special_char = add_special_character()

        password = (Password(password_length)
                    .add_special_char(add_special_char)
                    .generate())

        print(password)

        stop_program = input("Would you want to continue? (yes/no or n/y): ").strip().lower()

        if stop_program in ('n', 'no'):
            print("Goodbye")
            break
        else:
            print("Continue to generate password")



def main() -> None:
    print("===== PASSWORD GENERATING =====")
    run_process()


if __name__ == '__main__':
    main()
