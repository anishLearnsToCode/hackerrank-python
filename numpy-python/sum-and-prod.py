# https://www.hackerrank.com/challenges/np-sum-and-prod/problem

import numpy

N, M = map(int, input().split())
data = []
for _ in range(N):
    data.append(list(map(int, input().split())))

data = numpy.array(data)
data = data.sum(axis=0)
product = data.prod()
print(product)
