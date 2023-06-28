import json
import os
import io


def startup_check(path: str):
    if os.path.isfile(path) and os.access(path, os.R_OK):
        return True
    else:
        return False


def save_to_file(file_name: str, data: dict):
    path = f"./{file_name}.json"
    file_status = startup_check(path)

    if file_status:
        with open(f"{file_name}.json", "r+") as file:
            file_data = json.load(file)
            for k, v in data.items():
                file_data[k] = v
            file.seek(0)
            json.dump(file_data, file, indent=4)
            file.truncate()
    else:
        with open(f"{file_name}.json", "w") as file:
            json.dump(data, file)


def read_file(file_name: str):
    try:
        with open(file_name, "r") as file:
            data = json.load(file)
            print(data)
    except FileNotFoundError:
        print("File not found")
