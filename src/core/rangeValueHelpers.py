from core.range import Range
from core.rangeParseHelpers import parseCheckSequence, parseSplitCommon
from core.types import CommonRange, DivideDismissConquer


def isCandidate[T](a: Range[T], b: Range[T]) -> bool:
    isSameSize = a.length == b.length

    isCommon = len(a.valueSet.symmetric_difference(b.valueSet)) == 0

    return isSameSize & isCommon


def divideAndDismiss[T](a: Range[T], b: Range[T]) -> DivideDismissConquer[T]:
    if isCandidate(a, b):
        return parseCheckSequence(a, b)
    else:
        return parseSplitCommon(a, b)


def conquer[T](common: CommonRange[T], commonRanges: list[CommonRange[T]]):
    commonRanges.append(common)


def sufficientRemaining[T](aRanges: list[Range[T]], bRanges: list[Range[T]]):
    return len(aRanges) > 0 and len(bRanges) > 0
