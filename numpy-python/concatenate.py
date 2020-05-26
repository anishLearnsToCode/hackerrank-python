# https://www.hackerrank.com/challenges/np-concatenate/problem

import numpy

N, M, P = map(int, input().split())

data1 = []
for _ in range(N):
    data1.append(list(map(int, input().split())))

data2 = []
for _ in range(M):
    data2.append(list(map(int, input().split())))

result = numpy.concatenate((data1, data2), axis=0)
print(result)
