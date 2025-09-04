from core import solver
from core.range import Range
from core.symmetricIndex import toSymmetricIndex
from core.types import CommonRange, CommonRanges
from core.vectors import getPartitionVectors


class CultivatedSolver[T](solver.AbstractSolver[T]):
    commonRanges: list[CommonRange] = []

    def __init__(self, a: Range, b: Range):
        super().__init__(a, b)

    def process(self):
        a = self.a
        b = self.b

        cra = self.commonRanges

        commonSet = a.parts.intersection(b.parts)

        positiveVectors = getPartitionVectors(a.values, commonSet)

        xValuePositionsMap = toSymmetricIndex(b.values, commonSet)

        progress: CommonRanges = dict()

        for vector in positiveVectors:
            origin = vector.position

            for i_v in range(vector.length):
                position = origin + i_v

                value = a.values[position]

                xPositions = xValuePositionsMap.get(value) or [] # never None - check  python equivalent for TS '!' 

                for xp in xPositions:
                    prior = progress.get(xp - 1)

                    if prior:
                        prior.values.append(value)

                        progress[xp] = prior

                    else:
                        common = CommonRange(origin, xp, [value])

                        cra.append(common)

                        progress[xp] = common

                    self.step()

            progress.clear()

        return self
