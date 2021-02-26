from enum import Enum


class AwsClustersRetrieveExpand(str, Enum):
    AWSECSCLUSTERAWS_ECS_SERVICES = "awsecscluster.aws_ecs_services"
    AWSECSCLUSTERAWS_ECS_TASKS = "awsecscluster.aws_ecs_tasks"
    AWSECSCLUSTERAWS_VPC = "awsecscluster.aws_vpc"

    def __str__(self) -> str:
        return str(self.value)
