# https://www.hackerrank.com/challenges/py-set-add/problem

n = int(input())
stamps = set()
for i in range(n):
    country = input()
    stamps.add(country)

print(len(stamps))
