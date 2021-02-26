from enum import Enum


class AwsServicesListExpand(str, Enum):
    AWSECSSERVICEECS_CLUSTER = "awsecsservice.ecs_cluster"
    AWSECSSERVICEENVIRONMENT = "awsecsservice.environment"

    def __str__(self) -> str:
        return str(self.value)
