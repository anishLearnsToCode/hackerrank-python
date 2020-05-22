# https://www.hackerrank.com/challenges/itertools-permutations/problem

import itertools

line = input().split()
word = line[0]
k = int(line[1])

permutations = list(itertools.permutations(word, k))
permutations.sort()

for permutation in permutations:
    print(''.join(permutation))
