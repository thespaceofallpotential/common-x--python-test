from typing import TypeVar

T = TypeVar("T", None, int | str)


class PositionVector:
    position: int
    length: int

    def __init__(self, position: int, length: int):
        self.position = position
        self.length = length


type TPositionMap[T] = dict[T, int]


class CommonRange[T]:
    aPosition: int
    bPosition: int

    valueArray: list[T]

    def __init__(self, aPosition: int, bPosition: int, valueArray: list[T] = []):
        self.aPosition = aPosition
        self.bPosition = bPosition

        self.valueArray = valueArray


type CommonRanges = dict[int, CommonRange]
