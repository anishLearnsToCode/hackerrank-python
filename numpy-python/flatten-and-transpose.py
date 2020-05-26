# https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem

import numpy

N, M = map(int, input().split())
data = []
for _ in range(N):
    data.append(list(map(int, input().split())))

data = numpy.array(data)
print(data.transpose())
print(data.flatten())
