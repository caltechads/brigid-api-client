from enum import Enum


class AwsTasksListExpand(str, Enum):
    AWSECSTASKECS_CLUSTER = "awsecstask.ecs_cluster"
    AWSECSTASKENVIRONMENT = "awsecstask.environment"

    def __str__(self) -> str:
        return str(self.value)
