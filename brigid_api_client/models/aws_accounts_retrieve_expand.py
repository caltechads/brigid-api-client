from enum import Enum


class AwsAccountsRetrieveExpand(str, Enum):
    AWSACCOUNTAWS_VPCS = "awsaccount.aws_vpcs"
    AWSACCOUNTCONTACTS = "awsaccount.contacts"
    AWSACCOUNTTEAM = "awsaccount.team"

    def __str__(self) -> str:
        return str(self.value)
