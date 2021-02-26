from enum import Enum


class ApplicationsListExpand(str, Enum):
    APPLICATIONDEPENDENT_SOFTWARE = "application.dependent_software"
    APPLICATIONECOSYSTEM = "application.ecosystem"
    APPLICATIONOWNING_TEAM = "application.owning_team"
    APPLICATIONPIPELINES = "application.pipelines"
    APPLICATIONPRIMARY_SOFTWARE = "application.primary_software"

    def __str__(self) -> str:
        return str(self.value)
