from enum import Enum


class DeploymentsRetrieveExpand(str, Enum):
    DEPLOYMENTECS_SERVICE_DEPLOYS = "deployment.ecs_service_deploys"
    DEPLOYMENTECS_TASK_DEPLOYS = "deployment.ecs_task_deploys"
    DEPLOYMENTENVIRONMENT = "deployment.environment"
    DEPLOYMENTRELEASE = "deployment.release"

    def __str__(self) -> str:
        return str(self.value)
