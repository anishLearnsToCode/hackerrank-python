# https://www.hackerrank.com/challenges/np-min-and-max/problem

import numpy

N, M = map(int, input().split())
data = []
for _ in range(N):
    data.append(list(map(int, input().split())))

data = numpy.array(data)
data = data.min(axis=1)
result = data.max()
print(result)
