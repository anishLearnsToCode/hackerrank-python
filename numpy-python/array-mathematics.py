# https://www.hackerrank.com/challenges/np-array-mathematics/problem

import numpy

N, M = map(int, input().split())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))
A = numpy.array(A)

B = []
for _ in range(N):
    B.append(list(map(int, input().split())))
B = numpy.array(B)

print(A + B)
print(A - B)
print(A * B)
print(A // B)
print(A % B)
print(A ** B)
