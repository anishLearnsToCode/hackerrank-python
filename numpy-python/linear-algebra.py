# https://www.hackerrank.com/challenges/np-linear-algebra/problem

import numpy

N = int(input())
matrix = []
for _ in range(N):
    matrix.append(list(map(float, input().split())))

result = round(numpy.linalg.det(matrix), 2)
print(result)
