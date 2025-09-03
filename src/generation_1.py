from core.range import Range

from gen_1.solvers.cultivatedSolver import CultivatedSolver

from data.a import A
from data.b import B
from gen_1.solvers.deductiveResolver import DeductiveResolver

space = " "

a = Range(str(A).split(space))

b = Range(str(B).split(space))

cultivated = CultivatedSolver(a, b)

cultivated.process()

for c in cultivated.commonRanges:
    print(str.join(" ", c.values))


# deductive = DeductiveResolver()

# deductive.process(a, b)

# for c in deductive.commonRanges:
#     print(str.join(" ", c.values))
