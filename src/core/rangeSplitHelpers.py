from core.range import Range
from core.commonRangeHelpers import toCommonRange
from core.rangeHelpers import toRanges


def splitCommon[T](a: Range[T], b: Range[T]) -> tuple[list[Range[T]], list[Range[T]]]:
    commonSet = a.valueSet.intersection(b.valueSet)

    aRanges = toRanges(a, commonSet)
    bRanges = toRanges(b, commonSet)

    return (aRanges, bRanges)


def splitFrom[T](range: Range[T], i: int) -> Range[T]:
    return Range[T](range.values[i:], range.position + i)


def splitOnNewLine[T](range: Range[T], newLine: T) -> list[Range[T]]:
    items: list[Range[T]] = []

    position: int = 0

    i: int = range.getIndex(newLine)

    while i > -1:
        items.append(Range[T](range.values[position:i], position))

        position = i

        i = range.getIndex(newLine, i + 1)

        if position < range.length:
            items.append(Range[T](range.values[position:], position))

    return items


