# https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem

import re

and_pattern = r' [&]{2}(?= )'
and_replacement = ' and'
or_pattern = r' [|]{2}(?= )'
or_replacement = ' or'

N = int(input())
for _ in range(N):
    string = input()
    string = re.sub(and_pattern, and_replacement, string)
    string = re.sub(or_pattern, or_replacement, string)
    print(string)
