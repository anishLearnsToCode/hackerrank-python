# https://www.hackerrank.com/challenges/np-polynomials/problem

import numpy
numpy.set_printoptions(legacy='1.13')

polynomial = list(map(float, input().split()))
x = float(input())
value = numpy.polyval(polynomial, x)
print(value)
