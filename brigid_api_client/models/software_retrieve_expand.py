from enum import Enum


class SoftwareRetrieveExpand(str, Enum):
    SOFTWAREAPPLICATIONS = "software.applications"
    SOFTWAREAUTHORS = "software.authors"

    def __str__(self) -> str:
        return str(self.value)
