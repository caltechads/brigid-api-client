from enum import Enum


class DockerImageBuildsListExpand(str, Enum):
    DOCKERIMAGEBUILDRELEASE = "dockerimagebuild.release"

    def __str__(self) -> str:
        return str(self.value)
