from enum import Enum


class ReleasesListExpand(str, Enum):
    RELEASEDEPLOYMENTS = "release.deployments"
    RELEASEDOCKER_IMAGE_BUILDS = "release.docker_image_builds"
    RELEASEPIPELINE_INVOCATIONS = "release.pipeline_invocations"
    RELEASESOFTWARE = "release.software"
    RELEASESTEP_INVOCATIONS = "release.step_invocations"

    def __str__(self) -> str:
        return str(self.value)
