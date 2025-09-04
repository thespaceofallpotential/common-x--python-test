from core.range import Range

from core.source import Source
from data.example1Source import aWords
from data.example1Source import bWords

from gen_1.solvers.cultivatedSolver import CultivatedSolver

from gen_1.solvers.deductiveResolver import DeductiveResolver

source = Source(aWords, bWords)

a = source.aWordRange

b = source.bWordRange

cultivated = CultivatedSolver(a, b)

cultivated.process()

for c in cultivated.commonRanges:
    print(str.join(" ", c.values))

deductive = DeductiveResolver()

deductive.process(a, b)

for c in deductive.commonRanges:
    print(str.join(" ", c.values))
