from enum import Enum


class AwsVpcsRetrieveExpand(str, Enum):
    AWSVPCAWS_ACCOUNT = "awsvpc.aws_account"
    AWSVPCAWS_ECS_CLUSTERS = "awsvpc.aws_ecs_clusters"
    AWSVPCCONTACTS = "awsvpc.contacts"

    def __str__(self) -> str:
        return str(self.value)
