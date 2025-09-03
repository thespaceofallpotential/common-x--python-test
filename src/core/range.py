class PositionVector:
    position: int
    length: int

    def __init__(self, position: int, length: int):
        self.position = position
        self.length = length
        
    def __repr__(self) -> str:
        return f"PositionVector({self.position=}, {self.length=})"


class Range[T](PositionVector):
    def __init__(
        self,
        values: list[T],
        position: int = 0,
        valueSet: set[T] | None = None,
    ):
        super().__init__(position, len(values))

        self.values = values

        self.valueSet = valueSet if valueSet else set(values)

    def getIndex(self, value: T, start: int = 0) -> int:
        return self.values.index(value, start)

    def __repr__(self) -> str:
        return f"Range({self.values=}, {self.valueSet=})"

