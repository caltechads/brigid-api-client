from enum import Enum


class EcsServiceDeploysRetrieveExpand(str, Enum):
    ECSSERVICEDEPLOYDEPLOYMENT = "ecsservicedeploy.deployment"
    ECSSERVICEDEPLOYDOCKER_IMAGE_BUILD = "ecsservicedeploy.docker_image_build"
    ECSSERVICEDEPLOYECS_SERVICE = "ecsservicedeploy.ecs_service"

    def __str__(self) -> str:
        return str(self.value)
