# https://www.hackerrank.com/challenges/validating-named-email-addresses/problem

import email.utils
import re


email_pattern = r'([a-zA-Z](\w|\d|_|-|[.])*)@([a-zA-Z])*[.]([a-zA-Z]{1,3})'


def is_valid_email_address(person):
    email = person[1]
    return re.fullmatch(email_pattern, email) is not None


people = []
n = int(input())
for _ in range(n):
    line = input()
    people.append(email.utils.parseaddr(line))

for element in (filter(is_valid_email_address, people)):
    print(email.utils.formataddr(element))
