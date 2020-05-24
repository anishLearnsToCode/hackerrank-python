# https://www.hackerrank.com/challenges/matrix-script/problem

import re

n, m = map(int, input().split())
data = []
for _ in range(n):
    data.append(input())

string = ''
for elem in zip(*data):
    string += ''.join(elem)

print(re.sub(r'(?<=\w)([^\w]+)(?=\w)', ' ', string))
