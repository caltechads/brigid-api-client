from enum import Enum


class OrganizationsListExpand(str, Enum):
    ORGANIZATIONTEAMS = "organization.teams"

    def __str__(self) -> str:
        return str(self.value)
