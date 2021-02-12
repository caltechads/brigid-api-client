from enum import Enum


class SiteUsersListExpand(str, Enum):
    SITEUSERORGANIZATION = "siteuser.organization"
    SITEUSERPEOPLE_TYPES = "siteuser.people_types"
    SITEUSERTEAM = "siteuser.team"

    def __str__(self) -> str:
        return str(self.value)
