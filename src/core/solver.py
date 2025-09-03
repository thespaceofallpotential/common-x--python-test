from core.range import Range
import abc


class AbstractSolver(metaclass=abc.ABCMeta):
    count: int = 0

    def __init__(self, a: Range, b: Range):
        self.a = a
        self.b = b

    def step(self, value: int = 1):
        self.count += value

        @abc.abstractmethod
        def process() -> AbstractSolver:
            return self
