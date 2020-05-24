# https://www.hackerrank.com/challenges/validating-postalcode/problem

import re


P = input()

regex_integer_in_range = r"^[1-9]\d{5}$"
regex_alternating_repetitive_digit_pair = r"(.)(?=.\1)"

print (bool(re.match(regex_integer_in_range, P))
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)
