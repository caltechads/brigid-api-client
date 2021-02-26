from enum import Enum


class EnvironmentsListExpand(str, Enum):
    ENVIRONMENTAPPLICATION = "environment.application"
    ENVIRONMENTAWS_ECS_SERVICES = "environment.aws_ecs_services"
    ENVIRONMENTDEPLOYMENTS = "environment.deployments"

    def __str__(self) -> str:
        return str(self.value)
