from core.types import T

type SymmetricIndex[T] = dict[T, list[int]]


def toSymmetricIndex(rangeArray: list[T], commonSet: set[T]) -> SymmetricIndex:
    symmetricIndex: SymmetricIndex = dict()

    for i, f in enumerate(rangeArray):
        if f not in commonSet:
            continue

        if f not in symmetricIndex:
            symmetricIndex[f] = [i] * 1
        else:
            symmetricIndex[f].append(i)

    return symmetricIndex
