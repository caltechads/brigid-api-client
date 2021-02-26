from enum import Enum


class PipeinesRetrieveExpand(str, Enum):
    PIPELINEAPPLICATION = "pipeline.application"
    PIPELINEAWS_ACCOUNT = "pipeline.aws_account"
    PIPELINEPIPELINE_INVOCATIONS = "pipeline.pipeline_invocations"
    PIPELINESTEPS = "pipeline.steps"

    def __str__(self) -> str:
        return str(self.value)
