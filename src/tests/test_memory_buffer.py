from datetime import datetime

from src.memory_buffer import Buffer, Text
from unittest.mock import patch, call
import pytest
from freezegun import freeze_time


class TestMemoryBuffer:
    def test_if_add_appends_correct_text_to_memory_buffer(self):
        buffer = Buffer()
        text_object = Text("test", 1, "encrypted")
        buffer.add(text_object)
        assert buffer.memory[0] == text_object

    @pytest.mark.parametrize(
        "test_list",
        [[Text("test", 1, "encrypted", datetime.now()), Text("cos", 2, "decrypted")]],
    )
    def test_if_memory_as_dict_converts_memory_elements(self, test_list):
        buffer = Buffer()
        buffer.memory = test_list

        memory_as_dict = buffer.memory_as_dict()

        for obj in memory_as_dict:
            assert isinstance(obj, dict)

    def test_if_display_prints_correct_msg_for_empty_buffer(self):
        with patch("builtins.print") as mock_print:
            buffer = Buffer()
            buffer.display()
            mock_print.assert_has_calls(
                [
                    call("Buffer empty"),
                ]
            )

    @freeze_time("2013-6-5 12:0:0")
    def test_if_display_prints_correct_msg(self):
        with patch("builtins.print") as mock_print:
            text_object_1 = Text("test", 1, "encrypted", datetime.now())
            text_object_2 = Text("cos", 2, "decrypted", datetime.now())
            buffer = Buffer()
            buffer.add(text_object_1)
            buffer.add(text_object_2)
            buffer.display()
            mock_print.assert_has_calls(
                [
                    call(
                        "1. Text(text='test', rot_type=1, status='encrypted', created_at=FakeDatetime(2013, 6, 5, "
                        "12, 0))"
                    ),
                    call(
                        "2. Text(text='cos', rot_type=2, status='decrypted', created_at=FakeDatetime(2013, 6, 5, 12, "
                        "0))"
                    ),
                ]
            )
