# https://www.hackerrank.com/challenges/re-group-groups/problem

import re

pattern = r'([a-zA-Z0-9])\1+'
match = re.search(pattern, input().strip())
print(match.groups()[0] if match else -1)
