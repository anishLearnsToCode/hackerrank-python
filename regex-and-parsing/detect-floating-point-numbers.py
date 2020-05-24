# https://www.hackerrank.com/challenges/introduction-to-regex/problem

import re

pattern = '([+|-]){0,1}(\d)*[.](\d)+'


def is_float(number):
    try:
        float(number)
        info = re.match(pattern, number)
        return info is not None and info.span() == (0, len(number))
    except ValueError as _:
        return False


queries = int(input())
for _ in range(queries):
    number = input()
    print(is_float(number))
