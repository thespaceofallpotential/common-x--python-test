from typing import Dict, TypeVar

T = TypeVar("T")


class PositionVector:
    position: int
    length: int

    def __init__(self, position: int, length: int):
        self.position = position
        self.length = length


class CommonRange[T]:
    aPosition: int
    bPosition: int

    valueArray: list[T]

    def __init__(self, aPosition: int, bPosition: int, valueArray: list[T] = []):
        self.aPosition = aPosition
        self.bPosition = bPosition

        self.valueArray = valueArray


type CommonRanges = Dict[int, CommonRange]
