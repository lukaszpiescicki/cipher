import pytest
from src.file_handler import save_to_file, read_file
from datetime import datetime
import json


@pytest.fixture
def tmp_path(tmp_path):
    return tmp_path


class TestFileHandler:
    def test_save_to_file_existing(self, tmp_path):
        data_1 = [{"text": "xyz"}]
        data_2 = [{"text": "test"}]
        result = [{"text": "xyz"}, {"text": "test"}]
        save_to_file("test_file_1", data_1, tmp_path)
        save_to_file("test_file_1", data_2, tmp_path)

        with open(tmp_path / "test_file_1.json", "r") as file:
            file_data = json.load(file)
            assert file_data["items"] == result

    def test_save_to_file_new(self, tmp_path):
        data = [
            {
                "text": "xyz",
                "rot_type": "rot13",
                "status": "encrypted",
                "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            }
        ]
        save_to_file("test_file_2", data, tmp_path)

        with open(tmp_path / "test_file_2.json", "r") as file:
            file_data = json.load(file)
            assert file_data["items"] == data

    def test_read_file_existing(self, tmp_path):
        data = {
            "items": [
                {
                    "text": "xyz",
                    "rot_type": "rot13",
                    "status": "encrypted",
                    "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                }
            ]
        }
        with open(tmp_path / "test_file_3.json", "w") as file:
            json.dump(data, file)

        assert read_file(tmp_path / "test_file_3.json") == data

    def test_read_file_nonexistent(self, capsys):
        read_file("fail")
        captured = capsys.readouterr()
        assert captured.out == "File not found\n"

    def test_read_file_empty(self, tmp_path):
        assert read_file(tmp_path / "test_file_4.json") is None
