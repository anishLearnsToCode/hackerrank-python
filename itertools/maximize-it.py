# https://www.hackerrank.com/challenges/maximize-it/problem

import itertools


def get_list():
    return list(map(int, input().split()))


line = input().split()
K = int(line[0])
M = int(line[1])

data = []
for i in range(K):
    data.append(get_list()[1:])

result = 0
for entry in itertools.product(*data):
    result = max(result, sum(x*x for x in entry) % M)

print(result)
