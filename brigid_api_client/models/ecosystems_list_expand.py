from enum import Enum


class EcosystemsListExpand(str, Enum):
    ECOSYSTEMAPPLICATIONS = "ecosystem.applications"

    def __str__(self) -> str:
        return str(self.value)
