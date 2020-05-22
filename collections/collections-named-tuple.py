# https://www.hackerrank.com/challenges/py-collections-namedtuple/problem

import collections

n, columns = (int(input()), input().split())
Grade = collections.namedtuple('Grade', columns)
marks = [int(Grade(*input().split()).MARKS) for _ in range(n)]
print((sum(marks) / len(marks)))
