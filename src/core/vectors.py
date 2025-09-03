from core.range import PositionVector


def getPositiveVectors[T](
    values: list[T], commonSet: set[T]
) -> list[PositionVector]:
    positionVectors: list[PositionVector] = []

    current: PositionVector | None = None

    for i, f in enumerate(values):
        if f in commonSet:
            if current == None:
                current = PositionVector(i, 0)

                positionVectors.append(current)

            current.length += 1

            continue

        current = None

    return positionVectors
