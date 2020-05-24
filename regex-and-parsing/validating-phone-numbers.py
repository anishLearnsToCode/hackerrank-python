# https://www.hackerrank.com/challenges/validating-the-phone-number/problem

import re


phone_number_pattern = r'^[789]\d{9}$'
N = int(input())
for _ in range(N):
    line = input()
    match = re.fullmatch(phone_number_pattern, line)
    print('YES' if match is not None and match.span() == (0, len(line)) else 'NO')
