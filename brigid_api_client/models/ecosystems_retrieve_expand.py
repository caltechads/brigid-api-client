from enum import Enum


class EcosystemsRetrieveExpand(str, Enum):
    ECOSYSTEMAPPLICATIONS = "ecosystem.applications"

    def __str__(self) -> str:
        return str(self.value)
