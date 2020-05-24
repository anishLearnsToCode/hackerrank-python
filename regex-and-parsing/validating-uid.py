# https://www.hackerrank.com/challenges/validating-uid/problem

import re

pattern_2_upper_case = r'[A-Z]{2}'
pattern_3_digits = r'(\d){3}'
pattern_alphanum = r'[0-9a-zA-Z]{10}'
pattern_has_repitions = r'^.*(.).*\1.*$'

for _ in range(int(input())):
    uid = ''.join(sorted(input()))
    try:
        assert re.search(pattern_2_upper_case, uid)
        assert re.search(pattern_3_digits, uid)
        assert re.search(pattern_alphanum, uid)
        assert not re.search(pattern_has_repitions, uid)
        assert len(uid) == 10
        print("Valid")
    except:
        print('Invalid')
