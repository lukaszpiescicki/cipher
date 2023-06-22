class Cipher:
    def __init__(self) -> None:
        pass

    def encrypt(self, text: str, key: int) -> str:
        result: str = ""
        for i in range(len(text)):
            char: str = text[i]

            if char == " ":
                result += " "
            elif char.isupper():
                result += chr((ord(char) + key - 65) % 26 + 65)
            else:
                result += chr((ord(char) + key - 97) % 26 + 97)
        return result

    def decrypt(self, text: str, key: int):
        result = ""

        for i in range(len(text)):
            char: str = text[i]

            if char == " ":
                result += " "
            elif char.isupper():
                result += chr((ord(char) - key - 65) % 26 + 65)
            else:
                result += chr((ord(char) - key - 97) % 26 + 97)
        return result


def main():
    cp = Cipher()


if __name__ == "__main__":
    main()


