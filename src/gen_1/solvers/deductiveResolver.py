from core import resolver
from core.debug import outputValues, outputVectors
from core.parsers import parseCheck, smartRepartition
from core.range import Range
from core.types import CommonRange, CommonalityResult


def isCandidate[T](a: Range[T], b: Range[T]) -> bool:
    # customisable: dependent upon kind of problem
    
    isSameSize = a.length == b.length

    isCommon = len(a.parts.symmetric_difference(b.parts)) == 0

    return isSameSize & isCommon


def areValid[T](aRanges: list[Range[T]], bRanges: list[Range[T]]):
    # customisable: dependent upon kind of problem
    
    return len(aRanges) > 0 and len(bRanges) > 0


class DeductiveResolver[T](resolver.AbstractResolver[T]):
    commonRanges: list[CommonRange[T]] = []

    def __init__(self) -> None:
        super().__init__()

    def process(self, a: Range[T], b: Range[T], depth: int = 1) -> resolver.AbstractResolver:

        outputVectors(a, b)

        result = parseCheck(a, b) if isCandidate(a, b) else smartRepartition(a, b)

        if result.common:
            outputValues(a, b)

            # either:
            #   candidate & result of parseCheck, or
            #   non-candidate, but smartRepartitioning led to one-to-one partitions (a == 1 and b == 1), then parsed
            self.commonRanges.append(result.common)

        aRanges = result.aRanges  # add filtering here: minimum length, etc
        bRanges = result.bRanges

        if areValid(aRanges, bRanges):  # non-zero
            # fractal recursion:
            #   this process function: 1) attempts parse; 2) repartitions ranges; 3) if partitions are valid, calls processRanges
            #   the processRanges function iteratively cross-checks partitions, by calling this function
            self.processRanges(aRanges, bRanges, depth + 1)

            # self.step(len(result.aRanges) + len(result.bRanges))
            # // TODO: need to update this value... ballpark for now; custom data-structures will significanly reduce & custom hardware will eliminate

        return self
