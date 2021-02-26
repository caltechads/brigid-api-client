from enum import Enum


class DockerImageBuildsRetrieveExpand(str, Enum):
    DOCKERIMAGEBUILDRELEASE = "dockerimagebuild.release"

    def __str__(self) -> str:
        return str(self.value)
