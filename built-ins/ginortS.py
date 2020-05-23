# https://www.hackerrank.com/challenges/ginorts/problem

line = sorted(input(), key=lambda c: (c.isdigit() - c.islower(), c in '02468', c))
print(''.join(line))
