import json
import os

from memory_buffer import Text


class File:
    def __init__(self, path):
        self.path = path

    def exist(self) -> bool:
        return os.path.isfile(self.path)

    def readable(self) -> bool:
        return os.access(self.path, os.R_OK)

    def is_empty(self) -> bool:
        return os.stat(self.path).st_size == 0


def is_valid_file(file: File) -> bool:
    return file.exist() and file.readable() and not file.is_empty()


def save_to_file(file_name: str, data: list[Text]):
    path = f"./files/{file_name}.json"
    file_obj = File(path)

    if is_valid_file(file_obj):
        with open(f"{file_name}.json", "r+") as file:
            file_data = json.load(file)
            file_data["items"] += data
            file.seek(0)
            json.dump(file_data, file, indent=4)
    else:
        dct = {"items": data}
        with open(f"{file_name}.json", "w") as f:
            json.dump(dct, f)


def read_file(file_name: str):
    try:
        with open(file_name, "r") as file:
            data = json.load(file)
            print(data)
    except FileNotFoundError:
        print("File not found")
