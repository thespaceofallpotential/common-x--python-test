from core.range import Range

isActive = False


def outputVectors[T](a: Range[T], b: Range[T]):
    if isActive:
        print(f"a:[{a.position},{a.length}] | b:[{b.position},{b.length}]")


def output[T](a: Range[T], b: Range[T]):
    if isActive:
        print(f"{a.values} | {b.values}")
