from core.types import T, TPositionMap


class GlobalDomain[T]:
    globalValueSet: set[T]

    globalValueArray: list[T]

    valuePositionMap: TPositionMap[T]

    def __init__(self, gvs: set[T]) -> None:
        self.globalValueSet = gvs

        self.globalValueArray = list(gvs)

        self.valuePositionMap = dict()

        for i, value in enumerate(self.globalValueArray):
            self.valuePositionMap[value] = i

    def toValues(self, valueArray: list[T]) -> list[int]:

        def valueToPosition(value: T) -> int:
            return self.valuePositionMap[value]

        return list(map(valueToPosition, valueArray))

    def toPositions(self, positionArray: list[int]) -> list[T]:

        def positionToValue(position: int) -> T:
            return self.globalValueArray[position]

        return list(map(positionToValue, positionArray))
