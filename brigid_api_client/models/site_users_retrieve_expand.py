from enum import Enum


class SiteUsersRetrieveExpand(str, Enum):
    USERAWS_ACCOUNTS = "user.aws_accounts"
    USERAWS_VPCS = "user.aws_vpcs"
    USEROWNED_APPLICATIONS = "user.owned_applications"
    USERPERSON_TYPES = "user.person_types"
    USERTEAM = "user.team"

    def __str__(self) -> str:
        return str(self.value)
