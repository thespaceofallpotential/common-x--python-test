from core.types import T, PositionVector


class Range(PositionVector):
    def __init__(
        self,
        rangeArray: list[T],
        position: int = 0,
        rangeSet: set[T] | None = None,
    ):
        super().__init__(position, len(rangeArray))

        self.rangeArray = rangeArray

        self.rangeSet = rangeSet if rangeSet else set(rangeArray)
