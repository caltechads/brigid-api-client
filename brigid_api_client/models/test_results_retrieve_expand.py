from enum import Enum


class TestResultsRetrieveExpand(str, Enum):
    TESTRESULTRELEASE = "testresult.release"

    def __str__(self) -> str:
        return str(self.value)
