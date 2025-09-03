from typing import TypeVar

from core.rangeVector import RangeVector

T = TypeVar("T")

class Range(RangeVector):
    def __init__(
        self,
        rangeArray: list[T],
        position: int = 0,
        rangeSet: set[T] | None = None,
    ):
        super().__init__(position, len(rangeArray))

        self.rangeArray = rangeArray

        self.rangeSet = rangeSet if rangeSet else set(rangeArray)
