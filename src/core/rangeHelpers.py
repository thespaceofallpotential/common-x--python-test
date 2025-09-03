from core.range import PositionVector, Range
from core.vectors import getPositiveVectors


def toRange[T](range: Range[T], positionVector: PositionVector) -> Range[T]:
    return Range(
        range.values[positionVector.position : positionVector.length],
        positionVector.position,
    )


def toRanges[T](range: Range[T], commonSet: set[T]) -> list[Range[T]]:
    positionVectors = getPositiveVectors(range.values, commonSet)

    def positionToValue(positionVector: PositionVector) -> Range[T]:
        return toRange(range, positionVector)

    return list(map(positionToValue, positionVectors))
