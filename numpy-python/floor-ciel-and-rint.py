# https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem

import numpy

numpy.set_printoptions(sign=' ')

array = numpy.array(list(map(float, input().split())), dtype=float)
print(numpy.floor(array))
print(numpy.ceil(array))
print(numpy.rint(array))
