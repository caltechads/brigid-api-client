from enum import Enum


class StatusEnum(str, Enum):
    SUCCESS = "success"
    FAILED = "failed"

    def __str__(self) -> str:
        return str(self.value)
