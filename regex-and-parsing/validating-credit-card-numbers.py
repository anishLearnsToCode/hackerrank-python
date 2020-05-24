# https://www.hackerrank.com/challenges/validating-credit-card-number/problem

import re

pattern_start = r'^'
pattern_no_repetition = r'(?!.*(\d)(-?\1){3})'
credit_card_pattern = r'[456]((\d){15}|(\d){3}(-[\d]{4}){3})'
pattern_end = r'$'

pattern = re.compile(
    pattern_start
    + pattern_no_repetition
    + credit_card_pattern
    + pattern_end
)

for _ in range(int(input())):
    credit_card = input()
    print("Valid" if pattern.search(credit_card) else 'Invalid')
