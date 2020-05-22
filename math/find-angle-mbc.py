# https://www.hackerrank.com/challenges/find-angle/problem

import math

AB = int(input())
BC = int(input())
h = math.sqrt(pow(AB, 2) + pow(BC, 2))
print(str(round(math.degrees(math.acos(BC / h)))) + '°')
