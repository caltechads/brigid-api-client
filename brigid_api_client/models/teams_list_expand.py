from enum import Enum


class TeamsListExpand(str, Enum):
    TEAMORGANIZATION = "team.organization"

    def __str__(self) -> str:
        return str(self.value)
