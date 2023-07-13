# from __future__ import annotations
from memory_buffer import Text

# from abc import ABC, abstractmethod

# class Rot(ABC):
#     @abstractmethod
#     def encrypt(self):
#         pass
#
#     @abstractmethod
#     def decrypt(self):
#         pass
#
#     @staticmethod
#     def get_rot(rot_type: str) -> Rot13 | Rot47:
#         if rot_type == 'rot13':
#             return Rot13()
#         elif rot_type == 'rot47':
#             return Rot47()
#
# class Rot13(Rot):
#     def encrypt(self):
#         pass
#
#     def decrypt(self):
#         pass
#
#
# class Rot47(Rot):
#     def encrypt(self):
#         pass
#
#     def decrypt(self):
#         pass
#
#
# class Rot15(Rot):
#     pass


class Cipher:
    @staticmethod
    def encrypt(text: str, key: int) -> Text:
        result: str = ""
        for char in text:
            if char == " ":
                result += " "
            elif char.isupper():
                result += chr((ord(char) + key - 65) % 26 + 65)
            else:
                result += chr((ord(char) + key - 97) % 26 + 97)
        return Text(result, key, "encrypted")

    @staticmethod
    def decrypt(text: str, key: int) -> Text:
        result = ""

        for char in text:
            if char == " ":
                result += " "
            elif char.isupper():
                result += chr((ord(char) - key - 65) % 26 + 65)
            else:
                result += chr((ord(char) - key - 97) % 26 + 97)
        return Text(result, key, "decrypted")
