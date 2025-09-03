from core.types import TPositionMap


class GlobalDomain[T]:
    globalValueSet: set[T]

    globalValues: list[T]

    valuePositionMap: TPositionMap[T]

    def __init__(self, gvs: set[T]) -> None:
        self.globalValueSet = gvs

        self.globalValues = list(gvs)

        self.valuePositionMap = dict()

        for i, value in enumerate(self.globalValues):
            self.valuePositionMap[value] = i

    def toValues(self, values: list[T]) -> list[int]:

        def valueToPosition(value: T) -> int:
            return self.valuePositionMap[value]

        return list(map(valueToPosition, values))

    def toPositions(self, positions: list[int]) -> list[T]:

        def positionToValue(position: int) -> T:
            return self.globalValues[position]

        return list(map(positionToValue, positions))
