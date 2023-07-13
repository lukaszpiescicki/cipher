from memory_buffer import Buffer
from cipher import Cipher, Text
from file_handler import save_to_file, read_file
from typing import Tuple


class Manager:
    def __init__(self):
        self.buffer = Buffer()

    def run(self):
        options = {
            "1": Cipher.encrypt,
            "2": Cipher.decrypt,
            "3": save_to_file,
            "4": read_file,
        }

        while True:
            user_input = input("Your choice:")
            if user_input in options:
                ciphered_word = options.get(user_input)
                self.buffer.add(ciphered_word)
                print(ciphered_word.text)

            elif user_input == "5":
                break
            else:
                print("Type in a valid number")

    def get_user_input(self, msg: str) -> str:
        return input(msg)

    def get_user_data(self) -> Tuple[str, str]:
        user_word: str = input("Insert a word: ")
        user_num: str = input("Insert a cipher key: ")
        return user_word, user_num

    def encrypt_file(self) -> Text:
        user_word, user_num = self.get_user_data()
        ciphered_word = Cipher.encrypt(user_word, int(user_num))
        return ciphered_word

    def save_file(self):
        user_file_name = self.get_user_input("Give a file name: ")
        save_to_file(user_file_name, self.buffer.memory_as_dict())

    def display_menu(self):
        print(
            f"Choose a number:\n"
            f"1.Encrypt a word\n"
            f"2.Decrypt a word\n"
            f"3.Save word to a file\n"
            f"4.Check words saved in the file\n"
            f"5.Exit\n"
        )
