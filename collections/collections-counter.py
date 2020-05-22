# https://www.hackerrank.com/challenges/collections-counter/problem

import collections

number_of_shoes = int(input())
shoes = collections.Counter(list(map(int, input().split())))
queries = int(input())

profit = 0
for _ in range(queries):
    size, price = map(int, input().split())
    if size in shoes:
        profit += price
        if shoes[size] == 1:
            del shoes[size]
        else:
            shoes[size] -= 1

print(profit)
