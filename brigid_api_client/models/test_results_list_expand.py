from enum import Enum


class TestResultsListExpand(str, Enum):
    TESTRESULTRELEASE = "testresult.release"

    def __str__(self) -> str:
        return str(self.value)
