# https://www.hackerrank.com/challenges/np-zeros-and-ones/problem

import numpy

dimensions = tuple(map(int, input().split()))
print(numpy.zeros(dimensions, dtype=numpy.int))
print(numpy.ones(dimensions, dtype=numpy.int))
