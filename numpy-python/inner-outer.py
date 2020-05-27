# https://www.hackerrank.com/challenges/np-inner-and-outer/problem

import numpy
numpy.set_printoptions(legacy='1.13')

A = numpy.array(list(map(int, input().split())))
B = numpy.array(list(map(int, input().split())))

print(numpy.inner(A, B))
print(numpy.outer(A, B))
