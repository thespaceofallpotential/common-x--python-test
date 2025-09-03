from core.range import Range

from gen_1.solvers.cultivatedSolver import CultivatedSolver

from data.a import A
from data.b import B

space = " "

a = Range(str(A).split(space))

b = Range(str(B).split(space))

cultivated = CultivatedSolver(a, b)

cultivated.process()

for c in cultivated.commonRanges:
    print(str.join(" ", c.valueArray))
