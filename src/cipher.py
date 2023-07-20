from .memory_buffer import Text


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
