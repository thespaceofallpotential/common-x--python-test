from core.range import Range

from core.source import Source
from data.example1Source import aWords
from data.example1Source import bWords

from gen_1.solvers.cultivatedSolver import CultivatedSolver

from gen_1.solvers.deductiveResolver import DeductiveResolver

source = Source(aWords, bWords) # words <-> tokens

a = source.aWordRange # or token ranges

b = source.bWordRange

# solvers

# cultivted solver: search-free "grown" solution; growth from curated parts/ cultivated environment

cultivated = CultivatedSolver(a, b)

cultivated.process()

for c in cultivated.commonRanges:
    print(str.join(" ", c.values)) # TODO: better reporting

# deductive resolver: knowledge-free "whittled" solution; iterative elimination of negative-space 

deductive = DeductiveResolver()

deductive.process(a, b)

for c in deductive.commonRanges:
    print(str.join(" ", c.values))
