from typing import Dict, Callable
from .memory_buffer import Buffer
from .cipher import Cipher
from .file_handler import save_to_file, read_file


class Manager:
    def __init__(self) -> None:
        self.buffer = Buffer()
        self.is_running = True

    def run(self) -> None:
        options: Dict[str, Callable] = {
            "1": lambda: self.process_text("encrypt"),
            "2": lambda: self.process_text("decrypt"),
            "3": self.save_file,
            "4": self.read_file,
            "5": self.buffer.display,
            "6": self.stop_program,
        }

        while self.is_running:
            self.display_menu()
            user_input = self.get_user_input("Choose an option: ")
            if user_input in options:
                options.get(user_input)()
            else:
                print("Type in a valid number")

    def get_user_input(self, msg: str) -> str:
        return input(msg)

    def process_text(self, operation: str) -> None:
        user_word = self.get_user_input("Type in a word to encrypt: ")
        user_num = self.get_user_input("Type in a key: ")

        if operation == "encrypt":
            processed_text = Cipher.encrypt(user_word, int(user_num))
        elif operation == "decrypt":
            processed_text = Cipher.decrypt(user_word, int(user_num))
        else:
            print("Invalid Operation")
            return

        self.buffer.add(processed_text)

    def save_file(self) -> None:
        user_file_name: str = self.get_user_input("Give a file name: ")
        save_to_file(user_file_name, self.buffer.memory_as_dict())

    def read_file(self) -> None:
        user_file_name: str = self.get_user_input(
            "Give name of a file you want to read: "
        )
        read_file(user_file_name)

    def stop_program(self) -> None:
        self.is_running = False

    def display_menu(self) -> None:
        print(
            f"Choose a number:\n"
            f"1.Encrypt a word\n"
            f"2.Decrypt a word\n"
            f"3.Save word to a file\n"
            f"4.Check words saved in the file\n"
            f"5.Check words saved in the buffer\n"
            f"6.Exit\n"
        )
