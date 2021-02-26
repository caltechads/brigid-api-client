from enum import Enum


class AwsServicesRetrieveExpand(str, Enum):
    AWSECSSERVICEECS_CLUSTER = "awsecsservice.ecs_cluster"
    AWSECSSERVICEENVIRONMENT = "awsecsservice.environment"

    def __str__(self) -> str:
        return str(self.value)
