from dataclasses import dataclass
from datetime import datetime
from typing import List, Dict


@dataclass
class Text:
    text: str
    rot_type: int
    status: str
    created_at: datetime = datetime.now()

    def to_dict(self) -> Dict[str, str | int]:
        formatted_date = self.created_at.strftime("%Y-%m-%d %H:%M:%S")
        return {
            "text": self.text,
            "rot_type": self.rot_type,
            "status": self.status,
            "created_at": formatted_date,
        }


class Buffer:
    def __init__(self) -> None:
        self.memory: List[Text] = []

    def __len__(self) -> int:
        return len(self.memory)

    def add(self, text: Text) -> None:
        self.memory.append(text)

    def memory_as_dict(self) -> List[Dict[str, str | int]]:
        return [text.to_dict() for text in self.memory]

    def display(self) -> None:
        if len(self) == 0:
            print("Buffer empty")
        else:
            for idx, text in enumerate(self.memory, start=1):
                print(f"{idx}. {text}")
