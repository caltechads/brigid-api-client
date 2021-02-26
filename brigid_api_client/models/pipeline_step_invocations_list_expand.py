from enum import Enum


class PipelineStepInvocationsListExpand(str, Enum):
    STEPINVOCATIONINVOKER = "stepinvocation.invoker"
    STEPINVOCATIONRELEASE = "stepinvocation.release"

    def __str__(self) -> str:
        return str(self.value)
