from unittest.mock import patch, call
from unittest import TestCase
from src.manager import Manager


class Test(TestCase):
    @patch("builtins.input", return_value="value")
    def test_if_get_user_input_returns_correct_string(self, mock):
        manager = Manager()
        self.assertEqual(manager.get_user_input("hello"), "value")


def test_if_process_text_encrypt_adds_records_to_buffer():
    manager = Manager()
    with patch.object(Manager, "get_user_input") as get_user_input:
        get_user_input.side_effect = ["Hello", 3]
        manager.process_text("encrypt")
        actual_text = manager.buffer.memory[0]
        expected = "Khoor"
        assert actual_text.text == expected
        assert actual_text.rot_type == 3
        assert actual_text.status == "encrypted"


def test_if_process_text_decrypt_adds_records_to_buffer():
    manager = Manager()
    with patch.object(Manager, "get_user_input") as get_user_input:
        get_user_input.side_effect = ["Test", 1]
        manager.process_text("decrypt")
        actual_text = manager.buffer.memory[0]
        expected = "Sdrs"
        assert actual_text.text == expected
        assert actual_text.rot_type == 1
        assert actual_text.status == "decrypted"
