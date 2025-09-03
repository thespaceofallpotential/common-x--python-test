from core import solver
from core.range import Range
from core.symmetricIndex import toSymmetricIndex
from core.types import CommonRange, CommonRanges
from core.vectors import getPositiveVectors


class CultivatedSolver[T](solver.AbstractSolver[T]):
    commonRanges: list[CommonRange] = []

    def __init__(self, a: Range, b: Range):
        super().__init__(a, b)

    def process(self):
        a = self.a
        b = self.b

        cra = self.commonRanges

        commonSet = a.valueSet.intersection(b.valueSet)

        positiveRanges = getPositiveVectors(a.values, commonSet)

        xValuePositionsMap = toSymmetricIndex(b.values, commonSet)

        progress: CommonRanges = dict()

        for rangeVectors in positiveRanges:
            origin = rangeVectors.position

            for i_rangeVectors in range(rangeVectors.length):
                position = origin + i_rangeVectors

                value = a.values[position]

                xPositions = xValuePositionsMap.get(value) or []

                for xPosition in xPositions:
                    prior = progress.get(xPosition - 1)

                    if prior:
                        prior.values.append(value)

                        progress[xPosition] = prior

                    else:
                        common = CommonRange(origin, xPosition, [value])

                        cra.append(common)

                        progress[xPosition] = common

                    self.step()

            progress.clear()

        return self
