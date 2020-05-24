# https://www.hackerrank.com/challenges/hex-color-code/problem

import re

hex_color = r'(?<!^)#([0-9a-fA-F]{3}){1,2}'

N = int(input())
for _ in range(N):
    line = input()
    for elem in re.finditer(hex_color, line):
        print(line[elem.start(): elem.end()] if elem is not None else '')
