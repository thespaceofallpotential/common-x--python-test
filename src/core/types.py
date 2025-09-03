from core.range import Range


type TPositionMap[T] = dict[T, int]


class CommonRange[T]:
    aPosition: int
    bPosition: int

    values: list[T]

    def __init__(self, aPosition: int, bPosition: int, values: list[T] = []):
        self.aPosition = aPosition
        self.bPosition = bPosition

        self.values = values

    def __repr__(self) -> str:
        return f"CommonRange({self.aPosition=}, {self.bPosition=}, {self.values=})"

type CommonRanges = dict[int, CommonRange]


class DivideDismissConquer[T]:
    aRanges: list[Range[T]]
    bRanges: list[Range[T]]

    commonRanges: CommonRange[T] | None

    def __init__(
        self,
        aRanges: list[Range[T]],
        bRanges: list[Range[T]],
        commonRanges: CommonRange[T] | None,
    ) -> None:
        self.aRanges = aRanges
        self.bRanges = bRanges
        self.commonRanges = commonRanges


type DivideDismissConquer2[T] = tuple[Range[T], Range[T], CommonRange[T] | None]


# export type CommonPoint<T extends Token | Word> = [ap: Position, bp: Position, v: T];
# export type CommonPoints<T extends Token | Word> = CommonPoint<T>[];

# export type DivideDismissConquer<T extends Token | Word> = [a: IRange<T>[], b: IRange<T>[], CommonRange<T> | undefined];
