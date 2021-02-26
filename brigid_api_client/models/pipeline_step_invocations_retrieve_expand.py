from enum import Enum


class PipelineStepInvocationsRetrieveExpand(str, Enum):
    STEPINVOCATIONINVOKER = "stepinvocation.invoker"
    STEPINVOCATIONRELEASE = "stepinvocation.release"

    def __str__(self) -> str:
        return str(self.value)
