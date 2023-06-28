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
        print("istnieje")
        with open(f"{file_name}.json", "r+") as file:
            file_data = json.load(file)
            for k, v in data.items():
                file_data[k] = v
            file.seek(0)
            json.dump(file_data, file, indent=4)
            file.truncate()
    else:
        print("nie istnieje")
        with open(f"{file_name}.json", "w") as file:
            json.dump(data, file)


x = {"organization": "GeeksForGeeks", "city": "Noida", "country": "India"}
y = {"pin": 110096}

save_to_file("test", x)
save_to_file("test", y)
