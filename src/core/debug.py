from core.range import Range
from core.reporting import rangeValueString, vectorString, vectorsString

isActive = False


def outputVectors[T](a: Range[T], b: Range[T]):
    if isActive:
        print(vectorsString(a, b))


def outputValues[T](a: Range[T], b: Range[T]):
    if isActive:
        print(f"{rangeValueString(a)} | {rangeValueString(b)}")
