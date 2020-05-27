# https://www.hackerrank.com/challenges/np-mean-var-and-std/problem

import numpy

# added for proper formatting in the output - complete stupidity by the problem setter
numpy.set_printoptions(legacy='1.13')

N, M = map(int, input().split())
data = []
for _ in range(N):
    data.append(list(map(int, input().split())))

data = numpy.array(data)
print(data.mean(axis=1))
print(data.var(axis=0))
print(data.std())
