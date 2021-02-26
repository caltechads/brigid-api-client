from enum import Enum


class TeamsListExpand(str, Enum):
    TEAMAWS_ACCOUNTS = "team.aws_accounts"
    TEAMAWS_VPCS = "team.aws_vpcs"
    TEAMORGANIZATION = "team.organization"
    TEAMOWNED_APPLICATIONS = "team.owned_applications"
    TEAMUSERS = "team.users"

    def __str__(self) -> str:
        return str(self.value)
