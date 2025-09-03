from core.types import T, PositionVector


def getPositiveVectors(rangeArray: list[T], commonSet: set) -> list[PositionVector]:
    positionVectorArray: list[PositionVector] = []

    current: PositionVector | None = None

    for i, f in enumerate(rangeArray):
        if f in commonSet:
            if current == None:
                current = PositionVector(i, 0)

                positionVectorArray.append(current)

            current.length += 1

            continue

        current = None

    return positionVectorArray
