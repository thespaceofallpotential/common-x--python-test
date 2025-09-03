from core import resolver
from core.range import Range
from core.rangeParseHelpers import parseCheckSequence, parseSplitCommon
from core.rangeValueHelpers import conquer, divideAndDismiss, sufficientRemaining
from core.types import CommonRange, DivideDismissConquer

print("DeductiveResolver: NOT COMPLETED")

class DeductiveResolver[T](resolver.AbstractResolver[T]):
    commonRanges: list[CommonRange[T]] = []

    def __init__(self) -> None:
        super().__init__()

    def process(
        self, a: Range[T], b: Range[T], depth: int = 1
    ) -> resolver.AbstractResolver:

        result = divideAndDismiss(a, b)

        if result.commonRanges:
            conquer(result.commonRanges, self.commonRanges)

        if sufficientRemaining(result.aRanges, result.bRanges):
            # fractal recursion:
            #   process (ranges) -> split to sub-ranges -> processRanges ->
            #   iteratively cross-check sub-ranges -> process (sub-ranges -> ranges) |->
            self.processRanges(result.aRanges, result.bRanges, depth + 1)

        self.step(len(result.aRanges) + len(result.bRanges))
        # // TODO: need to update this value... ballpark for now; custom data-structures will significanly reduce & custom hardware will eliminate

        return self
