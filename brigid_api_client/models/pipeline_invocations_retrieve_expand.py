from enum import Enum


class PipelineInvocationsRetrieveExpand(str, Enum):
    PIPELINEINVOCATIONPIPELINE = "pipelineinvocation.pipeline"

    def __str__(self) -> str:
        return str(self.value)
