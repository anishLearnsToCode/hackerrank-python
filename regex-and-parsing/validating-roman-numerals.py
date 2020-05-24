# https://www.hackerrank.com/challenges/validate-a-roman-number/problem

import re


roman_numeral_strict = r'^(?=[MDCLXVI])M{0,3}(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[XV]|V?I{0,3})$'
number = input()
match = re.fullmatch(roman_numeral_strict, number)
print(match and match.span() == (0,len(number)))
