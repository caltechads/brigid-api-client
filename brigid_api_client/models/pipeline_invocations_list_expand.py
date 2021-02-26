from enum import Enum


class PipelineInvocationsListExpand(str, Enum):
    PIPELINEINVOCATIONPIPELINE = "pipelineinvocation.pipeline"

    def __str__(self) -> str:
        return str(self.value)
