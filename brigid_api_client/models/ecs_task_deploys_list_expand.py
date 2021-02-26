from enum import Enum


class EcsTaskDeploysListExpand(str, Enum):
    ECSTASKDEPLOYDEPLOYMENT = "ecstaskdeploy.deployment"
    ECSTASKDEPLOYDOCKER_IMAGE_BUILD = "ecstaskdeploy.docker_image_build"
    ECSTASKDEPLOYECS_TASK = "ecstaskdeploy.ecs_task"

    def __str__(self) -> str:
        return str(self.value)
