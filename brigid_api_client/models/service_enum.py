from enum import Enum


class ServiceEnum(str, Enum):
    BITBUCKET = "bitbucket"
    GITHUB = "github"

    def __str__(self) -> str:
        return str(self.value)
