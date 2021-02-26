from enum import Enum


class PipelineStepsListExpand(str, Enum):
    STEPDEECENDENTS = "step.deecendents"
    STEPPIPELINE = "step.pipeline"
    STEPPREDECESSOR = "step.predecessor"
    STEPSTEP_INVOCATIONS = "step.step_invocations"
    STEPSTEP_TYPE = "step.step_type"

    def __str__(self) -> str:
        return str(self.value)
