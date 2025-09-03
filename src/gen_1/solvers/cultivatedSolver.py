from typing import List
from core import solver
from core.helpers import getPositiveVectors
from core.symmetricIndex import toSymmetricIndex
from core.types import CommonRange, CommonRanges


class CultivatedSolver(solver.AbstractSolver):
    commonRanges: List[CommonRange] = []

    def __init__(self, a, b):
        super().__init__(a, b)

    def process(self) -> solver.AbstractSolver:
        a = self.a
        b = self.b
        cra = self.commonRanges

        commonSet = a.rangeSet.intersection(b.rangeSet)

        positiveRanges = getPositiveVectors(a.rangeArray, commonSet)

        xValuePositionArrayMap = toSymmetricIndex(b.rangeArray, commonSet)

        progress: CommonRanges = dict()

        for vectors in positiveRanges:
            origin = vectors.position

            for iR in range(vectors.length):
                position = origin + iR

                value = a.rangeArray[position]

                xPositionArray = xValuePositionArrayMap.get(value) or []

                for xPosition in xPositionArray:
                    prior = progress.get(xPosition - 1)

                    if prior:
                        prior.valueArray.append(value)

                        progress[xPosition] = prior

                    else:
                        common = CommonRange(origin, xPosition, [value])

                        cra.append(common)

                        progress[xPosition] = common

                    self.step()

            progress.clear()

        return self
