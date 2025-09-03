from core.range import Range
from core.types import CommonRange


def toCommonRange[T](
    a: Range[T], b: Range[T]
) -> tuple[CommonRange | None, int | None, int | None]:
    common = CommonRange(a.position, b.position)

    for i, aValue in enumerate(a.values):
        bValue = b.values[i]

        if i >= len(b.values):
            return (common, i, None)

        if aValue != bValue:
            return (None, i, i)

        common.values.append(aValue)

    i_error = 0

    if len(a.values) < len(b.values):
        i_error = len(a.values)
    else:
        i_error = None

    return (common, None, i_error)
