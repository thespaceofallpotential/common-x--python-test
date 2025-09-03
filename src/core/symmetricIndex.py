type SymmetricIndex[T] = dict[T, list[int]]


def toSymmetricIndex[T](values: list[T], commonSet: set[T]) -> SymmetricIndex:
    symmetricIndex: SymmetricIndex = dict()

    for i, f in enumerate(values):
        if f not in commonSet:
            continue

        if f not in symmetricIndex:
            symmetricIndex[f] = [i] * 1
        else:
            symmetricIndex[f].append(i)

    return symmetricIndex
