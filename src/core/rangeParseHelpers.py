from core.commonRangeHelpers import toCommonRange
from core.range import Range
from core.rangeSplitHelpers import splitCommon, splitFrom
from core.types import DivideDismissConquer


def parseCheckSequence[T](a: Range[T], b: Range[T]) -> DivideDismissConquer[T]:
    [common, i_a, i_b] = toCommonRange(a, b)

    if common:
        if i_a != None and i_a > 0:
            return DivideDismissConquer([a], [b], None)

        if i_b != None and i_b > 0:
            return DivideDismissConquer([a], [b], None)

        return DivideDismissConquer([], [], common)

    return DivideDismissConquer([a], [b], None)


def parseSplitSequence[T](
    a: Range[T], b: Range[T], haltOnUnhandled: bool = False
) -> DivideDismissConquer[T]:

    [common, i_a, i_b] = toCommonRange(a, b)

    if common:
        if i_a != None and i_a > 0:
            a2 = splitFrom(a, i_a)

            return DivideDismissConquer([a2], [b], common)

        if i_b != None and i_b > 0:
            b2 = splitFrom(b, i_b)

            return DivideDismissConquer([], [b2], common)

        return DivideDismissConquer([], [], common)

    # if haltOnUnhandled:
    # TODO

    return DivideDismissConquer([], [], None)


def parseSplitCommon[T](a: Range[T], b: Range[T]) -> DivideDismissConquer[T]:
    if len(a.valueSet.intersection(b.valueSet)) == 0:
        return DivideDismissConquer([], [], None)

    [aRanges, bRanges] = splitCommon(a, b)

    if len(aRanges) > 1 or len(bRanges) > 1:
        return DivideDismissConquer(aRanges, bRanges, None)

    if len(aRanges) == 0 or len(bRanges) == 0:
        return DivideDismissConquer([], [], None)

    return parseSplitSequence(aRanges[0], bRanges[0])
