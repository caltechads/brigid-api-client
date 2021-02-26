from enum import Enum


class EnvironmentsRetrieveExpand(str, Enum):
    ENVIRONMENTAPPLICATION = "environment.application"
    ENVIRONMENTAWS_ECS_SERVICES = "environment.aws_ecs_services"
    ENVIRONMENTDEPLOYMENTS = "environment.deployments"

    def __str__(self) -> str:
        return str(self.value)
