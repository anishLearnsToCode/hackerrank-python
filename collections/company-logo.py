# https://www.hackerrank.com/challenges/most-commons/problem

import collections

name = sorted(input())
frequencies = collections.Counter(name)
frequencies = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)

count = 0
for element in frequencies:
    if count == 3:
        break
    print(element[0], element[1])
    count += 1
