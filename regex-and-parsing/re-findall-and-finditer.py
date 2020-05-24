# https://www.hackerrank.com/challenges/re-findall-re-finditer/problem

import re


consonants = '[qwrtypsdfghjklzxcvbnm]'
a = re.findall("(?<=" + consonants + ")([aeiou]{2,})" + consonants, input(), re.I)
print('\n'.join(a or ['-1']))
